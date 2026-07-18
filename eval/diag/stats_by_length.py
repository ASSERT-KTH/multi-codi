"""Length-binned SFT-vs-CODI comparison over eval_len.py --out JSONs. Run from codi_trace/:
    python -m eval.diag.stats_by_length --results sft15.json codi15.json --labels sft1.5b codi1.5b
Over-budget (n_fwd >= max_new) rows are truncated -> invalid -> wrong.
"""

import argparse
import json

from eval.diag.binstats import bin_label, order

EDGES = [0, 256, 512, 1024, 2048, 3072, 4096, 8192, 16384, 24576, 32768, 40960]  # canonical + 8K-wide long tail


def bin_run(path):
    d = json.load(open(path))
    default_cap = d.get("max_new_tokens", 1 << 60)
    bins = {}
    for r in d["results"]:
        b = bins.setdefault(bin_label(EDGES, r["trace_len"]),
                            {"n": 0, "correct": 0, "valid": 0, "fwd": 0, "gen": 0, "ratio": 0.0, "trunc": 0})
        in_budget = r.get("n_fwd", 0) < r.get("max_new", default_cap)
        b["n"] += 1
        b["valid"] += int(in_budget and r.get("predicted") is not None)
        b["correct"] += int(in_budget and bool(r["correct"]))
        b["fwd"] += r.get("n_fwd", 0)
        b["gen"] += r.get("n_gen", 0)
        b["ratio"] += r.get("n_fwd", 0) / r["trace_len"] if r["trace_len"] else 0
        b["trunc"] += int(not in_budget)
    return bins


def fmt_row(lb, b):
    ca = b["correct"] / b["valid"] if b["valid"] else 0.0
    return (f"{lb:>12} {b['n']:>5} {b['correct'] / b['n']:>8.4f} {100 * b['valid'] / b['n']:>6.1f}% "
            f"{ca:>8.4f} {b['gen'] / b['n']:>9.1f} {b['fwd'] / b['n']:>9.1f} {b['ratio'] / b['n']:>8.2f} "
            f"{100 * b['trunc'] / b['n']:>6.1f}%")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--results", nargs="+", required=True)
    ap.add_argument("--labels", nargs="+", default=None)
    ap.add_argument("--out", default="")
    args = ap.parse_args()
    labels = args.labels or [p.split("/")[-1].removesuffix(".json") for p in args.results]
    runs = {lab: bin_run(p) for lab, p in zip(labels, args.results)}
    all_bins = sorted({b for r in runs.values() for b in r}, key=order)

    for lab in labels:
        bins = runs[lab]
        print(f"\n== {lab}")
        print(f"{'trace_len':>12} {'n':>5} {'pass@1':>8} {'valid%':>7} {'condAcc':>8} "
              f"{'mean_gen':>9} {'mean_fwd':>9} {'fwd/ref':>8} {'trunc%':>7}")
        tot = {"n": 0, "correct": 0, "valid": 0, "fwd": 0, "gen": 0, "ratio": 0.0, "trunc": 0}
        for lb in all_bins:
            b = bins.get(lb)
            if not b:
                continue
            print(fmt_row(lb, b))
            for k in tot:
                tot[k] += b[k]
        print(fmt_row("ALL", tot))

    print("\n== pass@1 by length")
    print(f"{'trace_len':>12} " + " ".join(f"{lab:>10}" for lab in labels))
    for lb in all_bins:
        cells = [f"{runs[lab][lb]['correct'] / runs[lab][lb]['n']:>10.4f}" if lb in runs[lab] else f"{'-':>10}"
                 for lab in labels]
        print(f"{lb:>12} " + " ".join(cells))

    if args.out:
        json.dump({"edges": EDGES, "runs": runs}, open(args.out, "w"), indent=2)


if __name__ == "__main__":
    main()
