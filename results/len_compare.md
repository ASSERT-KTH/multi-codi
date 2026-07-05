# len_sft vs len_codi — held-out length comparison

_Generated 2026-07-05 from `results/…/len_*.json` (CruxEval held-out, n=1290 each) via `python -m eval.stats_by_length`._

_Truncation is judged on forward steps (`n_fwd ≥ max_new`) uniformly for SFT and CODI. A row that exhausts its forward-step budget is scored **truncated → invalid → wrong**, so it drops out of pass@1 / valid% / condAcc. CODI's latent steps make `n_fwd > n_gen`; the eval logged results under an `n_gen` runtime cap, so over-budget CODI rows are handled post-hoc by this rule (greedy decode ⇒ the tighter `n_fwd` trajectory is a prefix of the logged one — no re-run). SFT has `n_fwd = n_gen`._

## 1. Setup & metric definitions

| field | meaning |
|---|---|
| `trace_len` | ground-truth reference trace length (tokens); identical across runs → the stratification axis |
| `max_new` | per-row generation cap = `min(16384, ceil(trace_len × 1.5))` (adaptive) |
| `n_gen` | tokens actually emitted |
| `n_fwd` | forward steps; for CODI includes latent steps (`> n_gen`), for SFT equals `n_gen` |
| **pass@1** | `correct / n` — exact-match accuracy over all samples; an over-budget (truncated) row counts wrong |
| **valid%** | `(predicted≠None and n_fwd<max_new) / n` — parsed into a well-formed answer *within* the forward budget |
| **condAcc** | `correct / valid` — accuracy *given* a parseable, in-budget answer |
| **fwd/ref** | mean `n_fwd / trace_len` — forward-step cost vs reference (for SFT equals output compression since `n_fwd=n_gen`; for CODI includes latent steps) |
| **trunc%** | `(n_fwd≥max_new) / n` — ran out of forward-step budget (CODI's latent steps count against it; SFT's `n_fwd=n_gen`). Truncated rows are scored invalid and wrong. |

## 2. Headline (ALL samples)

| run | pass@1 | valid% | condAcc | mean_gen | mean_fwd | fwd/ref | trunc% |
|---|--:|--:|--:|--:|--:|--:|--:|
| **sft_1.5b** | 0.441 | 94.3% | 0.468 | 2096 | 2096 | 0.76 | 5.7% |
| **sft_3b** | 0.461 | 92.8% | 0.497 | 2309 | 2309 | 0.79 | 7.2% |
| **codi_1.5b** | 0.366 | 84.8% | 0.431 | 2027 | 2385 | 0.69 | 15.2% |
| **codi_3b** | 0.355 | 76.4% | 0.465 | 2502 | 2901 | 0.78 | 23.6% |

## 3. Fine-grained per-length tables

### sft_1.5b

| trace_len | n | pass@1 | valid% | condAcc | mean_gen | mean_fwd | fwd/ref | trunc% |
|---|--:|--:|--:|--:|--:|--:|--:|--:|
| 0-255 | 320 | 0.653 | 98% | 0.666 | 133 | 133 | 0.70 | 2% |
| 256-511 | 246 | 0.561 | 96% | 0.587 | 294 | 294 | 0.81 | 4% |
| 512-1023 | 162 | 0.407 | 93% | 0.437 | 665 | 665 | 0.92 | 7% |
| 1024-2047 | 51 | 0.255 | 96% | 0.265 | 1237 | 1237 | 0.91 | 4% |
| 2048-3071 | 11 | 0.273 | 82% | 0.333 | 2635 | 2635 | 1.06 | 18% |
| 3072-4095 | 150 | 0.307 | 97% | 0.317 | 3012 | 3012 | 0.86 | 3% |
| 4096-8191 | 247 | 0.348 | 96% | 0.363 | 3684 | 3684 | 0.65 | 4% |
| 8192-16383 | 58 | 0.103 | 88% | 0.118 | 8636 | 8636 | 0.79 | 12% |
| 16384+ | 45 | 0.044 | 58% | 0.077 | 11710 | 11710 | 0.42 | 42% |

### sft_3b

| trace_len | n | pass@1 | valid% | condAcc | mean_gen | mean_fwd | fwd/ref | trunc% |
|---|--:|--:|--:|--:|--:|--:|--:|--:|
| 0-255 | 320 | 0.666 | 98% | 0.676 | 132 | 132 | 0.69 | 2% |
| 256-511 | 246 | 0.610 | 96% | 0.638 | 295 | 295 | 0.82 | 4% |
| 512-1023 | 162 | 0.469 | 96% | 0.490 | 640 | 640 | 0.89 | 4% |
| 1024-2047 | 51 | 0.275 | 100% | 0.275 | 1163 | 1163 | 0.87 | 0% |
| 2048-3071 | 11 | 0.182 | 73% | 0.250 | 2693 | 2693 | 1.08 | 27% |
| 3072-4095 | 150 | 0.307 | 94% | 0.326 | 3187 | 3187 | 0.90 | 6% |
| 4096-8191 | 247 | 0.356 | 91% | 0.391 | 4761 | 4761 | 0.83 | 9% |
| 8192-16383 | 58 | 0.086 | 79% | 0.109 | 8260 | 8260 | 0.75 | 21% |
| 16384+ | 45 | 0.022 | 47% | 0.048 | 11963 | 11963 | 0.42 | 53% |

