# Copyright (c) Meta Platforms, Inc. and affiliates.

"""Shared CWM execution-trace representation: parse and render.

A trace is a sequence of *frames*, each an observation (locals) + action
(source line). Wire format (see PROMPTING_GUIDE.md, demos/cwmdbg.py):

    <|call_sep|>$LOCALS<|action_sep|>$SOURCE<|frame_sep|>
    <|line_sep|>$LOCALS<|action_sep|>$SOURCE<|frame_sep|>
    <|return_sep|><|action_sep|>$SOURCE<|arg_sep|>$VALUE<|frame_sep|>
    <|exception_sep|><|action_sep|>$SOURCE<|arg_sep|>$VALUE<|frame_sep|>

$LOCALS is a JSON object of name -> JSON-string value (e.g. "5", "\"abc\"",
"[1, 2]"); a value unchanged since the previous same-scope frame renders as
"..". $VALUE is the JSON-encoded return/raised value. GPU-free and import-light
for direct unit testing.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from enum import Enum

# Wire-format pieces (matches CWMInstructTokenizer.*_ID constants).
CALL_SEP = "<|call_sep|>"
LINE_SEP = "<|line_sep|>"
RETURN_SEP = "<|return_sep|>"
EXCEPTION_SEP = "<|exception_sep|>"
ACTION_SEP = "<|action_sep|>"
ARG_SEP = "<|arg_sep|>"
FRAME_SEP = "<|frame_sep|>"
END_OF_TEXT = "<|end_of_text|>"

DIFF_PLACEHOLDER = ".."
_START_MARKER = "  # << START_OF_TRACE"


class TraceEvent(Enum):
    CALL = "call"
    LINE = "line"
    RETURN = "return"
    EXCEPTION = "exception"


_EVENT_TOKENS: dict[str, TraceEvent] = {
    CALL_SEP: TraceEvent.CALL,
    LINE_SEP: TraceEvent.LINE,
    RETURN_SEP: TraceEvent.RETURN,
    EXCEPTION_SEP: TraceEvent.EXCEPTION,
}
_EVENT_TO_TOKEN: dict[TraceEvent, str] = {v: k for k, v in _EVENT_TOKENS.items()}


@dataclass
class TraceFrame:
    """A single execution-trace frame.

    ``locals`` is the parsed diff-locals, or None if malformed; ``full_locals``
    the non-diff snapshot. ``locals_str`` / ``full_locals_str`` are the JSON
    strings of each (the diff/full reconstruction targets), filled on the
    generation side. ``source`` has the START_OF_TRACE marker stripped.
    """

    event: TraceEvent
    source: str
    locals_str: str = ""
    locals: dict[str, str] | None = None
    full_locals: dict[str, str] | None = None
    full_locals_str: str = ""
    arg: str | None = None
    malformed: bool = False

    @property
    def has_locals(self) -> bool:
        return self.event in (TraceEvent.CALL, TraceEvent.LINE)


def normalize_source(source: str) -> str:
    """Strip the trace start marker and trailing newline from a source line."""
    return source.rstrip("\n").rstrip(_START_MARKER).rstrip()


def parse_locals(locals_str: str) -> dict[str, str] | None:
    """Parse a `$LOCALS` payload into a dict, or None if it is not a JSON object."""
    locals_str = locals_str.strip()
    if locals_str == "":
        return {}
    try:
        obj = json.loads(locals_str)
    except json.JSONDecodeError:
        return None
    if not isinstance(obj, dict):
        return None
    # Coerce defensively: values should already be JSON strings.
    return {str(k): v if isinstance(v, str) else json.dumps(v) for k, v in obj.items()}


def parse_generated_trace(generation: str) -> tuple[list[TraceFrame], bool]:
    """Parse a generation string into ``(frames, well_formed)``.

    ``well_formed`` (the "Valid Trace Format" metric) is True iff every frame had
    its event token, an ``<|action_sep|>`` (and an ``<|arg_sep|>`` for
    return/exception), with no leftover garbage before end-of-text. Malformed
    frames are still returned so other metrics can use whatever parsed cleanly.
    """
    # Everything after end-of-text is irrelevant.
    if END_OF_TEXT in generation:
        generation = generation.split(END_OF_TEXT, 1)[0]

    frames: list[TraceFrame] = []
    well_formed = True
    segments = generation.split(FRAME_SEP)
    # Text after the last frame_sep should be empty for a clean trace.
    trailing = segments.pop() if segments else ""
    if trailing.strip() != "":
        well_formed = False

    for seg in segments:
        if seg.strip() == "":
            # Stray empty segment (e.g. leading text before first token).
            continue
        frame, ok = _parse_segment(seg)
        if frame is None:
            well_formed = False
            continue
        well_formed = well_formed and ok
        frames.append(frame)

    if not frames:
        well_formed = False

    return frames, well_formed


def _parse_segment(seg: str) -> tuple[TraceFrame | None, bool]:
    # Identify the (first) event token.
    event: TraceEvent | None = None
    for tok, evt in _EVENT_TOKENS.items():
        idx = seg.find(tok)
        if idx != -1:
            event = evt
            seg = seg[idx + len(tok):]
            break
    if event is None:
        return None, False

    if event in (TraceEvent.CALL, TraceEvent.LINE):
        if ACTION_SEP not in seg:
            return TraceFrame(event=event, source="", malformed=True), False
        locals_str, source = seg.split(ACTION_SEP, 1)
        parsed = parse_locals(locals_str)
        return (
            TraceFrame(
                event=event,
                source=normalize_source(source),
                locals_str=locals_str.strip(),
                locals=parsed,
                malformed=parsed is None,
            ),
            True,
        )

    # RETURN / EXCEPTION
    if ACTION_SEP not in seg:
        return TraceFrame(event=event, source="", malformed=True), False
    seg = seg.split(ACTION_SEP, 1)[1]
    if ARG_SEP in seg:  # ok only when the arg separator is present
        source, arg = seg.split(ARG_SEP, 1)
        arg = _parse_arg(arg)
    else:
        source, arg = seg, None
    return (
        TraceFrame(event=event, source=normalize_source(source), arg=arg),
        ARG_SEP in seg,
    )


def render_frames_to_generation(frames: list[TraceFrame]) -> str:
    """Render frames back to the wire string; inverse of ``parse_generated_trace``.

    A ground-truth trace rendered this way must round-trip to a perfect score.
    """
    out: list[str] = []
    for f in frames:
        out.append(_EVENT_TO_TOKEN[f.event])
        if f.has_locals:
            out.append(json.dumps(f.locals if f.locals is not None else {}))
        out.append(ACTION_SEP)
        out.append(f.source)
        if f.event in (TraceEvent.RETURN, TraceEvent.EXCEPTION):
            out.append(ARG_SEP)
            out.append(json.dumps(f.arg))
        out.append(FRAME_SEP)
    out.append(END_OF_TEXT)
    return "".join(out)


def _parse_arg(arg_str: str) -> str | None:
    arg_str = arg_str.strip()
    if arg_str == "":
        return None
    try:
        # Frame stores json.dumps(value_string); unwrap one level (e.g. -> '"x9ja"', '17').
        loaded = json.loads(arg_str)
        return loaded if isinstance(loaded, str) else arg_str
    except json.JSONDecodeError:
        return arg_str
