# Auto-extracted from ds_lt256k_500.jsonl
# record_id=43  entry=f  input='10'  output='3485'  tokens=106126

def fn0(g, e, a):
    d = [182, 696, 413, 939, 506, 554]
    e = (a + 14) // 5 // 5
    t0 = a - e << 4
    t1 = (e - 11) * 6
    g = t0 * t1 % 251
    for z in range(6):
        for c in range(12):
            t2 = z - 1 - (c | 1)
            e = (t2 | e) & 16383
        t3 = g + e ^ a
        a = t3 % 251
        if e // 7 == 40:
            t4 = g * e * a
            e = t4 >> 2 & 8191
            t5 = 7 * 20 * z
            a = t5 + g & 65535
    t6 = a + d[e % 6]
    t7 = (8 - g) * (e << 3)
    t8 = t6 - d[g % 6]
    e = (t7 - t8) % 9973
    t9 = d[e % 6] & 3
    t10 = a // 3 - (a + e)
    t11 = t10 - (g >> 3) * t9
    return t11 & 32767

def fn1(a, e, d):
    c = [87, 71, 32, 77, 45]
    t0 = (d - 12) * d | a
    u = t0 % 251
    prv = 10 + 8 & a
    t1 = 14 - 3
    g = t1 ^ (e ^ d)
    u = prv ^ g
    for acc in range(6):
        buf = 0
        while buf < 4:
            t2 = prv & d
            t3 = t2 * (11 ^ buf)
            c[buf % 5] = t3 % 97
            t4 = (u >> 1) * a
            d = (t4 - buf) % 97
            t5 = 10 ^ d
            prv = t5 & prv * acc
            buf = buf + 1
        t6 = c[u % 5] - g % 65521
        t7 = (1 << 3 ^ 8 - acc) + t6
        u = t7 % 97
    v = 0
    while v < 3:
        a = (a - 2 ^ v) & 131071
        t8 = (v - 13) * d
        a = (t8 ^ u) % 97
        c[prv % 5] = (7 + a) % 97
        v = v + 1
    for s in range(9):
        for val in range(11):
            t9 = c[s % 5]
            t10 = c[prv % 5]
            t11 = 9 * t9
            t12 = t11 + (t10 - a)
            u = (t12 | val) % 97
            t13 = (c[u % 5] | 19) * 3
            g = (t13 ^ val) & 32767
            t14 = c[u % 5] - e
            u = (t14 >> 1) % 65521
    return (7 + a - prv) % 97

def f(x):
    for lo in range(6):
        x = x % 4093
        x = (3 - x) % 1009
        if x - 18 <= 59:
            x = ((x | 20) + lo + 3) % 4093
            t0 = (lo | 8) * (x >> 2) >> 1
            x = t0 & 511
        else:
            x = (13 ^ 10) + x & 262143
    nxt = 0
    while nxt < 7:
        x = (nxt ^ x) % 17
        x = (x ^ 14) & 16383
        x = (x ^ 12) + nxt & 131071
        nxt = nxt + 1
    if 6 << 1 ^ x > 25:
        t1 = x ^ 7
        t2 = t1 - x // 5
        t3 = x * x & 1023
        t4 = ((x | 19) >> 2) % 4093
        x = fn0(t2 & 65535, t3, t4)
        t5 = x | 12 | 4
        t6 = (x + x) % 9973
        t7 = (x + x) * (2 * 18)
        x = fn1(t5 & 4095, t6, t7 & 511)
    else:
        x = (x | 20) + 3
        t8 = x ^ 11
        t9 = t8 | 7 + 1
        x = t9 | x
    w = x // 3
    t10 = ((w >> 2) - (x ^ 7)) // 7
    t11 = x // 2 - w
    t12 = (t11 + (x + x) * w) % 1009
    t13 = x // 5 % 4093
    w = fn0(t10 & 8191, t12, t13)
    for prv in range(20):
        for tmp in range(7):
            t14 = (tmp ^ 15) - (x & prv)
            x = (t14 ^ x) % 1009
        t15 = (x ^ 7) >> 1
        t16 = t15 >> 4 | w
        w = t16 % 1009
        w = (17 + prv) * w * x & 2047
    for y in range(2):
        w = (x - 6 >> 4) + y & 2047
        w = (13 & x ^ y) % 9973
    t17 = (x - 5 - w) % 17
    t18 = x // 6 + 20
    t19 = (w >> 1) - (16 + x) & 4
    w = fn0(t17, t18 % 9973, t19)
    t20 = (7 ^ w) - x
    return t20 % 4093

if __name__ == "__main__":
    arg = 10
    expected = 3485
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
