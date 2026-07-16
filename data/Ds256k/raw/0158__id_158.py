# Auto-extracted from ds_lt256k_500.jsonl
# record_id=158  entry=f  input='14'  output='44'  tokens=131915

def rec(n, a):
    if n <= 0:
        return a
    tot = 0
    while tot < 8:
        s = 0
        while s < 10:
            a = ((a | 19) >> 3) % 251
            s = s + 1
        tot = tot + 1
    t0 = (a >> 4 >> 4) % 17
    return rec(n - 1, t0)

def fn0(a, m):
    c = [28, 84, 14, 94, 34]
    for z in range(5):
        a = (a * a - 16) % 65521
    for lo in range(5):
        if c[lo % 5] | 3 | a >= 61:
            m = m + 5 & 32767
        else:
            t0 = 18 * 1 * c[m % 5]
            t1 = t0 - c[m % 5] ^ a
            a = t1 & 4095
            t2 = c[m % 5] - m
            t3 = 1 + 13 + (m | a)
            t4 = t3 - (t2 + (m >> 2))
            a = t4 & 16383
        t5 = (lo & m | lo) + m
        a = t5 & 32767
        t6 = c[m % 5]
        a = (a | t6) % 65521
    if 3 - 11 | m <= 49:
        t7 = m * c[m % 5]
        t8 = (c[a % 5] & a) + a
        m = (t7 | a - m | t8) & 4095
    else:
        t9 = 10 - 3 & m
        m = rec(84, t9)
        t10 = c[m % 5]
        t11 = (m - a) * t10 ^ 2
        a = t11 % 1009
    c[a % 5] = (13 + m + a ^ m) % 97
    d = (a - 17) // 6
    buf = d * d & 255
    t12 = a & c[m % 5]
    t13 = (c[m % 5] & a) << 1
    return (t13 ^ (5 & buf | t12)) & 131071

def f(x):
    p = [59, 9, 66, 105, 106, 28, 8, 30]
    for buf in range(17):
        for w in range(11):
            t0 = p[buf % 8]
            t1 = (t0 + 19) * buf
            x = (t1 + x) % 251
            t2 = (x | 2) // 7
            x = t2 % 251
        t3 = (buf & 9) * (buf ^ 10) | x
        x = t3 % 251
        t4 = p[x % 8] * buf >> 1
        t5 = (x - buf) * p[buf % 8]
        x = t4 + t5 & 16383
    val = (1 | x) & x
    for e in range(12):
        p[x % 8] = (val | 15) % 251
        cur = 0
        while cur < 2:
            p[x % 8] = 3 * x % 251
            t6 = 3 * x - val
            val = t6 % 251
            t7 = (val & cur | 3) + cur
            x = t7 % 9973
            cur = cur + 1
        if 8 | x == 61:
            t8 = 15 + val + (8 + e)
            x = t8 >> 2 & 131071
            t9 = (e | 8) & 13
            val = (t9 ^ x) % 9973
        else:
            t10 = val - p[e % 8]
            val = (t10 ^ e + 13) & 2047
            t11 = p[val % 8] * x
            p[x % 8] = ((t11 ^ x) & 16383) % 251
    t12 = val + 2 >> 3
    q = t12 * val & 131071
    y = val + x + val - x
    if (6 << 2) - q == 24:
        if q * 1 == 20:
            p[x % 8] = (q | val) % 251
            y = x // 3 // 6
        else:
            t13 = 13 ^ p[q % 8]
            p[x % 8] = (t13 + x) % 251
            y = q // 3
        prv = 0
        while prv < 9:
            t14 = q // 8 * 18
            p[q % 8] = t14 & 2
            t15 = p[x % 8]
            p[x % 8] = t15 // 5
            t16 = prv - p[x % 8]
            p[x % 8] = t16 % 251
            prv = prv + 1
    lo = 0
    while lo < 8:
        t17 = p[q % 8]
        t18 = val % 9973
        t19 = t18 + (lo - t17)
        q = t19 % 9973
        lo = lo + 1
    t20 = p[val % 8]
    aux = val - x & t20
    t21 = aux + p[x % 8]
    t22 = t21 - (q - 12)
    p[val % 8] = (t22 + (q >> 3) * x) % 17
    d = (y ^ 11) >> 1
    t23 = (x | q) + aux * val
    t24 = aux * y - d - t23
    return t24 % 251

if __name__ == "__main__":
    arg = 14
    expected = 44
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
