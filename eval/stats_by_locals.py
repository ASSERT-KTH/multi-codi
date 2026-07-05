"""Stratify a CRUXEval-O eval by the SFT-CoT's locals complexity (pass@1 per bin).
Companion to eval.stats_by_frames. axis=nvars: #distinct local names; axis=locals_len:
mean rendered-locals size per state frame (chars, or tokens with --model). Run from codi_trace/:
    python -m eval.stats_by_locals --results r.json --axis nvars
    python -m eval.stats_by_locals --results r.json --axis locals_len --model <ckpt>
"""

import argparse
import json

from data.ground_truth import ground_truth_trace
from data.sources import load_cruxeval
from data.trace_format import TraceEvent

EDGES = {"nvars": [1, 2, 3, 4, 5, 6], "locals_len": [0, 16, 24, 32, 48, 64]}


def metric(code, input_str, axis, max_frames, tok):
    frames, err = ground_truth_trace(code, input_str, align_to_prompt=True, max_frames=max_frames)
    state = [f for f in frames if f.event in (TraceEvent.CALL, TraceEvent.LINE)] if not err else []
    if not state:
        return None
    if axis == "nvars":
        return len({n for f in state for n in (f.full_locals or {})})
    sizes = [json.dumps(f.locals or {}) for f in state]
    return sum(len(tok(s, add_special_tokens=False)["input_ids"]) if tok else len(s) for s in sizes) / len(sizes)


def label(edges, k):
    for lo, hi in zip(edges, edges[1:]):
        if lo <= k < hi:
            return f"{lo}-{hi - 1}" if hi - 1 > lo else f"{lo}"
    return f"{edges[-1]}+"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--results", required=True)
    ap.add_argument("--axis", choices=["nvars", "locals_len"], default="nvars")
    ap.add_argument("--edges", default="")
    ap.add_argument("--model", default="", help="tokenizer; locals_len in tokens (else chars)")
    ap.add_argument("--max_frames", type=int, default=5000)
    ap.add_argument("--out", default="")
    args = ap.parse_args()

    edges = sorted(int(x) for x in args.edges.split(",")) if args.edges else EDGES[args.axis]
    tok = None
    if args.axis == "locals_len" and args.model:
        from transformers import AutoTokenizer
        tok = AutoTokenizer.from_pretrained(args.model, use_fast=True)
    res = json.load(open(args.results))["results"]
    by_id = {str(r["id"]): r for r in load_cruxeval()}

    buckets, missing = {}, 0
    for r in res:
        row = by_id.get(str(r["id"]))
        if row is None:
            missing += 1
            continue
        k = metric(row["code"], row["input"], args.axis, args.max_frames, tok)
        b = buckets.setdefault("untraceable" if k is None else label(edges, k), [0, 0, 0])
        b[0] += 1
        b[1] += int(bool(r["correct"]))
        b[2] += int(r.get("predicted") is not None)

    order = lambda lbl: (1e9, 0) if lbl == "untraceable" else (0, int(lbl.split("-")[0].rstrip("+")))
    unit = ("tok" if tok else "chr") if args.axis == "locals_len" else ""
    print(f"{args.axis + (f'({unit})' if unit else ''):>14} {'n':>5} {'pass@1':>8} {'valid_fmt':>10}")
    tot, table = [0, 0, 0], []
    for lbl, (n, c, fmt) in sorted(buckets.items(), key=lambda kv: order(kv[0])):
        print(f"{lbl:>14} {n:>5} {c / n:>8.4f} {fmt / n:>10.4f}")
        table.append({"bin": lbl, "n": n, "pass_at_1": c / n, "valid_format": fmt / n})
        tot = [a + b for a, b in zip(tot, (n, c, fmt))]
    n, c, fmt = tot
    print(f"{'ALL':>14} {n:>5} {c / n:>8.4f} {fmt / n:>10.4f}"
          + (f"   ({missing} ids not in CRUXEval-O)" if missing else ""))
    if args.out:
        json.dump({"axis": args.axis, "unit": unit, "edges": edges, "bins": table,
                   "all": {"n": n, "pass_at_1": c / n, "valid_format": fmt / n}}, open(args.out, "w"), indent=2)


if __name__ == "__main__":
    main()
