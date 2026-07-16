# Auto-extracted from ds_lt256k_500.jsonl
# record_id=7  entry=f  input='9'  output='19958'  tokens=30342

def fn0(b, c, d):
    t0 = c + c + d
    nxt = t0 * c % 65521
    t1 = d // 2 * (b & c)
    w = 20 - b - 20 - t1 & 32767
    d = b * 17 % 65521
    for hi in range(4):
        t2 = (w + c) * (w << 4) // 5
        d = (t2 ^ hi) % 9973
        b = (hi | nxt) % 65521
    for aux in range(7):
        t3 = (20 << 3) * (13 + 14)
        t4 = (aux << 3 & 18) * t3
        w = (t4 | b) % 251
        nxt = (14 ^ 12) - (nxt - aux) & 262143
    t5 = b - 7 + nxt
    return t5 & 4095

def fn1(m):
    v = [160, 12, 82, 126, 93, 164, 161]
    hi = 18 - m
    m = (hi ^ m) * 16 & 131071
    prv = 0
    while prv < 2:
        t0 = v[hi % 7]
        t1 = m & t0
        t2 = t1 - (m ^ prv)
        t3 = prv * m >> 2
        m = (t2 | t3) & 2047
        hi = (prv | 7 | hi) & 32767
        prv = prv + 1
    if v[hi % 7] - 10 >= 48:
        idx = 0
        while idx < 10:
            t4 = hi * m | hi
            m = (t4 ^ idx) % 65521
            t5 = v[m % 7]
            t6 = (8 ^ idx) - t5 << 4
            v[m % 7] = t6 % 251
            idx = idx + 1
        m = 11 * hi
    t7 = hi + v[hi % 7]
    t8 = t7 + (v[m % 7] << 4)
    hi = t8 >> 3
    t9 = v[m % 7]
    t10 = v[hi % 7]
    t11 = t9 * hi
    t12 = t11 * (t10 & m)
    t13 = t12 >> 4 & 255
    t14 = (m | 10) // 2 & 8191
    t15 = (19 | m) % 17
    m = fn0(t13, t14, t15)
    return (19 & hi) * m & 255

def f(x):
    t0 = (10 & x | x) % 97
    t1 = x * x % 97
    t2 = (x << 3) + x * x & 32767
    x = fn0(t0, t1, t2)
    e = x * x % 97
    w = 17 - x - x
    for q in range(44):
        t3 = e * (3 | w)
        w = t3 & 1023
        t4 = 7 + e - 5
        w = (t4 | q) & 511
        t5 = e * 16 + x * e & e
        w = (t5 - q) % 251
    t = 15 + x + 3
    buf = (w ^ t) + w >> 1
    t6 = x ^ 2
    y = t6 + (x >> 1)
    s = (y >> 3 | buf) % 251
    t7 = 1 - t
    acc = t7 - (s | buf)
    m = (x | 5) % 251
    t8 = e ^ y ^ 9
    tot = (t8 - (buf - e) * t) % 251
    t9 = (acc & m) * (tot * x)
    t10 = t >> 4 | acc - 2
    p = (t9 + t10) % 251
    cur = t >> 1
    tmp = 8 ^ s
    return acc + acc & 32767

if __name__ == "__main__":
    arg = 9
    expected = 19958
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
