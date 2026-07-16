# Auto-extracted from ds_lt256k_500.jsonl
# record_id=143  entry=f  input='9'  output='3'  tokens=206272

def rec(n, a):
    if n <= 0:
        return a
    t0 = 17 + a >> 1
    t1 = (a | n) // 7
    tmp = (t0 | t1) % 4093
    t2 = 6 ^ a
    t3 = t2 ^ tmp & n
    e = t3 & 4095
    e = e + n & 2047
    t4 = tmp + a & tmp
    return rec(n - 1, t4)

def fn0(b, d, e):
    hi = 3 + e
    for m in range(10):
        t0 = b - hi - 1 >> 4
        e = t0 - e & 16383
        e = (d - m) % 9973
    if e >> 2 < 17:
        b = 6 ^ hi
        t1 = e ^ b
        t2 = t1 ^ b * e
        b = t2 * hi % 9973
    else:
        for a in range(7):
            hi = (e + a + d) % 9973
        w = 0
        while w < 9:
            t3 = b // 7 * (1 + hi)
            b = t3 * ((e << 3) + 18) & 511
            w = w + 1
    t4 = (hi << 2) * (d << 1)
    t5 = (19 * d * hi ^ t4) % 9973
    b = rec(77, t5)
    for cnt in range(7):
        res = 0
        while res < 12:
            t6 = 18 + b & d + e
            hi = (t6 >> 3 ^ res) % 9973
            d = d & cnt
            res = res + 1
        t7 = e + 4 - hi
        d = t7 + cnt & 262143
    if 11 + d < 32:
        t8 = 7 * hi * (hi * e)
        hi = (t8 ^ (16 | 12) - e) & 4095
        hi = (hi | 16) * e & 131071
    else:
        val = 0
        while val < 3:
            d = val * e & 131071
            val = val + 1
        buf = 0
        while buf < 2:
            e = (3 - buf ^ b) % 9973
            b = (b | 13) % 9973
            d = (d * b ^ b) & 511
            buf = buf + 1
    for c in range(6):
        t9 = e - 7 + 7
        t10 = t9 * b - c
        hi = t10 & 16383
    g = 9 + d
    return (d & b ^ hi) & 255

def f(x):
    tot = x * x
    t0 = tot * tot - 18 << 4
    lo = t0 % 251
    w = lo + x
    idx = (19 ^ tot) * x
    t1 = idx * w * (x * w) // 7
    e = t1 % 17
    for hi in range(7):
        t2 = e - 1 + hi
        lo = t2 % 17
        w = (1 * e ^ hi) % 97
        if e & 18 <= 14:
            t3 = (2 & x) - 15 << 3 ^ idx
            idx = t3 % 97
            t4 = w // 3 + tot
            tot = t4 & 32767
    acc = x - lo & 14
    cur = w & lo
    t = (idx + lo) * 12
    z = x % 17
    t5 = acc ^ w
    t6 = x - z
    t7 = t5 + t * tot
    t8 = t6 * (tot >> 1)
    g = t7 - t8 & 511
    buf = (acc & x & g) << 1
    for j in range(109):
        t9 = acc * t * buf
        buf = t9 & 65535
        t10 = buf + 4 + (6 - e)
        t11 = (w ^ cur) * 17 + t10
        acc = (t11 | acc) % 251
    s = t - 11 ^ acc ^ x + 5
    d = (lo * s | e) % 65521
    t12 = (z ^ 12) % 251
    t13 = acc - t & 2047
    t14 = s - x + tot
    t15 = acc + 10 + t14
    z = fn0(t12, t13, t15 % 65521)
    t16 = tot - z + tot
    t17 = t16 + (z * z & d)
    return t17 % 97

if __name__ == "__main__":
    arg = 9
    expected = 3
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
