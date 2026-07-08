# codi_recon — reconstruction-loss variants performance

_CRUXEval-O latent eval, n=800, greedy. Aggregated from `results/codi_recon_*/ck*.json`._

## Variant naming

| token | meaning |
|---|---|
| `delta` / `full` | reconstruction target: `delta` = reconstruct the hidden-state *delta*; `full` = reconstruct the full trace text |
| `local` | reconstruction attention (`--recon_attn`): `local` = recon query attends only within its own latent block; absent = full/global recon attention (all prior variants) |
| `ls1` / `ls2` | latent steps per reasoning step (1 or 2) |
| `rw0.03` / `rw0.1` | reconstruction loss weight (0.03 or 0.1) |
| `len128` / `len192` | reconstruction span cap (128 / 192 tokens; full variants only) |

Metrics: **pass@1** = exact-match / n · **valid%** = parseable-answer rate · **condAcc** = correct / valid (accuracy given a well-formed answer) · **fwd/gen** = mean forward steps / mean emitted tokens (latent overhead).

## 1. pass@1 by checkpoint

| config | model | best pass@1 | ckpt | per-ckpt |
|---|---|--:|---|---|
| **local** full ls1 rw0.1 len128 | 1.5b | **0.521** | ck900 | 300 .514 / 600 .518 / 900 .521 / 1200 .509 · _recheck 900 .521_ |
| full ls2 rw0.03 len192 | 1.5b | 0.453 | ck900 | 300 .416 / 600 .435 / 900 .453 / 1200 .443 / 1500 .445 |
| local full ls1 rw0.03 len128 | 1.5b | 0.441 | ck900 | 300 .413 / 600 .430 / 900 .441 |
| full ls2 rw0.1 len192 | 1.5b | 0.432 | ck900 | 300 .412 / 600 .431 / 900 .432 / 1200 .432 |
| local full ls1 rw0.1 len192 | 1.5b | 0.421 | ck600 | 300 .421 / 600 .421 / 900 .419 |
| delta ls2 rw0.03 | 1.5b | 0.395 | ck900 | 300 .378 / 600 .380 / 900 .395 / 1200 .395 |
| delta ls1 rw0.03 | 1.5b | 0.393 | ck1500 | 300 .376 / 600 .383 / 900 .391 / 1200 .388 / 1500 .393 |
| delta ls1 rw0.1 | 1.5b | 0.381 | ck600 | 300 .364 / 600 .381 / 900 .378 / 1200 .380 / 1500 .378 |

## 2. valid_format by checkpoint

| variant | ck300 | ck600 | ck900 | ck1200 | ck1500 |
|---|--:|--:|--:|--:|--:|
| local full ls1 rw0.1 len128 | 0.924 | 0.921 | 0.942 | 0.938 | — |
| local full ls1 rw0.03 len128 | 0.941 | 0.938 | 0.964 | — | — |
| local full ls1 rw0.1 len192 | 0.964 | 0.944 | 0.964 | — | — |
| delta ls1 rw0.03 | 0.941 | 0.932 | 0.935 | 0.932 | 0.931 |
| delta ls1 rw0.1 | 0.946 | 0.941 | 0.930 | 0.935 | 0.930 |
| delta ls2 rw0.03 | 0.950 | 0.930 | 0.915 | 0.920 | — |
| full ls2 rw0.03 len192 | 0.959 | 0.960 | 0.974 | 0.971 | 0.973 |
| full ls2 rw0.1 len192 | 0.985 | 0.968 | 0.974 | 0.971 | — |

## 3. condAcc (correct | valid) by checkpoint

| variant | ck300 | ck600 | ck900 | ck1200 | ck1500 |
|---|--:|--:|--:|--:|--:|
| local full ls1 rw0.1 len128 | 0.556 | 0.562 | 0.553 | 0.543 | — |
| local full ls1 rw0.03 len128 | 0.438 | 0.459 | 0.458 | — | — |
| local full ls1 rw0.1 len192 | 0.437 | 0.446 | 0.435 | — | — |
| delta ls1 rw0.03 | 0.400 | 0.410 | 0.418 | 0.416 | 0.421 |
| delta ls1 rw0.1 | 0.384 | 0.405 | 0.406 | 0.406 | 0.406 |
| delta ls2 rw0.03 | 0.397 | 0.409 | 0.432 | 0.429 | — |
| full ls2 rw0.03 len192 | 0.434 | 0.453 | 0.465 | 0.456 | 0.458 |
| full ls2 rw0.1 len192 | 0.419 | 0.446 | 0.444 | 0.445 | — |

## 4. Compute cost at best-pass checkpoint

| variant | mean_fwd | mean_gen | fwd/gen |
|---|--:|--:|--:|
| local full ls1 rw0.1 len128 | 397 | 334 | 1.19 |
| local full ls1 rw0.03 len128 | 363 | 308 | 1.18 |
| local full ls1 rw0.1 len192 | 395 | 332 | 1.19 |
| delta ls1 rw0.03 | 1004 | 837 | 1.20 |
| delta ls1 rw0.1 | 855 | 714 | 1.20 |
| delta ls2 rw0.03 | 1181 | 937 | 1.26 |
| full ls2 rw0.03 len192 | 618 | 497 | 1.24 |
| full ls2 rw0.1 len192 | 622 | 505 | 1.23 |

## 5. Key findings

0. **`local full ls1 rw0.1 len128` @ ck900 is the best: 0.521 pass@1** (recheck 0.521), vs 0.453 global-best and ≤0.395 delta. Also the cheapest (mean_gen 334, fwd/gen 1.19) and highest condAcc (0.55). Gain is reasoning/condAcc, not format — its valid% (0.92–0.94) trails the global full variants (0.97).

0a. **The 0.521 needs the exact `rw0.1 + len128` combo, not `local` alone.** Single-axis ablations off it collapse the gain: `rw0.1 → rw0.03` → 0.441, `len128 → len192` → 0.421 — both back in the global pack (condAcc ~0.44–0.46). So under local attention rw0.1 > rw0.03 (**reverses #2**) and len128 > len192.

1. **`full` >> `delta`.** Full-text variants (0.453 / 0.432) beat all delta (0.381–0.395) by ~5–6 pts at lower token cost (gen ~500 vs 800–940).

2. **Lower recon weight (rw0.03) wins under global attention** — full (0.453 vs 0.432), delta ls1 (0.393 vs 0.381). (Flips under local attention, see #0a.)

3. **`full` has the best format validity (97–98%)** vs ~91–95% delta; condAcc for full (0.46–0.47) also leads.

4. **Peak at ck900; later ckpts plateau/regress** (full ls2 rw0.03: 0.453@900 → 0.445@1500). ck900 is a reasonable early-stop.

5. **ls2 ≈ ls1 for delta** (0.395 vs 0.393) but costs more fwd (fwd/gen 1.26 vs 1.20).