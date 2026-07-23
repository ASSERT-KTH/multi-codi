#!/bin/bash
#SBATCH -A berzelius-2026-167
#SBATCH -p berzelius-cpu
#SBATCH -c 64
#SBATCH -t 08:00:00
#SBATCH -J precompute
#SBATCH -o precompute_%j.log

# CPU-only precompute for one length bucket's 10 shards (data/LenBuckets/<bucket>/shard<i>/data
# -> data/cache/lenbuckets/<bucket>/shard<i>). precompute.py skips shards whose output already
# exists, so this is safe to resubmit.
#   sbatch --export=ALL,BUCKET=0-256 precompute.sbatch
export PATH=/proj/assert-berzelius/users/x_sirli/conda/envs/CWM/bin:$PATH
export HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1

BUCKET="${BUCKET:?set BUCKET, e.g. 0-256}"
MODEL="${MODEL:-model_weights/Qwen2.5-Coder-1.5B}"

for i in 0 1 2 3 4 5 6 7 8 9; do
  python -m data.precompute --model "$MODEL" --sources "data/LenBuckets/$BUCKET/shard$i/data" \
    --max_frames -1 --out "data/cache/lenbuckets/$BUCKET/shard$i"
done
