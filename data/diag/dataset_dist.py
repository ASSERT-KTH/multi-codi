"""Per-dataset trace-complexity distributions: LINE frames / nvars / locals_len / trace_len.
locals_len, trace_len = TOKEN counts under the precompute tokenizer (Qwen2.5-Coder-1.5B +
trace tokens); trace_len == cache trace_ids length. Parallel + per-row timeout like precompute.py.
Run from codi_trace/:
    python -m data.diag.dataset_dist
"""

import argparse
import contextlib
import io
import json
import multiprocessing as mp
import signal

from data.ground_truth import ground_truth_trace
from data.sources import load_one
from data.trace_format import TraceEvent, render_frames_to_generation
from data.tokens import add_trace_tokens

EDGES = {"frames": [1, 2, 3, 4, 5, 7, 11, 21], "nvars": [1, 2, 3, 4, 5, 6],
         "locals_len": [0, 8, 12, 16, 24, 32], "trace_len": [0, 256, 512, 1024, 2048, 3072, 4096]}

TOK = MAX_FRAMES = TIMEOUT = None


def load_tokenizer(model):
    from transformers import AutoTokenizer
    tok = AutoTokenizer.from_pretrained(model, use_fast=True)
    add_trace_tokens(tok)
    return tok


def metrics(code, inp, max_frames, tok):
    """(n_line_frames, nvars, mean locals tokens, trace tokens); None if untraceable."""
    frames, err = ground_truth_trace(code, inp, align_to_prompt=True, max_frames=max_frames)
    nf = None if (err or not frames) else sum(f.event == TraceEvent.LINE for f in frames)
    state = [] if err else [f for f in (frames or []) if f.event in (TraceEvent.CALL, TraceEvent.LINE)]
    if not state:
        return nf, None, None, None
    nv = len({n for f in state for n in (f.full_locals or {})})
    enc = lambda s: len(tok.encode(s, add_special_tokens=False))
    ll = sum(enc(json.dumps(f.locals or {})) for f in state) / len(state)
    tl = enc(render_frames_to_generation(frames))
    return nf, nv, ll, tl


def _alarm(*_):
    raise TimeoutError


def _init(model, max_frames, timeout):
    global TOK, MAX_FRAMES, TIMEOUT
    TOK, MAX_FRAMES, TIMEOUT = load_tokenizer(model), max_frames, timeout
    signal.signal(signal.SIGALRM, _alarm)


def _work(row):
    signal.alarm(TIMEOUT)
    try:
        with contextlib.redirect_stdout(io.StringIO()):  # snippets print to stdout
            return metrics(row["code"], row["input"], MAX_FRAMES, TOK)
    except Exception:
        return (None, None, None, None)
    finally:
        signal.alarm(0)


def label(edges, k):
    for lo, hi in zip(edges, edges[1:]):
        if lo <= k < hi:
            return f"{lo}-{hi - 1}" if hi - 1 > lo else f"{lo}"
    return f"{edges[-1]}+"


def order(l):
    return (1e9,) if l == "untraceable" else (int(l.split("-")[0].rstrip("+")),)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sources", default="cruxeval,mbpp,humaneval,pyx")
    ap.add_argument("--max_frames", type=int, default=5000)
    ap.add_argument("--model", default="model_weights/qwen2.5-coder-1.5b")
    ap.add_argument("--workers", type=int, default=max(1, mp.cpu_count() // 2))
    ap.add_argument("--timeout", type=int, default=5)
    args = ap.parse_args()

    for name in (s.strip() for s in args.sources.split(",")):
        rows = load_one(name)
        pool = mp.Pool(args.workers, _init, (args.model, args.max_frames, args.timeout))
        bins = {ax: {} for ax in EDGES}
        for m in pool.imap_unordered(_work, rows, chunksize=32):
            for ax, k in zip(EDGES, m):
                l = "untraceable" if k is None else label(EDGES[ax], k)
                bins[ax][l] = bins[ax].get(l, 0) + 1
        pool.close()
        pool.join()
        for ax in EDGES:
            b = bins[ax]
            tot = sum(b.values())
            print(f"\n== {name}  axis={ax}  ({tot} rows)")
            for l, n in sorted(b.items(), key=lambda kv: order(kv[0])):
                print(f"{l:>12} {n:>6} {n / tot:>8.4f}")


if __name__ == "__main__":
    main()
