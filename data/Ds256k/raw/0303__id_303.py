# Auto-extracted from ds_lt256k_500.jsonl
# record_id=303  entry=f  input='1'  output='9'  tokens=17904

def rec(n, a):
    if n <= 0:
        return a
    t = 0
    while t < 10:
        t0 = 1 + a
        t1 = t0 ^ n - 14
        a = (t1 >> 1) % 17
        t = t + 1
    g = 0
    while g < 9:
        a = (g - 16 ^ a) % 251
        g = g + 1
    t2 = ((n & 20) - n | a) % 17
    return rec(n - 1, t2)

def fn0(g):
    if g - 2 < 16:
        g = g ^ 16
    t0 = g % 97 & g
    g = rec(42, t0)
    t1 = g ^ 13
    t2 = t1 + (g - 15)
    d = t2 & g
    for hi in range(7):
        t3 = (hi + 13 | d) // 6
        g = t3 % 1009
    return g * 9 // 8 + d & 4095

def fn1(m, e):
    t0 = 5 + m & 511
    e = rec(53, t0)
    e = fn0(m * m % 9973)
    for p in range(5):
        m = (p - m) % 9973
        t1 = m + p + p
        e = t1 % 9973
    for acc in range(3):
        e = (e & m) * e & 262143
    t2 = (m ^ 11) >> 3
    return t2 & 4095

def f(x):
    aux = [27, 84, 42, 198]
    t0 = aux[x % 4]
    t1 = t0 | x
    t2 = (x & 9) - x
    t3 = t1 + (x - 3)
    q = t2 - t3
    for c in range(5):
        t4 = 7 & aux[c % 4] | x
        q = t4 & 65535
    for s in range(18):
        t5 = ((5 ^ q) + (s - x)) // 4
        q = t5 % 17
    for nxt in range(10):
        if x - nxt > 8:
            t6 = 19 * nxt
            t7 = t6 & x + q
            aux[nxt % 4] = (t7 ^ 5) % 251
            t8 = (q >> 1) * nxt ^ 2
            aux[x % 4] = t8 % 251
        else:
            aux[x % 4] = (q + q | 1) % 251
            aux[x % 4] = (7 * q >> 1) % 251
        t9 = q - nxt
        x = t9 & q * 3
        t10 = (x ^ q) + (10 + q) - x
        x = t10 & 2047
    prv = q & 1 ^ 4 + x
    return prv + x - 20 & 1023

if __name__ == "__main__":
    arg = 1
    expected = 9
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
