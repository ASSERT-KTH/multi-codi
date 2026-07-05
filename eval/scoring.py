"""Answer extraction + execution scoring for CRUXEval-O trace evals (shared lib)."""

import json
import subprocess
import sys

ARG_SEP, FRAME_SEP, RETURN_SEP = "<|arg_sep|>", "<|frame_sep|>", "<|return_sep|>"


def extract_answer_trace_full(gen: str) -> str | None:
    """Value of main()'s last RETURN frame: ...<|arg_sep|>"value"<|frame_sep|>."""
    r = gen.rfind(RETURN_SEP)
    if r == -1:
        return None
    a = gen.find(ARG_SEP, r)
    if a == -1:
        return None
    rest = gen[a + len(ARG_SEP):]
    end = rest.find(FRAME_SEP)
    val = (rest[:end] if end != -1 else rest).strip()
    if not val:
        return None
    try:
        return json.loads(val)
    except json.JSONDecodeError:
        return val


def check_correct(code: str, expected: str, predicted: str, timeout: float = 3.0) -> bool:
    """Execute `code; assert expected == predicted` (CRUXEval semantics)."""
    test = f"{code}\nassert {expected} == {predicted}"
    try:
        return subprocess.run(
            [sys.executable, "-c", test], timeout=timeout, capture_output=True
        ).returncode == 0
    except Exception:
        return False
