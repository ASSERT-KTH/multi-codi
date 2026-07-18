"""pass@1 of a CRUXEval-O eval JSON stratified by a ground-truth difficulty axis. Run from codi_trace/:
    python -m eval.diag.stats_by_axis --results r.json --axis frames
    python -m eval.diag.stats_by_axis --results r.json --axis nvars
    python -m eval.diag.stats_by_axis --results r.json --axis locals_len --model <ckpt>
axis: frames = #LINE frames; nvars = #distinct local names; locals_len = mean rendered-locals size
per state frame (chars, or tokens with --model)."""

import argparse
import json

from data.ground_truth import ground_truth_trace
from data.dataset import load_dataset
from data.trace_format import TraceEvent
from eval.diag.binstats import bin_label, order

EDGES = {"frames": [1, 2, 3, 4, 5, 7, 11, 21], "nvars": [1, 2, 3, 4, 5, 6], "locals_len": [0, 16, 24, 32, 48, 64]}


def metric(code, input_str, axis, max_frames, tok):
    frames, err = ground_truth_trace(code, input_str, align_to_prompt=True, max_frames=max_frames)
    if err or not frames:
        return None
    if axis == "frames":
        return sum(f.event == TraceEvent.LINE for f in frames)
    state = [f for f in frames if f.event in (TraceEvent.CALL, TraceEvent.LINE)]
    if not state:
        return None
    if axis == "nvars":
        return len({n for f in state for n in (f.full_locals or {})})
    sizes = [json.dumps(f.locals or {}) for f in state]
    return sum(len(tok(s, add_special_tokens=False)["input_ids"]) if tok else len(s) for s in sizes) / len(sizes)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--results", required=True)
    ap.add_argument("--axis", choices=["frames", "nvars", "locals_len"], default="frames")
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
    by_id = {str(r["id"]): r for r in load_dataset("cruxeval")}

    buckets, missing = {}, 0
    for r in res:
        row = by_id.get(str(r["id"]))
        if row is None:
            missing += 1
            continue
        k = metric(row["code"], row["input"], args.axis, args.max_frames, tok)
        b = buckets.setdefault("untraceable" if k is None else bin_label(edges, k), [0, 0, 0])
        b[0] += 1
        b[1] += int(bool(r["correct"]))
        b[2] += int(r.get("predicted") is not None)

    unit = ("tok" if tok else "chr") if args.axis == "locals_len" else ""
    print(f"{args.axis + (f'({unit})' if unit else ''):>14} {'n':>5} {'pass@1':>8} {'valid_fmt':>10}")
    tot, table = [0, 0, 0], []
    for lbl in sorted(buckets, key=order):
        n, c, fmt = buckets[lbl]
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
