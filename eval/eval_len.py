"""Unified length-binned held-out eval over a precomputed codi cache (--dataset), filtered to
[--min_len,--max_len] trace_len. Ranks write crash-safe .rN.jsonl shards; merge_len_shards combines.
--mode picks the model + generation:
  sft    : SFT baseline, batched greedy full-trace decode (uses --batch_size)
  codi   : multi-frame latent decode (latent block at every <|line_sep|>)
  single : single-block CODI (one latent block, then decode the answer)
sft/codi use a per-row cap adaptive to trace_len (min(--max_new_tokens, trace_len*--len_mult));
single uses a fixed --max_new_tokens. Run via torchrun."""

import argparse
import json
import math
import os

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

from data.precompute_loader import _len, load_cache
from data.dataset import _prompt_str
from data.tokens import add_trace_tokens, token_ids
from eval.codi_infer import gen_latent, gen_single, load_codi, load_codi_single
from eval.scoring import check_correct, extract_answer_trace_full


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", required=True, choices=["sft", "codi", "single"])
    ap.add_argument("--model", required=True)
    ap.add_argument("--dataset", required=True)
    ap.add_argument("--n_samples", type=int, default=-1)
    ap.add_argument("--max_new_tokens", type=int, default=8192)  # hard ceiling (sft/codi) or fixed cap (single)
    ap.add_argument("--len_mult", type=float, default=1.5)       # sft/codi per-row cap = min(ceiling, trace_len*mult)
    ap.add_argument("--latent_steps", type=int, default=1)       # codi/single
    ap.add_argument("--batch_size", type=int, default=8)         # sft only; codi/single run per row
    ap.add_argument("--min_len", type=int, default=0)
    ap.add_argument("--max_len", type=int, default=1 << 60)
    ap.add_argument("--out", default="")
    args = ap.parse_args()

    rank = int(os.environ.get("RANK", 0))
    world = int(os.environ.get("WORLD_SIZE", 1))
    # oversubscribe: allow >1 rank per GPU (latent decode is bs=1 and uses ~3.5GB/~39% util,
    # so multiple shards/GPU fill it). rank stays unique for sharding; device wraps mod #GPUs.
    local_rank = int(os.environ.get("LOCAL_RANK", 0)) % torch.cuda.device_count()
    torch.cuda.set_device(local_rank)  # ranks independent; merge_len_shards combines

    # Per-mode: load the model + a gen_batch(batch, caps) -> [(gen_ids, n_gen, n_fwd)] closure.
    if args.mode == "sft":
        tok = AutoTokenizer.from_pretrained(args.model, use_fast=True)
        add_trace_tokens(tok)
        tok.padding_side = "left"  # left-pad so all generated tokens start at the same offset
        eot = token_ids(tok)["<|end_of_text|>"]
        model = AutoModelForCausalLM.from_pretrained(
            args.model, torch_dtype=torch.bfloat16).to(local_rank).eval()

        def gen_batch(batch, caps):
            enc = tok([_prompt_str(r["code"], r["input"]) for r in batch],
                      return_tensors="pt", padding=True, add_special_tokens=False).to(local_rank)
            with torch.no_grad():
                out = model.generate(**enc, max_new_tokens=max(caps), do_sample=False,
                                     eos_token_id=eot, pad_token_id=eot)
            res = []
            for j, cap in enumerate(caps):
                g = out[j, enc["input_ids"].shape[1]:][:cap].tolist()
                n = g.index(eot) if eot in g else len(g)  # n_fwd == n_gen (no latent)
                res.append((g, n, n))
            return res
    else:
        args.batch_size = 1  # latent decode is per-row (growing cache, per-row latent insertion)
        if args.mode == "codi":
            tok, ids, model = load_codi(args.model, args.latent_steps, local_rank)
            ls_id, act_id, eot = ids["<|line_sep|>"], ids["<|action_sep|>"], ids["<|end_of_text|>"]
        else:
            tok, ids, model = load_codi_single(args.model, args.latent_steps, local_rank)
            eot = ids["<|end_of_text|>"]

        def gen_batch(batch, caps):
            r, cap = batch[0], caps[0]
            pids = tok(_prompt_str(r["code"], r["input"]), return_tensors="pt",
                       add_special_tokens=False).to(local_rank)["input_ids"][0]
            if args.mode == "codi":
                g, n_fwd = gen_latent(model, pids, ls_id, act_id, eot, cap)
            else:
                g = gen_single(model, pids, eot, cap)
                n_fwd = len(g) + args.latent_steps + 1
            return [(g, len(g), n_fwd)]

    rows = [{"id": e["row_id"], "code": e["code"], "input": e["input"], "output": e["output"],
             "trace_len": _len(e)}
            for e in load_cache(args.dataset, min_len=args.min_len, max_len=args.max_len,
                                n_samples=args.n_samples)]
    shard = sorted(rows[rank::world], key=lambda r: r["trace_len"])  # length-homogeneous batches, balanced tail
    caps = [args.max_new_tokens if args.mode == "single"
            else min(args.max_new_tokens, math.ceil(r["trace_len"] * args.len_mult)) for r in shard]
    shard_f = open(f"{args.out}.r{rank}.jsonl", "w") if args.out else None

    n_correct = done = 0
    for bi, bs in enumerate(range(0, len(shard), args.batch_size)):
        batch, bcaps = shard[bs: bs + args.batch_size], caps[bs: bs + args.batch_size]
        for r, cap, (g, n_gen, n_fwd) in zip(batch, bcaps, gen_batch(batch, bcaps)):
            gen = tok.decode(g, skip_special_tokens=False)
            pred = extract_answer_trace_full(gen)
            ok = pred is not None and check_correct(r["code"], r["output"], pred)
            n_correct += ok
            rec = {"id": r["id"], "expected": r["output"], "predicted": pred, "correct": ok,
                   "n_gen": n_gen, "n_fwd": n_fwd, "trace_len": r["trace_len"],
                   "max_new": cap, "generation": gen}
            if shard_f:
                shard_f.write(json.dumps(rec) + "\n"); shard_f.flush()
        done += len(batch)
        if rank == 0 and (bi + 1) % 20 == 0:
            print(f"  rank0 {done}/{len(shard)}  pass@1={n_correct / done:.4f}", flush=True)
    if shard_f:
        shard_f.close()


if __name__ == "__main__":
    main()
