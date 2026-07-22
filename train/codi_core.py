"""Shared CODI primitives: projector, latent recurrence, shared-weight teacher,
Trainer, and TrainingArguments boilerplate. Variants build on these."""

import os

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.utils.checkpoint
from transformers import Trainer, TrainingArguments
from transformers.cache_utils import DynamicCache
from transformers.trainer_utils import get_last_checkpoint
from transformers.utils import WEIGHTS_NAME

from data.dataset import IGNORE_INDEX
from .wb import wandb_init


def sliding_window(cfg, w):
    if w and w > 0:
        cfg.use_sliding_window, cfg.sliding_window, cfg.max_window_layers = True, w, 0
        cfg.layer_types = ["sliding_attention"] * cfg.num_hidden_layers
    return cfg


def build_projector(h, device, dtype):
    return nn.Sequential(
        nn.Linear(h, h, bias=False), nn.GELU(),
        nn.Linear(h, h, bias=False), nn.LayerNorm(h),
    ).to(device=device, dtype=dtype)


def latent_block(body, head, emb, prj, ls_tok, le_tok, steps, cache, want_hidden=False):
    """latent_start + `steps` recurrent latents + latent_end on `cache`.
    Returns (cache, logits for the next real token, per-layer latent_end hiddens or None)."""
    o = body(inputs_embeds=emb(ls_tok), past_key_values=cache, use_cache=True)
    cache, h = o.past_key_values, o.last_hidden_state[:, -1:]
    for _ in range(steps):
        o = body(inputs_embeds=prj(h), past_key_values=cache, use_cache=True)
        cache, h = o.past_key_values, o.last_hidden_state[:, -1:]
    o = body(inputs_embeds=emb(le_tok), past_key_values=cache, use_cache=True, output_hidden_states=want_hidden)
    hid = [l[0, -1] for l in o.hidden_states[1:]] if want_hidden else None
    return o.past_key_values, head(o.last_hidden_state[:, -1]), hid


def rebuild_cache(chunks):
    """Pure function: reconstruct a DynamicCache from a list of past per-step (k0,v0,k1,v1,...)
    tuples. Pure = safe to re-invoke during torch.utils.checkpoint's backward recompute, unlike
    checkpointing directly against a stateful, incrementally-mutated cache (ported from
    train_codi_qlora.py's _rebuild_cache)."""
    if not chunks:
        return DynamicCache()
    num_layers = len(chunks[0]) // 2
    pairs = [(torch.cat([c[2 * l] for c in chunks], dim=2),
              torch.cat([c[2 * l + 1] for c in chunks], dim=2))
             for l in range(num_layers)]
    return DynamicCache(ddp_cache_data=pairs)


def checkpointed_step(module, chunks, embeds, want_hidden=False):
    """One incremental forward, checkpointed against a cache rebuilt from `chunks` (mutated in
    place with this call's new K/V tail) instead of a stateful incrementally-mutated cache --
    bounds peak memory to ~O(one chunk) instead of O(every chunk seen so far), at the cost of
    re-concatenating all past K/V every step and recomputing this step's forward on backward.
    `module` is either the full CausalLM (returns logits) or its transformer body (returns
    last_hidden_state); ported from train_codi_qlora.py's _step/_forward_rebuild.
    Returns (primary_output, hidden_states_or_None)."""
    prefix_len = sum(c[0].shape[2] for c in chunks)

    def _forward(embeds, chunks, prefix_len, want_hidden):
        cache = rebuild_cache(chunks)
        # a rebuilt (not incrementally-tracked) cache can't be trusted for RoPE's internal
        # position offset -- pass it explicitly.
        pos_ids = (prefix_len + torch.arange(embeds.shape[1], device=embeds.device))[None]
        out = module(inputs_embeds=embeds, past_key_values=cache, use_cache=True,
                     position_ids=pos_ids, output_hidden_states=want_hidden)
        tail = tuple(t[:, :, prefix_len:, :].contiguous()
                     for layer in out.past_key_values.layers for t in (layer.keys, layer.values))
        primary = out.logits if hasattr(out, "logits") else out.last_hidden_state
        return primary, out.hidden_states, tail

    primary, hidden, tail = torch.utils.checkpoint.checkpoint(
        _forward, embeds, tuple(chunks), prefix_len, want_hidden, use_reentrant=False)
    chunks.append(tail)
    return primary, hidden


def latent_block_ckpt(body, head, emb, prj, ls_tok, le_tok, steps, chunks, want_hidden=False):
    """chunks-based, memory-bounded equivalent of latent_block(): latent_start + `steps`
    recurrent latents + latent_end, each a checkpointed_step against `chunks` (mutated in
    place). Returns (logits for the next real token, per-layer latent_end hiddens or None)."""
    hs, _ = checkpointed_step(body, chunks, emb(ls_tok))
    h = hs[:, -1:]
    for _ in range(steps):
        hs, _ = checkpointed_step(body, chunks, prj(h))
        h = hs[:, -1:]
    hs, hidden = checkpointed_step(body, chunks, emb(le_tok), want_hidden=want_hidden)
    hid = [l[0, -1] for l in hidden[1:]] if want_hidden else None
    return head(hs[:, -1]), hid


