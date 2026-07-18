"""
Shared-weight teacher+student initialized from the Stage-1 SFT model.
- Teacher reads the full explicit trace (prompt+trace), CE = L_teacher.
- Student replaces each LINE frame's $LOCALS with a latent block (latent_start +
  `latent_steps` recurrent latents + latent_end; last hidden -> prj -> next embed)
  and teacher-forces the rest, CE = L_student over the emitted (non-locals) text.
- KD aligns the hidden at each frame's `<|action_sep|>` (student after latents vs
  teacher after locals), teacher detached. L = a*Lt + b*Ls + g*Lkd.
"""

import argparse

import torch
import torch.nn as nn
import torch.nn.functional as F
from transformers import AutoConfig, AutoModelForCausalLM, AutoTokenizer

from train.codi_core import add_common_args, build_projector, latent_block, run_training, shared_teacher, sliding_window
from data.precompute_loader import load_cache
from data.dataset import IGNORE_INDEX
from data.tokens import add_trace_tokens, token_ids


class CodiModel(nn.Module):
    def __init__(self, base, *, latent_start_id, latent_end_id, latent_steps,
                 a=1.0, b=1.0, g=1.0, kd_layers=None,
                 teacher=None, kd_target="hidden", kd_temp=2.0):
        super().__init__()
        self.model = base
        ref = base.get_input_embeddings().weight
        self.prj = build_projector(base.config.hidden_size, ref.device, ref.dtype)
        self.latent_steps, self.a, self.b, self.g = latent_steps, a, b, g
        self.teacher = [teacher] if teacher is not None else None  # list -> hidden from state_dict/DDP/optim
        self.kd_target, self.kd_temp = kd_target, kd_temp  # hidden: smooth_l1 on kd_layers; logit: KL on lm_head
        if kd_target == "logit" or (teacher is not None and kd_layers is None):
            kd_layers = [-1]  # logit KD is defined on the last layer only; frozen default = key (last) hidden
        self.kd_layers = kd_layers  # None -> all layers
        self.register_buffer("_ls_tok", torch.tensor([[latent_start_id]], dtype=torch.long), persistent=False)
        self.register_buffer("_le_tok", torch.tensor([[latent_end_id]], dtype=torch.long), persistent=False)
        self.body = base.model
        self.head = base.lm_head

    def _kd(self, hs):
        return hs[1:] if self.kd_layers is None else tuple(hs[l] for l in self.kd_layers)

    def _emb(self, ids):
        return self.model.get_input_embeddings()(ids)

    def _teacher(self, full_ids, labels, kd_pos):
        # Two modes: a separate frozen teacher (KD targets only, no teacher CE) or
        # the shared-weight teacher (own forward pass, provides both CE and KD).
        if self.teacher is not None:
            return self._frozen_teacher(full_ids, kd_pos)
        return shared_teacher(self.model, full_ids, labels, kd_pos, self.kd_layers)

    def _frozen_teacher(self, full_ids, kd_pos):
        # Frozen teacher: no CE (return None), only KD targets at kd_pos.
        tch, dev = self.teacher[0], full_ids.device
        if next(tch.parameters()).device != dev:
            tch.to(dev)
        pos = torch.as_tensor(kd_pos, device=dev)
        with torch.no_grad():
            if self.kd_target == "logit":  # target = teacher's own next-token logits
                logits = tch(input_ids=full_ids[None], use_cache=False).logits
                return None, [logits[0, pos]]
            hs = tch(input_ids=full_ids[None], use_cache=False, output_hidden_states=True).hidden_states
            return None, [l[0, pos] for l in self._kd(hs)]

    def _latent_block(self, cache):
        cache, logits, _ = latent_block(self.body, self.head, self._emb, self.prj,
                                        self._ls_tok, self._le_tok, self.latent_steps, cache)
        return cache, logits

    def _student(self, prompt_ids, trace_ids, spans):
        # Kept-text chunks of trace_ids, in order; between consecutive chunks the
        # locals trace_ids[i+1:j] are dropped and replaced by a latent block.
        # kd=True marks a chunk whose first token is a frame's <|action_sep|>.
        chunks, prev, kd = [], 0, False
        for i, j in spans:
            chunks.append((trace_ids[prev:i + 1], kd))
            prev, kd = j, True
        chunks.append((trace_ids[prev:], kd))

        out = self.model(inputs_embeds=self._emb(prompt_ids[None]), use_cache=True)
        
        cache, prev_logits = out.past_key_values, out.logits[:, -1]  # predicts trace_ids[0]
        ce_logits, ce_targets, kd_vecs = [], [], []
        for c, (ids, kd) in enumerate(chunks):
            out = self.model(inputs_embeds=self._emb(ids[None]), past_key_values=cache,
                             use_cache=True, output_hidden_states=kd)  # hiddens only for KD anchors
            cache, logits = out.past_key_values, out.logits[0]
            # carried prev_logits predicts ids[0], logits[:-1] predict ids[1:] -> together cover ids
            ce_logits.append(torch.cat([prev_logits, logits[:-1]])); 
            ce_targets.append(ids)
            prev_logits = logits[-1:]
            
            if kd:  # action_sep is this chunk's first token
                kd_vecs.append([hs[0, 0] for hs in self._kd(out.hidden_states)])
            if c + 1 < len(chunks):  # latent block replaces the dropped locals; overwrite prev_logits, no CE
                cache, prev_logits = self._latent_block(cache)
                
        ce = F.cross_entropy(torch.cat(ce_logits), torch.cat(ce_targets))
        s_kd = [torch.stack([v[l] for v in kd_vecs]) for l in range(len(kd_vecs[0]))]
        return ce, s_kd

    def _kd_loss(self, s_kd, t_kd):
        s, t = torch.stack(s_kd), torch.stack(t_kd).detach()
        if self.kd_target == "logit":  # s=student hidden, t=frozen-teacher logits; KL on distributions
            T = self.kd_temp
            sl, tl = self.head(s).flatten(0, -2) / T, t.flatten(0, -2) / T
            return F.kl_div(F.log_softmax(sl, -1), F.softmax(tl, -1), reduction="batchmean") * T * T
        return F.smooth_l1_loss(s, t)

    def forward(self, examples):
        dev = self.model.get_input_embeddings().weight.device
        tl = sl = kl = torch.tensor(0.0, device=dev)
        for ex in examples:
            prompt = torch.tensor(ex["prompt_ids"], device=dev)
            trace = torch.tensor(ex["trace_ids"], device=dev)
            spans = ex["spans"]
            full = torch.cat([prompt, trace])
            labels = None if self.teacher else torch.cat([full.new_full((len(prompt),), IGNORE_INDEX), trace])
            kd_pos = [len(prompt) + j for _, j in spans]
            t_ce, t_kd = self._teacher(full, labels, kd_pos)
            s_ce, s_kd = self._student(prompt, trace, spans)
            tl = tl + (t_ce if t_ce is not None else 0.0)  # frozen teacher -> no teacher CE
            sl, kl = sl + s_ce, kl + self._kd_loss(s_kd, t_kd)
        n = len(examples)
        loss = self.a * tl / n + self.b * sl / n + self.g * kl / n
        t_log = (tl / n).detach() if torch.is_tensor(tl) else torch.tensor(0.0)  # 0 under frozen teacher
        return {"loss": loss, "teacher_loss": t_log,
                "student_loss": (sl / n).detach(), "kd_loss": (kl / n).detach()}


