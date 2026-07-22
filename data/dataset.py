# Copyright (c) Meta Platforms, Inc. and affiliates.

"""Ground-truth execution traces -> tokenized examples. Prompt + rendered trace,
prompt masked in labels. Membership is set by _tokenize_trace; length filtering
happens at load (data.precompute_loader)."""

from __future__ import annotations

import glob
import os

from .ground_truth import ground_truth_trace, make_trace_context
from .trace_format import (
    ACTION_SEP,
    LINE_SEP,
    TraceEvent,
    render_frames_to_generation,
)

IGNORE_INDEX = -100
_MAX_GENERATION_CHARS = 200_000  # sanity cap on rendered trace text before tokenizing; see _tokenize_trace


def load_dataset(source: str) -> list[dict]:
    """source: a literal path, a glob pattern, or "cruxeval" (HF Hub, or $CRUXEVAL_DIR if set)."""
    if source.strip().lower() == "cruxeval":
        local_dir = os.environ.get("CRUXEVAL_DIR")
        if local_dir and os.path.isdir(local_dir):
            from datasets import load_from_disk

            return list(load_from_disk(local_dir))
        from datasets import load_dataset as hf_load_dataset

        return list(hf_load_dataset("cruxeval-org/cruxeval", split="test"))
    from datasets import load_from_disk

    paths = sorted(glob.glob(source)) if any(c in source for c in "*?[") else [source]
    rows = []
    for p in paths:
        rows.extend(list(load_from_disk(p)))
    return rows


def _prompt_str(code: str, input_str: str) -> str:
    ctx = make_trace_context(code, input_str)
    return f"<|trace_context_start|>{ctx}<|frame_sep|><|call_sep|>{{}}<|action_sep|>def main():\n<|frame_sep|>"


def _tokenize_trace(code, input_str, tokenizer, *, max_frames, trace_target="diff"):
    """``(prompt_ids, trace_ids, spans, locals_ids, full_locals_ids)``; None to skip. Trace must
    terminate in RETURN/EXCEPTION and have >=1 LINE span. Span ``(i, j)``: ``trace_ids[i]`` is
    ``<|line_sep|>``, ``j`` its ``<|action_sep|>``, ``trace_ids[i+1:j]`` the locals a CODI student
    swaps for a latent block. ``locals_ids``/``full_locals_ids``: per-LINE-frame diff/full locals,
    the two reconstruction targets, independent of which one ``trace_target`` renders into
    ``trace_ids`` itself. Single membership source for SFT and CODI; length cap at load."""
    frames, error = ground_truth_trace(code, input_str, align_to_prompt=True, max_frames=max_frames)
    if not frames or error == "frames_exceeded":
        return None
    if frames[-1].event not in (TraceEvent.RETURN, TraceEvent.EXCEPTION):
        return None
    # Qwen has no BOS (bos_token_id is None); CWM did. Prepend only if present.
    bos = [tokenizer.bos_token_id] if tokenizer.bos_token_id is not None else []
    prompt_ids = bos + tokenizer.encode(_prompt_str(code, input_str), add_special_tokens=False)
    trace_ids = tokenizer.encode(render_frames_to_generation(frames, use_full=trace_target == "full"),
                                  add_special_tokens=False)
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
    enc = lambda s: tokenizer.encode(s, add_special_tokens=False)
    lines = [f for f in frames if f.event == TraceEvent.LINE]
    locals_ids = [enc(f.locals_str) for f in lines]
    full_locals_ids = [enc(f.full_locals_str) for f in lines]
    if len(locals_ids) != len(spans):
        return None
    return prompt_ids, trace_ids, spans, locals_ids, full_locals_ids


def build_trace_record(code, input_str, tokenizer, *, max_frames=-1, trace_target="diff"):
    """Tokenized trace record ``{prompt_ids, trace_ids, spans, locals_ids, full_locals_ids}``; None to skip.
    ``trace_target``: which locals representation the visible ``trace_ids`` text itself renders
    (diff or full state); independent of the per-frame ``locals_ids``/``full_locals_ids`` targets."""
    r = _tokenize_trace(code, input_str, tokenizer, max_frames=max_frames, trace_target=trace_target)
    if r is None:
        return None
    prompt_ids, trace_ids, spans, locals_ids, full_locals_ids = r
    return {"prompt_ids": prompt_ids, "trace_ids": trace_ids, "spans": spans,
            "locals_ids": locals_ids, "full_locals_ids": full_locals_ids}


def rows_for_sources(sources):
    """Merge {id,code,input,output} rows across sources (cruxeval held out for eval)."""
    rows = []
    for name in sources:
        for i, row in enumerate(load_dataset(name)):
            missing = [k for k in ("id", "code", "input", "output") if k not in row]
            if missing:
                raise ValueError(f"{name} row {i} missing keys: {missing}")
            if not all(isinstance(row[k], str) for k in ("code", "input", "output")):
                raise TypeError(f"{name} row {i} must use string code/input/output")
            row = dict(row)
            row["id"] = str(row["id"])
            rows.append(row)
    return rows
