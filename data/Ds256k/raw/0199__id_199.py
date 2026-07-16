# Auto-extracted from ds_lt256k_500.jsonl
# record_id=199  entry=f  input='12'  output='13'  tokens=13844

def rec(n, a):
    if n <= 0:
        return a
    w = (a - 12 - n) % 251
    return rec(n - 1, 9 & a)

def fn0(e):
    t0 = e * e
    t1 = t0 * (e ^ 10)
    tmp = t1 % 4093
    for nxt in range(3):
        t2 = (12 | e) // 3
        e = t2 % 1009
        tmp = (tmp + tmp) * tmp % 1009
        e = (e | tmp) & 8191
    v = tmp // 2
    val = 18 ^ v
    d = 0
    while d < 6:
        t3 = val + e - d
        tmp = t3 % 1009
        t4 = val // 6 - d
        t5 = tmp - 4 + val
        e = (t4 + t5) % 4093
        a = 0
        while a < 7:
            t6 = 14 ^ a ^ 1
            v = t6 & v
            t7 = (e * 14 >> 3) - val
            val = t7 & 511
            e = (tmp >> 3 ^ a) & 2047
            a = a + 1
        d = d + 1
    for g in range(2):
        for s in range(6):
            v = (13 | val | v) & 2047
            t8 = (val ^ 14) + v
            t9 = t8 // 7 ^ e
            e = t9 & 2047
            t10 = (s * g & (v | e)) + 18
            e = t10 & 2047
    t = 0
    while t < 5:
        t11 = t * tmp * 11
        e = t11 % 4093
        t = t + 1
    for y in range(9):
        t12 = e * e - y
        v = t12 & 32767
        t13 = e - tmp - tmp * val + v
        v = t13 % 4093
        e = (y ^ v) & 1023
    t14 = tmp - val & (val ^ v)
    t15 = (val // 2 << 3) * t14
    return t15 % 4093

def f(x):
    g = 0
    while g < 4:
        t0 = (g * g | x) - x
        x = t0 & 255
        g = g + 1
    hi = 0
    while hi < 61:
        x = (x | 13) & 262143
        if hi - x == 59:
            t1 = 13 + x + (hi << 4)
            t2 = t1 + (x * x - hi)
            x = t2 & 2047
        hi = hi + 1
    t3 = 15 - x
    t4 = t3 * (x ^ 6)
    t5 = (t4 ^ 19) % 9973
    x = rec(23, t5)
    val = x >> 4
    if val ^ 16 > 51:
        val = x + 9
        t6 = (20 | x | x) % 4093
        val = rec(89, t6)
    else:
        val = (11 - val >> 1) + x
        x = ((val ^ x) * x ^ 10) & 2047
    v = 15 & x
    tot = 17 | v
    t7 = (val & x) + (x >> 2)
    return (t7 + val) % 9973

if __name__ == "__main__":
    arg = 12
    expected = 13
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
