"""code_gen/gen/<bucket>/shard*.jsonl -> data/LenBuckets/<bucket>/shard<i>/data, one row
dataset per shard (canonical shard indices 0..9, re-numbered from whatever indices the
raw shard files happen to have -- some buckets were generated with shard5..shard14).

    python -m code_gen.convert_lenbuckets --gen_root code_gen/gen --out_root data/LenBuckets
"""

import argparse
import json
import re
from pathlib import Path

from datasets import Dataset

_BUCKET_RE = re.compile(r"^\d+-\d+$")
_SHARD_RE = re.compile(r"^shard(\d+)\.jsonl$")


def _shard_files(bucket_dir):
    files = [(int(_SHARD_RE.match(p.name)[1]), p) for p in bucket_dir.glob("shard*.jsonl")]
    return [p for _, p in sorted(files)]


def convert_shard(bucket, i, path, out_root):
    rows = []
    for line in path.read_text().splitlines():
        r = json.loads(line)
        rows.append({"id": f"len{bucket}_s{i}_{r['id']}", "code": r["code"],
                     "input": r["input"], "output": r["output"]})
    assert len(rows) == 200, f"{path}: expected 200 rows, got {len(rows)}"
    assert len({r["id"] for r in rows}) == len(rows), f"{path}: duplicate ids"
    out = out_root / bucket / f"shard{i}" / "data"
    Dataset.from_list(rows).save_to_disk(str(out))
    return len(rows)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--gen_root", default="code_gen/gen")
    ap.add_argument("--out_root", default="data/LenBuckets")
    ap.add_argument("--buckets", nargs="+", default=None)
    args = ap.parse_args()

    gen_root, out_root = Path(args.gen_root), Path(args.out_root)
    buckets = args.buckets or sorted(
        p.name for p in gen_root.iterdir() if p.is_dir() and _BUCKET_RE.match(p.name))

    for bucket in buckets:
        shards = _shard_files(gen_root / bucket)
        assert len(shards) == 10, f"{bucket}: expected 10 shards, found {len(shards)}"
        for i, path in enumerate(shards):
            n = convert_shard(bucket, i, path, out_root)
            print(f"{bucket} shard{i} ({path.name}): {n} rows", flush=True)


if __name__ == "__main__":
    main()
