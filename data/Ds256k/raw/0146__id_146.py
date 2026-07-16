# Auto-extracted from ds_lt256k_500.jsonl
# record_id=146  entry=f  input='12'  output='185732'  tokens=148619

def fn0(a, e):
    g = [113, 247, 235, 2, 245, 71]
    b = e // 5 - (a ^ 16)
    b = e // 4
    t0 = g[b % 6] ^ 2
    t1 = t0 * (a - b) + e
    b = t1 & 262143
    if b + e < 36:
        g[e % 6] = (3 + e) % 251
    else:
        t2 = e >> 3 ^ e
        t3 = g[a % 6]
        g[e % 6] = t2 * t3 % 97
    t = 0
    while t < 2:
        t4 = t - g[e % 6]
        a = (t4 - (e + b) ^ b) % 4093
        t = t + 1
    for cnt in range(12):
        t5 = e ^ 2 | a
        a = t5 % 4093
        buf = 0
        while buf < 10:
            g[e % 6] = (buf - e) % 251
            g[a % 6] = e % 9973 % 251
            buf = buf + 1
    b = a ^ 18 ^ 14
    b = (6 + e) % 97
    t6 = 12 - e + a
    t7 = g[a % 6]
    t8 = t6 + t7 - b
    return t8 & 131071

def f(x):
    b = 17 - x + x
    t0 = x - 20 - 2
    j = t0 * ((b << 1) + b)
    t1 = b * j << 2
    w = (t1 ^ x) & 8191
    t2 = (x | b) % 97
    t3 = x + 9 & 2047
    j = fn0(t2, t3)
    for z in range(19):
        w = ((6 & x) - z) % 97
        prv = 0
        while prv < 4:
            w = w & x
            prv = prv + 1
        t4 = 14 & z ^ j
        x = t4 % 17
    t5 = x - j
    t6 = t5 | j + 9
    t7 = (b - 3) * x
    hi = t6 & t7
    for e in range(12):
        t8 = w * b
        t9 = t8 - (b + j)
        w = t9 & 4095
        t10 = (e + 4) * (j & w)
        t11 = t10 ^ (17 & j) * (x & e)
        j = t11 & 8191
        t12 = (hi | 18) & x ^ b
        b = t12 % 1009
    buf = 0
    while buf < 8:
        t13 = (x | 1) * (j - 3)
        x = t13 % 4093
        buf = buf + 1
    t14 = (11 - 9 + j) % 4093
    t15 = w * x % 17
    b = fn0(t14, t15)
    val = j - w
    lo = (w >> 1 << 2) - val
    t16 = hi + val + 15
    res = t16 - (w * 17 >> 1)
    u = (res + w) * 16 % 17
    t17 = lo ^ j
    t18 = (lo ^ res) & 7
    t19 = t17 ^ res + val
    return t18 * t19 & 262143

if __name__ == "__main__":
    arg = 12
    expected = 185732
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
