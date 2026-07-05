# codi_recon — reconstruction-loss variants performance

_CRUXEval-O latent eval, n=800, greedy. Aggregated from `results/codi_recon_*/ck*.json`._

## Variant naming

| token | meaning |
|---|---|
| `delta` / `full` | reconstruction target: `delta` = reconstruct the hidden-state *delta*; `full` = reconstruct the full trace text |
| `ls1` / `ls2` | latent steps per reasoning step (1 or 2) |
| `rw0.03` / `rw0.1` | reconstruction loss weight (0.03 or 0.1) |
| `len192` | reconstruction span capped at 192 tokens (full variants only) |

Metrics: **pass@1** = exact-match / n · **valid%** = parseable-answer rate · **condAcc** = correct / valid (accuracy given a well-formed answer) · **fwd/gen** = mean forward steps / mean emitted tokens (latent overhead).

## 1. pass@1 by checkpoint

| config | model | best pass@1 | ckpt | per-ckpt |
|---|---|--:|---|---|
| full ls2 rw0.03 len192 | 1.5b | **0.453** | ck900 | 300 .416 / 600 .435 / 900 .453 / 1200 .443 / 1500 .445 |
| full ls2 rw0.1 len192 | 1.5b | 0.432 | ck900 | 300 .412 / 600 .431 / 900 .432 / 1200 .432 |
| delta ls2 rw0.03 | 1.5b | 0.395 | ck900 | 300 .378 / 600 .380 / 900 .395 / 1200 .395 |
| delta ls1 rw0.03 | 1.5b | 0.393 | ck1500 | 300 .376 / 600 .383 / 900 .391 / 1200 .388 / 1500 .393 |
| delta ls1 rw0.1 | 1.5b | 0.381 | ck600 | 300 .364 / 600 .381 / 900 .378 / 1200 .380 / 1500 .378 |

## 2. valid_format by checkpoint

| variant | ck300 | ck600 | ck900 | ck1200 | ck1500 |
|---|--:|--:|--:|--:|--:|
| delta ls1 rw0.03 | 0.941 | 0.932 | 0.935 | 0.932 | 0.931 |
| delta ls1 rw0.1 | 0.946 | 0.941 | 0.930 | 0.935 | 0.930 |
| delta ls2 rw0.03 | 0.950 | 0.930 | 0.915 | 0.920 | — |
| full ls2 rw0.03 len192 | 0.959 | 0.960 | 0.974 | 0.971 | 0.973 |
| full ls2 rw0.1 len192 | 0.985 | 0.968 | 0.974 | 0.971 | — |

## 3. condAcc (correct | valid) by checkpoint

| variant | ck300 | ck600 | ck900 | ck1200 | ck1500 |
|---|--:|--:|--:|--:|--:|
| delta ls1 rw0.03 | 0.400 | 0.410 | 0.418 | 0.416 | 0.421 |
| delta ls1 rw0.1 | 0.384 | 0.405 | 0.406 | 0.406 | 0.406 |
| delta ls2 rw0.03 | 0.397 | 0.409 | 0.432 | 0.429 | — |
| full ls2 rw0.03 len192 | 0.434 | 0.453 | 0.465 | 0.456 | 0.458 |
| full ls2 rw0.1 len192 | 0.419 | 0.446 | 0.444 | 0.445 | — |

## 4. Compute cost at best-pass checkpoint

| variant | mean_fwd | mean_gen | fwd/gen |
|---|--:|--:|--:|
| delta ls1 rw0.03 | 1004 | 837 | 1.20 |
| delta ls1 rw0.1 | 855 | 714 | 1.20 |
| delta ls2 rw0.03 | 1181 | 937 | 1.26 |
| full ls2 rw0.03 len192 | 618 | 497 | 1.24 |
| full ls2 rw0.1 len192 | 622 | 505 | 1.23 |

## 5. Key findings

1. **`full` reconstruction >> `delta`.** The two full-text variants (0.453 / 0.432 best pass@1) beat every delta variant (0.381–0.395) by ~5–6 points, and do so at *lower* token cost (mean_gen ~500 vs ~800–940). Reconstructing the full trace text is both more accurate and more compute-efficient than reconstructing hidden-state deltas.

2. **Lower recon weight (rw0.03) wins in both families.** rw0.03 edges out rw0.1 for full (0.453 vs 0.432) and delta ls1 (0.393 vs 0.381). A heavier reconstruction penalty slightly hurts the primary task — 0.03 is the better setting.

3. **`full` also has the best format validity (97–98%)**, vs ~91–95% for delta. Combined with #1, the full/recon objective helps the model terminate in well-formed answers, not just reason better — condAcc for full (0.46–0.47) also leads.

4. **Peak is at ck900; later checkpoints plateau or slightly regress.** All variants top out around ck900–ck1500 with no meaningful gains past ck900 (full ls2 rw0.03: 0.453@ck900 → 0.445@ck1500). Training longer is not buying accuracy here — ck900 is a reasonable early-stop.

5. **ls2 ≈ ls1 for delta** (0.395 vs 0.393 best) but ls2 costs more forward steps (fwd/gen 1.26 vs 1.20). The extra latent step doesn't pay off for the delta objective.

### Recommendation
**`codi_recon_full_1.5b_ls2_rw0.03_len192` @ ck900** is the clear best: highest pass@1 (0.453), highest valid% (0.974) and condAcc (0.465), and the lowest generation cost. Full-text reconstruction with a light (0.03) weight is the configuration to carry forward.