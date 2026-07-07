# Copyright (c) Meta Platforms, Inc. and affiliates.

"""Ground-truth execution traces -> tokenized examples. Prompt + rendered trace,
prompt masked in labels. Membership is set by _tokenize_trace; length filtering
happens at load (data.cache)."""

from __future__ import annotations

import json

from .cache import load_cache
from .ground_truth import ground_truth_trace, make_trace_context
from .trace_format import (
    ACTION_SEP,
    LINE_SEP,
    TraceEvent,
    render_frames_to_generation,
)

IGNORE_INDEX = -100
def _prompt_str(code: str, input_str: str) -> str:
    ctx = make_trace_context(code, input_str)
    return f"<|trace_context_start|>{ctx}<|frame_sep|><|call_sep|>{{}}<|action_sep|>def main():\n<|frame_sep|>"


def _tokenize_trace(code, input_str, tokenizer, *, max_frames, recon_full=False):
    """``(prompt_ids, trace_ids, spans, recon_targets)``; None to skip. Trace must
    terminate in RETURN/EXCEPTION and have >=1 LINE span. Span ``(i, j)``: ``trace_ids[i]``
    is ``<|line_sep|>``, ``j`` its ``<|action_sep|>``, ``trace_ids[i+1:j]`` the locals a
    CODI student swaps for a latent block. Single source of membership so the SFT baseline
    and CODI train on identical data. No length cap here; filtering is done at load."""
    frames, error = ground_truth_trace(code, input_str, align_to_prompt=True, max_frames=max_frames)
    if not frames or error == "frames_exceeded":
        return None
    if frames[-1].event not in (TraceEvent.RETURN, TraceEvent.EXCEPTION):
        return None
    # Qwen has no BOS (bos_token_id is None); CWM did. Prepend only if present.
    bos = [tokenizer.bos_token_id] if tokenizer.bos_token_id is not None else []
    prompt_ids = bos + tokenizer.encode(_prompt_str(code, input_str), add_special_tokens=False)
    trace_ids = tokenizer.encode(render_frames_to_generation(frames), add_special_tokens=False)
    ls = tokenizer.convert_tokens_to_ids(LINE_SEP)
    asep = tokenizer.convert_tokens_to_ids(ACTION_SEP)
    spans, i, n = [], 0, len(trace_ids)
    while i < n:
        if trace_ids[i] == ls:
            j = i + 1
            while j < n and trace_ids[j] != asep:
                j += 1
            if j == n:
                break
            spans.append((i, j))
            i = j + 1
        else:
            i += 1
    if not spans:
        return None
    recon_targets, prev = [], {}  # full_locals, or per-frame delta vs previous frame
    for f in frames:
        if f.event != TraceEvent.LINE:
            continue
        full = f.full_locals or {}
        tgt = full if recon_full else {k: v for k, v in full.items() if prev.get(k) != v}
        recon_targets.append(tokenizer.encode(json.dumps(tgt, sort_keys=True), add_special_tokens=False))
        prev = full
    if len(recon_targets) != len(spans):
        return None
    return prompt_ids, trace_ids, spans, recon_targets


def build_example(code, input_str, tokenizer, *, max_frames=-1):
    """SFT ``(input_ids, labels)`` with the prompt masked; None to skip."""
    r = _tokenize_trace(code, input_str, tokenizer, max_frames=max_frames)
    if r is None:
        return None
    prompt_ids, trace_ids, _, _ = r
    return prompt_ids + trace_ids, [IGNORE_INDEX] * len(prompt_ids) + trace_ids


def build_codi_example(code, input_str, tokenizer, *, max_frames=-1, recon_full=False):
    """Multi-span CODI example ``{prompt_ids, trace_ids, spans, recon_targets}``; None to skip."""
    r = _tokenize_trace(code, input_str, tokenizer, max_frames=max_frames, recon_full=recon_full)
    if r is None:
        return None
    prompt_ids, trace_ids, spans, recon_targets = r
    return {"prompt_ids": prompt_ids, "trace_ids": trace_ids, "spans": spans,
            "recon_targets": recon_targets}


def rows_for_sources(sources):
    """Merge {id,code,input,output} rows across sources (cruxeval held out for eval)."""
    from . import sources as _src

    rows = []
    for name in sources:
        for i, row in enumerate(_src.load_one(name)):
            missing = [k for k in ("id", "code", "input", "output") if k not in row]
            if missing:
                raise ValueError(f"{name} row {i} missing keys: {missing}")
            if not all(isinstance(row[k], str) for k in ("code", "input", "output")):
                raise TypeError(f"{name} row {i} must use string code/input/output")
            row = dict(row)
            row["id"] = str(row["id"])
            rows.append(row)
    return rows


def build_codi_single_dataset(tokenizer, cache_dir, *, max_len, n_samples=-1):
    """Single-block CODI from cache: split each trace at its last <|return_sep|> into
    {prompt_ids, reasoning_ids, answer_ids} (reasoning = whole trace, answer = final RETURN)."""
    rsep = tokenizer.convert_tokens_to_ids("<|return_sep|>")
    out = []
    for e in load_cache(cache_dir, max_len=max_len, n_samples=n_samples):
        t = e["trace_ids"]
        idx = [i for i, x in enumerate(t) if x == rsep]
        if not idx or idx[-1] == 0:
            continue
        out.append({"prompt_ids": e["prompt_ids"], "reasoning_ids": t[:idx[-1]], "answer_ids": t[idx[-1]:]})
    return out
