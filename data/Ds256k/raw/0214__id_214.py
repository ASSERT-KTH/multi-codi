# Auto-extracted from ds_lt256k_500.jsonl
# record_id=214  entry=f  input='14'  output='103'  tokens=108740

def rec(n, a):
    if n <= 0:
        return a
    t0 = (8 << 3) - 14 + a
    y = (t0 ^ n) & 262143
    if a * a >= 24:
        y = (y | 16) % 4093
    else:
        v = 0
        while v < 4:
            t1 = n * y | v
            a = t1 % 4093
            y = (a // 3 ^ v) % 4093
            y = (a - n | y) % 17
            v = v + 1
        a = ((18 ^ 1) - y - a) % 17
    t2 = (a << 3) % 9973
    return rec(n - 1, t2)

def fn0(a, e, d):
    if 9 + a != 41:
        a = d - 6
    else:
        e = 8 * 3 + e
        d = e + d | d
    e = rec(101, e & d)
    t0 = (13 - 10 - a) % 17
    e = rec(76, t0)
    s = 0
    while s < 11:
        t1 = d & 12
        t2 = t1 | d >> 3
        e = (t2 ^ e) % 17
        t3 = ((a << 1) - 9) * 14 | s
        d = t3 & 255
        v = 0
        while v < 2:
            t4 = s * d
            t5 = (e ^ 1) - e
            t6 = t4 ^ 20 - d
            e = t5 * t6 & 511
            a = (e ^ d ^ v) % 9973
            d = ((a ^ 5) % 97 + v) % 9973
            v = v + 1
        s = s + 1
    val = a * d % 9973
    aux = 0
    while aux < 3:
        if val * 2 != 44:
            t7 = (a & d) - e
            d = t7 % 97
            t8 = (a + aux) * (val * e)
            t9 = t8 + (9 + e & a)
            a = t9 & 255
        t10 = val - 12 - (aux + val) - aux
        e = t10 % 17
        aux = aux + 1
    t11 = val - 12 + e
    return t11 & 16383

def fn1(m, a, e):
    y = a * m * (19 + 3) % 4093
    t0 = a % 97 << 3
    e = rec(55, t0 & 2047)
    if m * m < 32:
        t1 = (m >> 3 ^ y) & 9
        e = rec(90, t1)
        if a | y > 44:
            t2 = (e * e * y + a) % 97
            a = rec(94, t2)
            y = a ^ 20
        else:
            t3 = (e & y) // 4 & 2047
            t4 = e - y
            t5 = m * a << 3
            t6 = t4 ^ (m ^ 17)
            t7 = t5 * t6 & 1023
            t8 = (a * y | a) % 251
            m = fn0(t3, t7, t8)
    for cnt in range(12):
        a = (cnt | a) // 5 % 1009
    t9 = a // 7
    t10 = t9 | 2 ^ m
    t11 = 10 + e & e
    s = t10 ^ t11
    for acc in range(3):
        if a + e <= 12:
            m = m - y & s
            y = (m * y ^ s) % 97
        for res in range(9):
            t12 = res - 18 - res + res - y
            s = t12 % 97
            t13 = 20 * s + m ^ a
            a = t13 % 251
        t14 = m + 17 - a | y
        y = t14 & 131071
    tot = y - 20
    t15 = s + tot
    return t15 & e - y

def f(x):
    for d in range(7):
        x = x - 9 - d * x & 32767
        for w in range(2):
            x = (w * d | x) & 511
        if x * 12 != 35:
            x = d * d & (x | 13)
            x = (x + x) % 17
    if x * x >= 47:
        t0 = (x + x) % 17
        t1 = (x - 6) % 4093
        t2 = x ^ 4
        t3 = t2 + x * 9
        x = fn1(t0, t1, t3 % 4093)
        for m in range(8):
            x = (10 + x) % 4093
    t4 = x + 7 ^ x * x
    tot = (t4 | x) % 17
    t5 = tot | 19 | x
    t6 = (x - 18) * 20
    z = (t5 ^ t6) % 4093
    if x ^ z >= 27:
        x = x - 4
        val = 0
        while val < 6:
            z = z // 2 - x & 4095
            t7 = x // 8 * tot
            tot = t7 & 8191
            val = val + 1
    else:
        x = tot >> 2
        t8 = tot + tot & z + z
        t9 = t8 * (tot * x + tot)
        z = t9 % 17
    t = (3 | z) + (tot | x)
    t10 = 18 - x
    t11 = t10 & t - tot
    idx = t11 // 5
    t12 = idx * tot >> 2 << 1
    s = t12 % 17
    for res in range(283):
        t13 = tot * 4 % 17 ^ tot
        z = t13 + z & 8191
    if s ^ z <= 50:
        for u in range(6):
            t = (u * tot >> 4) % 4093
    else:
        idx = 6 * z
        idx = (idx + z) // 4
    if z - t == 1:
        tot = (t ^ s) + s
        for p in range(4):
            t14 = (13 - z) * (idx ^ tot)
            t = t14 + t & 16383
            tot = (19 | tot) * p << 3 & 2047
            t15 = t // 7 ^ p
            tot = t15 & 131071
    return ((1 & 12) + idx) % 4093

if __name__ == "__main__":
    arg = 14
    expected = 103
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
