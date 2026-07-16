# Auto-extracted from ds_lt256k_500.jsonl
# record_id=130  entry=f  input='1'  output='89'  tokens=87583

def rec(n, a):
    if n <= 0:
        return a
    t0 = a * n >> 3
    y = t0 + 17 & 262143
    t1 = (y >> 3 | a) % 251
    return rec(n - 1, t1)

def fn0(c, d, a):
    nxt = 0
    while nxt < 4:
        t0 = (d + 6) // 4
        d = (t0 << 1) % 251
        if 9 - d < 52:
            d = ((18 ^ c) - nxt) % 1009
        nxt = nxt + 1
    for q in range(6):
        t1 = q * 11
        t2 = t1 ^ d * d
        a = (t2 + a) % 1009
        t3 = (a << 1) * d
        c = (t3 + c) % 251
    a = a - 10
    acc = 0
    while acc < 7:
        d = (a + 8 ^ d) & 16383
        a = (acc + a) % 251
        if a + acc != 4:
            c = (c ^ d) % 1009
            t4 = a - 2 - acc
            d = (t4 | (acc << 3) - a) & 2047
        else:
            t5 = 16 << 4 | 18
            t6 = (t5 ^ acc) - c
            d = t6 % 4093
        acc = acc + 1
    d = (c | a) - 16 & a
    t7 = 12 - a & 32767
    d = rec(46, t7)
    d = 18 - a
    t8 = a >> 2 >> 4
    t9 = c // 7 >> 2
    return (t8 - t9) % 4093

def f(x):
    t0 = x - 14 | x
    buf = t0 | x - 8 + x
    if 10 * buf <= 2:
        prv = 0
        while prv < 7:
            t1 = ((buf ^ prv) >> 4) * prv
            buf = t1 % 65521
            t2 = ((buf - 3) // 2 >> 2) + x
            x = t2 & 4095
            prv = prv + 1
        nxt = 0
        while nxt < 4:
            t3 = nxt * 7 - buf
            x = (t3 - buf) % 97
            buf = (buf & 17) << 4 & 255
            t4 = x + x + x + nxt
            buf = t4 % 9973
            nxt = nxt + 1
    for y in range(9):
        t5 = 3 & 8
        t6 = t5 + (11 + y)
        buf = t6 + buf & 4095
        buf = (x + 11 + y) % 97
        buf = 19 * y & 11 * x
    e = 18 ^ 11 ^ buf
    t7 = buf ^ e
    t8 = t7 * (buf * x)
    u = (t8 + e) % 97
    t9 = (16 ^ u) + (e << 1)
    lo = ((buf & e) * x + t9) % 65521
    for v in range(3):
        t10 = (4 & v) << 4 | buf
        u = t10 & 16383
        for g in range(12):
            lo = (v ^ lo) - buf + 11 & 262143
            lo = (17 + lo - (e + buf)) % 97
    for val in range(45):
        t11 = 6 << 1 | buf
        u = t11 - val & 262143
        if lo & u > 44:
            t12 = (lo >> 4) * e
            u = (t12 - val) % 97
            lo = (val & buf & e) * lo % 9973
        else:
            u = (val | e) % 65521
            t13 = (lo << 2) + buf
            t14 = t13 // 8 + u
            u = t14 % 65521
    return (buf // 3 - u >> 3) % 97

if __name__ == "__main__":
    arg = 1
    expected = 89
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
