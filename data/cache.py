"""Load + length-filter a precompute.py cache. Length is token count:
sft=input_ids, codi=prompt_ids+trace_ids. Shared by training and eval."""

from datasets import load_from_disk


def _len(e):
    return len(e["input_ids"]) if "input_ids" in e else len(e["prompt_ids"]) + len(e["trace_ids"])


def load_cache(cache_dir, *, min_len=0, max_len=None, n_samples=-1):
    ex = [e for e in load_from_disk(cache_dir) if min_len <= _len(e) <= (max_len or 1 << 60)]
    return ex[:n_samples] if n_samples > 0 else ex
