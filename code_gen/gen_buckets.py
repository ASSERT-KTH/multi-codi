"""Batch-generate across 26 token-length buckets, 5 independent-seed shards each.
Each shard is its own forked process end-to-end (graph sampling + codegen + writing its
own file, no merge step) and loads its own tokenizer -- the HF fast tokenizer's Rayon
thread pool doesn't survive fork (children inherit the pool's bookkeeping but not its
actual OS threads, so a shared/pre-loaded tokenizer panics in every child). Resumable:
a shard already at its target is skipped, a partial one is appended to.

    python gen_buckets.py --workers 32
"""
from __future__ import annotations
import argparse, itertools, multiprocessing as mp, os, random, signal, sys, time

os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")
# each worker is single-threaded Python + one tokenizer call at a time; without this,
# every worker's numpy/torch import tries to grab its own BLAS thread pool and dozens of
# processes doing that at once exhausts the box's thread limit (pthread_create errors).
for _v in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import graph, code_gen

OUT_ROOT = os.path.join(HERE, "gen")
N_SHARDS = 10
TOKENIZER = os.path.join(HERE, "..", "model_weights/sft1.5b_lr2e5_bs32/checkpoint-6936")

# (lo, hi, total_target) -- k = 1024, 200/shard * 10 shards = 2000 for every bucket
# everything below 4096 is handled by a separately-tuned sub-task instead (see
# supplement_par*.py) -- default settings can't reliably hit those tight targets.
BUCKETS = [(lo, hi, 2000) for lo, hi in [
    (4096, 5120), (5120, 6144), (6144, 8192),
    (8192, 12288), (12288, 16384), (16384, 20480),
    (20480, 24576), (24576, 32768), (32768, 40960),
    (40960, 53248), (53248, 65536), (65536, 81920),
    (81920, 98304), (98304, 122880), (122880, 147456),
    (147456, 172032), (172032, 196608), (196608, 221184),
    (221184, 245760),
]]


def _jobs():
    for bi, (lo, hi, total) in enumerate(BUCKETS):
        shard_target = total // N_SHARDS
        label = f"{lo}-{hi}"
        for i in range(N_SHARDS):
            yield label, lo, hi, i, shard_target, bi * N_SHARDS + i


def _out_path(label, shard_idx):
    return os.path.join(OUT_ROOT, label, f"shard{shard_idx}.jsonl")


def _existing(label, shard_idx):
    p = _out_path(label, shard_idx)
    if not os.path.exists(p):
        return 0
    with open(p) as f:
        return sum(1 for _ in f)


def _load_tokenizer(path):
    from transformers import AutoTokenizer
    from data.tokens import add_trace_tokens
    tok = AutoTokenizer.from_pretrained(path)
    add_trace_tokens(tok)
    return tok


def _run_shard(tok, label, lo, hi, shard_idx, shard_target, seed):
    existing = _existing(label, shard_idx)
    remaining = shard_target - existing
    if remaining <= 0:
        return
    rng = random.Random(seed)
    progs = (graph.sample(rng) for _ in itertools.count())
    base_hi = min(max(hi * 50, 2000), 3_000_000)   # cheap early-abort for oversized candidates
    with open(_out_path(label, shard_idx), "a") as out_f:
        code_gen.generate(progs, seed, tok, out_f, tok_lo=lo, tok_hi=hi, base_hi=base_hi,
                           samples=remaining, start_id=existing, skip=existing)


def _worker(job, tokenizer_path):
    # children must not inherit the parent's cleanup handler (it manages the parent's
    # own process table, not this child's) -- fall back to default disposition.
    signal.signal(signal.SIGTERM, signal.SIG_DFL)
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    label, lo, hi, shard_idx, shard_target, seed = job
    out_dir = os.path.join(OUT_ROOT, label)
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, f"shard{shard_idx}.log"), "a") as log_f:
        # dup2 onto fd 1/2 (not just sys.stdout) -- OpenBLAS/tokenizer warnings write
        # straight to the C-level fd, so with N workers all inheriting the same shared
        # driver.log fd, they were all fighting over one file instead of their own.
        os.dup2(log_f.fileno(), 1)
        os.dup2(log_f.fileno(), 2)
        try:
            tok = _load_tokenizer(tokenizer_path)
            _run_shard(tok, label, lo, hi, shard_idx, shard_target, seed)
        except Exception as e:
            print(f"[{label} shard{shard_idx}] FAILED: {e}", flush=True)


def _report():
    for lo, hi, total in BUCKETS:
        label = f"{lo}-{hi}"
        counts = [_existing(label, i) for i in range(N_SHARDS)]
        print(f"  {label:>13}: {sum(counts):>5}/{total}  {counts}", flush=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--workers", type=int, default=os.cpu_count())
    ap.add_argument("--tokenizer", default=TOKENIZER)
    a = ap.parse_args()

    jobs = [j for j in _jobs() if j[4] - _existing(j[0], j[3]) > 0]
    print(f"{len(jobs)}/{len(BUCKETS) * N_SHARDS} shards pending, {a.workers} workers", flush=True)

    ctx = mp.get_context("fork")
    procs, idx, t0 = {}, 0, time.time()

    def _cleanup(signum, frame):   # forked children don't die with the parent by default
        for p in procs:
            p.terminate()
        for p in procs:
            p.join()
        sys.exit(1)

    signal.signal(signal.SIGTERM, _cleanup)
    signal.signal(signal.SIGINT, _cleanup)

    while idx < len(jobs) or procs:
        while idx < len(jobs) and len(procs) < a.workers:
            p = ctx.Process(target=_worker, args=(jobs[idx], a.tokenizer))
            p.start()
            procs[p] = jobs[idx]
            idx += 1
            time.sleep(0.3)   # stagger cold starts -- N simultaneous torch/tokenizer
                               # imports spiked memory into swap and thrashed I/O
        time.sleep(2)
        # os.waitpid(-1, ...) instead of Process.is_alive(): over a long run, most
        # finished children were sitting as unreaped zombies forever (is_alive() kept
        # reporting them alive), silently collapsing real parallelism far below --workers.
        by_pid = {p.pid: p for p in procs}
        while by_pid:
            try:
                pid, _ = os.waitpid(-1, os.WNOHANG)
            except ChildProcessError:
                break
            if pid == 0:
                break
            p = by_pid.pop(pid, None)
            if p is not None:
                del procs[p]
        if time.time() - t0 > 60:
            t0 = time.time()
            _report()
    _report()


if __name__ == "__main__":
    main()