def main():
    ap = argparse.ArgumentParser()
    add_common_args(ap)
    ap.add_argument("--latent_steps", type=int, default=1)
    ap.add_argument("--kd_layers", nargs="+", type=int, default=None)  # default: all layers (frozen -> last)
    ap.add_argument("--frozen_teacher", default="")  # path to frozen SFT teacher; "" -> shared-weight (legacy)
    ap.add_argument("--kd_target", default="hidden", choices=["hidden", "logit"])  # key-hidden align: smooth_l1 vs KL
    ap.add_argument("--kd_temp", type=float, default=2.0)  # logit-KD temperature
    args = ap.parse_args()

    tok = AutoTokenizer.from_pretrained(args.model, use_fast=True)
    add_trace_tokens(tok)  # idempotent
    ids = token_ids(tok)
    cfg = sliding_window(AutoConfig.from_pretrained(args.model), args.sliding_window)
    base = AutoModelForCausalLM.from_pretrained(args.model, config=cfg, torch_dtype=torch.bfloat16, attn_implementation=args.attn_impl)
    base.config.use_cache = True
    teacher = None
    if args.frozen_teacher:
        tcfg = sliding_window(AutoConfig.from_pretrained(args.frozen_teacher), args.sliding_window)
        teacher = AutoModelForCausalLM.from_pretrained(args.frozen_teacher, config=tcfg, torch_dtype=torch.bfloat16, attn_implementation=args.attn_impl)
        teacher.config.use_cache = False
        teacher.eval().requires_grad_(False)
    model = CodiModel(base, latent_start_id=ids["<|latent_start|>"], latent_end_id=ids["<|latent_end|>"],
                      latent_steps=args.latent_steps, a=args.alpha, b=args.beta, g=args.gamma,
                      kd_layers=args.kd_layers,
                      teacher=teacher, kd_target=args.kd_target, kd_temp=args.kd_temp)

    ds = load_cache(args.cache_dir, max_len=args.max_seq_len, n_samples=args.n_samples)
    print(f"{len(ds)} codi examples, latent_steps={args.latent_steps}")
    run_training(model, tok, ds, args, "codi")


if __name__ == "__main__":
    main()
