# Unknown-base investigation (CODI 0.52 reproduction)

**Goal.** Reproduce the strong CODI model `codi_recon_localfull_1.5b_ls1_rw0.1_len128_unknown_base`
(cruxeval pass@1 **0.52**, flat across ck300/600/900/1200). Its base `model_weights/sft-coder-1.5b`
was **deleted** — hence "unknown base".

## Controls — proven identical between GOOD and reproductions
| Variable | Check | Verdict |
|---|---|---|
| Training data | `codi_train_full` / `sft_train` cache mtime + content | identical, never rebuilt |
| CODI code | `git diff 8c0f86f HEAD -- train/codi_core.py train/train_codi_recon.py` | empty |
| CODI hyperparams | wandb config diff (lr, max_steps, seed, warmup, accum…) | all equal |
| Eval pipeline | re-eval GOOD's own ckpts | exact 0.514 / 0.521 |

→ The only difference is the **base checkpoint**.

## Base hypotheses — all refuted
| Hypothesis | Test | Result |
|---|---|---|
| Underfit level | probes from underfit2k ck200/400/1000 | plateau 0.38–0.40 |
| LR schedule (max_steps) | Exp A: ck1000 base, max_steps=1500 (=GOOD) | 0.39 flat; GOOD is 0.51 by ck300 |
| SFT learning rate | reproduce = lr1e5 ck6936 | 0.43 |
| Old code path | re-SFT @ git 7554ebc | weights ≈ underfit2k (Δ 7e-5) — no-op |
| Base snapshot / Instruct | GOOD ck300 deep layers vs capital base | 0.93% → same base, not Instruct |
| SFT seed / basin | SFT seed=1,7 vs 42 | Δ ~6e-5 — deterministic (mean-init) |
| Stock/raw base | Exp C: CODI from raw Qwen coder | 0.34–0.38 |
| Projector-init luck | fresh CODI, new random projector | still 0.52 (see below) |

**Weight-space picture.** `sft-coder` = a *very lightly* SFT'd Qwen coder (closest to the raw base;
lighter than underfit2k ck200). Largest non-projector diff from reproductions is in the **trace-token
embeddings (8.8%)**; attn/mlp differ ~0.6%. Explicit-CoT ceiling (SFT base, greedy) = **0.54**;
GOOD's CODI (0.52) nearly saturates it, all other CODI runs (0.40) fall short.

## Result — bootstrap reproduces 0.52
Extracted GOOD ck300's inner LM (strip CodiRecon wrapper + projector) → `model_weights/goodbase_ck300`.
Fresh CODI from it (GOOD recipe, **new random projector**): **ck300 = 0.5175, ck600 = 0.4975**.

**Conclusions.**
1. The 0.52 ability is **baked into the base weights** — a fresh random projector still reaches 0.52,
   so it is *not* projector-init luck and *not* a fragile run.
2. **Reproduction path = have this base.** `goodbase_ck300` reliably CODIs to ~0.52; every
   from-scratch base (underfit2k / raw / lr1e5) gives ~0.40.
3. Caveat: `goodbase_ck300` = sft-coder + 300 CODI steps, **recovered** from GOOD's checkpoint —
   this solves "obtain a base that reproduces 0.52" but **not** "how sft-coder was originally trained"
   (recipe unrecoverable; every recorded-recipe reconstruction gives ~0.40).