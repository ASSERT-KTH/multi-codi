"""Translate computation graphs into `f(x)` programs whose CODI trace spans 8k..1M tokens.

Reads graph JSON (see graph.py) from a file or stdin, fills the `k` hole so the trace
hits a log-uniform token target, and writes {id, code, input, output, tokens, graph}.

Length is the CODI training statistic: len(prompt_ids) + len(trace_ids), per data/precompute_loader.py.
Trace tokens are affine in `k` for every construct graph.py emits, but the slope spans
two decades across programs, so each program gets its own two-point fit.

    python graph.py -n 60 -s 0 | python code_gen.py -o codi_dataset_v5.jsonl
"""
from __future__ import annotations
import argparse, json, math, os, random, sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from data.dataset import build_trace_record
from data.tokens import add_trace_tokens

TOK_LO, TOK_HI, MIN_K, PROBE = 8_000, 1_000_000, 8, 32
MAX_LINE = 100
PREC = {"|": 1, "^": 2, "&": 3, "<<": 4, ">>": 4, "+": 5, "-": 5, "*": 6, "//": 6, "%": 6}
ATOM, CMP = 9, 0
SAFE = {"range": range}


def _prec(n):
    if n["t"] == "bin":
        return PREC[n["op"]]
    return CMP if n["t"] == "cmp" else ATOM


def _wrap(n, p, right, k):
    code, cp = _emit(n, k), _prec(n)
    return f"({code})" if (cp <= p if right else cp < p) else code


def _emit(n, k):
    t = n["t"]
    if t == "const":
        return str(n["v"])
    if t == "hole":
        return str(k)
    if t == "ref":
        return n["n"]
    if t == "list":
        return "[" + ", ".join(str(v) for v in n["v"]) + "]"
    if t == "idx":
        return f"{n['b']}[{_emit(n['i'], k)}]"
    if t == "call":
        return f"{n['f']}({', '.join(_emit(a, k) for a in n['a'])})"
    p = CMP if t == "cmp" else PREC[n["op"]]
    return f"{_wrap(n['l'], p, False, k)} {n['op']} {_wrap(n['r'], p, True, k)}"


def _lines(body, k, depth):
    out, pad = [], "    " * depth
    for s in body:
        t = s["t"]
        if t == "assign":
            out.append(f"{pad}{s['tgt']} = {_emit(s['e'], k)}")
        elif t == "setidx":
            out.append(f"{pad}{s['b']}[{_emit(s['i'], k)}] = {_emit(s['e'], k)}")
        elif t == "ret":
            out.append(f"{pad}return {_emit(s['e'], k)}")
        elif t == "for":
            out.append(f"{pad}for {s['i']} in range({_emit(s['trip'], k)}):")
            out += _lines(s["body"], k, depth + 1)
        elif t == "while":
            out.append(f"{pad}while {_emit(s['cond'], k)}:")
            out += _lines(s["body"], k, depth + 1)
        else:
            out.append(f"{pad}if {_emit(s['cond'], k)}:")
            out += _lines(s["then"], k, depth + 1)
            if s["els"]:
                out.append(f"{pad}else:")
                out += _lines(s["els"], k, depth + 1)
    return out


def to_python(prog, k=None):
    src = []
    for fn in prog["funcs"]:
        src.append(f"def {fn['name']}({', '.join(fn['params'])}):")
        src += _lines(fn["body"], k, 1)
        src += [f"    return {_emit(fn['ret'], k)}", ""]
    return "\n".join(src)


def fill(n, k):
    """Commit the trip count into the graph, so the emitted graph renders back to `code`."""
    if isinstance(n, list):
        return [fill(x, k) for x in n]
    if not isinstance(n, dict):
        return n
    if n.get("t") == "hole":
        return {"t": "const", "v": k}
    return {a: fill(b, k) for a, b in n.items()}


def run(code, arg):
    ns = {"__builtins__": SAFE}
    exec(compile(code, "<gen>", "exec"), ns)
    return ns["f"](arg)


def measure(code, arg, tokenizer):
    e = build_trace_record(code, str(arg), tokenizer, max_frames=-1)
    return -1 if e is None else len(e["prompt_ids"]) + len(e["trace_ids"])


def generate(progs, seed, tokenizer, out_file, tok_hi=TOK_HI, samples=None):
    """Targets are log-uniform over [8k, tok_hi], raised to whatever a program reaches in
    MIN_K iterations. The endpoints are not enforced; the middle is what matters.
    Stops once `samples` records are collected (None = exhaust `progs`). Each record is
    written+flushed to `out_file` as produced, so a kill keeps the samples already done."""
    rng, n = random.Random(seed), 0
    for prog in progs:
        if samples is not None and n >= samples:
            break
        arg = prog["input"]
        zero, probe = to_python(prog, 0), to_python(prog, PROBE)
        if max(len(l) for l in zero.splitlines()) > MAX_LINE:
            continue
        base, hot = measure(zero, arg, tokenizer), measure(probe, arg, tokenizer)
        if base < 0 or hot <= base:
            continue
        c = (hot - base) / PROBE
        lo = base + MIN_K * c            # the cheapest trace this program can produce
        if lo > tok_hi:
            continue
        target = math.exp(rng.uniform(math.log(max(TOK_LO, lo)), math.log(tok_hi)))
        k = max(MIN_K, round((target - base) / c))
        code = to_python(prog, k)
        tokens = measure(code, arg, tokenizer)
        if tokens < 0 or tokens >= tok_hi:
            continue
        rec = dict(id=n, code=code, input=str(arg), output=repr(run(code, arg)),
                   tokens=tokens, graph=fill(prog, k))
        out_file.write(json.dumps(rec) + "\n")
        out_file.flush()
        n += 1
        print(f"[{n:>4}] target={target:>9,.0f} tokens={tokens:>9,} "
              f"k={k:>7,} tok/iter={c:.1f}", flush=True)
    return n


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("graphs", nargs="?", type=argparse.FileType(), default=sys.stdin)
    ap.add_argument("-s", type=int, default=0)
    ap.add_argument("-o", default="codi_dataset_v5.jsonl")
    ap.add_argument("--tok-hi", type=int, default=TOK_HI,
                    help="cap the trace-length target; every sample has tokens < this")
    ap.add_argument("--samples", type=int, default=None,
                    help="stop after collecting this many samples")
    ap.add_argument("--tokenizer", default=os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "..",
        "model_weights/sft1.5b_lr2e5_bs32/checkpoint-6936"))
    a = ap.parse_args()
    from transformers import AutoTokenizer
    tok = AutoTokenizer.from_pretrained(a.tokenizer)
    add_trace_tokens(tok)
    with open(a.o, "w") as f:
        n = generate((json.loads(l) for l in a.graphs), a.s, tok, f,
                     tok_hi=a.tok_hi, samples=a.samples)
    print(f"\nWrote {n} -> {a.o}")


if __name__ == "__main__":
    main()
