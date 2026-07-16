# Auto-extracted from ds_lt256k_500.jsonl
# record_id=281  entry=f  input='9'  output='18'  tokens=200307

def fn0(a):
    c = [23, 37, 44, 92, 3, 9, 5]
    m = a % 65521
    c[m % 7] = (a | c[m % 7]) % 97
    t0 = c[m % 7]
    t1 = (11 * a | t0) // 5
    w = t1 % 4093
    if c[a % 7] >> 1 > 23:
        m = a + a
    for b in range(12):
        if (b & 1) - w > 61:
            t2 = c[m % 7]
            t3 = a + t2 - b
            a = t3 % 1009
            c[a % 7] = (a << 1) % 97
        lo = 0
        while lo < 9:
            t4 = (13 ^ 5) * a // 5
            w = (t4 | lo) & 16383
            lo = lo + 1
    for prv in range(8):
        t5 = a + w
        t6 = t5 - 14 * a
        w = t6 & 1023
        a = (w - 4 + prv | m) & 32767
    t7 = a * 7 + m
    m = t7 - (a - 14) % 4093
    for y in range(12):
        if 12 * y - m == 59:
            t8 = m // 3 * (w * 9)
            a = t8 * (y + m * m) & 32767
            t9 = (12 & w) - m
            t10 = t9 | m - 14 >> 4
            a = (t10 ^ y) & 8191
        else:
            t11 = (w ^ 5) - a
            m = t11 - m & 4095
        w = w + 2 & 511
        m = ((5 & a) - y) % 1009
    t12 = m - 1
    t13 = t12 - (w + 15)
    return t13 % 9973

def f(x):
    p = x + 17
    t0 = (x | 9) + p
    x = fn0(t0 % 1009)
    cur = x | 12
    t1 = (cur << 2) * (cur - 8)
    z = t1 * 18 % 1009
    for c in range(246):
        if z ^ c == 40:
            x = (13 - p + c) % 1009
    tmp = (p | z) & z
    if 7 + p <= 33:
        tmp = 16 << 3 ^ tmp | x
        t2 = (tmp & p) * x
        x = t2 % 1009
    m = p * tmp % 1009
    t3 = 12 - m
    t4 = t3 ^ x - 10
    m = fn0(t4 % 17)
    cur = fn0((cur - 17 | x) // 6 & 1023)
    d = x - 9
    buf = tmp * cur * (14 | cur) & 511
    g = x | cur
    m = fn0(p * x % 1009)
    a = (19 | z) + buf
    t5 = (x >> 3) * a * x
    b = t5 % 17
    return cur % 1009 & (buf ^ 18)

if __name__ == "__main__":
    arg = 9
    expected = 18
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
