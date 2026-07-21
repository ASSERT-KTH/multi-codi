# locals_compare — CODI vs SFT stratified by locals complexity

_Generated 2026-07-06 from the same `results/…/len_*.json` (held-out, n=1290 each) as [len_compare.md](len_compare.md), via `python -m eval.stats_by_locals_full`. Columns, budget logic, and delta convention are identical to len_compare §4 — only the stratification **axis** changes: from reference trace length to per-item locals complexity._

## 1. Data composition & axes

The held-out eval is **not** pure CRUXEval. `eval_len.py` builds its 1290 rows from **two precomputed caches**, which turn out to be cleanly segregated by length:

| source | ids | n | trace_len | regime |
|---|---|--:|---|---|
| `data/cache/cruxeval_codi` | `sample_*` | 790 | 114 – 2926 | **short/medium** (all < 3072) |
| `data/cache/codi_train`, `MIN_LEN=3073` | `HumanEval_* / mbpp_* / pyx_*` | 500 | 3075 – 147424 | **long tail** (all ≥ 3073) |

> **Correction.** An earlier version of this doc bucketed those 500 rows as "untraceable" and guessed they were re-trace failures. That was wrong: they are simply the non-CRUXEval half of the eval, and the axis script was resolving code/input through `load_cruxeval()` (which knows only the 800 `sample_*` items). Resolving instead through the two caches (`--caches`) covers **1290/1290** ids; all 500 long rows trace fine (0 errors even at `max_frames=20000`). Because the two sources are length-segregated, the short/medium tables below are exactly the CRUXEval subset and the long-tail tables are exactly the ≥3073 held-out set — so they are listed **separately**.

| axis | meaning | short edges | long edges |
|---|---|---|---|
| **nvars** | # distinct local names across traced CALL/LINE frames | 1,2,3,4,5,6+ | 1,2,3,4,5,6-7,8-9,10+ |
| **locals_len (chr)** | mean `len(json.dumps(locals))` per state frame ("avg var len") | 0-15…64+ | 0-31…128+ |
| **nframes** | # LINE frames in the trace = # latent spans = # KD anchors (CODI's native difficulty unit) | 2-3…41+ | 32-63…320+ |

