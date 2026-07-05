"""Trace-complexity distribution of the data TRAINING ACTUALLY USES.
Also reports seeded RandomSampler prefixes, matching CODI training. Run from codi_trace/:
    python -m data.diag.train_used_dist --cache_dir data/cache/codi_train --max_seq_len 3072
"""

import argparse
import contextlib
import io
import logging
import math

import torch
from data.cache import _len, load_cache
from data.dataset import rows_for_sources
from data.diag.dataset_dist import EDGES, label, load_tokenizer, metrics, order


def show(title, bins):
    for ax in EDGES:
        b = bins[ax]
        tot = sum(b.values())
        print(f"\n== {title}  axis={ax}  ({tot} rows)")
        for l, n in sorted(b.items(), key=lambda kv: order(kv[0])):
            print(f"{l:>12} {n:>6} {n / tot:>8.4f}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cache_dir", default="data/cache/codi_train")
    ap.add_argument("--sources", default="mbpp,humaneval,pyx")
    ap.add_argument("--max_seq_len", type=int, default=3072)  # codi_multi.sbatch value
    ap.add_argument("--n_samples", type=int, default=-1)
    ap.add_argument("--max_frames", type=int, default=256)  # precompute value
    ap.add_argument("--model", default="model_weights/qwen2.5-coder-1.5b")
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--prefix_fracs", default="0.15,0.30")
    args = ap.parse_args()
    logging.disable(logging.CRITICAL)
    tok = load_tokenizer(args.model)
    fracs = [float(x) for x in args.prefix_fracs.split(",") if x.strip()]

    ex = load_cache(args.cache_dir)
    kept_before_n = [e for e in ex if _len(e) <= args.max_seq_len]
    kept = load_cache(args.cache_dir, max_len=args.max_seq_len, n_samples=args.n_samples)
    by_id = {str(r["id"]): r for r in rows_for_sources(tuple(s.strip() for s in args.sources.split(",")))}
    clipped = "" if args.n_samples <= 0 else f" -> n_samples {len(kept)}"
    print(f"cache {len(ex)} -> kept {len(kept_before_n)} at max_seq_len<={args.max_seq_len}{clipped} "
          f"({len(ex) - len(kept_before_n)} dropped by length, {len(kept) / len(ex):.3f} final)")
    g = torch.Generator().manual_seed(args.seed)
    order_idx = torch.randperm(len(kept), generator=g).tolist()
    prefix_sets = {f: set(order_idx[:math.ceil(len(kept) * f)]) for f in fracs}

    all_bins = {ax: {} for ax in EDGES}
    prefix_bins = {f: {ax: {} for ax in EDGES} for f in fracs}
    for i, e in enumerate(kept):
        row = by_id[e["row_id"]]
        try:
            with contextlib.redirect_stdout(io.StringIO()):  # snippets print to stdout
                _, nv, ll, _ = metrics(row["code"], row["input"], args.max_frames, tok)
        except Exception:
            nv = ll = None
        vals = {"frames": len(e["spans"]), "nvars": nv, "locals_len": ll,
                "trace_len": len(e["trace_ids"])}
        for bins in [all_bins] + [prefix_bins[f] for f in fracs if i in prefix_sets[f]]:
            for ax, k in vals.items():
                l = "untraceable" if k is None else label(EDGES[ax], k)
                bins[ax][l] = bins[ax].get(l, 0) + 1

    show("train-used ALL", all_bins)
    for f in fracs:
        show(f"train-prefix {100 * f:g}% seed={args.seed}", prefix_bins[f])


if __name__ == "__main__":
    main()
