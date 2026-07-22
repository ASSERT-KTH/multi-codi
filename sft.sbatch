#!/bin/bash
#SBATCH -A berzelius-2026-167
#SBATCH -C fat
#SBATCH --gpus 4
#SBATCH -t 1-00:00:00
#SBATCH -J sft
#SBATCH -o sft_%j.log

# Unified SFT launcher. SIZE picks the base model; output defaults to sft-coder-<size>.
#   sbatch --export=ALL,SIZE=1.5b sft.sbatch
#   sbatch --export=ALL,SIZE=3b,LR=1e-5,ACCUM=16 sft.sbatch
#   underfit probe: sbatch --export=ALL,SIZE=1.5b,MAX_STEPS=2000,SAVE_STEPS=200 sft.sbatch
export PATH=/proj/assert-berzelius/users/x_sirli/conda/envs/CWM/bin:$PATH
export HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 PYTHONHASHSEED=0
export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True

SIZE="${SIZE:-1.5b}"
case "$SIZE" in
  1.5b) : "${MODEL:=model_weights/qwen2.5-coder-1.5b}" ;;
  3b)   : "${MODEL:=model_weights/qwen2.5-coder-3b}" ;;
  *)    echo "unknown SIZE=$SIZE (want 1.5b|3b)" >&2; exit 1 ;;
esac
: "${OUTPUT_DIR:=model_weights/sft-coder-${SIZE}}"

# Length-mixing experiment: RATIO="PATH_OR_GLOB:WEIGHT ..." (e.g. "data/cache/lenbuckets/0-256/shard[0-7]:1.0")
# + TOTAL_N switches train_sft.py to load_mixed_cache; --cache_dir is unused in that case.
MIX_ARGS=()
[ -n "${RATIO:-}" ] && MIX_ARGS+=(--ratio $RATIO)
[ -n "${TOTAL_N:-}" ] && MIX_ARGS+=(--total_n "$TOTAL_N")
[ -n "${SEED:-}" ] && MIX_ARGS+=(--seed "$SEED")

torchrun --nproc_per_node=4 --master_port=$((20000 + RANDOM % 10000)) -m train.train_sft \
  --model "$MODEL" \
  --output_dir "$OUTPUT_DIR" \
  --cache_dir "${CACHE_DIR:-data/cache/sft_train}" \
  --max_seq_len "${MAX_SEQ_LEN:-3072}" \
  --epochs 4 \
  --lr "${LR:-2e-5}" \
  --batch_size "${BATCH:-1}" \
  --grad_accum "${ACCUM:-8}" \
  --max_steps "${MAX_STEPS:--1}" \
  --save_steps "${SAVE_STEPS:-500}" \
  "${MIX_ARGS[@]}"
