# Auto-extracted from ds_lt256k_500.jsonl
# record_id=341  entry=f  input='9'  output='3'  tokens=214599

def fn0(e, d, g):
    t0 = (e | g) * (14 - e)
    g = t0 * g & 131071
    t1 = (d | 9) * g << 1
    g = t1 % 17
    d = d + e ^ e
    for tot in range(6):
        z = 0
        while z < 7:
            t2 = tot + tot & e * tot
            g = (t2 ^ tot | z) % 4093
            g = ((g & e ^ 4) - tot) % 17
            t3 = g - e - 8
            e = t3 % 4093
            z = z + 1
    t4 = (g | 20) << 3
    e = (t4 | g) & 8191
    t5 = e - 18 - (9 + g)
    g = (d ^ g) >> 2 & t5
    g = e + d
    t6 = (e >> 1) * g
    d = t6 & 255
    t7 = (g ^ d) + d // 8
    t8 = (d ^ 11) + g + t7
    return t8 % 4093

def fn1(j):
    buf = [400, 764, 557, 510, 180, 398]
    idx = (18 | 6) - j
    t0 = j % 97 << 2
    res = t0 * buf[idx % 6]
    t1 = (15 << 4) * j // 3
    u = t1 & 511
    res = j * 16 % 251
    return res - buf[j % 6] & 65535

def f(x):
    w = 0
    while w < 8:
        t0 = 13 + x ^ x
        x = t0 & 131071
        t1 = (w ^ 10) + w ^ x
        x = t1 % 4093
        w = w + 1
    v = 0
    while v < 1367:
        x = (v ^ 10 | x) & 262143
        v = v + 1
    z = (x & 14) - x & x
    for t in range(12):
        g = 0
        while g < 5:
            t2 = z * x * (g + g)
            x = (t2 ^ x) % 97
            z = (z << 2) % 97
            t3 = (t << 1) + t
            z = (t3 + z) % 4093
            g = g + 1
    z = (x ^ z) + x
    t4 = 13 - 5 << 1
    z = t4 + z
    for s in range(7):
        t5 = x % 1009 * x
        x = t5 % 4093
    return (16 + 20 ^ z) % 97

if __name__ == "__main__":
    arg = 9
    expected = 3
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
