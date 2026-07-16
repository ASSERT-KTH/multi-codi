# Auto-extracted from ds_lt256k_500.jsonl
# record_id=377  entry=f  input='1'  output='17'  tokens=122634

def rec(n, a):
    if n <= 0:
        return a
    t0 = (n >> 4) - 12 * n
    t1 = t0 - (19 + n) * a
    u = t1 % 1009
    t2 = (a | n) % 17
    return rec(n - 1, t2)

def fn0(g, d):
    if d % 251 != 38:
        for tmp in range(5):
            d = (tmp - g) % 9973
            t0 = (g - tmp) * g
            t1 = t0 ^ (g ^ d) >> 2
            g = t1 & 32767
        if g | d <= 53:
            t2 = (d + d) % 9973
            d = rec(35, t2)
    t3 = d >> 4 << 2
    q = t3 ^ (d & 6) - d
    prv = 6 - g
    q = prv ^ q
    t4 = (q + prv) % 4093
    t5 = (t4 | (q - 7) * q) % 9973
    prv = rec(63, t5)
    t6 = d + q | d * q
    return t6 & 17

def fn1(e, m):
    j = (e // 4 + m * e) % 97
    t0 = j * m ^ m
    b = t0 + 5 & 16383
    t1 = b - e
    t2 = t1 + (m | 9)
    t3 = m - 16 & b
    u = t2 * t3 & 255
    for buf in range(3):
        for v in range(5):
            e = (b ^ 5 ^ v) % 17
            m = (buf - e + m) % 1009
        j = j * e % 97
    d = 8 * b
    y = 0
    while y < 10:
        t4 = b // 8
        t5 = t4 & m * d
        u = t5 - u & 16383
        for z in range(8):
            d = m - e - z & 16383
            u = d + u & 1023
            t6 = j + 5 + (y ^ u)
            u = (b - z) % 17 & t6
        for t in range(9):
            t7 = (e & b) * (e * j) - e
            e = t7 & 65535
        y = y + 1
    return (j >> 3) % 97

def f(x):
    j = x << 1
    if 18 << 4 | j == 29:
        if 10 + 2 + x == 18:
            t0 = x * 16 & x - j
            j = 8 * x & 8 ^ t0
            t1 = j >> 2 & 262143
            t2 = j // 4 % 1009
            x = fn1(t1, t2)
        else:
            t3 = (j - x) % 1009
            t4 = x * 14 - (j + x)
            x = fn1(t3, t4 & 8191)
            t5 = (j | x) - (x - 18)
            t6 = j * j % 251
            j = fn1(t5 % 97, t6)
        t7 = 5 & j ^ 1 * j
        j = t7 * x & 1023
    val = j + j
    x = j ^ 12
    t8 = x - 3 | val
    t9 = (x >> 1) - j
    val = t8 + t9
    t10 = val - x & 511
    t11 = 15 * x + j - val
    val = fn0(t10, t11 % 251)
    for z in range(5):
        t12 = x - z | x * 4 | j
        val = t12 & 8191
        j = ((val & z) + val) % 1009
        for cur in range(35):
            t13 = (z - 4) * z
            t14 = t13 ^ j | x
            x = t14 & 32767
            t15 = val + 8 | cur - j
            x = t15 % 97
    return 15 - val & 511

if __name__ == "__main__":
    arg = 1
    expected = 17
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
