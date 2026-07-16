# Auto-extracted from ds_lt256k_500.jsonl
# record_id=48  entry=f  input='11'  output='65'  tokens=254788

def rec(n, a):
    if n <= 0:
        return a
    t0 = a // 5 + a
    a = t0 % 65521
    a = (n - 10 - a) % 65521
    t1 = (18 + n) * n
    t2 = (t1 | a) % 1009
    return rec(n - 1, t2)

def fn0(e, b, j):
    b = b ^ j
    e = 10 - j // 2 - b
    if e ^ 12 != 27:
        t0 = j + e & 8191
        j = rec(93, t0)
    else:
        if j >> 2 == 20:
            t1 = (b - j - e) % 1009
            e = rec(48, t1)
            j = e * j % 17
        else:
            t2 = e - b & e + 4
            j = rec(31, t2)
        t3 = j | e
        j = t3 ^ (e ^ b)
    t4 = (e + j) % 1009
    j = rec(25, t4)
    if b * 5 < 6:
        t5 = e + e & 1023
        j = rec(80, t5)
    else:
        if j << 2 == 44:
            t6 = (j - 3) % 17
            j = t6 - ((15 ^ e) & b)
        for tot in range(2):
            e = (tot - 5 << 3 ^ j) % 17
            j = 1 + tot - j & 16383
    if e * j >= 41:
        t7 = j - 15 & 1023
        e = rec(83, t7)
    else:
        j = 14 ^ e
        b = b // 5 & 15
    t8 = b % 17 - j
    return t8 & 255

def f(x):
    u = 0
    while u < 2:
        cur = 0
        while cur < 3:
            t0 = u - cur + cur + x
            x = t0 % 4093
            cur = cur + 1
        t1 = (u | x) + u ^ x
        x = t1 & 255
        x = (x ^ 2) & 255
        u = u + 1
    t2 = x >> 1 & 255
    t3 = x // 2 % 9973
    t4 = (x << 3 >> 3) // 7 % 251
    x = fn0(t2, t3, t4)
    t5 = (x >> 4) - x // 4
    m = t5 - x
    for acc in range(6):
        m = (m - acc) % 1009
        t6 = acc - 1 - acc | x
        m = t6 % 251
    t7 = 11 - m - 13
    t8 = (x >> 1) % 9973
    j = t7 ^ t8
    t9 = 17 * 15 ^ m
    t10 = (x ^ 2) * (8 & j) + m
    t11 = (m | 11) % 9973
    x = fn0(t9 % 4093, t10 % 9973, t11)
    t12 = (10 + j) % 4093
    m = rec(43, t12)
    t13 = (m ^ j ^ j >> 3) * m
    lo = t13 & 65535
    for cnt in range(163):
        j = 10 * j // 5 & 1023
    t14 = (j // 2 ^ x * x) // 3
    d = t14 & 4095
    for s in range(12):
        res = 0
        while res < 2:
            lo = (16 ^ lo) // 2 & 131071
            t15 = 2 * m | j
            j = t15 & 32767
            x = (d - m | res) % 4093
            res = res + 1
        t16 = (x ^ m) + (s ^ lo) ^ 13
        j = t16 & 1023
    w = m | x
    t17 = (10 ^ j) * j
    nxt = t17 % 9973
    t18 = lo // 4 * (j & x)
    t19 = t18 ^ d + d + (m >> 4)
    tot = t19 & 2047
    q = 0
    while q < 12:
        tot = (lo << 4 | tot) & 255
        q = q + 1
    return (d - x + w // 6) % 251

if __name__ == "__main__":
    arg = 11
    expected = 65
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
