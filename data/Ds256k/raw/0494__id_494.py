# Auto-extracted from ds_lt256k_500.jsonl
# record_id=494  entry=f  input='12'  output='47978'  tokens=94766

def rec(n, a):
    if n <= 0:
        return a
    w = a - 14 + n & 4095
    if a * n < 3:
        for v in range(7):
            t0 = w // 7
            t1 = t0 - v * v
            w = t1 % 251
            w = (3 - w >> 3) % 1009
    else:
        w = ((w ^ a) * 9 - w) % 1009
        if 3 & w >= 2:
            t2 = (n & a) // 6
            a = t2 & w
            w = w - 16 & 16383
    t3 = a & 10
    t4 = t3 | a - 10
    a = t4 % 251
    t5 = ((w & n) - a) % 1009
    return rec(n - 1, t5)

def fn0(b, d, m):
    e = [143, 847, 531, 327, 1002, 73]
    s = 0
    while s < 5:
        b = b // 4 % 65521
        s = s + 1
    if e[d % 6] * d == 4:
        e[b % 6] = ((d & m | 3) + 11) % 1009
        for w in range(3):
            e[b % 6] = (d | 11) % 1009
            d = b - d & 511
            t0 = d * m + e[d % 6]
            e[b % 6] = t0 % 65521 % 1009
    tmp = 19 | b
    t1 = b % 4093 // 2
    t2 = (t1 - 4) % 4093
    b = rec(76, t2)
    t3 = d - 13 | tmp
    return t3 % 65521

def fn1(g):
    t0 = (3 & g) * (g * g)
    t1 = t0 // 7 & 255
    t2 = g % 65521 ^ 16 + g
    t3 = (17 ^ g) - g << 4
    g = fn0(t1, t2 & 4095, t3 % 65521)
    t4 = g - 7 & 2047
    t5 = (g ^ 15) * g % 65521
    t6 = (g - 5) % 9973
    g = fn0(t4, t5, t6)
    for val in range(4):
        if (2 & 18) - g == 51:
            g = g + val & 65535
            g = ((g ^ 1) % 4093 ^ val) & 16383
        else:
            g = (g | 6) + g & 65535
        g = (g + 17) % 65521
        g = g & 16
    s = g * g & 262143
    t7 = g * 16 - g * s
    t8 = t7 - s & 255
    t9 = g * s >> 2 >> 4
    t10 = g * s * g // 3 & 32767
    g = fn0(t8, t9 % 9973, t10)
    t11 = (g + 3) % 4093
    t12 = (g << 2) // 3
    t13 = t12 - (s * s << 3)
    t14 = 5 ^ g
    t15 = t14 * (g + s)
    g = fn0(t11, t13 & 2047, t15 % 65521)
    return g * s % 65521

def f(x):
    nxt = [527, 183, 376, 234]
    if x << 1 != 21:
        t0 = x * nxt[x % 4] + x
        nxt[x % 4] = t0 * 19 % 1009
        for z in range(3):
            t1 = nxt[z % 4]
            t2 = t1 * nxt[z % 4]
            t3 = t2 | x ^ nxt[z % 4]
            x = t3 // 2 % 97
            t4 = (z | 18) + (z - x)
            x = t4 & 255
    if x & nxt[x % 4] < 61:
        nxt[x % 4] = x + x
        x = (x | 3) + (x - 11)
    else:
        x = (1 - x) // 8
        c = 0
        while c < 10:
            x = (x // 6 + c) * 10 & 1023
            t5 = c * c & c | x
            x = t5 & 1023
            c = c + 1
    if nxt[x % 4] - 3 < 30:
        x = ((x ^ 13) & x) // 3
        t6 = nxt[x % 4]
        t7 = t6 // 2 >> 4
        x = t7 - x
    t8 = nxt[x % 4] << 4
    g = t8 << 1 >> 4
    for y in range(8):
        for cnt in range(6):
            t9 = (6 & y) + 6 ^ g
            x = (t9 ^ x) % 97
        t10 = g - 5 + x
        x = t10 + y & 262143
        g = g - 5 & 16383
    a = 0
    while a < 3:
        for b in range(8):
            x = (18 + x) % 4093
        g = (g ^ a ^ x) % 97
        t11 = nxt[x % 4] * g // 7
        x = t11 & 32767
        a = a + 1
    if x * 16 > 14:
        x = 10 + 11 + x
    else:
        if g + 7 > 41:
            x = 16 + 1 | g
        else:
            t12 = nxt[x % 4]
            nxt[g % 4] = t12 * 6 >> 4
    t = 0
    while t < 4:
        if 16 & t ^ g >= 26:
            t13 = (x >> 3) - x
            t14 = g >> 3 >> 1
            x = t13 * t14 & 1023
            t15 = nxt[t % 4]
            t16 = t - t15 | g
            x = t16 & 511
        else:
            t17 = x // 7 % 4093
            nxt[t % 4] = t17 // 5 % 1009
        t = t + 1
    if 10 * x >= 1:
        t18 = g - x + 7
        x = t18 ^ 8
        t19 = 18 - 6 ^ 16
        g = t19 | x - 3 & g
    t20 = nxt[g % 4] + g
    nxt[g % 4] = (t20 ^ x) << 4 & 511
    t21 = nxt[x % 4]
    aux = t21 // 7 >> 1
    t22 = g - 13 & 262143
    t23 = (aux >> 3) + (9 << 4)
    t24 = aux * x * x * t23
    t25 = 3 + 13 & aux
    x = fn0(t22, t24 % 65521, t25)
    t26 = nxt[g % 4]
    t27 = 1 ^ g
    t28 = t27 ^ g + t26
    t29 = g | x | g
    t30 = (t28 - t29) % 4093
    g = rec(27, t30)
    acc = 18 - aux
    t31 = (4 - x) * 7
    t32 = t31 ^ (g + acc) // 8
    return t32 % 65521

if __name__ == "__main__":
    arg = 12
    expected = 47978
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
