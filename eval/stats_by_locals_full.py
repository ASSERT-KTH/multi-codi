"""Stratify the SFT-vs-CODI comparison by locals complexity, with the full metric
set and budget logic of eval.stats_by_length (not just pass@1/valid_fmt like
eval.stats_by_locals). axis=nvars: #distinct local names; axis=locals_len: mean
rendered-locals size per state frame (chars, model-independent). The axis key is a
property of the CRUXEval item, computed once per id and shared across all runs.
Over-budget (n_fwd >= max_new) rows are truncated -> invalid -> wrong. Run from codi_trace/:
    python -m eval.stats_by_locals_full --results sft15.json codi15.json sft3b.json codi3b.json \
        --labels sft1.5b codi1.5b sft3b codi3b --axis nvars
"""

import argparse
import json

from data.ground_truth import ground_truth_trace
from data.sources import load_cruxeval
from data.trace_format import TraceEvent

EDGES = {"nvars": [1, 2, 3, 4, 5, 6], "locals_len": [0, 16, 24, 32, 48, 64],
         "nframes": [1, 2, 3, 4, 5, 7, 11, 21]}


def load_id_index(caches):
    """id -> {code,input} from precomputed codi caches (data/cache/*). Falls back to
    load_cruxeval() when no cache dir is given. The eval's held-out set spans several
    source datasets (cruxeval_codi + long-tail codi_train), so resolving through
    load_cruxeval() alone silently drops the ~500 non-CRUXEval rows into 'untraceable'.
    """
    if not caches:
        return {str(r["id"]): r for r in load_cruxeval()}
    from datasets import load_from_disk
    idx = {}
    for c in caches:
        for e in load_from_disk(c):
            idx.setdefault(str(e["row_id"]), {"code": e["code"], "input": e["input"]})
    return idx


def axis_metric(code, input_str, axis, max_frames):
    frames, err = ground_truth_trace(code, input_str, align_to_prompt=True, max_frames=max_frames)
    state = [f for f in frames if f.event in (TraceEvent.CALL, TraceEvent.LINE)] if not err else []
    if not state:
        return None
    if axis == "nvars":
        return len({n for f in state for n in (f.full_locals or {})})
    if axis == "nframes":  # #LINE frames = #latent spans = #KD anchors
        return sum(1 for f in state if f.event == TraceEvent.LINE)
    sizes = [len(json.dumps(f.locals or {})) for f in state]
    return sum(sizes) / len(sizes)


def label(edges, k):
    for lo, hi in zip(edges, edges[1:]):
        if lo <= k < hi:
            return f"{lo}-{hi - 1}" if hi - 1 > lo else f"{lo}"
    return f"{edges[-1]}+"


def order(lbl):
    return (1e9, 0) if lbl == "untraceable" else (0, int(lbl.split("-")[0].rstrip("+")))


def new_bin():
    return {"n": 0, "correct": 0, "valid": 0, "fwd": 0, "gen": 0, "ratio": 0.0, "trunc": 0}


def bin_run(path, key_of, edges):
    d = json.load(open(path))
    default_cap = d.get("max_new_tokens", 1 << 60)
    bins = {}
    for r in d["results"]:
        rid = str(r["id"])
        if rid not in key_of:        # filtered out by --subset
            continue
        k = key_of[rid]
        lb = "untraceable" if k is None else label(edges, k)
        b = bins.setdefault(lb, new_bin())
        in_budget = r.get("n_fwd", 0) < r.get("max_new", default_cap)
        b["n"] += 1
        b["valid"] += int(in_budget and r.get("predicted") is not None)
        b["correct"] += int(in_budget and bool(r["correct"]))
        b["fwd"] += r.get("n_fwd", 0)
        b["gen"] += r.get("n_gen", 0)
        b["ratio"] += r.get("n_fwd", 0) / r["trace_len"] if r["trace_len"] else 0
        b["trunc"] += int(not in_budget)
    return bins


def totals(bins):
    tot = new_bin()
    for b in bins.values():
        for k in tot:
            tot[k] += b[k]
    return tot


def m(b):
    """Derived metrics for one accumulator."""
    n = b["n"]
    return {
        "pass1": b["correct"] / n,
        "valid": 100 * b["valid"] / n,
        "condAcc": b["correct"] / b["valid"] if b["valid"] else 0.0,
        "gen": b["gen"] / n,
        "fwd": b["fwd"] / n,
        "ratio": b["ratio"] / n,
        "trunc": 100 * b["trunc"] / n,
    }


