# Auto-extracted from ds_lt256k_500.jsonl
# record_id=252  entry=f  input='9'  output='1911'  tokens=198809

def fn0(j, d, c):
    t0 = j * 1 & (j & 16)
    val = c + 15 & j ^ t0
    for tmp in range(7):
        j = (d // 7 | j) % 65521
        t1 = 9 * (j // 4) // 6 + tmp
        d = t1 % 17
        if c + j == 0:
            c = (c << 4 >> 1) % 65521
            val = (val >> 3) % 97
    t2 = val | d
    idx = t2 - (c - d)
    nxt = 0
    while nxt < 3:
        t3 = val * 2 >> 4
        val = t3 & 255
        nxt = nxt + 1
    if val * val != 45:
        val = j ^ idx
    res = j ^ idx | d + c
    t4 = j - 9 | c
    d = t4 - (idx >> 3 | c)
    return (res + val ^ j) & 255

def fn1(j):
    buf = [236, 177, 226, 155, 29, 209, 24, 201]
    for t in range(2):
        t0 = buf[j % 8]
        t1 = (j ^ t0) // 2
        t2 = t * j & t
        j = (t1 - t2) % 251
    t3 = buf[j % 8] << 1
    buf[j % 8] = ((t3 ^ j) >> 3) % 251
    t4 = buf[j % 8] * j
    t5 = t4 * buf[j % 8]
    d = (j & 20 ^ t5) & 2047
    t6 = 12 * 2
    t7 = t6 - (19 + j)
    j = t7 | d
    m = 0
    while m < 7:
        if buf[j % 8] + j > 40:
            t8 = (d - 16) * m
            buf[j % 8] = (t8 >> 3) % 251
        else:
            j = (d * 4 | m) & 32767
        m = m + 1
    t9 = buf[j % 8]
    t10 = t9 ^ j ^ d
    buf[j % 8] = (t10 >> 1) % 251
    t11 = (14 & 15) * 13 - j
    return (t11 - d) % 251

def f(x):
    tmp = x - 14
    t0 = x + x ^ tmp
    t1 = t0 * ((x & tmp) << 1)
    tmp = fn1(t1 & 8191)
    cur = 17 ^ tmp
    x = fn1((cur | 7) % 251)
    tot = (17 - tmp) // 2
    p = x + tot
    aux = (tot - x | tot * 16) & 255
    t2 = x + tmp & aux
    t3 = (t2 | x) % 4093
    t4 = cur * x % 97
    t5 = (tot | 2) * tmp & 16383
    tot = fn0(t3, t4, t5)
    t6 = (cur >> 1) * (p & 18)
    a = t6 - (aux << 2 & cur - x)
    t7 = (tmp - a) * cur
    t8 = t7 & (x * p | x)
    t9 = (x ^ a) * tmp
    t10 = (t9 + (a | 6) // 8) % 251
    aux = fn0(x % 97, t8, t10)
    d = 1 * aux
    if cur ^ x >= 29:
        a = (2 ^ x | 9) * aux & 262143
        lo = 0
        while lo < 8:
            a = (tot * p ^ a) % 9973
            p = ((13 << 3) - p) % 97
            d = d * lo % 251
            lo = lo + 1
    u = (p * 6 - a) % 9973
    t11 = tmp << 1
    t12 = t11 + (14 | a)
    v = t12 // 4 & 16383
    w = 4 | tot
    s = 15 + tmp
    if 2 - 18 | p == 25:
        for res in range(6):
            x = ((w + u) * tot + res) % 97
            t13 = (d | u) >> 4
            t14 = (t13 ^ 15) - res
            w = t14 & 131071
            t15 = s - p << 2
            t16 = a + d - w
            t17 = (t15 & t16) - res
            v = t17 % 4093
        t18 = x * 7 & 511
        t19 = (p ^ tmp) & 255
        v = fn0(t18, t19, 14 & u)
    else:
        t20 = (v ^ tot) % 251 * v
        v = t20 & 1023
        u = 12 | aux
    t21 = (a ^ d) * a
    t22 = d + v + aux
    t23 = (t21 + t22) % 4093
    t24 = (a - 4) * p
    t25 = u * tmp
    t26 = t25 | s >> 3
    s = fn0(t23, t24 % 9973, t26 % 97)
    for idx in range(5):
        for nxt in range(18):
            tot = (u - tmp - s ^ tot) & 2047
            t27 = 3 * tmp - cur
            a = (t27 | a) % 9973
            t28 = (s ^ tot) - tot
            t29 = (t28 << 1) - nxt
            p = t29 & 2047
        if x + 17 == 22:
            aux = (tot + 7 - a | idx) % 4093
            v = (20 | v) % 4093
        t30 = idx * 13 * (1 - u)
        v = t30 & 511
    t31 = v * 3
    t32 = a // 5
    t33 = t31 - (u - d)
    t34 = t32 - d * x
    return (t33 | t34) % 4093

if __name__ == "__main__":
    arg = 9
    expected = 1911
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