def shared_teacher(model, full, labels, pos, kd_layers=None):
    """Shared-weight teacher: one grad-ckpt forward; detached hidden@pos KD + CE."""
    pos = torch.as_tensor(pos, device=full.device)
    model.gradient_checkpointing_enable(gradient_checkpointing_kwargs={"use_reentrant": False})
    out = model(input_ids=full[None], use_cache=False, output_hidden_states=True)
    model.gradient_checkpointing_disable()
    hs = out.hidden_states
    sel = hs[1:] if kd_layers is None else [hs[l] for l in kd_layers]
    kd = [l[0, pos].detach() for l in sel]
    ce = F.cross_entropy(out.logits[0, :-1], labels[1:], ignore_index=IGNORE_INDEX)
    return ce, kd


class CodiTrainer(Trainer):
    _SUB = ("teacher_loss", "student_loss", "kd_loss", "recon_loss", "recon_trunc")

    def compute_loss(self, model, inputs, return_outputs=False, **kw):
        out = model(inputs["examples"])
        self._sub = {k: out[k] for k in self._SUB if k in out}
        return (out["loss"], out) if return_outputs else out["loss"]

    def log(self, logs, *a, **k):
        for key, v in getattr(self, "_sub", {}).items():
            logs[key] = v.item()
        super().log(logs, *a, **k)

    def _save(self, output_dir=None, state_dict=None):
        output_dir = output_dir or self.args.output_dir
        os.makedirs(output_dir, exist_ok=True)
        torch.save(state_dict or self.model.state_dict(), os.path.join(output_dir, WEIGHTS_NAME))
        torch.save(self.args, os.path.join(output_dir, "training_args.bin"))
        self.model.model.config.save_pretrained(output_dir)
        self.tok.save_pretrained(output_dir)
        torch.save(self.model.prj.state_dict(), os.path.join(output_dir, "thought_projector.pt"))


def add_common_args(ap):
    ap.add_argument("--model", required=True)
    ap.add_argument("--output_dir", required=True)
    ap.add_argument("--cache_dir", default="data/cache/codi_train")
    ap.add_argument("--n_samples", type=int, default=-1)
    ap.add_argument("--max_seq_len", type=int, default=4096)
    ap.add_argument("--epochs", type=float, default=10.0)
    ap.add_argument("--lr", type=float, default=1e-5)
    ap.add_argument("--batch_size", type=int, default=1)
    ap.add_argument("--grad_accum", type=int, default=4)
    ap.add_argument("--max_steps", type=int, default=-1)
    ap.add_argument("--save_steps", type=int, default=500)
    ap.add_argument("--optim", default="paged_adamw_8bit")
    ap.add_argument("--alpha", type=float, default=1.0)
    ap.add_argument("--beta", type=float, default=1.0)
    ap.add_argument("--gamma", type=float, default=1.0)
    ap.add_argument("--sliding_window", type=int, default=0)  # 0=off; >0 caps attention+KV to last W (needs flash-attn to save mem)
    ap.add_argument("--attn_impl", default="flash_attention_2")  # A100 compute nodes; sdpa fallback for non-Ampere
    return ap


def run_training(model, tok, ds, args, run_name):
    targs = TrainingArguments(
        output_dir=args.output_dir,
        per_device_train_batch_size=args.batch_size,
        gradient_accumulation_steps=args.grad_accum,
        num_train_epochs=args.epochs,
        max_steps=args.max_steps,
        learning_rate=args.lr,
        lr_scheduler_type="cosine",
        warmup_ratio=0.03,
        weight_decay=0.1,
        max_grad_norm=1.0,
        bf16=args.attn_impl != "flash_attention_2",  # FA2's q/k break under autocast -> native bf16 (model already bf16)
        optim=args.optim,
        ddp_find_unused_parameters=False,
        logging_steps=5,
        save_strategy="steps",
        save_steps=args.save_steps,
        save_total_limit=None,
        report_to=wandb_init(args, run_name),
        remove_unused_columns=False,
        label_names=[],
    )
    trainer = CodiTrainer(model=model, args=targs, train_dataset=ds,
                          data_collator=lambda b: {"examples": b})
    trainer.tok = tok
    ckpt = get_last_checkpoint(args.output_dir) if os.path.isdir(args.output_dir) else None
    trainer.train(resume_from_checkpoint=ckpt)
    trainer._save_checkpoint(trainer.model, trial=None)
