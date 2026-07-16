# Auto-extracted from ds_lt256k_500.jsonl
# record_id=228  entry=f  input='6'  output='14'  tokens=150269

def rec(n, a):
    if n <= 0:
        return a
    t0 = n * 16 & 13
    t1 = n - a ^ 17
    v = (t0 ^ t1) & 2047
    t2 = 17 - v | n
    a = t2 % 65521
    t3 = (v * n ^ v) + a
    return rec(n - 1, t3 % 17)

def fn0(j, e):
    g = (e - 5) // 8 | 8
    t = j >> 1
    for b in range(8):
        t = (e << 4 ^ b) % 17
        buf = 0
        while buf < 12:
            t0 = (buf + 15 + e) // 6
            e = t0 & 131071
            t1 = t + e
            t2 = t1 * (e | t)
            t3 = (g ^ b) * buf
            g = t2 * t3 % 4093
            buf = buf + 1
    t4 = (j * g ^ 17) % 9973
    j = rec(32, t4)
    return (j ^ t) & 262143

def fn1(d):
    t0 = d - 17 & 255
    t1 = (d * d ^ d) & 255
    d = fn0(t0, t1)
    t2 = d - 1 & 255
    t3 = d * d + 1
    d = fn0(t2, t3 % 65521)
    t4 = 6 - d ^ 10 << 2
    buf = t4 * d & 16383
    p = buf - d >> 2
    return (buf | 14) % 65521

def f(x):
    for b in range(6):
        t0 = x ^ b
        t1 = t0 - (x & 18)
        x = t1 & x
        if b + x < 23:
            t2 = (b ^ x) * (b + x) + x
            x = t2 & 2047
            t3 = (4 ^ 5) - x
            x = t3 % 9973
        else:
            t4 = 8 - b ^ x
            x = t4 & 2047
    for aux in range(11):
        lo = 0
        while lo < 12:
            t5 = (2 - 14) * lo
            t6 = t5 * ((aux ^ lo) << 4) ^ x
            x = t6 & 32767
            t7 = 4 * x + (aux << 1)
            x = (x * lo & 4 ^ t7) & 131071
            x = aux + x & 131071
            lo = lo + 1
        if x * 14 > 59:
            x = (x | 4) * x % 17
        t8 = x << 2 & 18
        x = (t8 - aux) % 17
    m = 0
    while m < 8:
        x = m * x % 17
        x = (x << 4) // 3 % 9973
        m = m + 1
    j = x // 7
    a = (x - 7) * (x % 17) % 9973
    t9 = (j + x - 10 - 17) % 9973
    j = rec(77, t9)
    if x * 19 <= 64:
        t10 = x + j >> 1
        j = t10 | (19 ^ 12) & j
        val = 0
        while val < 10:
            j = (10 + j - j) % 17
            t11 = (a ^ val) * a
            t12 = t11 | val + val & val
            x = t12 & 4095
            val = val + 1
    else:
        t13 = (j | x) % 17
        t14 = x + a & 4095
        x = fn0(t13, t14)
        j = (x & 18) * 15 & a
    hi = 4 * x - (j - x)
    cnt = a
    return ((15 ^ 9 | j) ^ x) % 65521

if __name__ == "__main__":
    arg = 6
    expected = 14
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
