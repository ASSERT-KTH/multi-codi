# Auto-extracted from ds_lt256k_500.jsonl
# record_id=492  entry=f  input='1'  output='0'  tokens=11234

def rec(n, a):
    if n <= 0:
        return a
    t0 = 17 ^ n | a
    tot = t0 & 65535
    tot = a * n & 1023
    t1 = n + 7 - a
    return rec(n - 1, t1 % 17)

def fn0(d, e, a):
    t0 = (20 - d) // 3
    t1 = (e - 11) % 4093
    t2 = (t0 | t1) % 251
    d = rec(56, t2)
    if a - 2 >= 64:
        if e // 8 < 20:
            t3 = a * d % 251
            e = rec(91, t3)
            t4 = (d - e) % 97
            e = rec(86, t4)
    t5 = (e >> 4) * (e >> 1)
    lo = (a << 4) * a * t5 % 97
    t6 = 18 << 3
    t7 = t6 & (19 & lo)
    d = rec(49, t7)
    if a ^ 13 == 54:
        e = 12 * a
    q = 0
    while q < 4:
        t8 = (lo + lo) * (d ^ 16)
        t9 = (d * d | e) - t8
        a = (t9 + a) % 251
        t10 = lo // 8 + q
        e = t10 & 1023
        q = q + 1
    return (lo ^ 7) % 251

def fn1(d, j, g):
    res = [33, 67, 123, 101, 174, 3]
    res[d % 6] = (g ^ 19) % 251
    t0 = (j ^ res[g % 6]) & 4
    w = t0 * g
    prv = 4 << 4 | g
    t1 = (w * j ^ j) - g & 255
    res[g % 6] = t1 % 251
    t2 = res[d % 6]
    t3 = res[g % 6]
    t4 = (t2 & t3) // 7
    j = t4 >> 2
    a = 0
    while a < 2:
        if j | 20 > 10:
            d = (a - j) % 4093
        if j - 7 == 58:
            t5 = res[j % 6] * 4
            t6 = d // 8 ^ t5
            t7 = t6 * (g // 5 ^ d)
            g = t7 & 511
        else:
            t8 = res[w % 6]
            t9 = t8 - res[prv % 6] - 11
            prv = t9 % 4093
        t10 = res[d % 6]
        t11 = res[g % 6]
        t12 = t10 ^ 17
        t13 = 7 + d >> 4
        t14 = t12 ^ (t11 ^ d)
        g = (t13 ^ t14) & 4095
        a = a + 1
    c = 0
    while c < 2:
        t15 = (g - c) * res[c % 6]
        w = t15 & 4095
        c = c + 1
    w = 8 + 11 + (j ^ prv)
    t16 = j // 4 ^ prv
    return t16 % 251

def f(x):
    val = x
    for d in range(10):
        val = (val ^ d) % 97
        if d + d - val < 40:
            t0 = d ^ x
            t1 = t0 ^ val & 2
            t2 = 9 * 14 + x
            x = (t1 + t2) % 97
            t3 = 13 + x
            val = t3 & (val & d)
    for w in range(12):
        t4 = (val | 19) // 3
        t5 = t4 | (x | 12) - x
        x = t5 % 97
        x = (11 * val | w) % 97
    t6 = (3 ^ x) % 17
    t7 = 20 * x | x
    acc = t6 | t7
    if x * 5 <= 49:
        t8 = (acc ^ x) * acc
        acc = rec(71, t8 % 251)
        c = 0
        while c < 4:
            t9 = (val >> 4) - 8
            val = t9 & 131071
            c = c + 1
    else:
        acc = (5 - 9 << 4) - acc
        t10 = acc * acc - (val | acc) | x
        x = t10 & 511
    return val & 12

if __name__ == "__main__":
    arg = 1
    expected = 0
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
