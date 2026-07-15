"""Fingerprint a base SFT checkpoint: mean teacher-CE on codi_train_full traces.

Replicates the CODI teacher path exactly (train_codi_recon.forward -> shared_teacher):
full = cat(prompt_ids, trace_ids); CE on the trace next-tokens only. This is the
CODI-step-0 teacher_loss of a run based on this checkpoint, so it locates the base's
fit level against the logged teacher_loss of GOOD/repro/probes (no CODI run needed).

Run (single GPU) from codi_trace/:
  python -m eval.diag.base_fingerprint --models A B C --n 256
"""

import argparse
import torch
import torch.nn.functional as F
from transformers import AutoModelForCausalLM, AutoTokenizer

from data.precompute_loader import load_cache
from data.dataset import IGNORE_INDEX
from data.tokens import add_trace_tokens


@torch.no_grad()
def trace_ce(model, prompt_ids, trace_ids, dev):
    full = torch.cat([torch.tensor(prompt_ids, device=dev), torch.tensor(trace_ids, device=dev)])
    labels = torch.cat([full.new_full((len(prompt_ids),), IGNORE_INDEX),
                        torch.tensor(trace_ids, device=dev)])
    logits = model(input_ids=full[None], use_cache=False).logits
    return F.cross_entropy(logits[0, :-1], labels[1:], ignore_index=IGNORE_INDEX).item()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--models", nargs="+", required=True)
    ap.add_argument("--cache_dir", default="data/cache/codi_train_full")
    ap.add_argument("--max_seq_len", type=int, default=3072)
    ap.add_argument("--n", type=int, default=256)
    args = ap.parse_args()

    dev = "cuda"
    ds = load_cache(args.cache_dir, max_len=args.max_seq_len, n_samples=-1)
    idx = list(range(min(args.n, len(ds))))  # deterministic first-N; same rows for every model
    print(f"{len(ds)} examples in cache; fingerprinting on first {len(idx)}", flush=True)

    for m in args.models:
        tok = AutoTokenizer.from_pretrained(m, use_fast=True)
        add_trace_tokens(tok)
        model = AutoModelForCausalLM.from_pretrained(m, torch_dtype=torch.bfloat16).to(dev).eval()
        ces = [trace_ce(model, ds[i]["prompt_ids"], ds[i]["trace_ids"], dev) for i in idx]
        ces_sorted = sorted(ces)
        mean = sum(ces) / len(ces)
        med = ces_sorted[len(ces) // 2]
        print(f"[{m}] mean_trace_CE={mean:.4f}  median={med:.4f}  "
              f"p10={ces_sorted[len(ces)//10]:.4f}  p90={ces_sorted[9*len(ces)//10]:.4f}", flush=True)
        del model
        torch.cuda.empty_cache()


if __name__ == "__main__":
    main()
