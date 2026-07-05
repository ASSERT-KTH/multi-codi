"""Merge per-rank {out}.r*.jsonl (written incrementally by eval_len.py) into the final --out JSON."""
import argparse
import glob
import json
import os

ap = argparse.ArgumentParser()
ap.add_argument("--out", required=True)
ap.add_argument("--max_new_tokens", type=int, default=0)
ap.add_argument("--len_mult", type=float, default=1.5)
ap.add_argument("--keep", action="store_true")
args = ap.parse_args()

shards = sorted(glob.glob(f"{args.out}.r*.jsonl"))
res = [json.loads(l) for f in shards for l in open(f) if l.strip()]
n = len(res)
if not n:
    raise SystemExit(f"no rows in {args.out}.r*.jsonl")
nc = sum(r["correct"] for r in res)
nf = sum(r["predicted"] is not None for r in res)
mean_fwd = sum(r["n_fwd"] for r in res) / n
mean_gen = sum(r["n_gen"] for r in res) / n
json.dump({"pass_at_1": nc / n, "valid_format": nf / n, "n": n,
           "max_new_tokens": args.max_new_tokens, "len_mult": args.len_mult,
           "mean_fwd": mean_fwd, "mean_gen": mean_gen, "results": res}, open(args.out, "w"), indent=2)
print(f"merged {len(shards)} shards  pass@1={nc / n:.4f} valid_format={nf / n:.4f} "
      f"(n={n}) mean_fwd={mean_fwd:.1f} mean_gen={mean_gen:.1f}", flush=True)
if not args.keep:
    for f in shards:
        os.remove(f)
