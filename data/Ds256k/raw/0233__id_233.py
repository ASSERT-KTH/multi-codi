# Auto-extracted from ds_lt256k_500.jsonl
# record_id=233  entry=f  input='11'  output='7'  tokens=50352

def rec(n, a):
    if n <= 0:
        return a
    t0 = 4 + n - n
    aux = (t0 | (a + n) % 1009) & 8191
    aux = (aux - a ^ aux) & 2047
    if a + 2 != 12:
        for g in range(5):
            t1 = aux // 3 ^ aux
            aux = t1 + n & 131071
            t2 = (g - aux) * (g ^ a)
            a = (t2 + 15) % 17
            t3 = a * g + n // 6
            a = (g ^ 4 ^ n) - t3 & 4095
    else:
        aux = (a // 3 | aux) & 131071
    t4 = 8 - a & 65535
    return rec(n - 1, t4)

def fn0(c, m):
    e = [136, 197, 149, 154, 248]
    t0 = e[c % 5] - c
    t1 = (m + m) * (m | 5)
    y = ((m >> 4) + t0 + t1) % 97
    b = 0
    while b < 9:
        t2 = e[b % 5]
        t3 = (b ^ t2) >> 3
        m = (t3 | m) % 97
        m = (y - 8 + (m - c)) % 97
        b = b + 1
    for idx in range(5):
        c = ((y ^ 19) + idx) % 97
        for lo in range(6):
            e[m % 5] = c // 5 % 251
            t4 = y & e[y % 5]
            t5 = (t4 & 19) * y - c
            c = t5 & 262143
            e[idx % 5] = ((c ^ y) + y) % 251
        t6 = e[y % 5] ^ idx
        m = t6 & 4095
    t7 = (15 & 18 | m) & 262143
    m = rec(69, t7)
    if c - y != 18:
        for t in range(9):
            t8 = e[m % 5] + c
            t9 = y // 3 + c
            t10 = t9 * (t8 + (m ^ 3))
            m = t10 % 251
            t11 = t * m >> 4
            e[y % 5] = (t11 ^ c) % 251
            t12 = e[m % 5]
            t13 = t12 * 17
            t14 = t13 * (t * t)
            m = t14 & 4095
    else:
        if c + y == 46:
            e[y % 5] = (m - c - (c ^ y)) % 251
            e[c % 5] = (1 + 1 + m ^ y) % 251
        else:
            t15 = m - y & e[y % 5]
            y = t15 - (m // 5 ^ c)
    t16 = 3 << 1
    t17 = t16 + 5 * 7
    tmp = t17 | c
    return (tmp | m | tmp * 4) & 14

def fn1(m):
    c = m % 17
    t0 = (m ^ c) * (m // 2)
    t1 = t0 - (m ^ 1) // 4
    t2 = c * c ^ c
    m = fn0(t1 & 131071, t2 & 262143)
    t3 = 3 * c + c
    m = t3 >> 1
    c = (m | c) ^ c << 3
    t4 = (20 * c + c) % 4093
    t5 = ((c | 2) & 7) * 19
    m = fn0(t4, t5 % 251)
    c = 4 * 2 | c
    t6 = m ^ 9 ^ m - 1
    m = (m - 20 >> 2) + t6
    m = (16 | c) * (c & 20) & m
    return (m - 4 | c) % 4093

def f(x):
    hi = [39, 83, 38, 101, 101]
    y = x << 2
    x = y * x
    y = y + x + y
    hi[x % 5] = (hi[x % 5] + x) % 251
    q = 0
    while q < 6:
        if y ^ q >= 38:
            t0 = hi[y % 5]
            t1 = t0 >> 4 ^ 19
            t2 = (q | 14) - x
            hi[q % 5] = t1 & t2
            t3 = hi[q % 5] >> 4
            t4 = (6 ^ q) + (y & 17)
            hi[y % 5] = t4 * (y // 3 + t3) % 251
        else:
            hi[y % 5] = x % 251 >> 1
            t5 = ((q | 2) - (5 ^ 7)) * y
            x = t5 & 1023
        t6 = hi[q % 5]
        t7 = x * q
        t8 = t7 - (t6 << 1)
        y = t8 % 251
        t9 = 7 << 4 ^ x
        x = t9 % 251
        q = q + 1
    for lo in range(20):
        t10 = y - x & x
        t11 = (5 | 10) << 3
        y = t10 * t11 % 251
        t12 = hi[lo % 5]
        t13 = t12 * x
        t14 = hi[lo % 5]
        t15 = t13 + (x << 3)
        t16 = (t14 + x) * lo
        y = (t15 + t16) % 251
        if lo - 4 ^ y > 45:
            t17 = hi[y % 5] + x
            hi[y % 5] = t17 % 251
    t18 = (x ^ 6) - 18
    t19 = t18 * (16 - 20 << 1)
    return (t19 + y) % 17

if __name__ == "__main__":
    arg = 11
    expected = 7
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
