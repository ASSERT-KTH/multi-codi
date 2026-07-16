# Auto-extracted from ds_lt256k_500.jsonl
# record_id=432  entry=f  input='11'  output='947'  tokens=81729

def rec(n, a):
    if n <= 0:
        return a
    for j in range(2):
        w = 0
        while w < 8:
            t0 = j * a
            t1 = t0 & 7 << 2
            a = t1 << 4 & 131071
            t2 = w * n // 7
            t3 = (t2 | w) - a
            a = t3 % 17
            w = w + 1
    t4 = a ^ 3 ^ n
    t5 = t4 >> 1 & 8191
    return rec(n - 1, t5)

def fn0(d, j):
    if d & 14 != 9:
        t0 = j ^ 3
        t1 = t0 ^ d + d
        j = t1 // 8
    d = d - 8 + (j >> 2)
    if j >> 4 <= 55:
        if j + d <= 21:
            t2 = d + 1 & 1023
            j = rec(73, t2)
            t3 = (d ^ 8) % 251
            d = rec(94, t3)
        else:
            j = j - 4 + d ^ j
            t4 = d >> 1 & 131071
            d = rec(114, t4)
    t5 = 4 * j
    t6 = t5 - (j << 3)
    d = t6 % 65521
    m = 0
    while m < 10:
        j = d % 251 - j & 1023
        if 13 | d != 58:
            t7 = (j >> 2) + 6
            d = t7 & (m & 7) + d
        j = (15 & j ^ 1) % 97
        m = m + 1
    d = 16 + d
    d = 18 - j - d
    if j >> 3 > 1:
        if 13 ^ j <= 28:
            d = (4 - j) // 4
        else:
            t8 = d + j - (j + j)
            d = t8 - (12 ^ d) * 13 & 1023
    else:
        t9 = (j & 8) - (d + 10)
        t10 = t9 - ((j ^ d) - (j >> 2))
        j = rec(28, t10 % 251)
        lo = 0
        while lo < 6:
            t11 = d - 3 - lo
            j = t11 % 251
            lo = lo + 1
    t12 = (d >> 4) - d
    return (t12 >> 2) % 1009

def f(x):
    z = x
    for idx in range(41):
        z = (idx + z) * z & 511
        for b in range(8):
            t0 = (z | idx) - x
            x = t0 & 4095
            z = ((15 ^ 17) - x ^ b) % 1009
        z = (z - 19) % 251
    m = 17 ^ x ^ 6 | 5
    for nxt in range(4):
        t1 = 7 - x << 2
        x = t1 & 262143
        if 13 * nxt - x > 62:
            t2 = m & x
            t3 = t2 - (17 - 12)
            m = t3 & 8191
    tot = 0
    while tot < 4:
        for g in range(6):
            t4 = x // 6 + (tot ^ 6)
            z = (t4 - z) % 251
            x = (tot - g | z) % 4093
            t5 = (m + g) % 1009
            z = t5 + ((4 << 4) + z) & 4095
        z = (x ^ tot) % 4093
        tot = tot + 1
    t6 = (x | 4) ^ z
    return (t6 - ((14 ^ x) + 20)) % 1009

if __name__ == "__main__":
    arg = 11
    expected = 947
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
