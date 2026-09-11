# milti-codi — Towards Latent Code World Models

Sirui Liu · André Silva · Martin Monperrus — KTH

**Code World Models (CWM)** [[1]] simulate program execution by explicitly verbalizing intermediate
execution states — faithful, but inference cost grows with trace length. **Latent Code World
Models** replace those explicit program states with continuous latent representations, potentially
decoupling reasoning cost from trace verbosity.

> Can explicit program states be replaced by latent representations without sacrificing faithful
> program-state reasoning?

We fine-tune Qwen2.5-Coder to generate CWM-style execution traces (the **teacher**), then adapt
CODI [[2]] to distill those traces into latent states (the **student**), and measure the gap.

[onepager]: https://docs.google.com/document/d/1p3xenGEjPYJxLLWlpZ8BabCx89fNCzVjwAVho9g09PQ/edit?usp=sharing
[1]: https://arxiv.org/abs/2510.02387
[2]: https://arxiv.org/abs/2502.21074

## Method

A trace is a sequence of frames — observation (`$LOCALS`) + action (source line):

```
<|line_sep|>$LOCALS<|action_sep|>$SOURCE<|frame_sep|>
```

**Stage 1** teaches a Qwen2.5-Coder base to emit this format (next-token CE, prompt masked).
**Stage 2** shares weights between teacher and student: the teacher reads the explicit trace; the
student replaces each frame's `$LOCALS` with a latent block (`<|latent_start|>` + N recurrent
latents + `<|latent_end|>`, hidden → projector → next embedding); KD aligns student latents to
teacher hidden states at each `<|action_sep|>` under smooth-L1.
`L = α·L_teacher + β·L_student + γ·L_KD`.

Student variants: `multi` (per-frame KD, main line), `frozen` (frozen teacher, no teacher CE),
`single` (faithful CODI — one latent block for the whole trace), `recon` (+ state-reconstruction
loss), and a standalone CWM-32B QLoRA path.

## Layout

| path | contents |
|---|---|
| `data/` | trace format, `sys.settrace` ground truth, tokenization, offline cache builder |
| `data/{MBPP,HumanEval,PyX,Ds256k}/` | dataset converters → `{id, code, input, output}` |
| `train/` | `codi_core.py` (shared primitives) · `train_sft.py` · `train_codi{,_recon,_single,_qlora}.py` |
| `eval/` | `eval_len.py` (sharded held-out eval) · `merge_len_shards.py` · `scoring.py` · `diag/` |
| `code_gen/` | synthetic long-trace generator (graph → program tuned to a token target) |
| `results/` | eval logs + comparison markdowns |
| `*.sbatch` | SLURM wrappers around the commands below |

## Requirements

- Python 3.10+, PyTorch, `transformers`, `datasets`, `peft`, `bitsandbytes`, `flash-attn`, `wandb`
- **Training:** 4×80 GB GPUs for full fine-tuning at 1.5B/3B, or for CWM-32B in 4-bit QLoRA
- **Evaluation:** 1+ GPU. Latent decode is batch-size 1 and uses ~3.5 GB per rank, so it pays to run
  several ranks per GPU

## Reproduction

### 1. Data

CRUXEval-O (800) is held out for evaluation; MBPP + HumanEval + PyX (~65k traceable rows) train.

```bash
# convert: turn each raw dataset into {id, code, input, output} rows
python -m data.MBPP.convert
python -m data.HumanEval.convert
python -m data.PyX.convert
python -m data.Ds256k.convert

# precompute: trace the training set and write the cache (diff target, shared by SFT/CODI)
python -m data.precompute --model <base> --workers 32 \
  --sources data/MBPP/data data/HumanEval/data data/PyX/data --out data/cache/codi_train

# precompute: held-out CRUXEval-O evaluation set
python -m data.precompute --model <base> --workers 32 \
  --sources cruxeval --out data/cache/cruxeval_codi

# precompute (recon only, skip by default): same training set, also write the full target
python -m data.precompute --model <base> --workers 32 \
  --sources data/MBPP/data data/HumanEval/data data/PyX/data \
  --out data/cache/codi_train_full --trace_target full
```

One cache serves both stages; length filtering happens at load. Only `codi_train_full` carries the
full-state reconstruction targets — a `recon` run against the plain cache silently loses them.

### 2. Train

