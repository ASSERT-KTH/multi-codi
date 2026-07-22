#!/bin/bash
#SBATCH -A berzelius-2026-167
#SBATCH --gpus 4
#SBATCH -C fat
#SBATCH -t 1-00:00:00
#SBATCH -J codi
#SBATCH -o codi_%j.log

# Unified CODI training launcher. MODE picks the variant, SIZE picks the base checkpoint.
#   frozen : train_codi + frozen SFT teacher (no teacher CE) + last-layer hidden/logit KD (alpha 0)
#   multi  : train_codi, full-layer + multi-anchor KD
#   recon  : train_codi_recon, co-trained CODI + locals reconstruction
#   single : train_codi_single, faithful single-block CODI
export PATH=/proj/assert-berzelius/users/x_sirli/conda/envs/CWM/bin:$PATH
export HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 PYTHONHASHSEED=0
export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True

MODE="${MODE:?set MODE=frozen|multi|recon|single}"
SIZE="${SIZE:-1.5b}"

# Effective batch is pinned at 16 (the 4 GPU x bs1 x accum4 setting); accum absorbs the GPU count.
GPUS="${GPUS:-${SLURM_GPUS:-4}}"
BATCH="${BATCH:-1}"
: "${ACCUM:=$(( 16 / (GPUS * BATCH) ))}"

# Base SFT checkpoint by size (student/teacher init); output defaults to codi_<mode>_<size>.
case "$SIZE" in
  1.5b) : "${MODEL:=model_weights/sft1.5b_lr2e5_bs32/checkpoint-6936}" ;;
  3b)   : "${MODEL:=model_weights/sft3b_lr1e5_bs32/checkpoint-3000}" ;;
  *)    echo "unknown SIZE=$SIZE (want 1.5b|3b)" >&2; exit 1 ;;
esac
: "${OUTPUT_DIR:=model_weights/codi_${MODE}_${SIZE}}"

# Per-mode: module, differing defaults, and the flags unique to that variant.
MODE_ARGS=()
case "$MODE" in
  frozen)
    MODULE=train.train_codi
    : "${ALPHA:=0}"
    MODE_ARGS=(
      --frozen_teacher "${FROZEN_TEACHER:-$MODEL}"
      --kd_target "${KD_TARGET:-hidden}"
      --kd_temp "${KD_TEMP:-2.0}"
    ) ;;

  multi)
    MODULE=train.train_codi ;;

  recon)
    MODULE=train.train_codi_recon
    # Only the *_full cache carries recon_targets; the plain codi_train cache predates them.
    : "${CACHE_DIR:=data/cache/codi_train_full}"
    MODE_ARGS=(
      --recon_w "${RECON_W:-0.1}"
      --max_recon_len "${MAX_RECON_LEN:-64}"
      --recon_attn "${RECON_ATTN:-local}"
      --recon_target "${RECON_TARGET:-diff}"
      --debug_recon_print "${DEBUG_RECON_PRINT:-0}"
    ) ;;

  single)
    MODULE=train.train_codi_single
    : "${LATENT_STEPS:=${LS:-6}}" ;;

  *)
    echo "unknown MODE=$MODE (want frozen|multi|recon|single)" >&2
    exit 1 ;;
esac

# Length-mixing experiment (MODE=frozen|multi only): RATIO="PATH_OR_GLOB:WEIGHT ..." (e.g.
# "data/cache/lenbuckets/0-256/shard[0-7]:1.0") + TOTAL_N switches train_codi.py to
# load_mixed_cache; --cache_dir is unused in that case.
MIX_ARGS=()
[ -n "${RATIO:-}" ] && MIX_ARGS+=(--ratio $RATIO)
[ -n "${TOTAL_N:-}" ] && MIX_ARGS+=(--total_n "$TOTAL_N")
[ -n "${SEED:-}" ] && MIX_ARGS+=(--seed "$SEED")

torchrun --nproc_per_node="$GPUS" --master_port=$((20000 + RANDOM % 10000)) -m "$MODULE" \
  --model "$MODEL" \
  --output_dir "$OUTPUT_DIR" \
  --max_seq_len "${MAX_SEQ_LEN:-3072}" \
  --epochs 5 \
  --lr 1e-5 \
  --latent_steps "${LATENT_STEPS:-1}" \
  --max_steps "${MAX_STEPS:-1500}" \
  --save_steps "${SAVE_STEPS:-300}" \
  --cache_dir "${CACHE_DIR:-data/cache/codi_train}" \
  --optim "${OPTIM:-paged_adamw_8bit}" \
  --alpha "${ALPHA:-1.0}" \
  --beta "${BETA:-1.0}" \
  --gamma "${GAMMA:-1.0}" \
  --batch_size "$BATCH" \
  --grad_accum "$ACCUM" \
  "${MODE_ARGS[@]}" "${MIX_ARGS[@]}"