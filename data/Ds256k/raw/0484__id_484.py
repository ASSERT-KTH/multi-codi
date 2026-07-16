# Auto-extracted from ds_lt256k_500.jsonl
# record_id=484  entry=f  input='17'  output='26'  tokens=203554

def rec(n, a):
    if n <= 0:
        return a
    a = (n - 2 ^ a) % 4093
    a = (12 + a) * (n * a) & 16383
    v = 0
    while v < 2:
        a = n * v - a & 1023
        a = (n + v - a) % 65521
        a = n * a % 4093
        v = v + 1
    t0 = (a & 18) - a + n
    return rec(n - 1, t0 % 65521)

def fn0(e, c, m):
    t0 = m + e ^ (m ^ c)
    t1 = t0 * ((m & 1) - (m + e))
    v = t1 % 17
    t2 = m + e + e
    t3 = 1 * v | m
    t4 = (t2 - t3) % 1009
    m = rec(53, t4)
    c = c % 97 * v
    if c % 9973 == 29:
        t5 = v - 16 & 4095
        m = rec(118, t5)
        e = 20 - e
    if 20 - 18 | m > 49:
        t6 = v + m + c
        e = t6 >> 1
        c = v + c
    else:
        for res in range(5):
            e = (v << 2 | res) & 4095
            t7 = (9 - res) * e * m
            v = t7 % 1009
            t8 = c ^ v ^ res
            v = t8 & 131071
    return 20 * c - v & 8191

def f(x):
    c = [165, 64, 0, 189, 201, 80]
    w = 5 + 6 + x
    if x - w > 32:
        t0 = 12 - c[w % 6] & 262143
        w = rec(96, t0)
        for val in range(3):
            c[val % 6] = x & 18 | x ^ 16
    if 12 & w > 2:
        w = (w & 11) << 3 << 1
    else:
        w = x ^ 17
        for cnt in range(10):
            x = (x | w) >> 2 & 32767
            t1 = w // 7 | x
            x = t1 & 4095
            t2 = c[x % 6]
            x = (t2 - x) % 97
    c[w % 6] = (12 - x) % 251
    t3 = x - 1 | w
    t4 = w * 3 * 17
    t5 = (t3 - t4) % 251
    w = rec(63, t5)
    t6 = (c[w % 6] - 8) * w
    t7 = (t6 ^ x) & 1023
    w = rec(60, t7)
    t8 = x * w + (w - 7)
    d = x // 6 + 8 + t8 & 65535
    t9 = c[d % 6]
    for v in range(11):
        a = 0
        while a < 23:
            c[w % 6] = (8 + w) % 251
            t10 = (a & 13) * v
            w = t10 + d & 131071
            a = a + 1
        x = (x | v) & 65535
    return t9 // 3 % 65521

if __name__ == "__main__":
    arg = 17
    expected = 26
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
