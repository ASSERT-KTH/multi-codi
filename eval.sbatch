#!/bin/bash
#SBATCH -A berzelius-2026-167
#SBATCH -C fat
#SBATCH --gpus 4
#SBATCH -t 12:00:00
#SBATCH -J eval
#SBATCH -o eval_%j.log

# Unified length-binned held-out eval launcher. MODE picks the variant; ranks write
# ${OUT}.r*.jsonl, then merge_len_shards aggregates into the final ${OUT} JSON.
#   sft    : SFT baseline (batched greedy full-trace)
#   codi   : multi-frame latent   (LEN_MULT=1e9 reproduces a fixed cap)
#   single : single-block CODI     (fixed MAXNEW)
# DATASET is any precomputed codi cache:
#   full CruxEval -> DATASET=data/cache/cruxeval_codi
#   long held-out -> DATASET=data/cache/codi_train MIN_LEN=3073   (leak boundary = training max_seq_len)
# Submit e.g.:
#   sbatch --export=ALL,MODE=codi,MODEL=<ckpt>,DATASET=data/cache/cruxeval_codi,OUT=results/crux_codi.json eval.sbatch
export PATH=/proj/assert-berzelius/users/x_sirli/conda/envs/CWM/bin:$PATH
export HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 PYTHONHASHSEED=0
export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True

MODE="${MODE:?set MODE=sft|codi|single}"
case "$MODE" in                             # per-mode defaults; unused flags are ignored by eval_len
  sft|codi) : "${MAXNEW:=16384}" "${LS:=1}" ;;
  single)   : "${MAXNEW:=256}"   "${LS:=6}" ;;
  *)        echo "unknown MODE=$MODE (want sft|codi|single)" >&2; exit 1 ;;
esac

torchrun --nproc_per_node="${NPROC:-4}" --master_port=$((20000 + RANDOM % 10000)) -m eval.eval_len \
  --mode "$MODE" \
  --model "${MODEL:?set MODEL}" \
  --dataset "${DATASET:?set DATASET}" \
  --n_samples "${N:--1}" \
  --min_len "${MIN_LEN:-0}" \
  --max_len "${MAX_LEN:-1152921504606846976}" \
  --max_new_tokens "$MAXNEW" \
  --len_mult "${LEN_MULT:-1.5}" \
  --latent_steps "$LS" \
  --batch_size "${BATCH:-8}" \
  --out "${OUT:?set OUT}"

# ranks write ${OUT}.r*.jsonl incrementally; merge into the final ${OUT} JSON
python -m eval.merge_len_shards --out "${OUT}"
