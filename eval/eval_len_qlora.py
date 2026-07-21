"""Length-binned held-out eval for a QLoRA adapter checkpoint (train_codi_qlora.py
output), MODE=codi only (multi-frame latent decode -- the only mode QLoRA checkpoints
were trained for). Mirrors eval_len.py's sharding/scoring/output format exactly so
results are directly comparable/mergeable with the rest of results/; only model
loading differs (base_model + adapter_dir instead of a single --model dir), via
eval.codi_infer_qlora.load_codi_qlora. Run via torchrun."""

import argparse
import json
import math
import os

import torch

from data.precompute_loader import _len, load_cache
from data.dataset import _prompt_str
from eval.codi_infer import gen_latent
from eval.codi_infer_qlora import load_codi_qlora
from eval.scoring import check_correct, extract_answer_trace_full


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base_model", required=True)
    ap.add_argument("--adapter_dir", required=True)
    ap.add_argument("--dataset", required=True)
    ap.add_argument("--n_samples", type=int, default=-1)
    ap.add_argument("--max_new_tokens", type=int, default=16384)
    ap.add_argument("--len_mult", type=float, default=1.5)
    ap.add_argument("--latent_steps", type=int, default=1)
    ap.add_argument("--min_len", type=int, default=0)
    ap.add_argument("--max_len", type=int, default=1 << 60)
    ap.add_argument("--out", default="")
    ap.add_argument("--sliding_window", type=int, default=0)
    ap.add_argument("--attn_impl", default="flash_attention_2")
    ap.add_argument("--load_in_4bit", type=int, default=1)  # match QLoRA training precision
    args = ap.parse_args()

    rank = int(os.environ.get("RANK", 0))
    world = int(os.environ.get("WORLD_SIZE", 1))
    local_rank = int(os.environ.get("LOCAL_RANK", 0)) % torch.cuda.device_count()
    torch.cuda.set_device(local_rank)

    tok, ids, model = load_codi_qlora(args.base_model, args.adapter_dir, args.latent_steps, local_rank,
                                      sw=args.sliding_window, attn_impl=args.attn_impl,
                                      load_in_4bit=bool(args.load_in_4bit))
    ls_id, act_id, eot = ids["<|line_sep|>"], ids["<|action_sep|>"], ids["<|end_of_text|>"]

    def gen_batch(batch, caps):
        r, cap = batch[0], caps[0]
        pids = tok(_prompt_str(r["code"], r["input"]), return_tensors="pt",
                   add_special_tokens=False).to(local_rank)["input_ids"][0]
        g, n_fwd = gen_latent(model, pids, ls_id, act_id, eot, cap)
        return [(g, len(g), n_fwd)]

    rows = [{"id": e["row_id"], "code": e["code"], "input": e["input"], "output": e["output"],
             "trace_len": _len(e)}
            for e in load_cache(args.dataset, min_len=args.min_len, max_len=args.max_len,
                                n_samples=args.n_samples)]
    shard = sorted(rows[rank::world], key=lambda r: r["trace_len"])
    caps = [min(args.max_new_tokens, math.ceil(r["trace_len"] * args.len_mult)) for r in shard]
    shard_f = open(f"{args.out}.r{rank}.jsonl", "w") if args.out else None

    n_correct = done = 0
    for i, (r, cap) in enumerate(zip(shard, caps)):
        g, n_gen, n_fwd = gen_batch([r], [cap])[0]
        gen = tok.decode(g, skip_special_tokens=False)
        pred = extract_answer_trace_full(gen)
        ok = pred is not None and check_correct(r["code"], r["output"], pred)
        n_correct += ok
        rec = {"id": r["id"], "expected": r["output"], "predicted": pred, "correct": ok,
               "n_gen": n_gen, "n_fwd": n_fwd, "trace_len": r["trace_len"],
               "max_new": cap, "generation": gen}
        if shard_f:
            shard_f.write(json.dumps(rec) + "\n"); shard_f.flush()
        done += 1
        if rank == 0 and (i + 1) % 20 == 0:
            print(f"  rank0 {done}/{len(shard)}  pass@1={n_correct / done:.4f}", flush=True)
    if shard_f:
        shard_f.close()


if __name__ == "__main__":
    main()
