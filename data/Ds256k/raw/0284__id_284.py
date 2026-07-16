# Auto-extracted from ds_lt256k_500.jsonl
# record_id=284  entry=f  input='5'  output='4'  tokens=249100

def rec(n, a):
    if n <= 0:
        return a
    res = a * n % 17
    val = ((a ^ 17) + n) % 1009
    t0 = val ^ a
    t1 = res * val // 5
    t2 = t0 - (n | 3)
    t3 = (t1 ^ t2) & 4095
    return rec(n - 1, t3)

def fn0(d, b):
    c = (d - 5 ^ 18) & d
    if 1 - 17 - b <= 9:
        t0 = c << 2 >> 1
        t1 = d >> 1 << 4
        b = t0 - t1
    for aux in range(6):
        t2 = aux - d
        t3 = t2 * (b ^ aux)
        c = t3 & 131071
    if d >> 2 < 41:
        if 12 + b == 21:
            t4 = 9 + b & (c ^ 11)
            d = rec(118, t4)
        else:
            t5 = (13 | c) & 511
            c = rec(89, t5)
            t6 = (12 - d) % 9973
            b = rec(110, t6)
        if b % 251 <= 61:
            t7 = 17 * b // 7
            b = t7 & c
        else:
            d = d + c ^ c
            t8 = ((c | b) & d) - c
            d = rec(32, t8 & 65535)
    else:
        t9 = (d - c - b) * 3
        b = t9 & 255
        t10 = d + 13 ^ 10
        b = rec(22, t10 % 251)
    for tmp in range(5):
        t11 = b - 1 + c
        b = t11 // 3 & 16383
    t12 = c - 19 + d // 3
    return (t12 | d) % 1009

def f(x):
    if 7 | 18 | x != 64:
        t0 = x * x % 65521
        x = rec(39, t0)
    else:
        t1 = x * 20 >> 1
        x = t1 - (x + x >> 3)
        for lo in range(6):
            x = (lo - 14 + x) % 65521
            x = (lo - x) % 251
            x = (lo ^ 19) - x & 4095
    if x * x <= 41:
        if x >> 4 != 57:
            t2 = (x >> 4) % 17
            x = rec(120, t2)
            t3 = (x + x) * x
            x = t3 % 17
    t4 = (x | 5) % 17
    t5 = ((x | 18) ^ x) % 251
    x = fn0(t4, t5)
    t6 = 13 * x - (x >> 2) | x
    hi = t6 % 251
    t7 = (4 | hi) & 65535
    t8 = (x | 9) % 17
    hi = fn0(t7, t8)
    t9 = hi + hi & x
    prv = t9 - x
    if x - 13 >= 55:
        if x ^ 3 >= 53:
            t10 = ((prv ^ hi) - hi // 7) % 17
            hi = rec(21, t10)
        else:
            t11 = 10 + prv + 12 * hi
            x = fn0(t11 & 1023, prv % 17)
    else:
        for cur in range(2):
            x = x + x & 16383
        t12 = hi >> 2 >> 3
        x = (t12 | prv) & 8191
    for tmp in range(134):
        t13 = hi // 8
        t14 = t13 * (tmp * x)
        x = t14 % 17
    b = (19 | prv) % 251 << 3
    a = hi << 3
    for v in range(4):
        m = 0
        while m < 7:
            prv = prv + m & 2047
            m = m + 1
        t15 = (a + b - (a << 4)) * b
        b = t15 % 17
    t16 = (b - prv) // 2
    g = t16 + ((prv & 5) - a) & 8191
    return b & 4

if __name__ == "__main__":
    arg = 5
    expected = 4
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
