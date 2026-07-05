"""CODI inference lib: load a trained CODI wrapper and greedily decode with latent blocks.
Shared by eval_len.py and eval/diag/*. `_latent`/`_latent_block` mirror training."""

import os

import torch
from transformers import AutoConfig, AutoModelForCausalLM, AutoTokenizer

from data.tokens import add_trace_tokens, token_ids
from train.train_codi import CodiModel
from train.train_codi_single import CodiSingle


def load_codi(m, latent_steps, dev):
    tok = AutoTokenizer.from_pretrained(m, use_fast=True)
    add_trace_tokens(tok)
    ids = token_ids(tok)
    base = AutoModelForCausalLM.from_config(AutoConfig.from_pretrained(m), torch_dtype=torch.bfloat16)
    model = CodiModel(base, latent_start_id=ids["<|latent_start|>"],
                      latent_end_id=ids["<|latent_end|>"], latent_steps=latent_steps)
    if os.path.exists(f"{m}/pytorch_model.bin"):  # epoch checkpoint: full CodiModel
        sd = torch.load(f"{m}/pytorch_model.bin", map_location="cpu")
        drop = [k for k in sd if k.startswith("recon_query.")]
        for k in drop:
            sd.pop(k)
        if drop:
            print(f"ignored {len(drop)} recon-only keys", flush=True)
        model.load_state_dict(sd)
    else:  # final export: backbone safetensors + separate projector
        model.model = AutoModelForCausalLM.from_pretrained(m, torch_dtype=torch.bfloat16)
        model.prj.load_state_dict(torch.load(f"{m}/thought_projector.pt", map_location="cpu"))
    return tok, ids, model.to(dev).eval()


@torch.no_grad()
def gen_latent(model, prompt_ids, ls_id, act_id, eot, max_new):
    dev = prompt_ids.device

    def step(t):  # emit token t, advance cache; return its next-token logits
        nonlocal cache
        o = model.model(input_ids=torch.tensor([[t]], device=dev), past_key_values=cache, use_cache=True)
        cache = o.past_key_values
        return o.logits[:, -1]

    o = model.model(input_ids=prompt_ids[None], use_cache=True)
    cache, logits = o.past_key_values, o.logits[:, -1]
    out, n_fwd = [], 0  # n_fwd: decode forward passes = text tokens + latent-block steps (latent_steps+2 each)
    while n_fwd < max_new:  # budget on forward steps, not emitted tokens
        t = int(logits.argmax(-1))
        if t == eot:
            break
        out.append(t); logits = step(t); n_fwd += 1
        if t == ls_id:  # latent block replaces $LOCALS; force <|action_sep|> (latent mode, no locals text)
            cache, _ = model._latent_block(cache)
            n_fwd += model.latent_steps + 2
            out.append(act_id); logits = step(act_id); n_fwd += 1
    return out, n_fwd


def load_codi_single(m, latent_steps, dev):
    tok = AutoTokenizer.from_pretrained(m, use_fast=True)
    add_trace_tokens(tok)
    ids = token_ids(tok)
    base = AutoModelForCausalLM.from_config(AutoConfig.from_pretrained(m), torch_dtype=torch.bfloat16)
    model = CodiSingle(base, latent_start_id=ids["<|latent_start|>"],
                       latent_end_id=ids["<|latent_end|>"], latent_steps=latent_steps)
    if os.path.exists(f"{m}/pytorch_model.bin"):  # checkpoint: full CodiSingle
        # body/head alias model.model/model.lm_head; older ckpts lack those dup keys -> load via the
        # shared model.* tensors (strict=False), but guard that nothing else is actually missing.
        res = model.load_state_dict(torch.load(f"{m}/pytorch_model.bin", map_location="cpu"), strict=False)
        bad = [k for k in res.missing_keys if not k.startswith(("body.", "head."))]
        assert not bad and not res.unexpected_keys, f"state_dict mismatch: missing={bad} unexpected={res.unexpected_keys}"
    else:  # final export: backbone safetensors + separate projector
        model.model = AutoModelForCausalLM.from_pretrained(m, torch_dtype=torch.bfloat16)
        model.prj.load_state_dict(torch.load(f"{m}/thought_projector.pt", map_location="cpu"))
    return tok, ids, model.to(dev).eval()


@torch.no_grad()
def gen_single(model, prompt_ids, eot, max_new):
    dev = prompt_ids.device
    cache = model.model.model(inputs_embeds=model._emb(prompt_ids[None]), use_cache=True).past_key_values
    cache, logits, _ = model._latent(cache)  # one latent block, then plain decode
    out = []
    for _ in range(max_new):
        t = int(logits.argmax(-1))
        if t == eot:
            break
        out.append(t)
        o = model.model(input_ids=torch.tensor([[t]], device=dev), past_key_values=cache, use_cache=True)
        cache, logits = o.past_key_values, o.logits[:, -1]
    return out
