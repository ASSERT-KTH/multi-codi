# Auto-extracted from ds_lt256k_500.jsonl
# record_id=413  entry=f  input='16'  output='352'  tokens=230654

def fn0(c, m, g):
    hi = [85, 51, 54, 44, 22, 60, 54, 65]
    t0 = hi[c % 8] & 8
    g = (t0 & g) << 4
    if m - 10 == 59:
        for cur in range(11):
            t1 = 15 & g
            t2 = t1 * (m // 7)
            c = t2 + c & 262143
    else:
        t3 = hi[g % 8]
        t4 = t3 | hi[m % 8]
        m = t4 >> 1
        t5 = (m >> 4) - c
        g = t5 // 7
    if g ^ 15 < 12:
        c = g ^ 17
    v = 0
    while v < 8:
        t6 = (14 ^ c) // 6
        t7 = (v + g) * g
        c = (t6 + t7) % 97
        g = (m + g) % 97
        aux = 0
        while aux < 11:
            c = ((9 ^ aux) - m) % 4093
            t8 = (aux ^ v) + v
            hi[g % 8] = (t8 - m) % 97
            aux = aux + 1
        v = v + 1
    t9 = 15 * c - c
    c = t9 % 97
    m = c * c % 4093
    t10 = (c << 2) % 4093
    m = t10 * g % 97
    if 20 ^ g != 5:
        if 3 * m != 39:
            t11 = 3 + hi[c % 8]
            g = (12 << 1) * t11
            hi[m % 8] = ((2 | c) & 2047) % 97
        t12 = hi[m % 8]
        t13 = m & 19
        c = t13 + t12 // 2
    return (c << 4) % 4093

def f(x):
    if x * x != 2:
        x = 11 - x
        x = x - 8
    else:
        t0 = (14 | x) - (x ^ 18)
        x = (x - 10) * t0
        if x - 8 < 43:
            t1 = (x - 14) % 65521
            t2 = x << 2 & 131071
            t3 = (x * 3 | x) & 32767
            x = fn0(t1, t2, t3)
        else:
            t4 = (x | 10) - x & 1023
            t5 = (x ^ 7) % 9973
            t6 = x * x - x
            t7 = t6 * 2 % 65521
            x = fn0(t4, t5, t7)
            t8 = 16 * x % 9973
            t9 = 18 * x * (x // 8)
            t10 = (x - 9) % 9973
            x = fn0(t8, t9 % 65521, t10)
    p = x + 15
    t11 = (13 - p) % 4093
    t12 = (t11 >> 1) % 9973
    t13 = (16 - x) // 5
    t14 = (t13 + x * p * x) % 65521
    t15 = x - p + (x + 11)
    p = fn0(t12, t14, t15 % 65521)
    nxt = 0
    while nxt < 5:
        c = 0
        while c < 5:
            t16 = p - 19
            t17 = t16 - (c ^ 4)
            x = t17 % 9973
            p = (8 ^ c | p) & x
            c = c + 1
        p = (nxt + p) % 9973
        g = 0
        while g < 9:
            t18 = (p + nxt) // 3
            p = t18 * x & 2047
            g = g + 1
        nxt = nxt + 1
    v = p // 6
    if 1 * 1 | x == 52:
        for tot in range(3):
            t19 = (x | p) + p
            x = (t19 >> 2) % 9973
            p = (p - x) % 4093
        p = (v + 6 | x) & x
    d = (v >> 1) - x
    t20 = (v + d) % 65521
    idx = t20 % 9973
    for cnt in range(7):
        p = (p * cnt ^ v) % 4093
        t21 = (d - x) // 6
        t22 = (4 & idx) - x
        d = t21 - t22 & 255
    if d + idx < 35:
        t23 = (v >> 1) - p
        idx = t23 | idx >> 4 << 4
        t24 = p >> 3 ^ d
        v = t24 & 2
    s = 14 & p
    t25 = (p + 6) % 9973
    t26 = (x | 8) & 65535
    t27 = (d << 1) % 65521
    d = fn0(t25, t26, t27)
    for tmp in range(5):
        t28 = idx // 7 ^ tmp
        x = t28 // 7 & 4095
        t29 = 9 - idx
        t30 = t29 * (p ^ idx)
        p = t30 // 7 & 511
    for u in range(51):
        t31 = d * v & (u | 4)
        idx = (t31 | 20 ^ s) & 16383
    buf = 20 & s + x
    if s | v <= 40:
        d = p % 65521 - buf
        hi = 0
        while hi < 4:
            t32 = (v // 5 ^ s) << 2
            buf = (t32 | buf) & 511
            hi = hi + 1
    else:
        t33 = s + d ^ idx
        t34 = (idx | p) & 2047
        t35 = buf // 6 | idx
        t36 = t35 + (p + s) % 4093
        idx = fn0(t33 & 511, t34, t36 % 9973)
    return (d & v | idx) % 4093

if __name__ == "__main__":
    arg = 16
    expected = 352
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
