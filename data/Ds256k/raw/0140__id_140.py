# Auto-extracted from ds_lt256k_500.jsonl
# record_id=140  entry=f  input='3'  output='894'  tokens=255575

def rec(n, a):
    if n <= 0:
        return a
    t0 = (n - a) * a
    a = t0 - n & 2047
    t1 = (a ^ 15) * (a ^ 5)
    t2 = t1 * ((n | a) // 8) % 251
    return rec(n - 1, t2)

def fn0(b, d, m):
    for y in range(4):
        b = (m * y ^ b) % 17
        for hi in range(9):
            t0 = 18 * 1 - (hi & 17)
            t1 = (hi & 12) - b ^ t0
            d = t1 % 9973
    if m << 2 != 53:
        m = (m * b - (d - m)) % 9973
        tot = 0
        while tot < 6:
            t2 = m >> 1 ^ d + 14
            d = (t2 ^ m * tot - 10) % 9973
            tot = tot + 1
    else:
        buf = 0
        while buf < 2:
            t3 = m * 19 - d
            d = t3 % 9973
            t4 = b // 8 - m
            m = t4 % 17
            buf = buf + 1
    t5 = 5 & 19 | b
    d = rec(110, t5 % 1009)
    lo = 0
    while lo < 10:
        for c in range(2):
            t6 = m % 9973 + c
            d = t6 & 2047
            t7 = (m + d) // 3
            b = t7 + c & 32767
            d = (c - 9) * lo - m & 255
        lo = lo + 1
    m = (d - b) * 11 & 255
    t8 = m // 3 // 2 >> 2
    return t8 & 2047

def fn1(c, a):
    t0 = (c ^ a) % 9973
    t1 = (14 | a) % 65521
    t2 = 6 | c
    t3 = c * c - a
    t4 = t2 + (a | 17)
    t5 = (t3 + t4) % 9973
    a = fn0(t0, t1, t5)
    if c >> 4 <= 59:
        for d in range(2):
            t6 = (19 + a | c) * d
            a = t6 % 9973
            t7 = c & 3 ^ 5
            t8 = 15 + d << 4
            c = t7 - t8 & 2047
        t9 = c << 2
        a = t9 + (a >> 3)
    else:
        c = a - c & 3
        g = 0
        while g < 4:
            a = (g ^ a) & 131071
            g = g + 1
    t10 = ((c + 3) * 4 | a) % 9973
    t11 = (a | 13) & 255
    t12 = (c ^ a) - (c - 8) & 4095
    a = fn0(t10, t11, t12)
    t13 = a - 1
    t14 = t13 + a * a
    val = (t14 + 4) % 9973
    for nxt in range(2):
        for z in range(7):
            t15 = 17 + c - z
            val = t15 % 65521
        t16 = 15 * val + (a | val)
        c = ((val + val) * t16 + nxt) % 65521
        a = nxt * val % 9973
    t17 = 1 + a + a + val
    return t17 & 1023

def f(x):
    t0 = x * 16 + (x - 19)
    s = t0 + (x - 4 ^ x)
    for z in range(8):
        t1 = (10 | s) // 2 * s
        x = (t1 ^ x) & 131071
    for idx in range(5):
        s = (x & 12 | 4 - s) & idx
        for nxt in range(203):
            s = (idx - x ^ s) % 65521
            t2 = x >> 2 | nxt
            s = t2 % 65521
    if s & x < 35:
        t3 = x + x ^ x >> 2
        s = t3 ^ 7
        if x * s == 35:
            t4 = (x + x & 8) * s % 251
            s = rec(83, t4)
        else:
            t5 = 13 << 4 << 4
            x = (t5 ^ s) % 97
            s = (s - x ^ s) % 251
    else:
        t6 = x * 9 + (15 + s)
        t7 = t6 * s % 251
        x = rec(83, t7)
    c = (s + s) * (x + s) % 65521
    t8 = (5 + x) * x % 9973
    return (t8 - s) % 9973

if __name__ == "__main__":
    arg = 3
    expected = 894
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