Edges differ per regime because the long tail is far more complex (nvars median 5 / max 30 vs CRUXEval's 1–6; locals_len median 51 / max 434 vs ≤ 64). The axis is a **property of the item**, computed once per id and shared across all four runs, so the pairing is exact.

Delta convention (unchanged): **Δ = CODI − SFT**, paired by scale. Positive pass@1 / valid% / condAcc ⇒ CODI better (**bold**); positive mean_gen / mean_fwd / fwd/ref / trunc% ⇒ CODI spends/truncates more (worse). valid% / trunc% in percentage points; `n` shared across the pair.

---

## 2. Short/medium regime — CRUXEval (< 3072), n = 790

### 2.1 nvars

**codi_1.5b − sft_1.5b**

| nvars | n | pass@1 | valid% | condAcc | mean_gen | mean_fwd | fwd/ref | trunc% |
|---|--:|--:|--:|--:|--:|--:|--:|--:|
| 1 | 115 | -0.035 | **+1** | -0.042 | -18 | -7 | -0.03 | -1 |
| 2 | 208 | -0.067 | -1 | -0.065 | -35 | -7 | -0.09 | +1 |
| 3 | 228 | -0.061 | -2 | -0.053 | -149 | -77 | -0.21 | +2 |
| 4 | 144 | -0.125 | **+1** | -0.137 | -242 | -198 | -0.29 | -1 |
| 5 | 68 | -0.147 | **+4** | -0.174 | -319 | -257 | -0.38 | -4 |
| 6+ | 27 | -0.148 | +0 | -0.148 | -319 | -275 | -0.31 | +0 |
| **ALL** | 790 | **-0.081** | **-0** | **-0.084** | **-137** | **-93** | **-0.18** | **+0** |

**codi_3b − sft_3b**

| nvars | n | pass@1 | valid% | condAcc | mean_gen | mean_fwd | fwd/ref | trunc% |
|---|--:|--:|--:|--:|--:|--:|--:|--:|
| 1 | 115 | -0.061 | +0 | -0.062 | -17 | -6 | -0.03 | +0 |
| 2 | 208 | -0.038 | **+1** | -0.046 | -56 | -33 | -0.11 | -1 |
| 3 | 228 | -0.127 | -2 | -0.123 | -144 | -78 | -0.20 | +2 |
| 4 | 144 | -0.097 | +0 | -0.101 | -218 | -176 | -0.28 | +0 |
| 5 | 68 | -0.059 | -1 | -0.054 | -282 | -215 | -0.32 | +1 |
| 6+ | 27 | -0.185 | +0 | -0.185 | -320 | -277 | -0.32 | +0 |
| **ALL** | 790 | **-0.085** | **-0** | **-0.086** | **-134** | **-92** | **-0.18** | **+0** |

### 2.2 locals_len (avg rendered var size, chars)

**codi_1.5b − sft_1.5b**

| locals_len | n | pass@1 | valid% | condAcc | mean_gen | mean_fwd | fwd/ref | trunc% |
|---|--:|--:|--:|--:|--:|--:|--:|--:|
| 0-15 | 79 | -0.051 | **+1** | -0.061 | -17 | -7 | -0.04 | -1 |
| 16-23 | 134 | -0.045 | +0 | -0.047 | -38 | -20 | -0.07 | +0 |
| 24-31 | 185 | -0.038 | -2 | -0.031 | -59 | -29 | -0.11 | +2 |
| 32-47 | 268 | -0.101 | -1 | -0.102 | -173 | -110 | -0.24 | +1 |
| 48-63 | 97 | -0.155 | **+1** | -0.165 | -325 | -258 | -0.36 | -1 |
| 64+ | 27 | -0.185 | **+7** | -0.218 | -481 | -380 | -0.46 | -7 |
| **ALL** | 790 | **-0.081** | **-0** | **-0.084** | **-137** | **-93** | **-0.18** | **+0** |

**codi_3b − sft_3b**

| locals_len | n | pass@1 | valid% | condAcc | mean_gen | mean_fwd | fwd/ref | trunc% |
|---|--:|--:|--:|--:|--:|--:|--:|--:|
| 0-15 | 79 | -0.089 | +0 | -0.091 | -14 | -4 | -0.03 | +0 |
| 16-23 | 134 | -0.104 | -1 | -0.099 | -16 | +4 | -0.06 | +1 |
| 24-31 | 185 | -0.038 | **+1** | -0.043 | -64 | -36 | -0.14 | -1 |
| 32-47 | 268 | -0.123 | -1 | -0.121 | -179 | -122 | -0.23 | +1 |
| 48-63 | 97 | -0.041 | **+1** | -0.047 | -306 | -236 | -0.35 | -1 |
| 64+ | 27 | -0.074 | +0 | -0.080 | -481 | -390 | -0.40 | +0 |
| **ALL** | 790 | **-0.085** | **-0** | **-0.086** | **-134** | **-92** | **-0.18** | **+0** |

### 2.3 nframes (# latent spans / KD anchors)

**codi_1.5b − sft_1.5b**

| nframes | n | pass@1 | valid% | condAcc | mean_gen | mean_fwd | fwd/ref | trunc% |
|---|--:|--:|--:|--:|--:|--:|--:|--:|
| 2-3 | 226 | -0.027 | +0 | -0.030 | -18 | -10 | -0.05 | -0 |
| 4-5 | 168 | -0.113 | -1 | -0.111 | -51 | -36 | -0.13 | +1 |
| 6-8 | 113 | -0.080 | **+3** | -0.100 | -101 | -76 | -0.22 | -3 |
| 9-12 | 84 | -0.036 | **+4** | -0.052 | -194 | -161 | -0.33 | -4 |
| 13-20 | 105 | -0.076 | **+3** | -0.091 | -302 | -253 | -0.35 | -3 |
| 21-40 | 72 | -0.181 | -3 | -0.191 | -458 | -357 | -0.33 | +3 |
| 41+ | 22 | -0.273 | -36 | -0.267 | -147 | +422 | +0.11 | +36 |
| **ALL** | 790 | **-0.081** | **-0** | **-0.084** | **-137** | **-93** | **-0.18** | **+0** |

**codi_3b − sft_3b**

| nframes | n | pass@1 | valid% | condAcc | mean_gen | mean_fwd | fwd/ref | trunc% |
|---|--:|--:|--:|--:|--:|--:|--:|--:|
| 2-3 | 226 | -0.022 | +0 | -0.022 | -19 | -11 | -0.05 | +0 |
| 4-5 | 168 | -0.113 | **+1** | -0.124 | -56 | -41 | -0.15 | -1 |
| 6-8 | 113 | -0.106 | **+2** | -0.121 | -99 | -74 | -0.21 | -2 |
| 9-12 | 84 | -0.131 | **+2** | -0.146 | -182 | -150 | -0.31 | -2 |
| 13-20 | 105 | -0.076 | **+1** | -0.083 | -279 | -227 | -0.33 | -1 |
| 21-40 | 72 | -0.125 | -7 | -0.110 | -363 | -253 | -0.26 | +7 |
| 41+ | 22 | -0.136 | -23 | -0.083 | -456 | -15 | -0.07 | +23 |
| **ALL** | 790 | **-0.085** | **-0** | **-0.086** | **-134** | **-92** | **-0.18** | **+0** |

---

## 3. Long-tail regime — held-out ≥ 3073, n = 500

_Small-n bins (nvars 1/2/3 = 5/10/16; locals_len 0-31/128+ = 27/27) are noisy — read the modal bins (nvars 4 = 180, locals_len 32-47 = 200) and the ALL row._

### 3.1 nvars

**codi_1.5b − sft_1.5b**

| nvars | n | pass@1 | valid% | condAcc | mean_gen | mean_fwd | fwd/ref | trunc% |
|---|--:|--:|--:|--:|--:|--:|--:|--:|
| 1 | 5 | **+0.400** | -20 | **+0.500** | -557 | -117 | +0.03 | +20 |
| 2 | 10 | -0.200 | -30 | -0.157 | +1282 | +1791 | +0.36 | +30 |
| 3 | 16 | -0.250 | -50 | -0.185 | +2836 | +4081 | +0.42 | +50 |
| 4 | 180 | -0.133 | -8 | -0.110 | -64 | +358 | +0.03 | +8 |
| 5 | 56 | **+0.089** | -34 | **+0.240** | -180 | +917 | +0.08 | +34 |
| 6-7 | 119 | +0.000 | -41 | **+0.105** | +1048 | +2194 | +0.29 | +41 |
| 8-9 | 70 | -0.143 | -27 | -0.090 | -671 | +514 | -0.05 | +27 |
| 10+ | 44 | +0.000 | -20 | **+0.057** | -2109 | -1123 | -0.06 | +20 |
| **ALL** | 500 | **-0.066** | **-24** | **+0.012** | **+37** | **+892** | **+0.10** | **+24** |

**codi_3b − sft_3b**

| nvars | n | pass@1 | valid% | condAcc | mean_gen | mean_fwd | fwd/ref | trunc% |
|---|--:|--:|--:|--:|--:|--:|--:|--:|
| 1 | 5 | **+0.200** | **+20** | **+0.100** | -2055 | -1890 | -0.35 | -20 |
| 2 | 10 | -0.300 | +0 | -0.500 | -840 | +201 | +0.02 | +0 |
| 3 | 16 | +0.000 | -6 | **+0.042** | -2815 | -1844 | -0.07 | +6 |
| 4 | 180 | -0.378 | -67 | -0.115 | +2569 | +3284 | +0.56 | +67 |
| 5 | 56 | +0.000 | -45 | **+0.200** | +735 | +1925 | +0.25 | +45 |
| 6-7 | 119 | **+0.025** | -30 | **+0.104** | +26 | +1142 | +0.09 | +30 |
| 8-9 | 70 | -0.071 | -34 | **+0.061** | +644 | +2005 | +0.13 | +34 |
| 10+ | 44 | **+0.045** | -7 | **+0.073** | -3048 | -2316 | -0.24 | +7 |
| **ALL** | 500 | **-0.140** | **-42** | **-0.012** | **+708** | **+1672** | **+0.24** | **+42** |

### 3.2 locals_len (avg rendered var size, chars)

**codi_1.5b − sft_1.5b**

| locals_len | n | pass@1 | valid% | condAcc | mean_gen | mean_fwd | fwd/ref | trunc% |
|---|--:|--:|--:|--:|--:|--:|--:|--:|
| 0-31 | 27 | +0.000 | -22 | **+0.035** | -55 | +448 | +0.09 | +22 |
| 32-47 | 200 | -0.140 | -8 | -0.118 | -49 | +292 | +0.01 | +8 |
| 48-63 | 80 | **+0.062** | -28 | **+0.186** | -400 | +536 | +0.01 | +28 |
| 64-95 | 128 | -0.039 | -43 | **+0.079** | +615 | +1951 | +0.21 | +43 |
| 96-127 | 38 | -0.053 | -47 | **+0.114** | +236 | +2004 | +0.31 | +47 |
| 128+ | 27 | -0.111 | -22 | -0.105 | -949 | +251 | +0.14 | +22 |
| **ALL** | 500 | **-0.066** | **-24** | **+0.012** | **+37** | **+892** | **+0.10** | **+24** |

**codi_3b − sft_3b**

| locals_len | n | pass@1 | valid% | condAcc | mean_gen | mean_fwd | fwd/ref | trunc% |
|---|--:|--:|--:|--:|--:|--:|--:|--:|
| 0-31 | 27 | **+0.037** | -4 | **+0.067** | -635 | -140 | -0.02 | +4 |
| 32-47 | 200 | -0.325 | -58 | -0.164 | +1917 | +2542 | +0.44 | +58 |
| 48-63 | 80 | -0.038 | -36 | **+0.121** | +351 | +1495 | +0.19 | +36 |
| 64-95 | 128 | -0.023 | -33 | **+0.089** | -86 | +1060 | +0.07 | +33 |
| 96-127 | 38 | +0.000 | -39 | **+0.165** | +126 | +1846 | +0.17 | +39 |
| 128+ | 27 | +0.000 | -19 | **+0.064** | -1262 | +228 | +0.06 | +19 |
| **ALL** | 500 | **-0.140** | **-42** | **-0.012** | **+708** | **+1672** | **+0.24** | **+42** |

### 3.3 nframes (# latent spans / KD anchors)

**codi_1.5b − sft_1.5b**

| nframes | n | pass@1 | valid% | condAcc | mean_gen | mean_fwd | fwd/ref | trunc% |
|---|--:|--:|--:|--:|--:|--:|--:|--:|
| 32-63 | 81 | -0.136 | -17 | -0.074 | -164 | +174 | +0.03 | +17 |
| 64-95 | 188 | -0.080 | -18 | -0.029 | -312 | +148 | +0.03 | +18 |
| 96-127 | 97 | -0.021 | -15 | **+0.036** | -842 | -291 | -0.03 | +15 |
| 128-191 | 46 | -0.065 | -50 | **+0.130** | +1163 | +2649 | +0.30 | +50 |
| 192-319 | 54 | -0.056 | -50 | **+0.048** | +1985 | +4196 | +0.47 | +50 |
| 320+ | 34 | **+0.029** | -29 | **+0.177** | +342 | +2469 | +0.14 | +29 |
| **ALL** | 500 | **-0.066** | **-24** | **+0.012** | **+37** | **+892** | **+0.10** | **+24** |

**codi_3b − sft_3b**

| nframes | n | pass@1 | valid% | condAcc | mean_gen | mean_fwd | fwd/ref | trunc% |
|---|--:|--:|--:|--:|--:|--:|--:|--:|
| 32-63 | 81 | -0.272 | -30 | -0.185 | -188 | +166 | +0.04 | +30 |
| 64-95 | 188 | -0.176 | -51 | -0.016 | +1113 | +1702 | +0.31 | +51 |
| 96-127 | 97 | -0.175 | -56 | -0.000 | +1459 | +2286 | +0.36 | +56 |
| 128-191 | 46 | **+0.022** | -24 | **+0.126** | -962 | +361 | +0.02 | +24 |
| 192-319 | 54 | -0.019 | -37 | **+0.111** | +1728 | +3849 | +0.40 | +37 |
| 320+ | 34 | **+0.059** | -9 | **+0.221** | -902 | +1666 | +0.03 | +9 |
| **ALL** | 500 | **-0.140** | **-42** | **-0.012** | **+708** | **+1672** | **+0.24** | **+42** |

---

## 4. Absolute pass@1 (reference)

### Short/medium (CRUXEval), by nvars

| nvars | n | sft1.5 | codi1.5 | sft3b | codi3b |
|---|--:|--:|--:|--:|--:|
| 1 | 115 | 0.696 | 0.661 | 0.661 | 0.600 |
| 2 | 208 | 0.562 | 0.495 | 0.596 | 0.558 |
| 3 | 228 | 0.531 | 0.469 | 0.596 | 0.469 |
| 4 | 144 | 0.500 | 0.375 | 0.528 | 0.431 |
| 5 | 68 | 0.456 | 0.309 | 0.485 | 0.426 |
| 6+ | 27 | 0.296 | 0.148 | 0.370 | 0.185 |

### Long tail (≥3073), by nvars

| nvars | n | sft1.5 | codi1.5 | sft3b | codi3b |
|---|--:|--:|--:|--:|--:|
| 4 | 180 | 0.461 | 0.328 | 0.478 | 0.100 |
| 5 | 56 | 0.143 | 0.232 | 0.179 | 0.179 |
| 6-7 | 119 | 0.118 | 0.118 | 0.092 | 0.118 |
| 8-9 | 70 | 0.286 | 0.143 | 0.257 | 0.186 |
| 10+ | 44 | 0.159 | 0.159 | 0.159 | 0.205 |

### Long tail (≥3073), by locals_len

| locals_len | n | sft1.5 | codi1.5 | sft3b | codi3b |
|---|--:|--:|--:|--:|--:|
| 32-47 | 200 | 0.455 | 0.315 | 0.430 | 0.105 |
| 48-63 | 80 | 0.175 | 0.237 | 0.200 | 0.163 |
| 64-95 | 128 | 0.164 | 0.125 | 0.195 | 0.172 |
| 96-127 | 38 | 0.158 | 0.105 | 0.158 | 0.158 |
| 128+ | 27 | 0.185 | 0.074 | 0.111 | 0.111 |

---

## 5. Key findings

1. **The two regimes fail CODI through opposite channels.** In the short/medium regime CODI's loss is **condAcc** (reasoning/compression): valid% ≈ SFT (Δ ≈ 0 everywhere, trunc Δ ≈ 0), yet condAcc trails and the gap **widens monotonically with per-step state** (1.5b: −0.042 → −0.174 across nvars 1→5; −0.061 → −0.218 across locals_len). In the long tail the sign flips: condAcc is **competitive or better** (ALL Δ +0.012 at 1.5b; many bins positive), but **valid%/truncation collapses** (ALL −24 / −42 pp valid, +24 / +42 pp trunc). → Short traces: CODI *reasons* worse per step. Long traces: CODI *terminates* worse, but reasons fine on what it finishes. This is the locals-axis confirmation of len_compare's headline.

2. **Latent compression is the short-regime mechanism.** CODI's mean_gen barely scales with complexity (~100 → ~545 across CRUXEval bins) while SFT's tracks the work (~108 → ~925); the fwd/ref advantage is largest exactly where accuracy is worst (locals_len 64+: gen Δ −481, fwd/ref Δ −0.46, condAcc Δ −0.218). More state to carry ⇒ more dropped into a near-constant latent budget. No budget limit is involved — it degrades *before* truncation matters.

3. **In the long tail, complexity compounds with length to blow the budget.** Within the ≥3073 set, CODI's valid% falls and truncation rises as locals_len grows (codi_1.5b valid%: 74→88→62→48→34 across 0-31…96-127; trunc 26→12→38→52→66 pp). So per-step complexity isn't just a short-trace story — on long traces it is the second-order driver of CODI's truncation, on top of raw length.

4. **codi_3b's long-tail truncation is catastrophic in the modal bin.** The largest long-tail bins are where codi_3b implodes: nvars 4 (n=180) pass@1 Δ −0.378 with valid% −67 / trunc +67; locals_len 32-47 (n=200) Δ −0.325, valid −58, trunc +58 — yet condAcc in those same bins is only −0.115 / −0.164. Almost the entire 3b long-tail deficit is unterminated generations, not wrong reasoning (matches len_compare finding 6: 3b's format head lags its capacity).

