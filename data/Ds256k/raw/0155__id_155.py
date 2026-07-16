# Auto-extracted from ds_lt256k_500.jsonl
# record_id=155  entry=f  input='6'  output='112'  tokens=39837

def fn0(m):
    u = [30, 455, 733, 709, 191, 840]
    u[m % 6] = 15 * m % 1009
    s = m * m & 8191
    t0 = u[m % 6]
    t1 = 20 | m
    t2 = t1 - (t0 + m)
    t3 = m * s | s
    v = t2 - t3 & 2047
    b = 0
    while b < 12:
        t4 = u[s % 6]
        t5 = t4 * u[m % 6] // 2
        s = (t5 - s) % 1009
        t6 = u[s % 6]
        t7 = t6 * b
        t8 = t7 * (s + m)
        v = t8 & 262143
        b = b + 1
    t9 = s * m | u[s % 6]
    s = t9 & 131071
    s = s & 20
    v = s + 14
    return (v * m + m) % 1009

def fn1(d, e, a):
    if e * d != 43:
        t0 = e * e + (d & a)
        e = fn0(t0 & 16383)
        t1 = d * d >> 4
        d = t1 & 1023
    t2 = (a & 11) << 3
    t3 = 14 + a ^ e
    t = t2 * t3 % 4093
    if 2 * e < 61:
        for lo in range(4):
            t = (6 - e ^ lo) & 131071
            t4 = e // 5 >> 2 >> 3
            t = (t4 + lo) % 4093
            t = ((e ^ d) + lo) % 17
    else:
        t = fn0(d % 17)
    for u in range(3):
        if e - u > 54:
            t5 = d >> 4 >> 4
            d = (t5 + d) % 4093
            e = ((a >> 1) + u) % 4093
        else:
            t6 = (d >> 3) - t
            t7 = (d | 1) ^ d
            d = (t6 | t7) & 4095
            t = u * e & 16383
    e = fn0(d - a + e & 2047)
    for cnt in range(11):
        for val in range(9):
            t8 = (12 << 1) * t * 14
            t = t8 % 17
            e = val * e % 4093
            d = (t + t | d) % 17
        t = (d - 10 | cnt) & 2047
        g = 0
        while g < 9:
            t = ((cnt ^ g) + d) % 4093
            g = g + 1
    m = 9 + 5 + t
    t9 = (m + a) // 3
    t10 = 2 - d | 8
    tot = t9 + t10
    return 17 - a - m & 255

def f(x):
    if x * 4 < 16:
        t0 = x + x ^ 19
        x = fn0((t0 - x) % 65521)
    else:
        t = 0
        while t < 2:
            x = ((t & 15) - x) % 17
            t = t + 1
    s = x // 3 - x & x
    lo = x // 8 // 5
    z = x >> 4
    t1 = 20 + lo ^ x
    t2 = t1 | s * s + x
    acc = t2 % 17
    for tot in range(8):
        t3 = ((1 ^ 12) - (lo - 18)) // 5
        z = (t3 | z) & 8191
    idx = 0
    while idx < 7:
        t4 = lo - 19
        s = t4 & z + s
        if 9 & acc >= 1:
            lo = (idx + idx | z) % 97
        idx = idx + 1
    p = 19 * z
    for g in range(115):
        t5 = (z - 5) * p ^ g
        acc = t5 % 97
    t6 = s + s
    t7 = t6 - (2 & lo)
    return (t7 ^ p) & 1023

if __name__ == "__main__":
    arg = 6
    expected = 112
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
