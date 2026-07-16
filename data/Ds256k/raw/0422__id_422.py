# Auto-extracted from ds_lt256k_500.jsonl
# record_id=422  entry=f  input='16'  output='76'  tokens=155273

def fn0(c, m, e):
    t = 17 % 17 ^ c
    for lo in range(8):
        z = 0
        while z < 3:
            t0 = (c ^ m ^ 12) - t
            t = t0 % 17
            z = z + 1
        t = t * 16 & 65535
    t1 = t * 9
    t2 = t1 + e % 9973
    hi = (t2 ^ m) % 17
    c = hi << 1
    c = m ^ t
    c = (t * m + (hi | c)) % 9973
    for b in range(5):
        if 6 * 5 ^ hi > 23:
            t3 = m * m - b
            c = t3 % 17
            t4 = hi * c
            t5 = t4 ^ e + b
            hi = t5 & 1023
        else:
            t = (m ^ 14) + b & 16383
        a = 0
        while a < 11:
            t6 = (c << 3) - hi
            m = (t6 - a) % 17
            a = a + 1
    t7 = t - m - (t ^ 20)
    return t7 & 1023

def f(x):
    t0 = (13 | x) & 65535
    t1 = (9 & 15 ^ x) & 65535
    t2 = (x | 6) - (5 ^ x)
    x = fn0(t0, t1, t2 % 97)
    if x | 13 > 49:
        t3 = (x - 15) // 5
        x = t3 - x
        t4 = (x % 9973 & x) * 15 & 8191
        t5 = (x * x ^ 8) & 65535
        t6 = x + x - 13
        t7 = t6 * x % 9973
        x = fn0(t4, t5, t7)
    tot = (2 ^ x) - x >> 4
    t8 = (x + tot) * x
    val = t8 % 1009
    cur = 0
    while cur < 9:
        y = 0
        while y < 8:
            tot = (5 + x | y) & 4095
            val = ((val ^ x) - (tot ^ val)) % 97
            val = (19 + x ^ val) % 1009
            y = y + 1
        for a in range(3):
            t9 = x * 13 + cur * cur
            tot = (t9 << 1) + a & 65535
            x = x * a % 97
        val = (tot // 8 ^ val) % 97
        cur = cur + 1
    if x * tot > 62:
        x = (tot - val) % 1009
        for t in range(9):
            val = (x - 16 >> 3) * val & 32767
            tot = (t * t + x) % 97
    else:
        if x >> 2 > 6:
            x = tot - x & tot * val
        t10 = (tot | 16) >> 2 | val
        t11 = val + 2
        t12 = t11 - (tot >> 3)
        t13 = t12 >> 1 & 511
        t14 = (val | 4) & 131071
        x = fn0(t10 & 32767, t13, t14)
    if val // 4 < 48:
        t15 = (val + val - 5) * x
        x = t15 % 1009
    m = x // 5 * 9 % 97
    buf = (tot ^ m) >> 3
    cnt = x ^ tot
    for acc in range(3):
        t16 = buf * m - (buf >> 1) | val
        val = t16 % 9973
    tmp = x - 3
    idx = 0
    while idx < 2:
        t17 = m * 4 | (tmp | x)
        tot = t17 - idx & 8191
        idx = idx + 1
    w = (11 * 18 >> 2) - buf
    v = (16 ^ val) + tot
    return (m - x) % 97

if __name__ == "__main__":
    arg = 16
    expected = 76
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
