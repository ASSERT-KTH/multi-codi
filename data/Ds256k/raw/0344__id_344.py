# Auto-extracted from ds_lt256k_500.jsonl
# record_id=344  entry=f  input='4'  output='0'  tokens=69089

def rec(n, a):
    if n <= 0:
        return a
    if n // 4 | a > 56:
        a = (19 | a) % 65521
    t0 = ((4 ^ 13) << 4) - a
    return rec(n - 1, t0 & 1023)

def fn0(e, a, g):
    idx = a << 1
    t0 = g + g
    t1 = t0 - a * 11
    a = (t1 << 2) % 65521
    t2 = (g >> 3) - (a ^ idx)
    t3 = (t2 + a) % 65521
    g = rec(108, t3)
    if e + g >= 52:
        a = idx % 9973 // 4 * 1
        g = g + idx
    if a - g == 64:
        for b in range(6):
            t4 = b * idx
            t5 = g >> 3 ^ e
            t6 = t4 | g * 17
            e = t5 - t6 & 262143
            t7 = g | 11
            t8 = t7 * (a + b)
            idx = t8 * a & 32767
        for tmp in range(12):
            t9 = (6 - idx) % 9973 // 3 + a
            a = t9 % 9973
            t10 = idx * a // 7
            g = t10 - tmp & 255
            t11 = (19 ^ a) // 4 ^ tmp
            a = t11 % 9973
    else:
        t12 = (a >> 4) % 65521
        a = rec(85, t12)
        t13 = idx ^ e ^ 11
        e = rec(79, t13 % 9973)
    t14 = a * 17 + idx
    return t14 % 9973

def fn1(c, b, g):
    for hi in range(3):
        c = (g // 7 ^ hi) & 1023
        if g >> 1 >= 2:
            t0 = g ^ 2
            t1 = t0 - (hi ^ 11)
            t2 = 7 + c >> 1
            g = t1 - t2 & 8191
            t3 = g - hi >> 4
            c = (t3 | hi - 4 ^ g) & 131071
        else:
            t4 = (g + hi) * 7
            t5 = (c & b) + b
            g = t4 * t5 % 251
            g = hi + hi + g & 65535
    t6 = g - c - (g & 10) & 131071
    t7 = b >> 4 & 511
    t8 = (c // 6 - g) % 17
    b = fn0(t6, t7, t8)
    for s in range(8):
        for j in range(11):
            g = g & c
            t9 = (3 << 4) * (g % 17)
            g = (3 - b & g ^ t9) & 255
            c = c * g // 6 % 251
    w = b * 6
    t10 = (20 + w) // 2
    return t10 << 2 & 1023

def f(x):
    if x ^ 6 > 11:
        d = 0
        while d < 8:
            t0 = x - 3
            t1 = t0 + (d - 12)
            x = t1 % 251
            t2 = x * x >> 3 << 3
            x = t2 & 8191
            d = d + 1
    for nxt in range(333):
        if x * 18 != 46:
            t3 = (9 ^ nxt) - x
            x = t3 & 262143
        else:
            t4 = nxt + x << 1
            x = t4 % 1009
    if x + x == 59:
        x = x // 7
    else:
        if x | 5 == 15:
            x = 4 - x & x
            x = (x >> 4) - x
        else:
            t5 = (x & 1) * 7 * x & 131071
            x = rec(43, t5)
        for t in range(10):
            t6 = x // 8
            t7 = t6 * (t * t)
            x = t7 + t & 1023
    res = 12 - 17 & x
    if 19 + x == 8:
        x = x * x % 17
        x = x + res + res
    t8 = res + 10
    idx = t8 ^ x & 5
    x = res - 5
    if idx * x != 2:
        for c in range(8):
            t9 = x - 5 - res
            res = t9 % 17
            res = (11 ^ res) % 1009
            x = idx & c & idx
        t10 = (idx - 1) * (res >> 2)
        t11 = (t10 + idx) % 251
        x = rec(38, t11)
    else:
        t12 = 1 | idx
        idx = t12 - (idx & 20)
    t13 = (res >> 2) * res
    return (t13 ^ 6 * idx & res) % 1009

if __name__ == "__main__":
    arg = 4
    expected = 0
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
