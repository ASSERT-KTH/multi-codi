# Auto-extracted from ds_lt256k_500.jsonl
# record_id=115  entry=f  input='17'  output='46'  tokens=204767

def rec(n, a):
    if n <= 0:
        return a
    t0 = ((a ^ 14) + (9 ^ n)) * n
    a = t0 % 4093
    t1 = (n + n - a) % 65521
    return rec(n - 1, t1)

def fn0(d, m, c):
    t0 = (d // 2 << 4) + m
    c = t0 % 1009
    c = d + d
    c = 18 * (m // 2) & 255
    t1 = d * d + d
    t2 = t1 - (d >> 1 ^ c)
    c = t2 & 65535
    for nxt in range(3):
        t3 = 14 + nxt + nxt * d
        m = t3 & 65535
        if 14 * 7 - m <= 2:
            d = (c + nxt) % 65521
        else:
            c = (c ^ d) & (5 & c)
            t4 = (m | d) // 8
            d = t4 % 1009
        if d ^ 4 >= 3:
            t5 = (m - c) // 3 % 1009
            d = (t5 | d) & 131071
    t6 = d * c % 4093
    d = rec(76, t6)
    t7 = d << 1 >> 1
    return (t7 >> 2) % 1009

def fn1(d, e):
    cur = d // 7
    e = 10 + cur
    w = 0
    while w < 6:
        t0 = w * cur - e + 19
        cur = t0 % 1009
        if e * cur < 61:
            t1 = e % 97 ^ 12
            t2 = (d & 4) + w
            d = (t1 ^ t2) & 8191
        else:
            t3 = (cur | e) + (w ^ d)
            t4 = d * w + d - t3
            cur = t4 & 4095
            t5 = cur - d | cur
            d = t5 & 32767
        e = (15 + cur | d) + w & 16383
        w = w + 1
    t6 = 5 - 18
    cur = t6 | e + e
    t7 = (cur | d) << 2
    t8 = t7 >> 1 & 2047
    t9 = 20 * cur + e
    t10 = (d | 13) + cur
    e = fn0(t8, t9 % 251, t10 & d)
    if 19 * cur == 25:
        e = (e << 2 | e) - cur
        z = 0
        while z < 2:
            d = (e ^ z) - e & 255
            t11 = e * cur * (20 * e)
            e = t11 % 4093
            z = z + 1
    e = (e // 7 & d) * 10
    t12 = cur >> 1
    t13 = t12 ^ (d | e)
    return t13 << 1 & 65535

def f(x):
    val = 2 & x
    t0 = (2 ^ 11) + 17
    j = t0 - x
    t1 = x + x - (x ^ j)
    t2 = t1 >> 2 & 16383
    t3 = val + 17 - j & 131071
    t4 = (val * x & x) - j
    j = fn0(t2, t3, t4 & 16383)
    for z in range(3):
        t5 = (x << 3) + (j + val)
        x = t5 & 131071
    hi = (j ^ 17) >> 3
    c = val + x - (12 - j)
    t6 = (j ^ x) + x
    t7 = t6 * ((hi | val) * c)
    nxt = t7 & 65535
    if val ^ c == 1:
        j = hi - 5 + x
        for w in range(8):
            t8 = x * 17
            t9 = t8 & 4 + nxt
            x = t9 * nxt % 97
            t10 = (4 ^ w) + w
            val = (t10 | val) % 97
    else:
        x = hi - x
        nxt = (c | x) - 11
    t = j + c - 3 | j
    t11 = nxt % 97
    t12 = t11 | val + 3
    t13 = (16 ^ j ^ hi ^ t) & 255
    t14 = t // 5 % 97
    nxt = fn0(t12 & hi, t13, t14)
    t15 = val // 3 & 20 << 4
    res = t15 | nxt
    for p in range(6):
        t16 = hi * t
        t17 = res + c & 17
        t18 = t16 ^ (12 | x)
        t19 = t17 ^ t18 | p
        j = t19 % 4093
    for y in range(8):
        t20 = (3 & res) + val
        t21 = nxt // 2 - 18
        res = t20 * t21 % 4093
        t = y + c & 511
        m = 0
        while m < 17:
            t22 = (8 ^ x) - res
            res = t22 & 2047
            t = ((res & 18 & x) - t) % 97
            m = m + 1
    t23 = (res + res) // 6
    return t23 % 97

if __name__ == "__main__":
    arg = 17
    expected = 46
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
