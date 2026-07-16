# Auto-extracted from ds_lt256k_500.jsonl
# record_id=85  entry=f  input='12'  output='1684'  tokens=225796

def fn0(a):
    aux = [699, 675, 268, 342, 788, 646, 907, 488]
    g = a - 8
    for s in range(11):
        a = a >> 1 & 2047
    aux[g % 8] = g & 7
    e = a // 5 & g & g
    g = e ^ 10
    t0 = aux[g % 8]
    a = 4 * t0
    t1 = aux[e % 8] ^ e | e
    return 6 * e % 251 * t1 % 4093

def fn1(e):
    p = 8 & e
    if 14 + p >= 9:
        t0 = 16 + e
        e = t0 & 12 + e
    else:
        t1 = (e & 4) + e
        e = fn0(t1 & 131071)
    for g in range(5):
        t2 = 4 * g
        t3 = (e + 13) // 4
        t4 = t2 * (e - g)
        e = (t3 ^ t4) % 17
        e = (e | 2) % 1009
    z = e | 10
    c = p * p - e
    t5 = e & 2 & 19
    t6 = t5 - (z + c) % 97
    return t6 % 65521

def f(x):
    if x & 16 >= 3:
        for q in range(10):
            x = q + 3 + x & 255
            t0 = 20 | x
            t1 = q + q & q
            t2 = t0 & q * 4
            x = t1 + t2 & 1023
    else:
        x = (x << 2) - x
    for c in range(11):
        x = (c - x) % 9973
        t3 = c | x
        t4 = t3 - (x >> 3)
        x = t4 & 8191
    g = 0
    while g < 3:
        x = (x >> 2) % 9973
        t5 = 6 * g + (g << 2)
        x = (t5 - x) % 17
        x = x % 4093
        g = g + 1
    t6 = x + x
    idx = t6 ^ 20 + x
    d = (x & 8) + idx
    t = idx + x
    for v in range(5):
        if t >> 1 > 30:
            t = (idx >> 4 ^ v) % 4093
        else:
            d = (4 | idx) & 1 - v
        for tmp in range(7):
            x = ((x * tmp & d) - d) % 4093
            t7 = x // 8 - tmp
            t = t7 & 1023
            t8 = t & 4 & 14
            x = (t8 - (x + v << 4)) % 4093
    if (17 << 4) - x <= 7:
        for val in range(3):
            t = ((t + val) * d + 2) % 4093
            t = (idx * x | t) % 17
        t = x + idx >> 2 ^ 10
    else:
        for u in range(8):
            idx = (6 | idx) % 17
            t9 = (idx | 18) * 6
            idx = t9 % 17
            t = idx - 8 + t & 2047
        if idx + 19 == 9:
            t10 = x ^ idx
            t11 = t10 * (d * d)
            t = fn1(t11 * 4 % 1009)
    hi = 18 * x
    buf = 19 & t
    if buf << 2 < 24:
        x = fn0((buf & d) * idx & 8191)
    for aux in range(6):
        b = 0
        while b < 41:
            t12 = t // 4 // 8 ^ b
            x = t12 % 4093
            t13 = (11 + d ^ d * aux) - buf
            buf = t13 % 1009
            b = b + 1
        d = (hi ^ buf) * aux % 9973
    prv = (d << 2) - idx
    tot = x + t
    w = t - tot
    t14 = (hi >> 3) * (7 * d)
    return (t14 ^ tot) % 4093

if __name__ == "__main__":
    arg = 12
    expected = 1684
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
