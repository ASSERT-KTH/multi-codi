# Auto-extracted from ds_lt256k_500.jsonl
# record_id=387  entry=f  input='7'  output='323'  tokens=152061

def rec(n, a):
    if n <= 0:
        return a
    for c in range(5):
        t0 = (13 + 15) * a | 10 * n
        a = t0 % 9973
    for z in range(12):
        a = (20 | 15 | a) % 65521
        a = (n - 1 + n ^ a) % 97
    t1 = (4 | a) & a
    t2 = t1 & n // 8 >> 4
    return rec(n - 1, t2)

def fn0(m, e):
    for g in range(9):
        if m >> 1 >= 46:
            m = g + e & 255
        m = (e | m) % 4093
    t0 = m % 4093 - m
    t1 = t0 << 4 & 32767
    m = rec(60, t1)
    if 10 * m == 34:
        if e * m > 35:
            e = 7 & m
            t2 = 11 - m >> 1
            t3 = t2 * (e << 4 ^ e)
            e = t3 % 17
    else:
        m = (e ^ 4) // 6
    for nxt in range(5):
        t4 = nxt + 19 - m
        m = (t4 >> 2) % 4093
        t5 = m ^ 14
        t6 = t5 - (1 - 7)
        t7 = (t6 << 4) + nxt
        e = t7 % 17
    t8 = 2 - e + 5
    return t8 * ((m - 5) % 17) & 511

def fn1(g, j, c):
    t0 = (g | 14) % 4093
    t1 = (12 | j) & j
    t2 = t1 ^ g * g % 9973
    g = fn0(t0, t2 % 4093)
    j = (c + j) * c % 9973
    g = c - j - g >> 4
    t3 = g + j + g
    t4 = (c ^ 12) >> 2
    t5 = (t3 + t4) % 4093
    j = rec(34, t5)
    for acc in range(6):
        g = g // 8 & c
        t6 = (g ^ j) >> 3
        t7 = t6 - (c - 3 + acc)
        j = t7 & 32767
        g = ((c | 9) ^ acc) % 9973
    j = c // 2
    t8 = j // 5 ^ g
    c = t8 >> 1
    t9 = g & 16
    t10 = j // 7 + 13
    t11 = t9 | g * g
    return (t10 | t11) % 9973

def f(x):
    t = [29, 26, 75, 47, 19]
    if 6 + x == 2:
        x = x - 3
    else:
        if t[x % 5] - 17 == 3:
            t[x % 5] = x - 13
            t0 = x ^ 9
            t1 = x + x
            t2 = t0 + (x - 16)
            t3 = t1 & (11 | x)
            t[x % 5] = (t2 ^ t3) % 97
        else:
            t4 = t[x % 5]
            x = x - t4 >> 3
        x = 9 * x - x
    w = (x >> 2) + x
    for nxt in range(9):
        w = (nxt - x) % 9973
        w = ((nxt | 18) ^ w) % 9973
    t5 = w << 3
    t6 = t5 - (x & 14)
    hi = t6 >> 1
    t7 = 14 * x
    t8 = t[hi % 5]
    t9 = t[hi % 5]
    t10 = w + t8
    t11 = t7 * (hi * hi)
    t12 = t10 + (t9 >> 1)
    y = (t11 + t12) % 9973
    for c in range(228):
        t13 = x * t[x % 5]
        w = (t13 ^ y >> 3 | c) & 4095
        t14 = (hi | 6) // 6 ^ w
        hi = t14 & 255
    for j in range(6):
        t15 = t[x % 5]
        t16 = j * j
        t17 = t16 * (t15 + x)
        hi = t17 % 9973
    x = ((x >> 3) - w) * x & 2047
    t18 = t[y % 5] + 7
    return (t18 + hi ^ 6) % 1009

if __name__ == "__main__":
    arg = 7
    expected = 323
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
