# Auto-extracted from ds_lt256k_500.jsonl
# record_id=6  entry=f  input='14'  output='33'  tokens=183669

def rec(n, a):
    if n <= 0:
        return a
    a = ((n >> 4) - 4 - a) % 1009
    t0 = (n + n & (n | 19)) - a
    a = t0 % 251
    t1 = (19 ^ n | a) % 251
    return rec(n - 1, t1)

def fn0(j):
    w = j * j % 65521 | j
    u = 0
    while u < 9:
        y = 0
        while y < 3:
            t0 = u - y ^ y + u
            j = (t0 | u) + w & 1023
            y = y + 1
        t1 = j * 4 // 2
        w = t1 * u & 8191
        u = u + 1
    t2 = 7 ^ w
    g = t2 ^ j - w
    if w * w == 2:
        if j & g == 40:
            t3 = w * w >> 3
            j = t3 // 7 % 65521
        else:
            g = g * g & 131071
        for buf in range(4):
            w = ((g << 1) - w) % 65521
            t4 = g + 19 - (6 ^ j)
            g = t4 - j & 8191
            w = (g + 6 ^ buf) & 8191
    else:
        w = g * g & 255
        for e in range(9):
            g = (13 - w | e) & 32767
            w = (w - e + w) % 65521
    t5 = (g * g ^ w) << 3 & 4095
    j = rec(70, t5)
    c = 7 ^ 2 | g
    c = w + g
    t6 = w + 19
    t7 = t6 - (g + g)
    return t7 // 6 & 255

def fn1(j, e):
    for b in range(3):
        t0 = b + b | (b | 13) | j
        j = t0 & 255
    if j >> 1 == 46:
        t1 = j ^ 2
        j = t1 + (j - 3)
        t2 = 16 - 6 - e
        e = rec(69, t2 % 9973)
    else:
        e = (9 + 7) * (e % 251) >> 1
    t3 = 2 + e | e
    q = t3 - 2
    if 4 ^ q == 12:
        u = 0
        while u < 11:
            t4 = e ^ 9 | j
            j = t4 % 251
            j = u + j + q & 2047
            u = u + 1
    else:
        for val in range(9):
            t5 = 13 ^ val ^ q
            j = t5 & 2047
            t6 = (q - val) * (7 & e)
            q = t6 * val & 2047
            t7 = 19 << 4 | q
            e = (t7 ^ e) % 97
        j = e % 251 + q
    for cnt in range(3):
        for z in range(11):
            q = z - j - j & 255
            t8 = (cnt | j) - q + cnt
            q = t8 & 2047
            t9 = (16 + z) * z | e
            j = t9 % 4093
    t10 = (20 ^ j) * (2 ^ q)
    y = t10 & 2047
    return (19 + q) % 251

def f(x):
    hi = x - 18
    t0 = hi * x * (x ^ 9)
    t1 = ((x & hi) + hi) * t0
    m = t1 & 65535
    t2 = (x ^ 13) - x
    q = t2 * 8
    if 15 - q >= 3:
        m = hi - m + x << 3
    else:
        if x + hi >= 13:
            q = (hi + q | 6) + q
            t3 = 2 + q >> 1 | q
            x = fn0(t3 & 8191)
    tot = 0
    while tot < 8:
        if q // 2 > 26:
            t4 = x // 6 & 15
            t5 = (t4 | q) ^ tot
            m = t5 % 1009
        else:
            q = x - 3 + hi - q & 65535
        for u in range(57):
            x = (20 + q ^ x) % 1009
            t6 = (tot & 20 & tot) - hi
            m = (t6 ^ m) % 65521
        tot = tot + 1
    t7 = (q + x) % 1009
    t8 = (m - 1 - x - 4) % 97
    x = fn1(t7, t8)
    t9 = 12 - m - (x - 10)
    aux = (m >> 3) // 2 + t9
    t10 = q + aux - q >> 2
    return t10 % 97

if __name__ == "__main__":
    arg = 14
    expected = 33
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
