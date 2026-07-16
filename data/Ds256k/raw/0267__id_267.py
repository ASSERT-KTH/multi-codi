# Auto-extracted from ds_lt256k_500.jsonl
# record_id=267  entry=f  input='9'  output='4093'  tokens=240567

def fn0(j):
    idx = j * j % 17
    j = idx + j
    if idx ^ 18 > 27:
        g = 0
        while g < 6:
            idx = idx * 7 & 16383
            g = g + 1
        idx = j ^ idx
    z = 0
    while z < 12:
        if j >> 2 < 21:
            j = z - idx & z
            t0 = idx + 13 + j
            j = t0 % 17
        else:
            j = (15 * z ^ idx) % 17
            idx = (idx - j >> 3) * j & 511
        for v in range(2):
            idx = ((v | 9) ^ idx) % 17
            j = v * idx & 16383
            t1 = idx << 1 & j
            j = t1 * 6 & 8191
        z = z + 1
    j = 9 ^ idx
    idx = 8 + j
    t2 = (idx >> 1) * (j | idx)
    idx = t2 * (18 * j - j) % 1009
    idx = idx // 6
    t3 = 1 + j | idx
    return t3 % 17

def fn1(g, d, m):
    t0 = d * 6 ^ 17 - d
    m = fn0((t0 ^ d) % 97)
    for y in range(9):
        t1 = (4 | g) * (g + y)
        t2 = t1 - (m + d ^ (16 | 11))
        g = t2 % 9973
        m = g + g - y & 65535
        t3 = (y ^ g) + g
        g = t3 % 1009
    cnt = 0
    while cnt < 11:
        q = 0
        while q < 7:
            t4 = g + d - (m - 6)
            d = t4 & 16383
            q = q + 1
        cnt = cnt + 1
    t5 = (m | d) * g
    m = fn0((t5 << 1) % 97)
    cur = (d >> 3) // 8
    t6 = g - m
    t7 = t6 * (cur % 17)
    g = fn0(t7 * g % 97)
    return (m & 16) - cur & 511

def f(x):
    t0 = x * x * (x ^ 6)
    t1 = (x ^ 10) + (x + x)
    q = t0 ^ t1
    lo = x - q
    t2 = x - 4
    t3 = x * x // 3
    t4 = t2 | x ^ 15
    x = t3 - t4
    q = fn0(lo * lo & 131071)
    t5 = lo // 3 * q % 65521
    t6 = q * lo + lo
    t7 = (t6 + lo) % 65521
    t8 = 12 * q
    t9 = t8 - x % 97
    t10 = t9 // 8 & 16383
    x = fn1(t5, t7, t10)
    if lo ^ x == 3:
        t11 = lo * q ^ q - 20
        x = t11 % 4093
    else:
        t12 = (q ^ lo) + (x - q)
        t13 = t12 + ((x >> 4) - 7)
        lo = fn0(t13 & 4095)
    if lo >> 3 == 24:
        t14 = q * x * lo
        t15 = t14 ^ lo // 4 - x
        lo = t15 & 65535
    else:
        x = (x - 15) % 97 - lo
    for nxt in range(12):
        t16 = x * q
        t17 = t16 + (nxt ^ 12)
        q = (t17 + q) % 65521
        a = 0
        while a < 8:
            t18 = (q // 8 | lo - 7) % 97
            x = (t18 + a) % 4093
            x = (20 ^ x) & 65535
            t19 = nxt * x
            t20 = a * 9 // 7
            t21 = t19 | a - nxt
            q = (t20 | t21) % 4093
            a = a + 1
    return (13 | q) & 32767

if __name__ == "__main__":
    arg = 9
    expected = 4093
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
