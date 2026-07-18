"""QLoRA CODI training for CWM-32B. Standalone: doesn't touch train_codi.py/
codi.sbatch (the Qwen full-FT path). No HF Trainer: teacher/student backward
are split so the teacher's graph frees before the student's is built (peak
VRAM = max, not sum), and gradient sync is a manual all_reduce over just the
trainable params (Trainer's DDP wrap doesn't like frozen 4-bit + LoRA mixes).
"""

import argparse
import os

import bitsandbytes
import torch
import torch.distributed as dist
import torch.nn as nn
import torch.nn.functional as F
import torch.utils.checkpoint
from peft import LoraConfig, TaskType, get_peft_model, prepare_model_for_kbit_training
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig, get_cosine_schedule_with_warmup
from transformers.cache_utils import DynamicCache

from data.dataset import IGNORE_INDEX
from data.precompute_loader import load_cache
from train.codi_core import build_projector, shared_teacher
from train.wb import wandb_init

LATENT_START = "<|reasoning_thinking_start|>"  # CWM's native thinking-block delimiters,
LATENT_END = "<|reasoning_thinking_end|>"      # reused as latent markers (LoRA never trains new embeddings)

LORA_TARGETS = ["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"]


def _rebuild_cache(chunks):
    # Pure function of `chunks` -> safe to re-invoke during checkpoint's backward
    # recompute (unlike checkpointing against a stateful, in-place-mutated cache).
    if not chunks:
        return DynamicCache()
    num_layers = len(chunks[0]) // 2
    pairs = [(torch.cat([c[2 * l] for c in chunks], dim=2),
              torch.cat([c[2 * l + 1] for c in chunks], dim=2))
             for l in range(num_layers)]
    return DynamicCache(ddp_cache_data=pairs)


def load_qlora_base(model_path, local_rank, attn_impl, lora_r, lora_alpha, lora_dropout):
    quant = BitsAndBytesConfig(
        load_in_4bit=True, bnb_4bit_quant_type="nf4",
        bnb_4bit_use_double_quant=True, bnb_4bit_compute_dtype=torch.bfloat16,
    )
    base = AutoModelForCausalLM.from_pretrained(
        model_path, quantization_config=quant, dtype=torch.bfloat16,
        device_map={"": local_rank}, attn_implementation=attn_impl,
    )
    base.config.use_cache = True
    # use_gradient_checkpointing=False: shared_teacher() below does its own
    # checkpointing per forward and needs use_cache free the rest of the time.
    base = prepare_model_for_kbit_training(base, use_gradient_checkpointing=False)
    lora_cfg = LoraConfig(task_type=TaskType.CAUSAL_LM, r=lora_r, lora_alpha=lora_alpha,
                          lora_dropout=lora_dropout, bias="none", target_modules=LORA_TARGETS)
    model = get_peft_model(base, lora_cfg)
    # from_pretrained() leaves the base in .eval() mode; GradientCheckpointingLayer
    # gates on self.training, so without this checkpointing silently never engages.
    model.train()
    return model


