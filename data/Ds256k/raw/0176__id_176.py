# Auto-extracted from ds_lt256k_500.jsonl
# record_id=176  entry=f  input='10'  output='409'  tokens=261141

def fn0(j, a, e):
    aux = [59, 54, 3, 64, 24, 22]
    e = e & 1
    e = (e + 15) // 5 << 4 & 32767
    for acc in range(6):
        for m in range(9):
            j = (18 & a ^ j) & 32767
            t0 = 10 - 9 - e
            e = t0 & 65535
    if e | aux[e % 6] != 51:
        for p in range(11):
            t1 = 8 * aux[j % 6]
            t2 = (6 | e) - t1 | p
            a = t2 % 9973
            t3 = aux[e % 6]
            t4 = aux[j % 6]
            t5 = t3 - t4 >> 3
            j = t5 & 4095
            j = (p - j) // 3 % 1009
    else:
        for s in range(6):
            a = (e - 1 ^ s) % 97
        j = a | aux[e % 6]
    t6 = aux[j % 6]
    t7 = (a ^ t6) + e
    t8 = (15 & j) * t7
    e = t8 % 17
    for d in range(5):
        a = d * j % 17
        e = (a & j) + d & 32767
        e = e * 4 % 1009 & e
    for idx in range(6):
        a = a + idx & 4095
        for cnt in range(10):
            t9 = aux[e % 6]
            t10 = t9 + e >> 1
            e = t10 % 1009
            e = ((a // 3 | idx) - cnt) % 9973
            t11 = (20 ^ 17 | 14) - j
            aux[a % 6] = t11 % 97
    t12 = a & 19
    return t12 & (a & j)

def fn1(e, m):
    t0 = (12 ^ 17) + e
    t1 = 3 * e & 13 ^ 6
    t2 = m * 13 % 97
    e = fn0(t0 & 2047, t1 % 9973, t2)
    b = (3 - e) // 8
    u = m + m
    for y in range(3):
        if e - 4 < 1:
            t3 = m * 14 << 1
            b = (t3 | b) & 32767
            e = (u * m + u ^ e) & 4095
        d = 0
        while d < 6:
            t4 = (4 + e) * 4
            e = t4 - d & 255
            e = b - 15 - e & 65535
            t5 = b - 13 >> 4 ^ 14 | d
            u = t5 % 97
            d = d + 1
        u = u - 9 & 2047
    g = u // 4
    m = u + 11
    if 20 + b < 26:
        e = m // 7 ^ m
        tmp = 0
        while tmp < 10:
            t6 = 16 * m * (e | tmp) ^ g
            u = t6 % 97
            tmp = tmp + 1
    else:
        for tot in range(6):
            u = (10 * tot ^ g) % 97
            t7 = g + e - 13
            m = t7 + m & 65535
        t8 = (20 ^ u) % 97
        t9 = (4 ^ u) - g << 3
        t10 = g % 9973
        t11 = t10 + (u >> 1)
        b = fn0(t8, t9 % 9973, t11 % 9973)
    m = 20 ^ e
    return (b << 4) % 97

def f(x):
    c = [22, 12, 40, 2]
    t0 = c[x % 4] - x
    m = t0 | 17
    cur = x ^ 4
    for tmp in range(11):
        t1 = (8 | m) % 251
        t2 = c[m % 4]
        t3 = t1 * t2 | x
        x = t3 % 9973
        t4 = 12 + x
        t5 = t4 - m * tmp
        x = t5 % 251
    res = cur + 5
    if x ^ cur == 43:
        t6 = cur - 2 + m
        c[x % 4] = t6 * (cur + m >> 1) % 97
        x = cur - res
    else:
        cur = (x | m) + (20 & 4)
        c[m % 4] = m >> 3 & x
    acc = (14 & 10) << 1 | cur
    t7 = acc >> 3
    t8 = t7 * (cur + x)
    prv = t8 & 1023
    for j in range(3):
        for y in range(2):
            t9 = prv + prv
            t10 = t9 * (x ^ res)
            t11 = (t10 + 14) % 1009
            c[x % 4] = t11 % 97
            t12 = c[cur % 4]
            t13 = prv + t12
            t14 = t13 - (y + 14)
            m = t14 % 251
        res = (6 & x) + j & 262143
        for tot in range(12):
            c[res % 4] = (13 + tot - (x - 17)) % 97
            t15 = m * cur
            t16 = t15 - (9 ^ 7)
            t17 = t16 * 8 & 2047
            c[j % 4] = t17 % 97
    t18 = c[acc % 4] | x
    u = (t18 ^ acc * cur) % 97
    if res - m <= 11:
        t19 = (prv + prv - acc) % 9973
        t20 = 9 + c[cur % 4]
        t21 = t20 ^ (c[u % 4] ^ prv)
        cur = fn1(t19, t21 & 1023)
        t = 0
        while t < 8:
            cur = prv + 20 - t & 65535
            c[x % 4] = ((x >> 2) // 8 + 11) % 97
            m = acc + m & 8191
            t = t + 1
    else:
        t22 = (m & x) % 1009
        c[cur % 4] = t22 // 3 % 97
        t23 = prv ^ x ^ cur
        c[cur % 4] = t23 % 97
    t24 = m // 6 - u // 6
    t25 = t24 ^ (m ^ prv) // 5
    return t25 % 1009

if __name__ == "__main__":
    arg = 10
    expected = 409
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
