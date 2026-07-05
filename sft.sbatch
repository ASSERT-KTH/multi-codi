#!/bin/bash
#SBATCH -A naiss2026-3-261
#SBATCH -C 4xA100
#SBATCH --gpus-per-node=A100:4
#SBATCH -t 1-00:00:00
#SBATCH -J sft
#SBATCH -o sft_%j.log

# Unified SFT launcher. SIZE picks the base model; output defaults to sft-coder-<size>.
#   sbatch --export=ALL,SIZE=1.5b sft.sbatch
#   sbatch --export=ALL,SIZE=3b,LR=1e-5,ACCUM=16 sft.sbatch
export PATH=/mimer/NOBACKUP/groups/assert-kth/siruil/conda_envs/CWM/bin:$PATH
export HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 PYTHONHASHSEED=0
export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True

SIZE="${SIZE:-1.5b}"
case "$SIZE" in
  1.5b) : "${MODEL:=model_weights/qwen2.5-coder-1.5b}" ;;
  3b)   : "${MODEL:=model_weights/qwen2.5-coder-3b}" ;;
  *)    echo "unknown SIZE=$SIZE (want 1.5b|3b)" >&2; exit 1 ;;
esac
: "${OUTPUT_DIR:=model_weights/sft-coder-${SIZE}}"

torchrun --nproc_per_node=4 --master_port=$((20000 + RANDOM % 10000)) -m train.train_sft \
  --model "$MODEL" \
  --output_dir "$OUTPUT_DIR" \
  --cache_dir data/cache/sft_train \
  --max_seq_len 3072 \
  --epochs 4 \
  --lr "${LR:-2e-5}" \
  --batch_size "${BATCH:-1}" \
  --grad_accum "${ACCUM:-8}"
