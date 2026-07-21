#!/bin/bash
#SBATCH -A berzelius-2026-167
#SBATCH -C fat
#SBATCH --gpus 2
#SBATCH -t 8:00:00
#SBATCH -J eval_qlora
#SBATCH -o eval_qlora_%j.log

# CruxEval (MODE=codi only) for a QLoRA adapter checkpoint from train_codi_qlora.py.
# Separate from eval.sbatch: that launcher's eval_len.py can't load an adapter-only
# checkpoint dir (no config.json/tokenizer, just adapter_config.json+safetensors);
# this uses eval/eval_len_qlora.py (base_model + adapter_dir split) instead.
# 32B-in-4bit needs far more per-rank VRAM than the 1.5B checkpoints eval.sbatch was
# tuned for, so default to 2 ranks/GPU (not eval.sbatch's 4) -- bump NPROC if a run
# shows headroom.
# Submit e.g.:
#   sbatch --export=ALL,ADAPTER_DIR=model_weights/codi_qlora_32b/checkpoint-100,OUT=results/codi_qlora_32b/cruxeval_ck100.json eval_qlora.sbatch
export PATH=/proj/assert-berzelius/users/x_sirli/conda/envs/CWM/bin:$PATH
export HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 PYTHONHASHSEED=0
export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True

BASE_MODEL="${BASE_MODEL:-model_weights/cwm_hf}"
DATASET="${DATASET:-data/cache/cruxeval_codi}"

torchrun --nproc_per_node="${NPROC:-4}" --master_port=$((20000 + RANDOM % 10000)) -m eval.eval_len_qlora \
  --base_model "$BASE_MODEL" \
  --adapter_dir "${ADAPTER_DIR:?set ADAPTER_DIR}" \
  --dataset "$DATASET" \
  --n_samples "${N:--1}" \
  --min_len "${MIN_LEN:-0}" \
  --max_len "${MAX_LEN:-1152921504606846976}" \
  --max_new_tokens "${MAXNEW:-16384}" \
  --len_mult "${LEN_MULT:-1.5}" \
  --latent_steps "${LS:-1}" \
  --sliding_window "${SLIDING_WINDOW:-0}" \
  --attn_impl "${ATTN_IMPL:-flash_attention_2}" \
  --load_in_4bit "${LOAD_IN_4BIT:-1}" \
  --out "${OUT:?set OUT}"

python -m eval.merge_len_shards --out "${OUT}"
