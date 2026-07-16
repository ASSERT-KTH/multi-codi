# Auto-extracted from ds_lt256k_500.jsonl
# record_id=150  entry=f  input='11'  output='135'  tokens=139682

def rec(n, a):
    if n <= 0:
        return a
    a = (n >> 4 ^ a) & 262143
    t0 = (8 + n) // 4 + a
    return rec(n - 1, t0 % 65521)

def fn0(j):
    if j >> 2 == 23:
        j = j + j
        if j * 14 >= 57:
            t0 = j - 14 ^ j - 13
            t1 = t0 * (19 - j + 9)
            j = t1 & 16383
    else:
        j = j - 14
    for q in range(6):
        c = 0
        while c < 3:
            j = (c * q | j) & 2047
            t2 = c - 7 - 15 - q
            j = t2 - j & 255
            j = j * 16 * c + j & 16383
            c = c + 1
    for nxt in range(2):
        t3 = nxt - 1 ^ j
        t4 = 8 * 20 >> 1
        j = (t3 ^ t4) & 2047
    y = (j | 7) - j
    p = 0
    while p < 3:
        t5 = p * p & p
        y = (t5 | j) & 4095
        t6 = 14 * y - (p ^ 9)
        j = t6 - j & 2047
        y = 15 * p - j & 1023
        p = p + 1
    if 11 * y >= 13:
        if 5 - j != 55:
            j = j ^ 12
        else:
            j = j + y
    t7 = (j >> 4) * j
    lo = t7 & 65535
    t8 = (j >> 4) * j ^ y
    return t8 & 16383

def fn1(d, a):
    if d >> 2 == 62:
        w = 0
        while w < 6:
            t0 = (a - 8) * a * 4 - d
            d = t0 % 97
            t1 = (w + a) * a
            a = t1 + d * 16 // 3 & 4095
            w = w + 1
    else:
        buf = 0
        while buf < 5:
            d = (d | a) & 262143
            buf = buf + 1
    for t in range(3):
        for cur in range(4):
            t2 = 5 + t ^ a
            a = t2 & 65535
            t3 = 19 - d >> 4
            a = (t3 - a) % 9973
            a = a & 2
        v = 0
        while v < 3:
            a = ((a - 9) * t - a) % 65521
            t4 = t * t + 15
            t5 = t4 ^ t | d
            a = (t5 ^ a) & 255
            t6 = (17 - 3) * (a + t) ^ v
            d = t6 % 97
            v = v + 1
    t7 = (14 | d | 1 << 1) * d
    a = rec(76, t7 % 65521)
    t8 = d + a ^ 15 + a
    t9 = (13 - a) * (a ^ d)
    acc = t8 & t9
    z = 16 ^ 3 | a
    t10 = (a << 4) - acc
    t11 = acc // 5 * 15
    return t10 - t11 & 8191

def f(x):
    y = [659, 875, 150, 788, 971, 678, 681]
    t0 = y[x % 7] + x
    t1 = x - y[x % 7]
    t2 = x * y[x % 7]
    t3 = t0 // 3 + (t1 + t2)
    x = fn0(t3 % 251)
    y[x % 7] = (x * 10 - 6) % 1009
    lo = 0
    while lo < 352:
        t4 = y[x % 7]
        y[x % 7] = (t4 | x) % 1009
        lo = lo + 1
    res = x << 2
    t5 = (x - 2) * (x ^ 5)
    q = t5 & 8191
    t6 = x - q ^ 8 * 9
    cnt = t6 & x + res - 11
    for aux in range(12):
        t7 = y[cnt % 7] - x
        t8 = cnt * y[aux % 7]
        t9 = t8 * (aux + x)
        x = (t7 + aux) * t9 & 511
        t10 = x // 8 - cnt % 9973
        x = t10 & 8191
        t11 = cnt % 9973 * (q * 3)
        cnt = t11 % 251
    t12 = y[x % 7]
    buf = t12 * res % 251
    t13 = x - 20
    t14 = t13 * (x << 2)
    tot = t14 * 19 & 255
    if q * y[res % 7] >= 34:
        t15 = y[x % 7]
        t16 = (tot - q) * t15
        t17 = (t16 ^ q) & 255
        cnt = rec(83, t17)
        t18 = y[tot % 7]
        t19 = buf * res
        t20 = res + 20 << 4
        t21 = t19 | t18 + cnt
        q = (t20 - t21) % 251
    else:
        t22 = cnt * cnt - (11 + q)
        q = t22 % 9973
    prv = tot + tot
    t23 = y[q % 7]
    t24 = t23 * x
    t25 = t24 | 4 * res
    return t25 % 251

if __name__ == "__main__":
    arg = 11
    expected = 135
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