class CodiModel(nn.Module):
    """Shared-weight teacher + student CODI on a 4-bit+LoRA base. Frozen-teacher
    variant disables the adapter instead of loading a second model copy."""

    def __init__(self, peft_model, *, latent_start_id, latent_end_id, latent_steps,
                 kd_layers, frozen_teacher=False):
        super().__init__()
        self.model = peft_model
        base = peft_model.get_base_model()
        self._embed_layer = base.get_input_embeddings()
        ref = self._embed_layer.weight
        self.prj = build_projector(base.config.hidden_size, ref.device, ref.dtype)
        self.latent_steps = latent_steps
        self.kd_layers = kd_layers
        self.frozen_teacher = frozen_teacher
        # plain tensors, not buffers: this module is never .to(device)'d itself
        self._ls_tok = torch.tensor([[latent_start_id]], dtype=torch.long, device=ref.device)
        self._le_tok = torch.tensor([[latent_end_id]], dtype=torch.long, device=ref.device)

    def _kd(self, hs):
        return tuple(hs[l] for l in self.kd_layers)

    def _emb(self, ids):
        return self._embed_layer(ids)

    def _teacher(self, full_ids, labels, kd_pos):
        if not self.frozen_teacher:
            return shared_teacher(self.model, full_ids, labels, kd_pos, self.kd_layers)
        pos = torch.as_tensor(kd_pos, device=full_ids.device)
        with self.model.disable_adapter(), torch.no_grad():
            hs = self.model(input_ids=full_ids[None], use_cache=False,
                            output_hidden_states=True).hidden_states
        return None, [l[0, pos] for l in self._kd(hs)]

    def _forward_rebuild(self, embeds, chunks, prefix_len, want_hidden):
        cache = _rebuild_cache(chunks)
        # A rebuilt (not incrementally-tracked) cache can't be trusted to give the
        # model the right position offset for RoPE -- pass it explicitly.
        pos_ids = (prefix_len + torch.arange(embeds.shape[1], device=embeds.device))[None]
        out = self.model(inputs_embeds=embeds, past_key_values=cache, use_cache=True,
                         position_ids=pos_ids, output_hidden_states=want_hidden)
        tail = tuple(t[:, :, prefix_len:, :].contiguous()
                     for layer in out.past_key_values.layers for t in (layer.keys, layer.values))
        return out.logits, out.hidden_states, tail

    def _step(self, chunks, embeds, want_hidden=False):
        # Per-call checkpoint: backward recomputes/holds one call's activations at
        # a time, not the whole trace's (ported from cwm_andre/codi_streaming.py).
        prefix_len = sum(c[0].shape[2] for c in chunks)
        logits, hidden, tail = torch.utils.checkpoint.checkpoint(
            self._forward_rebuild, embeds, tuple(chunks), prefix_len, want_hidden,
            use_reentrant=False)
        chunks.append(tail)
        return logits, hidden

    def _latent_block(self, chunks):
        _, hidden = self._step(chunks, self._emb(self._ls_tok), want_hidden=True)
        h = hidden[-1][:, -1:]
        for _ in range(self.latent_steps):
            _, hidden = self._step(chunks, self.prj(h), want_hidden=True)
            h = hidden[-1][:, -1:]
        logits, _ = self._step(chunks, self._emb(self._le_tok))
        return logits[:, -1]

    def _student(self, prompt_ids, trace_ids, spans):
        chunk_spans, prev, kd = [], 0, False
        for i, j in spans:
            chunk_spans.append((trace_ids[prev:i + 1], kd))
            prev, kd = j, True
        chunk_spans.append((trace_ids[prev:], kd))

        kv_chunks = []
        out_logits, _ = self._step(kv_chunks, self._emb(prompt_ids[None]))
        prev_logits = out_logits[:, -1]
        ce_logits, ce_targets, kd_vecs = [], [], []
        for c, (ids, kd) in enumerate(chunk_spans):
            out_logits, hidden = self._step(kv_chunks, self._emb(ids[None]), want_hidden=kd)
            logits = out_logits[0]
            ce_logits.append(torch.cat([prev_logits, logits[:-1]]))
            ce_targets.append(ids)
            prev_logits = logits[-1:]
            if kd:
                kd_vecs.append([hs[0, 0] for hs in self._kd(hidden)])
            if c + 1 < len(chunk_spans):
                prev_logits = self._latent_block(kv_chunks)

        ce = F.cross_entropy(torch.cat(ce_logits), torch.cat(ce_targets))
        s_kd = [torch.stack([v[l] for v in kd_vecs]) for l in range(len(kd_vecs[0]))]
        return ce, s_kd

    def teacher_step(self, ex, dev):
        prompt = torch.tensor(ex["prompt_ids"], device=dev)
        trace = torch.tensor(ex["trace_ids"], device=dev)
        full = torch.cat([prompt, trace])
        labels = torch.cat([full.new_full((len(prompt),), IGNORE_INDEX), trace])
        kd_pos = [len(prompt) + j for _, j in ex["spans"]]
        t_ce, t_kd = self._teacher(full, labels, kd_pos)
        return t_ce, t_kd, (prompt, trace, ex["spans"])

    def student_step(self, meta, t_kd):
        prompt, trace, spans = meta
        s_ce, s_kd = self._student(prompt, trace, spans)
        s, t = torch.stack(s_kd), torch.stack(t_kd).detach()
        return s_ce, F.smooth_l1_loss(s, t)

    def save(self, output_dir):
        self.model.save_pretrained(output_dir)
        torch.save(self.prj.state_dict(), os.path.join(output_dir, "thought_projector.pt"))


