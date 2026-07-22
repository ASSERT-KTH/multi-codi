"""Load + length-filter the dataset written by precompute.py. Length is token count:
sft=input_ids, codi=prompt_ids+trace_ids. Shared by training and eval."""

import random

from datasets import load_from_disk

from .dataset import load_dataset as load_path


def _len(e):
    return len(e["input_ids"]) if "input_ids" in e else len(e["prompt_ids"]) + len(e["trace_ids"])


def load_cache(cache_dir, *, min_len=0, max_len=None, n_samples=-1):
    ex = [e for e in load_from_disk(cache_dir) if min_len <= _len(e) <= (max_len or 1 << 60)]
    return ex[:n_samples] if n_samples > 0 else ex


def parse_kv(items, cast=float):
    return {k: cast(v) for k, v in (s.split(":") for s in items)}


def load_mixed_cache(*, ratio=None, total_n=None, per_bucket_n=None, seed=42, max_len=None):
    """ratio/per_bucket_n: {path_or_glob: weight_or_count} -- the dict key IS the cache location
    (a literal precompute.py --out path, or a glob like ".../shard[0-7]" to pool several shards
    into one group), resolved via data.dataset.load_dataset -- no bucket/shard naming convention
    baked in here, works the same for a sharded or a single-directory cache. Pass either `ratio`
    (weight, sampled proportionally to `total_n`) or `per_bucket_n` (fixed count). Concatenated
    rows are shuffled once with `seed`, then filtered to max_len token length (same _len() as
    load_cache)."""
    counts = per_bucket_n
    if ratio is not None:
        total_w = sum(ratio.values())
        counts = {p: round(w / total_w * total_n) for p, w in ratio.items()}
        counts[next(iter(counts))] += total_n - sum(counts.values())
    rng = random.Random(seed)
    rows = []
    for path, n in counts.items():
        rows.extend(rng.sample(load_path(path), n))
    rng.shuffle(rows)
    if max_len is not None:
        rows = [e for e in rows if _len(e) <= max_len]
    return rows
