# Auto-extracted from ds_lt256k_500.jsonl
# record_id=165  entry=f  input='12'  output='3535'  tokens=109769

def rec(n, a):
    if n <= 0:
        return a
    buf = (a + n ^ 19) & 262143
    buf = buf & 13
    t0 = buf + buf >> 2
    t1 = t0 * buf + a
    a = t1 % 9973
    t2 = buf % 1009 // 5
    t3 = (t2 + a) % 251
    return rec(n - 1, t3)

def fn0(g, e, a):
    y = [912, 107, 936, 346]
    for lo in range(2):
        if g >> 2 <= 44:
            t0 = y[e % 4] | 2
            g = lo * (t0 ^ e + g) & 511
            t1 = (g >> 4) + a
            a = t1 % 17
        t2 = e - g ^ (17 ^ e)
        g = (t2 ^ lo) % 65521
    s = a * a % 251
    s = (e - 14 | g // 8) & 10
    s = e + 6
    for buf in range(8):
        t3 = (14 ^ s) - s
        s = t3 & 1023
    t4 = y[e % 4]
    t5 = a // 5
    t6 = t5 | t4 * 11
    g = t6 + a
    t7 = 3 * y[e % 4] - s
    return t7 & 255

def f(x):
    m = [46, 28, 63, 91, 74, 46, 81]
    q = 0
    while q < 8:
        t0 = q * q - x
        x = (t0 - ((x | q) & x)) % 97
        x = q - x & q
        q = q + 1
    d = x - 2 ^ x + x
    t1 = x ^ d ^ 7 - d
    lo = (d + x >> 2) * t1
    acc = 0
    while acc < 25:
        for v in range(11):
            t2 = acc << 2 ^ lo
            x = (t2 | v) % 97
        if d & 7 != 3:
            t3 = 4 + x - acc * d
            x = t3 % 4093
            t4 = m[lo % 7] & x
            t5 = x * d | 9 * d
            d = t4 + 9 * lo - t5 & 255
        else:
            t6 = (2 | acc) ^ d // 3
            t7 = t6 * m[acc % 7]
            x = t7 & 255
            t8 = 4 - 13 + acc * d
            x = t8 - lo & 4095
        acc = acc + 1
    b = 16 - x
    aux = (b - 6) % 4093
    return (aux | d) % 4093

if __name__ == "__main__":
    arg = 12
    expected = 3535
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
