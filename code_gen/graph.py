"""Sample random computation graphs; one program per line of JSON on stdout.

    expr := {t:const,v} | {t:list,v} | {t:ref,n} | {t:idx,b,i} | {t:hole,n}
          | {t:bin,op,l,r} | {t:cmp,op,l,r} | {t:call,f,a}
    stmt := {t:assign,tgt,e} | {t:setidx,b,i,e} | {t:ret,e}
          | {t:for,i,trip,body} | {t:while,cond,body} | {t:if,cond,then,els}
    prog := {funcs:[{name,params,body,ret}], entry, input}

`hole` is the trip count of one randomly chosen loop of `f`: the single length lever.
Values stay bounded because `_bound` is an interval estimate and `_fit` inserts a
reducer (`% m` or `& mask`) exactly where it exceeds LIMIT -- on loop-carried updates
always, on straight-line code only when it overflows. `while` is only ever emitted as
`i = 0 / while i < N / ... / i = i + 1`, so it terminates by construction.

Stdlib only, no knowledge of Python syntax -- see code_gen.py for the translator.
"""
from __future__ import annotations
import argparse, json, math, random

LIMIT, DEPTH, NEST, MAXW = 10**6, 3, 2, 20
SPLIT = (2, 4)                  # per-statement split threshold is sampled from here, for variety
TRIP, RECD = 12, 120           # a call inside a `for TRIP` inside a `for TRIP` must stay cheap
MODS = (17, 97, 251, 1009, 4093, 9973, 65521)
CALLB = max(MODS)
SMALL = 64                     # `a // c` and `a >> c` collapse to 0 below this
OPS = ("+", "-", "*", "^", "|", "&", "<<", "%", "//", ">>")
WT = (4, 4, 4, 3, 2, 2, 1, 1, 2, 2)    # no single op dominates, so split residuals vary
JOIN = ("+", "-", "^", "|")            # ops `_use` may add; all keep values bounded
CMPS = ("<", "<=", ">", ">=", "==", "!=")
IDEM = {"-", "^", "&", "|"}    # `a op a` is degenerate; never emit it
NAMES = "a b c d e g j m p q s t u v w y z acc cur tmp buf idx tot val cnt res aux lo hi nxt prv".split()

C = lambda v: {"t": "const", "v": v}
R = lambda n: {"t": "ref", "n": n}
B = lambda op, l, r: {"t": "bin", "op": op, "l": l, "r": r}
A = lambda tgt, e: {"t": "assign", "tgt": tgt, "e": e}


def _bound(e, bnd):
    t = e["t"]
    if t == "const":
        return abs(e["v"])
    if t == "list":
        return max(abs(v) for v in e["v"])
    if t == "ref":
        return bnd[e["n"]]
    if t == "idx":
        return bnd[e["b"]]
    if t == "call":
        return CALLB
    if t == "cmp":
        return 1
    if t == "hole":
        return LIMIT
    l, r, op = _bound(e["l"], bnd), _bound(e["r"], bnd), e["op"]
    if op in ("+", "-"):
        return l + r
    if op == "*":
        return l * r
    if op == "%":
        return r - 1
    if op == "//":
        return l
    if op == ">>":
        return l >> e["r"]["v"]
    if op == "<<":
        return l << e["r"]["v"]
    if op == "&":
        return min(l, r)
    return 1 << max(l, r).bit_length()


def _reduce(rng, s, e):
    if e["t"] == "bin" and e["op"] in ("%", "&"):     # already bounded; don't stack `% m % m`
        return e
    if rng.random() < .55:
        return B("%", e, C(rng.choice(s["mods"])))
    return B("&", e, C((1 << rng.randint(8, 18)) - 1))


def _fit(rng, s, e, force):
    return _reduce(rng, s, e) if force or _bound(e, s["bnd"]) > LIMIT else e


def _size(e):
    if e["t"] in ("bin", "cmp"):
        return 1 + _size(e["l"]) + _size(e["r"])
    if e["t"] == "idx":
        return 1 + _size(e["i"])
    return 0


def _hoist(rng, s, e, pre):
    t = f"t{s['nt']}"
    s["nt"] += 1
    s["bnd"][t] = _bound(e, s["bnd"])
    pre.append(A(t, e))
    return R(t)


def _split(rng, s, e, pre, thr):
    """Return `e` rewritten so every rendered line (this one and each temp) has <= thr ops:
    linearize the children, then pull the larger operand aside until the node itself fits."""
    if e["t"] in ("bin", "cmp"):
        e = dict(e, l=_split(rng, s, e["l"], pre, thr), r=_split(rng, s, e["r"], pre, thr))
    elif e["t"] == "idx":
        e = dict(e, i=_split(rng, s, e["i"], pre, thr))
    while e["t"] in ("bin", "cmp") and _size(e) > thr:
        side = "l" if _size(e["l"]) >= _size(e["r"]) else "r"
        e = dict(e, **{side: _hoist(rng, s, e[side], pre)})
    return e


