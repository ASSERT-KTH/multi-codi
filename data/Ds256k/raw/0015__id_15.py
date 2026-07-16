# Auto-extracted from ds_lt256k_500.jsonl
# record_id=15  entry=f  input='19'  output='3'  tokens=81207

def fn0(e):
    res = e ^ 9
    if e + res > 2:
        t0 = res ^ 20
        t1 = t0 + (18 & res)
        res = t1 // 3
        res = 19 - e
    else:
        e = e - 19 - e % 251
    tot = 13 + e
    t2 = (e << 3) // 3
    t3 = (18 & res) << 4
    return t2 & t3

def fn1(m, j):
    acc = [998, 327, 11, 479]
    s = j + m - 13 * j
    buf = j % 9973
    c = 0
    while c < 3:
        t0 = m * 19 << 1
        t1 = (t0 + m) % 9973
        acc[c % 4] = t1 % 1009
        buf = buf // 8 % 1009
        t2 = buf * m // 8
        m = t2 >> 3 & 32767
        c = c + 1
    z = (m - 11 >> 2) - m
    j = 17 + 3 - (20 + j)
    t3 = acc[z % 4]
    t4 = s >> 1 >> 2
    t5 = (t3 | z) << 2
    return t4 * t5 & 255

def f(x):
    c = [43, 15, 44, 88, 40, 7, 53]
    if x + x > 23:
        t0 = x * 17 << 3
        x = t0 // 8
        x = x ^ 7
    else:
        if x ^ 9 < 4:
            t1 = c[x % 7] & x
            c[x % 7] = ((1 | 4) + t1) % 97
        else:
            x = 9 & x
            c[x % 7] = (12 + x) % 97
        x = 10 * x
    x = fn0((20 << 4) + x & 1023)
    t2 = c[x % 7]
    j = t2 * x % 97
    t3 = x - c[x % 7]
    m = (6 - x | t3) & j
    t4 = c[j % 7] - m - 1
    t5 = j >> 1 & 511
    j = fn1(t4 % 17, t5)
    w = x ^ 1
    s = m // 8 << 4
    g = 0
    while g < 2:
        for lo in range(7):
            t6 = c[x % 7]
            c[w % 7] = (t6 | j) % 97
            m = ((19 ^ j) + lo * w) % 17
            t7 = c[m % 7] >> 4
            t8 = t7 + (j + c[x % 7])
            c[w % 7] = t8 % 97
        for val in range(21):
            c[g % 7] = (13 + val | m) % 97
            t9 = c[s % 7]
            t10 = t9 // 5
            t11 = t10 ^ s * x
            c[g % 7] = (t11 - 20) % 97
            m = (m ^ 8) & 1023
        g = g + 1
    t12 = c[j % 7]
    t13 = t12 * c[s % 7]
    cur = t13 | 7
    hi = w * x % 97
    if 16 & cur >= 5:
        s = (6 + m) * x & 511
    if hi ^ w == 37:
        t14 = x - 11 - w
        c[j % 7] = t14 % 97
    acc = 0
    while acc < 10:
        hi = hi + c[s % 7] & 255
        acc = acc + 1
    for e in range(2):
        for y in range(11):
            t15 = e - 16 | s
            c[w % 7] = (t15 ^ m) % 97
    if s // 5 == 13:
        if x & cur > 58:
            t16 = j + 4 + w * x
            c[j % 7] = ((3 | x) & x) * t16 % 17
            cur = (hi - x) // 6
        else:
            c[w % 7] = (s + x) % 97
        if cur + j != 37:
            c[m % 7] = (9 ^ w) % 97
        else:
            t17 = c[x % 7]
            t18 = t17 * 12 + 15
            c[w % 7] = t18 // 4 % 97
    else:
        u = 0
        while u < 4:
            t19 = 8 - cur ^ m
            hi = (t19 | hi) % 4093
            u = u + 1
        t20 = 19 * 8 << 3
        t21 = 4 * 20 * 3
        m = t20 + t21 | m
    t22 = w * x | w
    return t22 % 17

if __name__ == "__main__":
    arg = 19
    expected = 3
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
