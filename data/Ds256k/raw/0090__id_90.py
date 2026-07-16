# Auto-extracted from ds_lt256k_500.jsonl
# record_id=90  entry=f  input='16'  output='1004'  tokens=179497

def rec(n, a):
    if n <= 0:
        return a
    t0 = n * 6
    t1 = (n ^ 19) & n
    t2 = t0 ^ a + n
    tot = t1 * t2 & 511
    t3 = (n // 2 ^ a) % 65521
    return rec(n - 1, t3)

def fn0(g, e):
    hi = e // 8 + e
    b = (hi >> 1) + g ^ hi
    t0 = (14 ^ hi) - b
    t1 = e >> 1 << 4
    p = t0 * t1 & 65535
    for buf in range(4):
        t2 = e % 65521 << 2
        e = t2 // 8 & 4095
        prv = 0
        while prv < 8:
            t3 = b % 17 - (e >> 4)
            e = t3 % 65521
            prv = prv + 1
    g = (9 - p) // 5
    return g * g + p & 4095

def f(x):
    t0 = (x | 13) & 131071
    x = rec(118, t0)
    for q in range(12):
        t1 = 9 * x
        t2 = t1 ^ 3 * q
        x = t2 % 1009
        x = x * q % 97
    for nxt in range(8):
        t3 = nxt - 20 & 19
        x = t3 + x & 262143
        if nxt - x < 0:
            x = (nxt + x) % 97
            x = (nxt - x) % 97
        else:
            x = (x * nxt ^ x) % 1009
            x = (x - 2) * (x << 4) % 1009
        if nxt + x >= 19:
            x = (x & 3 ^ x) % 97
    tmp = 0
    while tmp < 10:
        x = (9 & 2) - x & 32767
        x = (tmp + tmp | x) % 1009
        if tmp - 17 + x <= 43:
            x = x % 97
            x = (13 * x | tmp + x) & 16383
        tmp = tmp + 1
    if x | 10 > 17:
        t4 = 5 - x
        t5 = t4 + (x + 9)
        t6 = x * x // 2 & 511
        x = fn0(t5 % 1009, t6)
        t7 = x // 5 ^ x
        t8 = (x ^ 5) & 1023
        x = fn0(t7 % 97, t8)
    else:
        x = (x - 19) // 7
    lo = (x ^ 7) % 1009
    for cur in range(449):
        lo = 4 - 16 - cur + x & 1023
    g = x - 5
    t9 = lo * 1
    t10 = t9 + 3 * g
    prv = t10 ^ 11 - lo
    if x * lo < 1:
        t11 = lo + x + x
        t12 = x // 4 ^ 20
        prv = t11 * t12 % 97
    else:
        if g + g >= 19:
            lo = x + lo
        else:
            t13 = ((x >> 3) + g >> 4) % 97
            t14 = (x * g - (lo & x)) % 1009
            x = fn0(t13, t14)
    t15 = g >> 1
    t16 = t15 | lo & 20
    res = t16 * 4
    t17 = lo - 15 | 18 - lo
    return t17 % 1009

if __name__ == "__main__":
    arg = 16
    expected = 1004
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