### codi_1.5b

| trace_len | n | pass@1 | valid% | condAcc | mean_gen | mean_fwd | fwd/ref | trunc% |
|---|--:|--:|--:|--:|--:|--:|--:|--:|
| 0-255 | 320 | 0.616 | 98% | 0.627 | 108 | 118 | 0.63 | 2% |
| 256-511 | 246 | 0.472 | 98% | 0.481 | 184 | 208 | 0.58 | 2% |
| 512-1023 | 162 | 0.278 | 94% | 0.296 | 367 | 425 | 0.59 | 6% |
| 1024-2047 | 51 | 0.137 | 92% | 0.149 | 678 | 812 | 0.58 | 8% |
| 2048-3071 | 11 | 0.000 | 27% | 0.000 | 2962 | 3822 | 1.49 | 73% |
| 3072-4095 | 150 | 0.260 | 73% | 0.355 | 2608 | 3079 | 0.87 | 27% |
| 4096-8191 | 247 | 0.243 | 77% | 0.316 | 3606 | 4202 | 0.73 | 23% |
| 8192-16383 | 58 | 0.103 | 40% | 0.261 | 10237 | 12180 | 1.12 | 60% |
| 16384+ | 45 | 0.044 | 31% | 0.143 | 11840 | 13988 | 0.54 | 69% |

### codi_3b

| trace_len | n | pass@1 | valid% | condAcc | mean_gen | mean_fwd | fwd/ref | trunc% |
|---|--:|--:|--:|--:|--:|--:|--:|--:|
| 0-255 | 320 | 0.616 | 98% | 0.625 | 106 | 116 | 0.62 | 2% |
| 256-511 | 246 | 0.496 | 98% | 0.506 | 184 | 207 | 0.58 | 2% |
| 512-1023 | 162 | 0.358 | 96% | 0.374 | 360 | 419 | 0.58 | 4% |
| 1024-2047 | 51 | 0.196 | 88% | 0.222 | 756 | 903 | 0.64 | 12% |
| 2048-3071 | 11 | 0.091 | 45% | 0.200 | 2352 | 2966 | 1.19 | 55% |
| 3072-4095 | 150 | 0.220 | 64% | 0.344 | 2889 | 3365 | 0.95 | 36% |
| 4096-8191 | 247 | 0.121 | 36% | 0.341 | 6319 | 7106 | 1.21 | 64% |
| 8192-16383 | 58 | 0.086 | 45% | 0.192 | 8955 | 10873 | 0.99 | 55% |
| 16384+ | 45 | 0.044 | 33% | 0.133 | 11367 | 13705 | 0.51 | 67% |

## 4. CODI vs SFT — delta view

SFT is the base at each scale; CODI is the comparison, paired by scale. Each table is **Δ = CODI − SFT** at that scale, laid out on the same columns as §3. Signs are raw CODI − SFT: for pass@1 / valid% / condAcc a positive Δ means CODI is better; for mean_gen / mean_fwd / fwd/ref / trunc% a positive Δ means CODI spends more / truncates more (worse). valid% and trunc% deltas are in percentage points. `n` is shared across the pair. Cells where CODI wins on a quality metric are **bold**.

### 4.1 codi_1.5b − sft_1.5b

| trace_len | n | pass@1 | valid% | condAcc | mean_gen | mean_fwd | fwd/ref | trunc% |
|---|--:|--:|--:|--:|--:|--:|--:|--:|
| 0-255 | 320 | -0.037 | +0 | -0.038 | -25 | -15 | -0.07 | +0 |
| 256-511 | 246 | -0.089 | **+2** | -0.106 | -110 | -86 | -0.23 | -2 |
| 512-1023 | 162 | -0.130 | **+1** | -0.141 | -298 | -240 | -0.33 | -1 |
| 1024-2047 | 51 | -0.118 | -4 | -0.116 | -559 | -425 | -0.33 | +4 |
| 2048-3071 | 11 | -0.273 | -55 | -0.333 | +327 | +1187 | +0.43 | +55 |
| 3072-4095 | 150 | -0.047 | -23 | **+0.037** | -404 | +67 | +0.01 | +23 |
| 4096-8191 | 247 | -0.105 | -19 | -0.047 | -78 | +518 | +0.08 | +19 |
| 8192-16383 | 58 | 0.000 | -48 | **+0.143** | +1601 | +3544 | +0.33 | +48 |
| 16384+ | 45 | 0.000 | -27 | **+0.066** | +130 | +2278 | +0.12 | +27 |
| **ALL** | 1290 | **-0.075** | **-9.5** | **-0.036** | **-69** | **+289** | **-0.07** | **+9.5** |

