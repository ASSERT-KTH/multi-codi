"""Per-sample raw metrics for the train pool (codi_train_full, <=3072 filter) and the
cruxeval-O test set (cruxeval_codi cache), saved as npz for fine-grained plotting.

Four axes, per CODI example (== what the model sees):
  frames     = len(spans)                        (# LINE frames / latent spans)
  nvars      = distinct local var names          (re-traced, ground_truth_trace)
  locals_len = mean token len of each frame's locals = mean(j-i-1 over spans)
  trace_len  = len(trace_ids)                    (total trace tokens)

frames/locals_len/trace_len come straight from the cache (exact); only nvars is re-traced.
Run from codi_trace/:  python -m data.diag.extract_dist_raw
"""
import multiprocessing as mp
import signal

import numpy as np
from datasets import load_from_disk

from data.ground_truth import ground_truth_trace
from data.trace_format import TraceEvent

MAX_FRAMES = 1024
TIMEOUT = 5


def _len(e):
    return len(e["prompt_ids"]) + len(e["trace_ids"])


def _alarm(*_):
    raise TimeoutError


def _init():
    signal.signal(signal.SIGALRM, _alarm)


def _nvars(args):
    code, inp = args
    signal.alarm(TIMEOUT)
    try:
        frames, err = ground_truth_trace(code, inp, align_to_prompt=True, max_frames=MAX_FRAMES)
        if err or not frames:
            return -1
        state = [f for f in frames if f.event in (TraceEvent.CALL, TraceEvent.LINE)]
        if not state:
            return -1
        return len({n for f in state for n in (f.full_locals or {})})
    except Exception:
        return -1
    finally:
        signal.alarm(0)


def collect(cache_dir, max_len=None):
    ds = load_from_disk(cache_dir)
    rows = [e for e in ds if (max_len is None or _len(e) <= max_len)]
    frames = np.array([len(e["spans"]) for e in rows], dtype=np.int32)
    trace_len = np.array([len(e["trace_ids"]) for e in rows], dtype=np.int32)
    locals_len = np.array(
        [np.mean([j - i - 1 for i, j in e["spans"]]) if e["spans"] else 0.0 for e in rows],
        dtype=np.float32,
    )
    with mp.Pool(min(64, mp.cpu_count()), _init) as pool:
        nvars = np.array(
            list(pool.imap(_nvars, [(e["code"], e["input"]) for e in rows], chunksize=64)),
            dtype=np.int32,
        )
    print(f"{cache_dir}: n={len(rows)}  nvars_failed={(nvars < 0).sum()}")
    return dict(frames=frames, nvars=nvars, locals_len=locals_len, trace_len=trace_len)


def main():
    out = {}
    train = collect("data/cache/codi_train_full", max_len=3072)
    crux = collect("data/cache/cruxeval_codi", max_len=None)
    for k, v in train.items():
        out["train_" + k] = v
    for k, v in crux.items():
        out["crux_" + k] = v
    path = "data/diag/dist_raw.npz"
    np.savez(path, **out)
    print("wrote", path, "train_n", len(train["frames"]), "crux_n", len(crux["frames"]))


if __name__ == "__main__":
    main()
