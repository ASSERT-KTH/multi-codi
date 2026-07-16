# Auto-extracted from ds_lt256k_500.jsonl
# record_id=174  entry=f  input='20'  output='8182'  tokens=152372

def rec(n, a):
    if n <= 0:
        return a
    t0 = n << 1
    t1 = t0 + (a | 9)
    prv = t1 >> 2 & 65535
    p = (14 & n | a) % 17
    t2 = a // 3 - prv // 6
    t3 = (18 ^ 9) * a ^ t2
    return rec(n - 1, t3 % 251)

def fn0(g, m, d):
    if d * g > 38:
        if g & d > 9:
            g = d - g
            d = rec(32, d % 9973)
        else:
            t0 = m ^ 17
            t1 = t0 * (9 + g)
            m = rec(53, t1 % 97)
            d = g >> 1
        t2 = (d - 13) // 6
        d = t2 & ((m | d) ^ m)
    else:
        m = d * d & 131071
        for u in range(5):
            t3 = u * g // 7
            m = t3 % 9973
            t4 = m // 2 + u
            g = t4 % 9973
            t5 = (u & 11) + (17 | 11)
            m = (t5 ^ 7 | g) % 9973
    for s in range(4):
        m = m * s % 97
        for j in range(4):
            t6 = m >> 3 | g
            g = t6 & 8191
    if g + 12 < 38:
        m = g // 6 & g - 13
    w = 0
    while w < 11:
        t7 = (d | m) ^ 20
        t8 = t7 * m | g
        g = t8 & 32767
        d = (m ^ w) % 9973
        w = w + 1
    hi = m ^ 15
    t9 = hi - g ^ m
    res = t9 + d
    t10 = m - d
    t11 = t10 + (res | d)
    return t11 & m

def fn1(e, c, d):
    d = c * d & 16383
    if d ^ c != 32:
        d = 12 + 14 - e
        if c - d == 4:
            e = (c ^ d) & c - 12 | d
            d = 5 * c
        else:
            t0 = d | 6
            t1 = t0 & c // 3
            t2 = (t1 >> 1) % 97
            t3 = (11 | d) & 4095
            t4 = (d ^ c) + e ^ 14
            d = fn0(t2, t3, t4 & 262143)
    else:
        c = (d + c) // 5
    nxt = 0
    while nxt < 7:
        t5 = e ^ 4 ^ nxt + c
        c = t5 % 1009
        nxt = nxt + 1
    return (d ^ 2) // 2 % 1009

def f(x):
    w = x | 13
    b = x - w ^ 1
    c = x * w + 16
    t0 = (b * w * x - 7) % 97
    t1 = c + b & (w & 19) ^ w
    t2 = (b ^ c) % 97
    x = fn1(t0, t1 & 65535, t2)
    g = 20 * c + b
    t3 = (w + g ^ 12 * c) % 9973
    g = rec(57, t3)
    z = g + x
    p = c // 2
    for prv in range(9):
        t4 = (z >> 1) + c
        t5 = t4 % 4093 ^ g
        g = t5 % 97
        for a in range(11):
            t6 = prv << 3 & g + p
            z = t6 - z & 32767
            t7 = 7 ^ g ^ (a | w)
            z = t7 % 4093
    if c + b <= 62:
        if p * 15 == 40:
            t8 = (g ^ p) - x
            g = t8 % 4093
            t9 = p * 19
            t10 = t9 - (p - w)
            t11 = (w - g | g) & 511
            t12 = (p >> 1) - b + z & 255
            c = fn1(t10 & 16383, t11, t12)
        else:
            c = g - 13 + g
            t13 = g & 5
            t14 = t13 ^ (19 ^ z)
            w = t14 >> 1
        for cur in range(3):
            t15 = cur | b
            t16 = t15 - (p | 20)
            x = t16 % 9973
            z = (z | x) >> 4 & 8191
            t17 = (cur ^ w) // 8
            t18 = t17 - (x + 4 << 4)
            g = t18 & 8191
    else:
        if w % 9973 < 8:
            t19 = (w * c | p) & 4095
            t20 = (g ^ p) % 97
            t21 = (w << 2) % 4093
            c = fn1(t19, t20, t21)
            g = 20 - c
    for tot in range(68):
        t22 = z // 5 ^ x
        x = t22 % 4093
        w = (x - w ^ z) >> 3 & 16383
    tmp = (g >> 4) // 6 ^ 11
    t23 = 6 - x >> 4
    return t23 + b & 8191

if __name__ == "__main__":
    arg = 20
    expected = 8182
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
