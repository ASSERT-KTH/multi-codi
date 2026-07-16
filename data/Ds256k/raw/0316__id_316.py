# Auto-extracted from ds_lt256k_500.jsonl
# record_id=316  entry=f  input='3'  output='156'  tokens=252126

def rec(n, a):
    if n <= 0:
        return a
    a = (a ^ 9) & 20
    t0 = (12 + 3 + a) % 17
    return rec(n - 1, t0)

def fn0(e, b, c):
    if e & 12 > 5:
        t0 = (e >> 3) - b * c
        t1 = (c | 5) // 6 * t0
        e = t1 & 16383
    else:
        if b * e <= 8:
            t2 = c + c | e * 13
            c = rec(80, t2 & 8191)
            t3 = b * e % 251
            c = rec(63, t3)
        else:
            c = 14 + e
        b = b * b % 251
    for d in range(10):
        u = 0
        while u < 9:
            c = ((e | b) - c) % 17
            b = b * e & (16 | e)
            u = u + 1
    idx = e - 3
    for z in range(6):
        t4 = b % 251 - (c >> 1)
        t5 = z * 10 + (16 - idx)
        idx = t4 + t5 & 4095
    t6 = (idx | 4) ^ c
    nxt = t6 + c
    t7 = (nxt ^ c) * (1 << 3)
    t8 = t7 * (b * 1 ^ idx)
    tot = t8 & 16383
    t9 = (6 | e) + idx
    t10 = nxt & 14 & idx
    return t9 & t10

def fn1(d, e):
    for acc in range(8):
        if 17 * acc ^ d > 24:
            t0 = d // 8 * 18
            t1 = t0 * (e // 8 // 6)
            d = t1 % 97
            e = (d << 4 & e ^ d) & 511
        else:
            t2 = (d - e + (d + e)) // 7
            d = t2 & 65535
            t3 = (d >> 2) + e
            e = t3 % 4093
    j = 0
    while j < 11:
        if d ^ 4 < 42:
            e = (1 ^ j | d) & 16383
        else:
            e = (d & 6) - j & 511
        t4 = (e >> 3) - e
        t5 = d - e & j
        d = t4 * t5 % 97
        t6 = d * j & 3
        e = t6 - d & 16383
        j = j + 1
    if (9 << 1) + d != 4:
        for tmp in range(7):
            t7 = (18 << 1) * (d << 1)
            d = (6 ^ 10) * t7 & 255
            t8 = e + e + 10 | d
            d = t8 & 1023
    t9 = e * e
    t10 = t9 - d * e
    t11 = d - e + d
    t12 = (t11 >> 1) % 9973
    t13 = d - 2 + d
    e = fn0(t10 & 32767, t12, t13 % 97)
    for p in range(10):
        if p | d != 53:
            t14 = 10 * 19 ^ e
            e = t14 * (e + 9 >> 1) & 32767
    return 2 * e % 4093

def f(x):
    idx = [90, 5, 46, 61]
    for aux in range(4):
        for lo in range(4):
            t0 = idx[aux % 4]
            t1 = (11 ^ t0) + x
            idx[x % 4] = t1 % 97
            idx[x % 4] = 5 + lo + (x + 7) ^ aux
            x = (aux + 5 + x) % 251
    for a in range(7):
        p = 0
        while p < 4:
            idx[p % 4] = (a + p | x) % 97
            idx[p % 4] = (x * 20 >> 3) % 97
            p = p + 1
        t2 = x - 8 ^ x
        idx[x % 4] = t2 % 97
    res = (x + 9 & x + x) + x
    if res << 2 != 48:
        q = 0
        while q < 4:
            x = (res ^ q) & 4095
            q = q + 1
        t3 = idx[res % 4]
        t4 = t3 - res - res
        x = t4 << 3
    if res >> 4 <= 27:
        t5 = idx[x % 4]
        t6 = 7 * res
        t7 = t6 * (t5 >> 1)
        res = t7 * 8 & 1023
    else:
        t8 = res * 20 + (19 + 18)
        idx[res % 4] = (t8 ^ 13 * x // 7) % 97
        if res + idx[x % 4] != 4:
            res = (x << 4) + (16 & x)
            t9 = (x | 17) // 4
            idx[res % 4] = t9 % 97
        else:
            res = res * x & 65535
    for w in range(12):
        t10 = 7 ^ idx[w % 4]
        t11 = idx[x % 4] | 5
        t12 = (res ^ w) * t10
        t13 = t12 | (res * res | t11)
        res = t13 % 251
    for d in range(11):
        for v in range(4):
            idx[res % 4] = 9 & res
            t14 = idx[res % 4] // 8 << 1
            res = t14 >> 3 & 511
        x = x * d & x << 1
    y = (res - 17 << 4 ^ 16) & 262143
    t15 = idx[x % 4]
    t16 = y + t15 & 4095
    t17 = (x ^ y) // 8
    t18 = res // 2 ^ idx[res % 4]
    x = fn0(t16, t17 & res, t18 & 262143)
    c = 0
    while c < 10:
        for buf in range(3):
            y = (y | 16) % 65521
            t19 = idx[buf % 4] * c
            t20 = t19 + idx[c % 4] * 2
            idx[res % 4] = (t20 + res) % 97
            t21 = res + c + buf
            idx[buf % 4] = t21 % 97
        c = c + 1
    for tmp in range(11):
        g = 0
        while g < 8:
            idx[y % 4] = (11 + 11 ^ y) % 97
            res = (res - y >> 3) % 65521
            g = g + 1
    s = res * y + y & 131071
    t22 = idx[x % 4]
    t23 = (t22 | 16) >> 3
    t24 = idx[x % 4]
    z = t23 - t24
    t25 = idx[s % 4]
    t26 = t25 & 16
    t27 = t26 - (s << 3)
    cnt = t27 % 1009
    return (19 * z >> 1) % 251

if __name__ == "__main__":
    arg = 3
    expected = 156
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