def _refs(e):
    t = e["t"]
    if t == "ref":
        return {e["n"]}
    if t == "idx":
        return {e["b"]} | _refs(e["i"])
    if t == "call":
        return set().union(set(), *(_refs(a) for a in e["a"]))
    if t in ("bin", "cmp"):
        return _refs(e["l"]) | _refs(e["r"])
    return set()


def _atom(rng, s):
    p = rng.random()
    if s["lists"] and p < .12:
        b, ln, _ = rng.choice(s["lists"])
        return {"t": "idx", "b": b, "i": B("%", R(rng.choice(s["vars"] + s["idxs"])), C(ln))}
    return R(rng.choice(s["vars"] + s["idxs"])) if p < .78 else C(rng.randint(1, 20))


def _expr(rng, s, d):
    if d <= 0:
        return _atom(rng, s)
    l = _expr(rng, s, d - 1)
    ops = OPS if _bound(l, s["bnd"]) >= SMALL else OPS[:-2]
    op = rng.choices(ops, WT[:len(ops)])[0]
    if op == "%":
        m = rng.choice(s["mods"])
        return l if _bound(l, s["bnd"]) < m else B("%", l, C(m))   # a no-op mod is redundant
    elif op == "//":
        r = C(rng.randint(2, 8))
    elif op in ("<<", ">>"):
        r = C(rng.randint(1, 4))
    else:
        r = _expr(rng, s, d - 1) if rng.random() < .4 else _atom(rng, s)
        if op in IDEM and r == l:
            r = C(rng.randint(1, 20))
    return B(op, l, r)


def _use(rng, e, pool):
    """Force `e` to read `pool`, so no statement is a folded constant or loop-invariant."""
    return e if _refs(e) & set(pool) else B(rng.choice(JOIN), e, R(rng.choice(pool)))


def _rhs(rng, s, force, pool=None):
    e = _use(rng, _expr(rng, s, rng.randint(1, DEPTH)), pool or s["vars"])
    return _fit(rng, s, e, force)


def _cond(rng, s):
    l = _use(rng, _expr(rng, s, 1), s["vars"])
    hi = max(2, min(64, _bound(l, s["bnd"])))
    return {"t": "cmp", "op": rng.choice(CMPS), "l": l, "r": C(rng.randint(0, hi))}


def _assign(rng, s, depth, loop):
    fresh = depth == 0 and len(s["vars"]) < s["w"]
    tgt = s["names"].pop() if fresh else rng.choice(s["vars"])
    e = _use(rng, _expr(rng, s, rng.randint(1, DEPTH)), s["vars"])
    if loop:
        e = _use(rng, e, ([] if fresh else [tgt]) + s["idxs"][-1:] or s["vars"])
    e = _fit(rng, s, e, loop)
    pre = []
    e = _split(rng, s, e, pre, rng.randint(*SPLIT))
    if fresh:
        s["vars"].append(tgt)
    s["bnd"][tgt] = max(s["bnd"].get(tgt, 0), _bound(e, s["bnd"]))
    return pre + [A(tgt, e)]


def _setidx(rng, s):
    b, ln, m = rng.choice(s["lists"])
    v = _rhs(rng, s, False)
    v = v if _bound(v, s["bnd"]) < m else B("%", v, C(m))     # only mod when it can exceed m
    pre = []
    i = B("%", R(rng.choice(s["vars"] + s["idxs"])), C(ln))
    v = _split(rng, s, v, pre, rng.randint(*SPLIT))
    return pre + [{"t": "setidx", "b": b, "i": i, "e": v}]


def _arg(rng, s, e, pre, np):
    """Split an arg to a few ops, and give a multi-arg call its own line per dense arg."""
    e = _split(rng, s, e, pre, rng.randint(*SPLIT))
    return _hoist(rng, s, e, pre) if np > 1 and _size(e) > 1 else e


def _call(rng, s):
    name, np, rec = rng.choice(s["callees"])
    raw = [_reduce(rng, s, _rhs(rng, s, False)) for _ in range(np)]
    if rec:
        raw[0] = C(rng.randint(20, RECD))       # recursion depth, never the length lever
    pre = []
    a = [_arg(rng, s, e, pre, np) for e in raw]
    tgt = rng.choice(s["vars"])
    s["bnd"][tgt] = max(s["bnd"][tgt], CALLB)
    return pre + [A(tgt, {"t": "call", "f": name, "a": a})]


def _counter(s, trip):
    """Live only inside its own body: an `if` branch may skip it, `range(0)` never binds it."""
    i = s["names"].pop()
    s["idxs"].append(i)
    s["bnd"][i] = trip
    return i