def init_dist():
    world_size = int(os.environ.get("WORLD_SIZE", 1))
    if world_size == 1:
        return 0, 0, 1, torch.device("cuda" if torch.cuda.is_available() else "cpu")
    dist.init_process_group(backend="nccl")
    local_rank = int(os.environ["LOCAL_RANK"])
    torch.cuda.set_device(local_rank)
    return dist.get_rank(), local_rank, world_size, torch.device(f"cuda:{local_rank}")


def sync_gradients(params):
    for p in params:
        if p.grad is None:
            p.grad = torch.zeros_like(p)
        dist.all_reduce(p.grad, op=dist.ReduceOp.AVG)


def parse_args():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True)
    ap.add_argument("--output_dir", required=True)
    ap.add_argument("--cache_dir", required=True)
    ap.add_argument("--max_seq_len", type=int, default=1536)
    ap.add_argument("--n_samples", type=int, default=-1)
    ap.add_argument("--epochs", type=int, default=5)
    ap.add_argument("--max_steps", type=int, default=-1)  # >0 stops training at this optimizer-step count
    ap.add_argument("--lr", type=float, default=1e-4)
    ap.add_argument("--grad_accum", type=int, default=32)
    ap.add_argument("--latent_steps", type=int, default=1)
    ap.add_argument("--kd_layers", nargs="+", type=int, default=[-1])
    ap.add_argument("--frozen_teacher", action="store_true")
    ap.add_argument("--alpha", type=float, default=1.0)  # teacher CE weight
    ap.add_argument("--beta", type=float, default=1.0)   # student CE weight
    ap.add_argument("--gamma", type=float, default=1.0)  # KD weight
    ap.add_argument("--lora_r", type=int, default=16)
    ap.add_argument("--lora_alpha", type=int, default=32)
    ap.add_argument("--lora_dropout", type=float, default=0.05)
    ap.add_argument("--attn_impl", default="sdpa")
    ap.add_argument("--save_every_steps", type=int, default=0)  # 0 = only at end
    ap.add_argument("--seed", type=int, default=42)
    return ap.parse_args()


