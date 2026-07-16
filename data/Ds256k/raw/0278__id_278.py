# Auto-extracted from ds_lt256k_500.jsonl
# record_id=278  entry=f  input='6'  output='15376'  tokens=115956

def rec(n, a):
    if n <= 0:
        return a
    t = (a - 16 ^ n) % 17
    t0 = n + n
    t1 = t0 - (a | n)
    return rec(n - 1, t1 & 511)

def fn0(e, a, g):
    prv = 17 & a
    t0 = prv - 10 ^ 3
    acc = t0 | (prv << 4 | a)
    res = 0
    while res < 4:
        if 1 ^ g <= 51:
            t1 = a // 8 ^ (prv ^ res)
            e = ((13 - g) * 7 ^ t1) & 511
            g = (20 + e + g) % 1009
        else:
            t2 = a + g + 8 * 17
            a = t2 % 65521
            e = (acc | res) * 1 % 65521
        if 17 * res + prv < 63:
            t3 = 5 * a << 2
            t4 = t3 * (g // 8 // 4) - acc
            acc = t4 & 65535
            t5 = g + res | a
            g = t5 & prv
        else:
            t6 = prv - a - (a + prv) ^ res
            g = t6 & 32767
        res = res + 1
    for val in range(2):
        if val + g < 15:
            prv = prv % 65521
            e = (prv | e) & 4095
        if 2 + a == 18:
            t7 = (a & 18) * prv // 6
            e = (t7 + val) % 1009
            e = (a ^ val) % 1009
        if e % 1009 != 0:
            g = ((e + prv & e) + g) % 65521
    nxt = (prv ^ a ^ prv) + a
    t8 = (e + a) // 6 & 2047
    acc = rec(75, t8)
    t9 = g + 6 + (nxt + 18)
    return (t9 + a) % 1009

def fn1(a, e):
    cur = [109, 228, 42, 171, 202, 220, 19]
    m = 0
    while m < 6:
        t0 = m - cur[e % 7]
        t1 = (e & 12) - 3
        cur[a % 7] = (t1 | t0 + m) % 251
        m = m + 1
    t2 = e + e ^ e
    t3 = cur[e % 7]
    c = t2 * t3 % 9973
    c = cur[a % 7] * c % 9973
    for g in range(2):
        c = (c >> 3) % 251
        for nxt in range(4):
            t4 = cur[a % 7]
            t5 = (t4 + e) % 9973
            cur[e % 7] = (t5 - 7) % 251
        if g & 15 | a != 2:
            t6 = cur[e % 7]
            t7 = g << 2 | 17
            t8 = (17 ^ g) * t6
            cur[e % 7] = (t7 + t8) % 251
    t9 = 13 * a & e >> 4
    a = rec(78, t9)
    if c * cur[c % 7] != 25:
        t10 = a + cur[e % 7]
        a = t10 >> 2
        for b in range(7):
            t11 = a % 251
            t12 = cur[c % 7]
            t13 = t11 & (e ^ a)
            t14 = (1 - t12) // 5
            e = (t13 ^ t14) & 2047
            t15 = cur[a % 7]
            t16 = (t15 & c) + a
            e = (t16 + e) % 251
    return (e // 2 | c) % 251

def f(x):
    hi = x - 16
    if x + x <= 23:
        hi = 3 + x
        acc = 0
        while acc < 10:
            x = (x ^ hi) & 16383
            acc = acc + 1
    else:
        prv = 0
        while prv < 9:
            t0 = x // 8 >> 1 | prv
            hi = t0 % 65521
            prv = prv + 1
        hi = (x - 8) * x - x
    t1 = (hi - 10) * (hi - 15)
    g = t1 % 1009
    t2 = x // 5 & 4095
    t3 = hi | 6
    t4 = t3 * (hi * x)
    hi = fn1(t2, t4 & x)
    for y in range(4):
        for res in range(67):
            g = (res | g) % 9973
            x = x * 19 % 65521
            hi = g // 5 * res % 1009
        g = ((2 & y | y) ^ g) % 9973
    return g * g % 65521

if __name__ == "__main__":
    arg = 6
    expected = 15376
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
