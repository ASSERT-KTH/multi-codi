"""Stage 1: explicit full-trace SFT = baseline = CODI teacher.

Teach a non-CWM base (Qwen2.5-Coder) to emit CWM-format execution traces.
Plain next-token CE; labels mask the prompt in this script.
"""

import argparse
import os

import torch
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    Trainer,
    TrainingArguments,
)
from transformers.trainer_utils import get_last_checkpoint

from data.precompute_loader import load_cache
from data.dataset import IGNORE_INDEX
from data.tokens import add_trace_tokens, resize_and_init
from .wb import wandb_init


def collate(batch, pad_id):
    n = max(len(ids) for ids, _ in batch)
    input_ids, labels, attn = [], [], []
    for ids, lab in batch:
        p = n - len(ids)
        input_ids.append(ids + [pad_id] * p)
        labels.append(lab + [IGNORE_INDEX] * p)
        attn.append([1] * len(ids) + [0] * p)
    return {
        "input_ids": torch.tensor(input_ids),
        "attention_mask": torch.tensor(attn),
        "labels": torch.tensor(labels),
    }


def sft_pair(example):
    prompt_ids = example["prompt_ids"]
    trace_ids = example["trace_ids"]
    return prompt_ids + trace_ids, [IGNORE_INDEX] * len(prompt_ids) + trace_ids


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="Qwen/Qwen2.5-Coder-1.5B")
    ap.add_argument("--output_dir", required=True)
    ap.add_argument("--n_samples", type=int, default=-1)
    ap.add_argument("--max_seq_len", type=int, default=4096)  # load-time token filter
    ap.add_argument("--epochs", type=float, default=3.0)
    ap.add_argument("--lr", type=float, default=1e-5)
    ap.add_argument("--batch_size", type=int, default=4)
    ap.add_argument("--grad_accum", type=int, default=4)
    ap.add_argument("--max_steps", type=int, default=-1)  # >0 for smoke
    ap.add_argument("--save_steps", type=int, default=500)
    ap.add_argument("--sources", nargs="+", default=["mbpp", "humaneval", "pyx"])
    ap.add_argument("--cache_dir", default=None)  # load offline tokenized examples from precompute.py
    args = ap.parse_args()

    tok = AutoTokenizer.from_pretrained(args.model, use_fast=True)
    if tok.pad_token_id is None:
        tok.pad_token = tok.eos_token
    model = AutoModelForCausalLM.from_pretrained(args.model, torch_dtype=torch.bfloat16)
    model.config.use_cache = False  # required with gradient checkpointing
    n_added = add_trace_tokens(tok)
    resize_and_init(model, tok, n_added)

    ds = [sft_pair(e)
          for e in load_cache(args.cache_dir, max_len=args.max_seq_len, n_samples=args.n_samples)]
    print(f"{len(ds)} trace examples")

    report_to = wandb_init(args, "sft")

    targs = TrainingArguments(
        output_dir=args.output_dir,
        per_device_train_batch_size=args.batch_size,
        gradient_accumulation_steps=args.grad_accum,
        num_train_epochs=args.epochs,
        max_steps=args.max_steps,
        learning_rate=args.lr,
        lr_scheduler_type="cosine",
        warmup_ratio=0.03,
        weight_decay=0.1,
        max_grad_norm=1.0,
        bf16=True,
        optim="paged_adamw_8bit",  # 8-bit Adam (paged), aligned with train_codi.py
        gradient_checkpointing=True,
        gradient_checkpointing_kwargs={"use_reentrant": False},
        logging_steps=5,
        save_strategy="steps",
        save_steps=args.save_steps,
        save_total_limit=None,  # keep every checkpoint
        report_to=report_to,
    )
    trainer = Trainer(
        model=model,
        args=targs,
        train_dataset=ds,
        data_collator=lambda b: collate(b, tok.pad_token_id),
        processing_class=tok,  # tokenizer saved into every checkpoint
    )
    # Auto-resume from the latest checkpoint if the job was interrupted.
    ckpt = get_last_checkpoint(args.output_dir) if os.path.isdir(args.output_dir) else None
    trainer.train(resume_from_checkpoint=ckpt)
    trainer._save_checkpoint(trainer.model, trial=None)  # final step as a resumable checkpoint-<step>


if __name__ == "__main__":
    main()