def main():
    args = parse_args()
    rank, local_rank, world_size, device = init_dist()
    is_rank0 = rank == 0
    # Same seed on every rank so LoRA's kaiming_uniform_ init matches across ranks --
    # otherwise each rank starts from a different A matrix, sync_gradients' averaging
    # is meaningless from step 2 onward, and ranks silently diverge into unrelated models.
    torch.manual_seed(args.seed)

    tok = AutoTokenizer.from_pretrained(args.model, use_fast=True)
    latent_start_id = tok.convert_tokens_to_ids(LATENT_START)
    latent_end_id = tok.convert_tokens_to_ids(LATENT_END)

    peft_base = load_qlora_base(args.model, local_rank, args.attn_impl,
                                args.lora_r, args.lora_alpha, args.lora_dropout)
    model = CodiModel(peft_base, latent_start_id=latent_start_id, latent_end_id=latent_end_id,
                      latent_steps=args.latent_steps, kd_layers=args.kd_layers,
                      frozen_teacher=args.frozen_teacher)

    ds = load_cache(args.cache_dir, max_len=args.max_seq_len, n_samples=args.n_samples)
    # load_cache's length only counts prompt+trace tokens; the student also inserts a
    # latent block (latent_steps+2 extra positions) per span, so filter those out too.
    ds = [e for e in ds if len(e["prompt_ids"]) + len(e["trace_ids"])
          + len(e["spans"]) * (args.latent_steps + 2) <= args.max_seq_len]
    if is_rank0:
        print(f"{len(ds)} codi examples, latent_steps={args.latent_steps}")
    ds = ds[: len(ds) - len(ds) % world_size]  # equal per-rank length keeps all_reduce call counts in sync
    ds = ds[rank::world_size]

    params = [p for p in model.parameters() if p.requires_grad]
    optimizer = bitsandbytes.optim.AdamW8bit(params, lr=args.lr, weight_decay=0.01)
    total_steps = args.max_steps if args.max_steps > 0 else args.epochs * (len(ds) // args.grad_accum + 1)
    scheduler = get_cosine_schedule_with_warmup(optimizer, num_warmup_steps=max(1, int(0.03 * total_steps)),
                                                num_training_steps=total_steps)
    wandb_init(args, "codi_qlora")
    import wandb

    step, out_dir = 0, args.output_dir
    os.makedirs(out_dir, exist_ok=True)
    try:
        for epoch in range(args.epochs):
            optimizer.zero_grad()
            window = {"loss": 0.0, "teacher": 0.0, "student": 0.0, "kd": 0.0}
            for i, ex in enumerate(ds):
                if is_rank0 and device.type == "cuda" and i == 0:
                    torch.cuda.reset_peak_memory_stats(device)
                t_ce, t_kd, meta = model.teacher_step(ex, device)
                if t_ce is not None:
                    (args.alpha * t_ce / args.grad_accum).backward()
                if is_rank0 and device.type == "cuda" and i == 0:
                    teacher_peak = torch.cuda.max_memory_allocated(device) / 1024**3
                    torch.cuda.reset_peak_memory_stats(device)
                s_ce, kl = model.student_step(meta, t_kd)
                ((args.beta * s_ce + args.gamma * kl) / args.grad_accum).backward()
                if is_rank0 and device.type == "cuda" and i == 0:
                    student_peak = torch.cuda.max_memory_allocated(device) / 1024**3
                    print(f"peak VRAM (first example): teacher={teacher_peak:.1f}GB student={student_peak:.1f}GB")

                t = t_ce.item() if t_ce is not None else 0.0
                s, k = s_ce.item(), kl.item()
                window["teacher"] += t
                window["student"] += s
                window["kd"] += k
                window["loss"] += args.alpha * t + args.beta * s + args.gamma * k

                will_step = (i + 1) % args.grad_accum == 0 or i + 1 == len(ds)
                if not will_step:
                    continue
                n = (i % args.grad_accum) + 1
                if n < args.grad_accum:  # partial final window: rescale so it matches a full one
                    scale = args.grad_accum / n
                    for p in params:
                        if p.grad is not None:
                            p.grad.mul_(scale)
                if world_size > 1:
                    sync_gradients(params)
                torch.nn.utils.clip_grad_norm_(params, 1.0)
                optimizer.step()
                scheduler.step()
                optimizer.zero_grad()
                step += 1
                if is_rank0:
                    print(f"epoch {epoch} step {step} loss={window['loss']/n:.4f} "
                          f"teacher={window['teacher']/n:.4f} student={window['student']/n:.4f} "
                          f"kd={window['kd']/n:.4f}")
                    if wandb.run is not None:
                        wandb.log({k: v / n for k, v in window.items()} | {"epoch": epoch}, step=step)
                    if args.save_every_steps and step % args.save_every_steps == 0:
                        model.save(os.path.join(out_dir, f"checkpoint-{step}"))
                for key in window:
                    window[key] = 0.0
                if args.max_steps > 0 and step >= args.max_steps:
                    break
            if is_rank0:
                model.save(os.path.join(out_dir, f"epoch-{epoch}"))
            if args.max_steps > 0 and step >= args.max_steps:
                break
        if is_rank0:
            model.save(out_dir)
    except BaseException:
        if is_rank0:
            model.save(os.path.join(out_dir, "crash"))
        if world_size > 1:
            os._exit(1)  # skip graceful DDP teardown; other ranks may be blocked in a collective
        raise
    finally:
        if world_size > 1:
            dist.destroy_process_group()


if __name__ == "__main__":
    main()