```bash
# teacher
torchrun --nproc_per_node=4 -m train.train_sft --model <qwen-coder-base> \
  --output_dir <out> --cache_dir data/cache/sft_train \
  --max_seq_len 3072 --epochs 10 --lr 2e-5 --batch_size 1 --grad_accum 8

# student (α=β=γ=1, effective batch 16)
torchrun --nproc_per_node=4 -m train.train_codi --model <teacher-ckpt> \
  --output_dir <out> --cache_dir data/cache/codi_train \
  --max_seq_len 3072 --lr 1e-5 --latent_steps 1 --max_steps 1500 --save_steps 300 \
  --alpha 1.0 --beta 1.0 --gamma 1.0 --batch_size 1 --grad_accum 4
```

Variants swap the module and add their own flags:

| variant | module | added flags |
|---|---|---|
| `frozen` | `train.train_codi` | `--frozen_teacher <ckpt> --kd_target hidden\|logit --alpha 0` |
| `single` | `train.train_codi_single` | `--latent_steps 6` |
| `recon` | `train.train_codi_recon` | `--recon_w 0.1 --max_recon_len 128 --recon_attn local --recon_target full` |
| QLoRA | `train.train_codi_qlora` | `--max_seq_len 1536 --lr 1e-4 --lora_r 16 --lora_alpha 32` |

### 3. Evaluate

Ranks write `${OUT}.r*.jsonl`; `merge_len_shards` produces the final JSON.

```bash
# stage 1: each rank evaluates in parallel, writing its own ${OUT}.r*.jsonl shard
torchrun --nproc_per_node=8 -m eval.eval_len --mode codi --model <ckpt> \
  --dataset data/cache/cruxeval_codi --max_new_tokens 16384 --len_mult 1.5 \
  --latent_steps 1 --out <out.json>

# stage 2: merge all shards into the final JSON
python -m eval.merge_len_shards --out <out.json>
```

`--mode sft|codi|single` picks the decoder. `--min_len` filters a cache to rows at or above a given trace length.

> In training, if use `--dataset data/cache/codi_train --min_len 3073`, which only takes rows up to `max_seq_len` (3072). Then this `--min_len 3073` selects the long rows the model never trained on as evaluation.

QLoRA checkpoints use `eval.eval_len_qlora` with `--base_model` + `--adapter_dir`.

---

Each row gets a forward-step budget `min(args.max_new_tokens, ceil(trace_len * args.len_mult))`. A row is **truncated when `n_fwd` exceeds budget**, same rule for teacher and student. `n_fwd` counts every forward pass, not just emitted tokens. For the student, each latent step is a forward pass that emits no token, so `n_fwd > n_gen`. 

Any truncated row scores invalid, which counts as wrong regardless of what it generated.

Metrics: **pass@1** (correct/n) · **valid%** (parseable and in-budget) · **cond. acc**
(correct/valid) · **fwd/ref** (`n_fwd / trace_len`) · **trunc%**.

## Results

CRUXEval-O, n=800, greedy. Full tables in [the one-pager][onepager] and `results/*_compare.md`.

**The cost of going latent — ~9 pp, stable across scale:**

| model | pass@1 |
|---|--:|
| teacher 1.5B / 3B | 0.5463 / 0.5763 |
| student 1.5B / 3B | 0.4612 / 0.4875 |

Simple fixes don't close it: single-block CODI 0.465 (3B), frozen+logit KD 0.495 (3B), scheduled
sampling 0.4775 (3B), state reconstruction 0.453 (1.5B).

On evaluation, for cases with trace no longer than the distillation boundary of student, the student follows the CWM trace format as good as the teacher, and almost the whole pass@1 gap comes from answers that are well-formed but wrong.

For cases with trace longer than the distillation bounday, many outputs can not be parsed into an answer. Varying the distillation set reproduces this consistently: students trained on traces of up to 512, 1k, 2k and 4k tokens each show the same switch, at their own length.

## References

1. FAIR CodeGen Team et al. *CWM: An Open-Weights LLM for Research on Code Generation with World
   Models.* [arXiv:2510.02387][1], 2025.
   Repro branch: <https://github.com/ASSERT-KTH/cwm/tree/andre/feat/cruxeval>
2. Z. Shen et al. *CODI: Compressing Chain-of-Thought into Continuous Space via Self-Distillation.*
   [arXiv:2502.21074][2], 2025.
