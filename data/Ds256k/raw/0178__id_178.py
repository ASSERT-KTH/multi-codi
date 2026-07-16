# Auto-extracted from ds_lt256k_500.jsonl
# record_id=178  entry=f  input='8'  output='71'  tokens=154117

def fn0(a, d):
    val = [78, 25, 10, 96, 10, 64, 15]
    for idx in range(2):
        t0 = d % 97 - a
        a = t0 >> 2 & 511
    for buf in range(5):
        a = buf * a + 19 - 19 & 255
        for prv in range(4):
            t1 = a >> 3 ^ a // 8
            a = t1 % 4093
            t2 = buf - a + a ^ 11
            val[a % 7] = t2 % 97
            a = 19 - buf - a & 8191
    t3 = val[d % 7]
    t4 = d ^ a
    cur = t4 + (t3 ^ d)
    for acc in range(3):
        t5 = cur + acc & (a ^ d)
        t6 = 12 * cur + acc | t5
        d = t6 % 97
        for lo in range(5):
            t7 = lo & cur
            t8 = t7 - (d - 3)
            cur = t8 & 1023
        t9 = val[acc % 7] + cur
        d = ((14 ^ a) - t9) * d & 511
    t10 = val[d % 7]
    d = t10 * val[a % 7]
    d = d ^ cur
    t11 = cur + val[d % 7]
    return (t11 - (7 - a)) % 97

def fn1(g, b, m):
    t0 = g * m
    t1 = t0 ^ m + m
    b = t1 * m % 251
    if m ^ 12 >= 6:
        g = (b + 8) // 5
    else:
        g = m ^ g
        lo = 0
        while lo < 6:
            t2 = (b & m) + (b - m)
            t3 = b // 5 // 4 - t2 | g
            g = t3 % 251
            t4 = 9 * b + g
            b = t4 % 9973
            m = ((b - g | g) ^ m) % 1009
            lo = lo + 1
    for v in range(5):
        m = (b ^ v) >> 2 & 8191
        b = ((b | 15) << 4) % 251
    t5 = b * m >> 3
    t6 = (b + g - (b & m)) // 7
    g = fn0(t5 & 262143, t6 % 9973)
    g = g | m
    t7 = g // 6 % 251
    return t7 >> 2 & 4095

def f(x):
    t0 = (x - 15) * x
    nxt = t0 ^ x
    m = x * x
    t1 = nxt >> 4
    t2 = t1 + 10 * x
    t3 = (11 & x) * (19 * x % 251)
    x = fn0(t2 & m, t3 & 32767)
    t4 = (x | 15) // 7 * (nxt >> 3)
    d = t4 % 251
    for e in range(37):
        for res in range(5):
            t5 = (9 ^ d) >> 1
            d = (t5 ^ (1 + x) // 7) % 251
            t6 = x % 9973 - e
            t7 = t6 >> 4 | m
            m = t7 % 251
    q = x * d & 255
    t8 = q ^ 15 ^ 19 + x
    t9 = (t8 - 1) % 9973
    t10 = q * d % 9973
    nxt = fn0(t9, t10)
    t11 = (5 ^ x) // 7
    t12 = x * 3 + 11
    buf = t11 * t12 % 251
    return (q | m) & 8191

if __name__ == "__main__":
    arg = 8
    expected = 71
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
