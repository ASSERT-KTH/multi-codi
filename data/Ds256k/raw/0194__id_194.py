# Auto-extracted from ds_lt256k_500.jsonl
# record_id=194  entry=f  input='9'  output='6'  tokens=153599

def fn0(m, g):
    m = g >> 1
    t0 = m // 7
    t1 = 1 + g + 18
    t2 = t0 ^ m - g
    g = t1 - t2
    for tmp in range(3):
        for res in range(5):
            t3 = (4 ^ 5) - g // 6
            m = (res + m ^ t3) & 4095
            t4 = (res + m) * (res + m) - m
            m = t4 & 255
    t5 = m // 5 << 4
    m = (t5 | (m * g | 11)) & 255
    m = g * m % 9973
    val = 0
    while val < 5:
        for buf in range(9):
            m = (buf - 16 - buf - g) % 251
        g = (val - g) % 4093
        val = val + 1
    return g * g & 65535

def fn1(g, c):
    for t in range(5):
        t0 = 5 + g & 4 * g | c
        c = t0 % 4093
    if 18 | c <= 12:
        if 11 - c >= 43:
            g = 12 | c
            t1 = (2 | c) * g
            t2 = g // 6 >> 4
            t3 = (t1 | t2) & 8191
            t4 = (g ^ 17) * (c * c)
            t5 = (g + g) // 7 * t4 & 131071
            g = fn0(t3, t5)
        c = g - c >> 4
    if 10 + 14 - g < 46:
        t6 = (11 + g) * (c * g)
        g = t6 // 8 % 65521
    t7 = c + c << 4
    res = (t7 + c) % 65521
    d = 8 ^ c
    if c // 5 > 39:
        t8 = d - res & 65535
        t9 = (d - res + (res << 1)) % 65521
        res = fn0(t8, t9)
    else:
        res = res & 14
    return (12 + 5) * res % 4093

def f(x):
    t0 = x * x + (x | 7) - 2
    t1 = (x | 11) << 4
    t2 = (t1 ^ x) & 32767
    x = fn1(t0 & 262143, t2)
    t3 = (6 | x) * (x - 16)
    t4 = (x + 8) % 17
    x = fn1(t3 % 97, t4)
    idx = x & 6
    t5 = idx ^ 2
    t6 = t5 * (19 ^ idx)
    tot = t6 ^ idx
    for c in range(50):
        t7 = c | 15
        t8 = t7 - (idx & tot)
        idx = t8 & 65535
        idx = (tot * tot + tot + c) % 1009
        t9 = x * c // 4 ^ x
        idx = t9 & 255
    val = 0
    while val < 8:
        tot = (tot | 4) & 511
        if idx // 8 != 49:
            tot = val * x & 4095
        t = 0
        while t < 9:
            t10 = val + x
            t11 = t10 + val * t
            t12 = tot - 3 + 11
            x = t11 & t12
            idx = t + idx & 4095
            t = t + 1
        val = val + 1
    t13 = ((x >> 4) % 17 ^ 15) & 131071
    t14 = (x + x - (idx ^ 20)) % 1009
    x = fn0(t13, t14)
    y = (x ^ idx) + x
    aux = tot // 2 ^ (8 | 17)
    if x ^ tot != 36:
        t15 = idx ^ x ^ x
        aux = (t15 << 3) % 1009
    buf = 0
    while buf < 10:
        t16 = (x >> 1) + idx
        idx = t16 & 65535
        t17 = (4 & 9) << 1
        t18 = t17 - aux | buf
        y = t18 % 97
        buf = buf + 1
    t19 = (aux ^ 18) + 1
    acc = t19 - aux
    return (aux + x) // 8 % 17

if __name__ == "__main__":
    arg = 9
    expected = 6
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
