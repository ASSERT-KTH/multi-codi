# Auto-extracted from ds_lt256k_500.jsonl
# record_id=434  entry=f  input='11'  output='64463'  tokens=74763

def fn0(e, m, c):
    idx = c | 12
    hi = 0
    while hi < 5:
        u = 0
        while u < 7:
            t0 = c * 8 // 3
            t1 = t0 | e ^ c ^ e
            e = t1 % 1009
            t2 = (m << 3) * c - e ^ u
            idx = t2 % 1009
            u = u + 1
        hi = hi + 1
    if e + idx >= 34:
        lo = 0
        while lo < 2:
            c = (lo | 18) - e & 8191
            t3 = lo - 12 + (c << 2)
            t4 = t3 * (c % 1009 * (c // 3))
            m = t4 % 4093
            t5 = 17 * 8 + c - idx
            idx = t5 & 32767
            lo = lo + 1
    else:
        for res in range(6):
            c = idx + c << 1 & 2047
            t6 = c & 9
            t7 = e >> 1
            t8 = t6 + (m ^ c)
            t9 = t7 ^ e << 1
            e = t8 + t9 & 131071
            m = (idx ^ 9 | m) % 1009
    p = (m << 2) * idx & 511
    tmp = (p | m) // 6
    if m // 6 > 36:
        for nxt in range(8):
            p = ((c >> 1) - e | nxt) & 2047
            t10 = 9 + tmp >> 4 | nxt
            idx = t10 & 262143
            t11 = tmp * 20 * (1 << 1)
            t12 = t11 | (m | idx) ^ tmp // 7
            m = t12 % 1009
    else:
        p = e + m ^ tmp
        for cur in range(10):
            t13 = 11 + tmp & 16
            e = t13 * (e + tmp >> 3) & 16383
    for w in range(4):
        t14 = p + idx
        e = t14 & 10 * w
    return p - idx & 4095

def f(x):
    for hi in range(561):
        x = (hi - x - hi * 1) % 65521
        x = (x >> 1) % 251
    v = 0
    while v < 5:
        for val in range(2):
            t0 = (13 & 6) * (18 + v)
            x = (t0 & val ^ x) & 16383
        v = v + 1
    idx = 0
    while idx < 3:
        a = 0
        while a < 8:
            x = (8 | a | x) % 17
            t1 = idx * x - 2
            x = t1 & 262143
            t2 = 8 & a ^ idx * x
            x = (t2 - 4) % 251
            a = a + 1
        for prv in range(9):
            t3 = (15 | x) + prv
            x = t3 & 32767
        x = idx - x & 20
        idx = idx + 1
    tot = (17 + x) % 1009
    c = tot * tot & 8191
    cnt = x * x & 262143
    return x - c & 65535

if __name__ == "__main__":
    arg = 11
    expected = 64463
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