def _for(rng, s, depth):
    trip = rng.randint(2, TRIP)
    i = _counter(s, trip)
    node = {"t": "for", "i": i, "trip": C(trip),
            "body": _block(rng, s, rng.randint(1, 3), depth + 1, True)}
    s["idxs"].remove(i)
    if not s["inif"]:
        s["cand"].append((node, "trip"))
    return [node]


def _while(rng, s, depth):
    trip = rng.randint(2, TRIP)
    i = _counter(s, trip)
    cond = {"t": "cmp", "op": "<", "l": R(i), "r": C(trip)}
    body = _block(rng, s, rng.randint(1, 3), depth + 1, True) + [A(i, B("+", R(i), C(1)))]
    s["idxs"].remove(i)
    if not s["inif"]:
        s["cand"].append((cond, "r"))
    return [A(i, C(0)), {"t": "while", "cond": cond, "body": body}]


def _if(rng, s, depth, loop):
    cond, was = _cond(rng, s), s["inif"]
    s["inif"] = True
    then = _block(rng, s, rng.randint(1, 2), depth + 1, loop)
    els = _block(rng, s, rng.randint(1, 2), depth + 1, loop) if rng.random() < .5 else []
    s["inif"] = was
    return [{"t": "if", "cond": cond, "then": then, "els": els}]


def _block(rng, s, n, depth, loop):
    out = []
    for _ in range(n):
        p = rng.random()
        if depth < NEST and p < .16:
            out += _for(rng, s, depth)
        elif depth < NEST and p < .26:
            out += _while(rng, s, depth)
        elif depth < NEST and p < .38:
            out += _if(rng, s, depth, loop)
        elif s["lists"] and p < .46:
            out += _setidx(rng, s)
        elif s["callees"] and not loop and p < .54:
            out += _call(rng, s)
        else:
            out += _assign(rng, s, depth, loop)
    return out


def _state(rng, params, w, callees, pbnd):
    return {"vars": list(params), "idxs": [], "lists": [], "cand": [], "inif": False, "w": w,
            "nt": 0, "names": [n for n in rng.sample(NAMES, len(NAMES)) if n not in params],
            "callees": callees, "mods": rng.sample(MODS, rng.randint(2, 4)),
            "bnd": {p: pbnd for p in params}}


def _func(rng, name, params, w, callees, pbnd=CALLB):
    s = _state(rng, params, w, callees, pbnd)
    body = []
    if rng.random() < .35:
        b, ln, m = s["names"].pop(), rng.randint(4, 8), rng.choice((97, 251, 1009))
        body.append(A(b, {"t": "list", "v": [rng.randrange(m) for _ in range(ln)]}))
        s["lists"].append((b, ln, m))
        s["bnd"][b] = m - 1
    body += _block(rng, s, max(w, rng.randint(3, 8)), 0, False)
    locs = [v for v in s["vars"] if v not in params]     # returning a param wastes the body
    ret = _split(rng, s, _rhs(rng, s, True, locs), body, rng.randint(*SPLIT))
    return {"name": name, "params": params, "body": body, "ret": ret}, s


def _recfunc(rng, w):
    s = _state(rng, ["a"], w, [], CALLB)
    s["idxs"].append("n")           # readable, never assigned -- so `rec(n - 1, ..)` terminates
    s["bnd"]["n"] = RECD
    body = [{"t": "if", "cond": {"t": "cmp", "op": "<=", "l": R("n"), "r": C(0)},
             "then": [{"t": "ret", "e": R("a")}], "els": []}]
    body += _block(rng, s, rng.randint(1, 3), 0, True)
    arg = _arg(rng, s, _rhs(rng, s, True, ["a"]), body, 2)
    ret = {"t": "call", "f": "rec", "a": [B("-", R("n"), C(1)), arg]}
    return {"name": "rec", "params": ["n", "a"], "body": body, "ret": ret}


def sample(rng):
    funcs, callees = [], []
    if rng.random() < .45:
        funcs.append(_recfunc(rng, rng.randint(1, 3)))
        callees.append(("rec", 2, True))
    for i in range(rng.randint(0, 2)):
        np = rng.randint(1, 3)
        fn, _ = _func(rng, f"fn{i}", rng.sample(NAMES[:8], np), rng.randint(2, 6), list(callees))
        funcs.append(fn)
        callees.append((f"fn{i}", np, False))
    w = round(math.exp(rng.uniform(math.log(2), math.log(MAXW))))
    main, s = _func(rng, "f", ["x"], w, callees, pbnd=20)
    if not s["cand"]:
        main["body"] += _for(rng, s, 0)
    node, key = rng.choice(s["cand"])
    node[key] = {"t": "hole", "n": "k"}
    return {"funcs": funcs + [main], "entry": "f", "input": rng.randint(1, 20)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-n", type=int, default=60)
    ap.add_argument("-s", type=int, default=0)
    a = ap.parse_args()
    rng = random.Random(a.s)
    for _ in range(a.n):
        print(json.dumps(sample(rng)))


if __name__ == "__main__":
    main()
