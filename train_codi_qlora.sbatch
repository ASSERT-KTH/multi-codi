#!/bin/bash
#SBATCH -A berzelius-2026-167
#SBATCH --gpus 4
#SBATCH -C fat
#SBATCH -t 1-16:00:00
#SBATCH -J codi_qlora
#SBATCH -o codi_qlora_%j.log

# Standalone CWM-32B QLoRA CODI launcher. Independent of codi.sbatch/train_codi.py
# (the Qwen full-FT pipeline). max_seq_len=1536 matches the config that actually
# produced good CruxEval-O results in cwm_andre last month (job 16800904-907),
# not the 1280 in that repo's current (regressed) train_qlora.sbatch.
export PATH=/proj/assert-berzelius/users/x_sirli/conda/envs/CWM/bin:$PATH
export HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 PYTHONHASHSEED=0
export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True

MODEL="${MODEL:-model_weights/cwm_hf}"
OUTPUT_DIR="${OUTPUT_DIR:-model_weights/codi_qlora_32b}"

# FROZEN_TEACHER must be exactly "1" to enable -- bash's ${VAR:+...} triggers on
# any non-empty value (including "0"), which silently flips the flag on for
# anyone trying to disable it that way.
FROZEN_TEACHER_ARGS=()
[ "${FROZEN_TEACHER:-0}" = "1" ] && FROZEN_TEACHER_ARGS=(--frozen_teacher)

torchrun --nproc_per_node="${GPUS:-4}" --master_port=$((20000 + RANDOM % 10000)) -m train.train_codi_qlora \
  --model "$MODEL" \
  --output_dir "$OUTPUT_DIR" \
  --cache_dir "${CACHE_DIR:-data/cache/codi_train_cwm}" \
  --max_seq_len "${MAX_SEQ_LEN:-1536}" \
  --epochs "${EPOCHS:-5}" \
  --max_steps "${MAX_STEPS:-1500}" \
  --lr "${LR:-1e-4}" \
  --grad_accum "${GRAD_ACCUM:-4}" \
  --latent_steps "${LATENT_STEPS:-1}" \
  --alpha "${ALPHA:-1.0}" \
  --beta "${BETA:-1.0}" \
  --gamma "${GAMMA:-1.0}" \
  --lora_r "${LORA_R:-16}" \
  --lora_alpha "${LORA_ALPHA:-32}" \
  --lora_dropout "${LORA_DROPOUT:-0.05}" \
  --attn_impl "${ATTN_IMPL:-sdpa}" \
  --save_every_steps "${SAVE_EVERY_STEPS:-100}" \
  "${FROZEN_TEACHER_ARGS[@]}"
