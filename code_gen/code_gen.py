"""Translate computation graphs into `f(x)` programs whose CODI trace spans 8k..1M tokens.

Reads graph JSON (see graph.py) from stdin/file, fills each program's holes to hit a
token target, writes {id, code, input, output, tokens, base, holes, graph}.

Length = len(prompt_ids) + len(trace_ids) (data/precompute_loader.py). Trace tokens are
affine in each hole's `k`; each hole gets its own two-point fit.

    python graph.py -n 60 -s 0 | python code_gen.py -o codi_dataset_v5.jsonl
"""
from __future__ import annotations
import argparse, json, math, os, random, signal, sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from data.dataset import build_trace_record
from data.tokens import add_trace_tokens

TOK_LO, TOK_HI, MIN_K, PROBE = 8_000, 1_000_000, 8, 32
SAFETY_CAP = 5000   # frame cap for hot/final measure(): k=need/slope can blow up if slope~0
TIMEOUT_S = 20   # wall-clock backstop: a single line can be slow on a huge value regardless of frame count
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
        return str(k[n["n"]])
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
    """Commit the trip counts into the graph, so the emitted graph renders back to `code`."""
    if isinstance(n, list):
        return [fill(x, k) for x in n]
    if not isinstance(n, dict):
        return n
    if n.get("t") == "hole":
        return {"t": "const", "v": k[n["n"]]}
    return {a: fill(b, k) for a, b in n.items()}


def run(code, arg):
    ns = {"__builtins__": SAFE}
    exec(compile(code, "<gen>", "exec"), ns)
    return ns["f"](arg)


def measure(code, arg, tokenizer, max_frames=-1):
    e = build_trace_record(code, str(arg), tokenizer, max_frames=max_frames)
    return -1 if e is None else len(e["prompt_ids"]) + len(e["trace_ids"])


def _raise_timeout(signum, frame):
    raise TimeoutError


signal.signal(signal.SIGALRM, _raise_timeout)


def _try_prog(prog, rng, tokenizer, tok_lo, tok_hi, base_lo, base_hi, min_iters, slope_hi):
    """One candidate: the accepted record (sans id), or None. No side effects besides
    consuming `rng` -- callers rely on that determinism to replay a candidate stream."""
    arg, holes = prog["input"], prog["holes"]
    zero = to_python(prog, {h: 0 for h in holes})
    if max(len(l) for l in zero.splitlines()) > MAX_LINE:
        return None
    # base_hi doubles as a frame cap: aborts oversized traces early instead of fully executing
    # them just to reject them.
    base = measure(zero, arg, tokenizer, max_frames=base_hi if base_hi < math.inf else -1)
    if base < 0 or not (base_lo <= base <= base_hi):
        return None
    if base > tok_hi:   # more iterations only grow the trace, so base alone already dooms it
        return None
    slope = {}
    for h in holes:
        hot = measure(to_python(prog, {hh: PROBE if hh == h else 0 for hh in holes}), arg, tokenizer,
                      max_frames=SAFETY_CAP)
        if hot <= base:
            break
        slope[h] = (hot - base) / PROBE
        if slope[h] > slope_hi:
            break
    if len(slope) < len(holes):
        return None
    lo = base + min_iters * sum(slope.values())   # cheapest trace this program can produce
    if lo > tok_hi:
        return None
    target = math.exp(rng.uniform(math.log(max(tok_lo, lo)), math.log(tok_hi)))
    need = (target - base) / len(holes)
    k = {h: max(min_iters, round(need / slope[h])) for h in holes}
    code = to_python(prog, k)
    tokens = measure(code, arg, tokenizer, max_frames=SAFETY_CAP)
    if tokens < 0 or tokens >= tok_hi:
        return None
    return dict(code=code, input=str(arg), output=repr(run(code, arg)),
                tokens=tokens, base=base, holes=k, graph=fill(prog, k))


def generate(progs, seed, tokenizer, out_file, tok_lo=TOK_LO, tok_hi=TOK_HI,
             base_lo=0, base_hi=math.inf, min_iters=MIN_K, slope_hi=math.inf, samples=None,
             start_id=0, skip=0):
    """Fills holes to hit a log-uniform target in [tok_lo, tok_hi], split evenly across
    holes. base_lo/base_hi filter zero-iteration size; min_iters/slope_hi bound each
    hole's floor and per-iteration cost (both stack with hole count). Stops after
    `samples` records; writes+flushes as it goes. The candidate stream is deterministic
    in `seed`, so resuming a shard replays it from the start: `skip` lets a restart
    replay-but-not-rewrite the `skip` candidates already on disk instead of duplicating
    them, while `start_id` picks up numbering where the file left off."""
    rng, n = random.Random(seed), start_id
    for prog in progs:
        if samples is not None and n - start_id >= samples:
            break
        signal.alarm(TIMEOUT_S)   # backstop: a huge value can make one line slow regardless of frame count
        try:
            rec = _try_prog(prog, rng, tokenizer, tok_lo, tok_hi, base_lo, base_hi, min_iters, slope_hi)
        except TimeoutError:
            rec = None
        finally:
            signal.alarm(0)
        if rec is None:
            continue
        if skip > 0:
            skip -= 1
            continue
        rec["id"] = n
        out_file.write(json.dumps(rec) + "\n")
        out_file.flush()
        n += 1
        print(f"[{n:>4}] tokens={rec['tokens']:>9,} base={rec['base']:>9,} holes={rec['holes']}", flush=True)
    return n - start_id


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("graphs", nargs="?", type=argparse.FileType(), default=sys.stdin)
    ap.add_argument("-s", type=int, default=0)
    ap.add_argument("-o", default="codi_dataset_v5.jsonl")
    ap.add_argument("--tok-lo", type=int, default=TOK_LO,
                    help="floor the trace-length target")
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
                     tok_lo=a.tok_lo, tok_hi=a.tok_hi, samples=a.samples)
    print(f"\nWrote {n} -> {a.o}")


if __name__ == "__main__":
    main()
