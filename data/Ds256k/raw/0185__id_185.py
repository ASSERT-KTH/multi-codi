# Auto-extracted from ds_lt256k_500.jsonl
# record_id=185  entry=f  input='13'  output='63'  tokens=109120

def rec(n, a):
    if n <= 0:
        return a
    t0 = (a | 20) // 5
    y = (t0 | n) % 251
    t1 = n // 2
    t2 = t1 * (n // 4)
    a = (t2 ^ y) & 255
    t3 = (y * 15 + 3) // 5
    a = t3 - a & 32767
    t4 = a | 11
    t5 = t4 - (y << 3)
    t6 = t5 >> 3 & 16383
    return rec(n - 1, t6)

def fn0(j, e, g):
    t0 = e ^ 4 ^ j << 2
    hi = t0 + ((j ^ 5) + e)
    t1 = j - 7 + (e + hi)
    tot = t1 ^ j
    if e // 6 <= 25:
        for z in range(12):
            e = (tot * z ^ (g ^ e)) % 17
        g = e + e << 1 | hi
    else:
        tmp = 0
        while tmp < 7:
            t2 = (7 - hi) % 251 + j
            j = t2 & 8191
            g = (hi + 10 ^ g) % 17
            j = hi - e - j & 8191
            tmp = tmp + 1
    for lo in range(7):
        t3 = j - tot + lo
        j = t3 % 4093
    for s in range(9):
        u = 0
        while u < 5:
            j = (u * 19 - tot) % 251
            t4 = u + s + 6
            t5 = t4 * (11 & 14 | u)
            e = (t5 + j) % 4093
            u = u + 1
        if 4 | j > 34:
            j = (hi * e + s) % 251
        else:
            hi = hi % 17
            t6 = j * tot + 18 + g
            g = t6 % 251
        for m in range(8):
            g = g * tot & 255
            t7 = (hi & 17) - e
            e = t7 & 8191
            t8 = e - j + g
            e = (t8 >> 4) % 4093
    return (tot | j) - g & 131071

def f(x):
    idx = [90, 43, 64, 89, 0, 70]
    t0 = idx[x % 6]
    t1 = x + 8
    t2 = t1 | t0 * x
    hi = t2 - 12
    if hi >> 1 == 34:
        for w in range(9):
            x = ((19 & w) - x) % 251
        t3 = x * hi ^ hi
        x = t3 * x & 16383
    if hi * x <= 34:
        x = hi - 7
        t4 = idx[x % 6]
        hi = t4 - x
    t5 = hi + idx[hi % 6]
    t6 = t5 // 7 & 8191
    x = rec(102, t6)
    cur = (hi // 7 >> 1) // 6
    t7 = (8 | hi) - (x + cur)
    for aux in range(123):
        t8 = (hi | aux) >> 1
        x = t8 & 262143
        cur = (20 * x | cur) & 131071
    return t7 // 4 % 251

if __name__ == "__main__":
    arg = 13
    expected = 63
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