def fmt_run_row(lb, b):
    x = m(b)
    return (f"| {lb} | {b['n']} | {x['pass1']:.3f} | {x['valid']:.0f}% | {x['condAcc']:.3f} | "
            f"{x['gen']:.0f} | {x['fwd']:.0f} | {x['ratio']:.2f} | {x['trunc']:.0f}% |")


def sgn(v, dec, pct=False):
    s = f"{v:+.{dec}f}"
    return s + ("" if not pct else "")


def fmt_delta_row(lb, n, base, comp):
    a, c = m(base), m(comp)
    return (f"| {lb} | {n} | {c['pass1'] - a['pass1']:+.3f} | {c['valid'] - a['valid']:+.0f} | "
            f"{c['condAcc'] - a['condAcc']:+.3f} | {c['gen'] - a['gen']:+.0f} | {c['fwd'] - a['fwd']:+.0f} | "
            f"{c['ratio'] - a['ratio']:+.2f} | {c['trunc'] - a['trunc']:+.0f} |")


HDR = "| {axis} | n | pass@1 | valid% | condAcc | mean_gen | mean_fwd | fwd/ref | trunc% |"
SEP = "|---|--:|--:|--:|--:|--:|--:|--:|--:|"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--results", nargs="+", required=True,
                    help="ordered: sft1.5 codi1.5 sft3b codi3b")
    ap.add_argument("--labels", nargs="+", required=True)
    ap.add_argument("--axis", choices=["nvars", "locals_len", "nframes"], default="nvars")
    ap.add_argument("--edges", default="")
    ap.add_argument("--max_frames", type=int, default=20000)
    ap.add_argument("--caches", nargs="*", default=None,
                    help="codi cache dirs for id->code/input (else load_cruxeval)")
    ap.add_argument("--subset", choices=["all", "crux", "long"], default="all",
                    help="crux=sample_* ids only; long=the non-CRUXEval held-out tail")
    args = ap.parse_args()

    edges = sorted(int(x) for x in args.edges.split(",")) if args.edges else EDGES[args.axis]

    # axis key per id, computed once (data property, shared across runs)
    by_id = load_id_index(args.caches)
    ids = [str(r["id"]) for r in json.load(open(args.results[0]))["results"]]
    keep = {"all": lambda i: True, "crux": lambda i: i.startswith("sample_"),
            "long": lambda i: not i.startswith("sample_")}[args.subset]
    ids = [i for i in ids if keep(i)]
    key_of = {}
    for i in ids:
        row = by_id.get(i)
        key_of[i] = None if row is None else axis_metric(row["code"], row["input"], args.axis, args.max_frames)

    runs = {lab: bin_run(p, key_of, edges) for lab, p in zip(args.labels, args.results)}
    all_bins = sorted({b for r in runs.values() for b in r}, key=order)

    axname = args.axis + ("(chr)" if args.axis == "locals_len" else "")

    print(f"# axis = {args.axis}  edges = {edges}\n")
    # per-run tables
    for lab in args.labels:
        bins = runs[lab]
        print(f"### {lab}\n")
        print(HDR.format(axis=axname));  print(SEP)
        for lb in all_bins:
            if lb in bins:
                print(fmt_run_row(lb, bins[lb]))
        print(fmt_run_row("**ALL**", totals(bins)))
        print()

    # delta tables, paired by scale: (labels[0],labels[1]) and (labels[2],labels[3])
    pairs = [(args.labels[1], args.labels[0]), (args.labels[3], args.labels[2])] if len(args.labels) >= 4 \
        else [(args.labels[1], args.labels[0])]
    for comp, base in pairs:
        print(f"### {comp} − {base}\n")
        print(HDR.format(axis=axname));  print(SEP)
        for lb in all_bins:
            if lb in runs[comp] and lb in runs[base]:
                print(fmt_delta_row(lb, runs[base][lb]["n"], runs[base][lb], runs[comp][lb]))
        print(fmt_delta_row("**ALL**", totals(runs[base])["n"], totals(runs[base]), totals(runs[comp])))
        print()


if __name__ == "__main__":
    main()
