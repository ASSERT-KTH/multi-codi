# Auto-extracted from ds_lt256k_500.jsonl
# record_id=20  entry=f  input='20'  output='10'  tokens=181778

def fn0(d, c, a):
    nxt = [837, 305, 233, 798, 84, 587]
    t0 = a - d | 12 + d
    t1 = c >> 1 ^ d >> 1
    b = t0 * t1 & 65535
    for tot in range(8):
        for hi in range(11):
            nxt[d % 6] = (b + 11 + a) % 1009
            t2 = nxt[c % 6] >> 1
            t3 = (c | 2) * t2 ^ tot
            nxt[b % 6] = (t3 & 16383) % 1009
    b = d >> 4
    a = b * b % 1009
    c = c % 65521 // 5
    for e in range(6):
        for cur in range(4):
            t4 = 13 - nxt[a % 6]
            b = (10 + b - t4) % 65521
    t5 = nxt[a % 6]
    c = b - t5
    b = (6 & 9) + d
    t6 = c * d + b
    return t6 % 1009

def fn1(d, j, g):
    p = [887, 642, 356, 1005, 189]
    m = d * d % 97 - d
    t0 = d | g
    t1 = t0 & d // 3
    t2 = (t1 | d) % 17
    t3 = p[j % 5]
    t4 = p[g % 5]
    t5 = (j | t3) ^ t4
    t6 = p[d % 5] - j
    t7 = t6 * m % 97
    j = fn0(t2, t5 % 17, t7)
    s = 0
    while s < 12:
        d = (18 + g ^ 14) - d & 2047
        t8 = p[g % 5] * j << 3
        j = t8 % 97
        s = s + 1
    t9 = g + p[m % 5]
    p[d % 5] = (t9 ^ j & g) % 1009
    if 2 | j != 13:
        j = m | 3
        d = p[g % 5] * 2
    else:
        g = (d & g) // 8
        t10 = 12 & p[j % 5]
        t11 = (d ^ g) & 32767
        t12 = j // 7 - 9 & 2047
        g = fn0(t10, t11, t12)
    t13 = (10 + j >> 3) + j
    return (t13 + m) % 1009

def f(x):
    lo = 0
    while lo < 215:
        t0 = (x & 12) + (x | 13)
        x = (t0 ^ x) % 17
        t1 = (x << 1) - lo * 5 - lo
        x = t1 & 262143
        if lo + x == 35:
            x = (x << 2) % 17
        else:
            x = (lo + lo ^ x) & 1023
        lo = lo + 1
    t2 = 6 * x - (x ^ 4)
    t3 = (x + 6) % 17 << 4 & 65535
    t4 = ((x | 19) + x + x) % 97
    x = fn1(t2 & 32767, t3, t4)
    e = x + x & 9 * x
    s = x & 20
    if e & 4 >= 2:
        t5 = s + s & 8191
        t6 = s * 18 & 262143
        t7 = (7 + x) % 65521
        s = fn1(t5, t6, t7)
        t8 = (s << 3) * (e * 17)
        t9 = t8 * (e // 5 ^ s - 1)
        x = t9 & 262143
    else:
        p = 0
        while p < 11:
            s = ((x * s ^ s) >> 4) % 65521
            p = p + 1
        t10 = x + 17 ^ s
        t11 = t10 << 1 & 16383
        t12 = e // 6 - x * e
        t13 = (e - 17 | 1) % 97
        x = fn0(t11, t12 & 4095, t13)
    m = x * x & 1023
    t14 = s + e - s
    return (t14 - (x - s & e)) % 97

if __name__ == "__main__":
    arg = 20
    expected = 10
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
