"""ds256k (long-trace synthetic, code_gen/code_gen.py) -> {id, code, input, output}.
Run `python -m data.Ds256k.convert` to save_to_disk ./data.

Source is local, not a Hub dataset: 500 programs generated to hit CODI trace lengths
in [8k, 256k) tokens, one `NNNN__id_ID.py` file per row under ./raw. Each file is a
`# record_id=<id>  entry=<name>  input=<repr>  output=<repr>  tokens=<n>` header line,
the generated code, and a trailing `if __name__ == "__main__":` self-check block that
we strip (not part of the traced program).
"""

import ast
import re
from pathlib import Path

from datasets import Dataset

_HEADER = re.compile(
    r"^# record_id=(?P<id>\d+)\s+entry=(?P<entry>\S+)\s+"
    r"input=(?P<input>'(?:[^'\\]|\\.)*')\s+output=(?P<output>'(?:[^'\\]|\\.)*')\s+tokens=\d+\s*$"
)
_MAIN = 'if __name__ == "__main__":'


def _parse(path: Path) -> dict:
    lines = path.read_text().splitlines()
    m = _HEADER.match(lines[1])
    if not m:
        raise ValueError(f"{path}: unrecognized header {lines[1]!r}")
    cut = next(i for i, l in enumerate(lines) if l.startswith(_MAIN))
    code = "\n".join(lines[3:cut]).rstrip("\n") + "\n"
    entry = m["entry"]
    if entry != "f":
        code += f"\nf = {entry}\n"
    return {
        "id": f"ds256k_{m['id']}",
        "code": code,
        "input": ast.literal_eval(m["input"]),
        "output": ast.literal_eval(m["output"]),
    }


def to_rows() -> list[dict]:
    raw = Path(__file__).parent / "raw"
    return [_parse(p) for p in sorted(raw.glob("*.py"))]


if __name__ == "__main__":
    rows = to_rows()
    out_dir = Path(__file__).parent / "data"
    Dataset.from_list(rows).save_to_disk(str(out_dir))
    print(f"Ds256k: {len(rows)} rows -> {out_dir}")