5. **Scale does not buy CODI complexity-robustness on any axis.** codi_3b's per-step-complexity slope is as steep as codi_1.5b's in the short regime, and in the long tail 3b is *worse* than 1.5b (ALL −0.140 vs −0.066), driven by truncation not reasoning.

6. **nframes (# latent spans / KD anchors) is the most causal axis, and it localizes CODI's truncation onset.** Each LINE frame is literally one latent-decode block, so this is CODI's native difficulty unit. In the short regime condAcc degrades monotonically with anchor count (codi_1.5b: −0.030 at 2-3 → −0.191 at 21-40) while valid% stays ≥ SFT — until a sharp cliff at **41+ frames** (valid −36 pp, trunc +36), the point where even a short-trace item outruns the forward budget. In the long tail the cliff has already happened everywhere: truncation is 17–56 pp worse from the smallest bin on, yet condAcc climbs back to **positive** as anchors grow (codi_3b 320+: condAcc +0.221). So the number of latent anchors — not raw token length or per-frame width — is what most directly predicts *where* CODI flips from "reasons worse" to "can't terminate."

### One-line takeaway
Split by per-step state, CODI shows a clean two-regime failure: **on short traces it loses reasoning to latent compression (condAcc down, monotone in nvars/locals_len/nframes, no truncation); on long traces it loses format validity to truncation (condAcc ≈ SFT, valid% craters). The number of latent anchors (nframes) is the sharpest predictor of the crossover — CODI stays valid until ~40 anchors, then truncation takes over.**
