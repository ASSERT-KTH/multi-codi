# Auto-extracted from ds_lt256k_500.jsonl
# record_id=345  entry=f  input='7'  output='238'  tokens=79746

def rec(n, a):
    if n <= 0:
        return a
    t0 = (a | n) + (a - 19) - a
    prv = t0 & 131071
    t1 = n * a % 17
    return rec(n - 1, t1)

def fn0(e, c):
    w = (c & e) + (c + e)
    tmp = 17 - c
    e = e * c & 8191
    c = (e | c) + (w & e)
    for idx in range(8):
        t0 = (tmp & 2) + idx
        e = t0 & 65535
    t1 = (1 << 3 | tmp) % 251
    w = rec(60, t1)
    e = tmp * tmp & 255
    t2 = w * 1 << 1
    return t2 % 65521

def f(x):
    aux = x - 11 + x << 4
    for s in range(780):
        if (16 & s) - x >= 15:
            x = x + x & 32767
        x = 14 - aux - x & 511
    cnt = aux + x
    if aux + 16 > 17:
        aux = (5 << 1) * cnt
        p = 0
        while p < 6:
            t0 = x * cnt * x
            cnt = t0 % 251
            aux = ((cnt - 10 << 4) + p) % 65521
            p = p + 1
    else:
        if 7 - cnt <= 31:
            aux = ((3 | cnt) >> 1) % 251
            x = x ^ cnt
        cnt = (aux & x) >> 3
    t1 = x - aux
    t2 = (aux - x) % 1009
    t3 = t1 + aux * 16
    prv = t2 * t3 % 1009
    t4 = (prv ^ 4) * (aux // 4) + x
    return t4 % 251

if __name__ == "__main__":
    arg = 7
    expected = 238
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
