# Auto-extracted from ds_lt256k_500.jsonl
# record_id=61  entry=f  input='17'  output='3390'  tokens=244090

def fn0(b, e, d):
    g = [102, 69, 146, 153, 5, 72]
    t0 = g[e % 6]
    e = t0 & 1
    if e ^ b != 29:
        g[e % 6] = (e - d - b) % 251
    else:
        g[b % 6] = (d + d) % 251
        t1 = 6 * b * g[b % 6]
        d = ((e ^ b) - b) * t1 & 131071
    t2 = (d - 3) * e
    t3 = t2 | g[e % 6]
    e = t3 & 32767
    return (e - 11) % 251 & d

def fn1(j, a, d):
    q = [132, 107, 59, 33]
    y = 0
    while y < 5:
        if d - y != 26:
            a = (y | j) % 65521
        y = y + 1
    t = a * d % 65521
    tot = (a | 18) % 97
    t0 = j + 3 | tot * j
    a = (j >> 4 & a) * t0 % 97
    d = q[d % 4] * j & 8191
    t1 = (11 ^ a) & 19
    return (t1 ^ t) % 65521

def f(x):
    if 14 ^ x >= 6:
        x = x * x - x
    else:
        for cnt in range(2):
            t0 = (cnt ^ 3) - cnt
            x = t0 + x & 1023
        if 1 * x > 63:
            t1 = x - 13
            t2 = 18 & x
            t3 = t1 * (x // 8)
            t4 = t2 + (x ^ 20)
            t5 = (t3 + t4) % 4093
            t6 = x - 11
            t7 = x * x << 1
            t8 = t6 - (x << 1)
            t9 = (t7 | t8) % 4093
            t10 = (x // 4 << 4) % 9973
            x = fn0(t5, t9, t10)
            t11 = x + x & 8191
            t12 = (x ^ 1) % 9973
            t13 = x >> 2 & 8191
            x = fn1(t11, t12, t13)
    if (10 ^ 18) - x < 26:
        x = (x + 8 + x) % 65521
        t14 = (x ^ 16) * (3 ^ x) % 9973
        t15 = x * x - (5 + x) & 8191
        t16 = x + x & 65535
        x = fn1(t14, t15, t16)
    else:
        for b in range(3):
            t17 = x * b // 3 >> 2
            x = t17 & 262143
            t18 = (b ^ 17) * (x // 7)
            x = t18 & 8191
            x = 19 + 7 - b - x & 16383
    t19 = (2 + x >> 3) % 4093
    t20 = (4 ^ x) % 65521
    t21 = 19 - 1 & x
    x = fn1(t19, t20, t21)
    if x // 6 <= 44:
        t22 = x + x - (x - 20)
        x = (x + x) // 2 + t22
    else:
        if x - 1 >= 23:
            x = 11 + x
        for v in range(4):
            t23 = (3 << 3) * 10
            t24 = t23 // 7 | x
            x = t24 & 4095
            x = x * 6 * 14 & x
    aux = 0
    while aux < 328:
        if 20 * x < 23:
            x = (x >> 1) % 97
            x = (aux ^ x) % 9973
        t25 = (aux - 20) * (aux - x)
        x = t25 % 4093
        if x - 18 < 3:
            x = (aux * x << 3) // 4 % 97
            t26 = (aux + 17) * (x + aux) + x
            x = t26 % 4093
        else:
            x = (x | 9) - aux * 9 & 262143
        aux = aux + 1
    w = (x - 12 << 3) % 97
    return w * x % 4093

if __name__ == "__main__":
    arg = 17
    expected = 3390
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