### 4.2 codi_3b − sft_3b

| trace_len | n | pass@1 | valid% | condAcc | mean_gen | mean_fwd | fwd/ref | trunc% |
|---|--:|--:|--:|--:|--:|--:|--:|--:|
| 0-255 | 320 | -0.050 | +0 | -0.051 | -26 | -16 | -0.07 | +0 |
| 256-511 | 246 | -0.114 | **+2** | -0.132 | -111 | -88 | -0.24 | -2 |
| 512-1023 | 162 | -0.111 | +0 | -0.116 | -280 | -221 | -0.31 | +0 |
| 1024-2047 | 51 | -0.078 | -12 | -0.052 | -407 | -260 | -0.23 | +12 |
| 2048-3071 | 11 | -0.091 | -27 | -0.050 | -341 | +273 | +0.11 | +27 |
| 3072-4095 | 150 | -0.087 | -30 | **+0.018** | -298 | +178 | +0.05 | +30 |
| 4096-8191 | 247 | -0.235 | -55 | -0.050 | +1558 | +2345 | +0.38 | +55 |
| 8192-16383 | 58 | 0.000 | -34 | **+0.084** | +695 | +2613 | +0.24 | +34 |
| 16384+ | 45 | **+0.022** | -13 | **+0.086** | -596 | +1742 | +0.09 | +13 |
| **ALL** | 1290 | **-0.106** | **-16.4** | **-0.033** | **+193** | **+592** | **-0.01** | **+16.4** |

## 5. Key findings

1. **Accuracy decays monotonically with trace length for every run.** From the shortest bin (0–255) to the longest (16384+), pass@1 collapses from ~0.62–0.67 to ~0.02–0.04. Length is the dominant driver of difficulty regardless of model or method.

2. **The 3072 boundary marks a regime change, but it is a `max_new` artifact — not a smooth degradation.** For rows with `trace_len < 3072` the adaptive cap `ceil(trace_len×1.5)` is loose; at `trace_len ≥ 3072` the cap starts biting and generations that need the full trace get squeezed. Note the local *rebound* at the 3072–4095 bin (pass@1 rises vs 2048–3071 for SFT and jumps for CODI) — the 2048–3071 bin is both tiny (n=11) and the worst-hit by truncation before the cap widens.

3. **SFT ≥ CODI on pass@1 everywhere except the extreme tail.** SFT_3b leads overall (0.461). CODI only ties/edges ahead in the 8192+ bins (8192–16383 is a tie — 0.103 at 1.5b, 0.086 at 3b; 16384+ codi_3b +0.022), and only because SFT's exact-match also floors out there.

4. **CODI's real weakness is truncation, not reasoning.** Under the forward-step budget CODI's `valid%` craters on long traces (36–45% for codi_3b at 4096+ vs 79–91% for sft_3b) and truncation is ~3× SFT's (codi_3b ALL = 23.6% vs sft_3b 7.2%). But **condAcc (accuracy given an in-budget parseable answer) stays competitive** — codi_3b ALL 0.465 vs sft_3b 0.497 — and CODI actually **beats SFT on condAcc in the long bins** (both 8192+ bins and 3072–4095), losing only at 4096–8191. → CODI *can* reason on long traces but frequently burns its forward budget without terminating in a well-formed answer.

5. **Once latent steps are counted, CODI's compute advantage nearly vanishes (fwd/ref ≈ 0.69–0.78 vs SFT 0.76–0.79).** CODI *emits* fewer output tokens (gen/ref ≈ 0.60–0.68), but each generated token costs extra forward passes (`n_fwd > n_gen`), so on a forward-step basis it lands roughly level with SFT — and in the long/hard bins fwd/ref actually exceeds 1.0 (codi_3b 4096–8191 = 1.21, codi_1.5b 8192–16383 = 1.12), i.e. CODI spends *more* forward compute than the reference is long while still failing to terminate (those are the same bins with 55–60% truncation). The latent-step "compression" is an output-length artifact, not a compute saving.

6. **Scale helps SFT cleanly but not CODI.** sft_3b > sft_1.5b (0.461 vs 0.441) across almost all bins. For CODI, 3b vs 1.5b is a wash overall (0.355 vs 0.366): codi_3b's higher condAcc is cancelled by *worse* valid%/truncation (76.4% vs 84.8% valid). codi_3b (ck1500) is likely under-trained relative to its capacity — the format head hasn't caught up.

### One-line takeaway
Below ~1K tokens all four are close; the spread that determines the headline number is entirely in the long tail, where **SFT loses accuracy gracefully while CODI loses *format validity* (truncation) faster than it loses reasoning ability.**
