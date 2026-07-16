# Auto-extracted from ds_lt256k_500.jsonl
# record_id=429  entry=f  input='4'  output='4091'  tokens=158112

def fn0(g, a):
    j = [159, 155, 80, 34, 239, 230, 219, 0]
    b = 0
    while b < 5:
        p = 0
        while p < 8:
            g = (g - 19) * (5 + b) & 511
            p = p + 1
        b = b + 1
    for acc in range(7):
        if a >> 2 == 21:
            t0 = g - acc
            t1 = 14 * acc
            t2 = t0 ^ a + g
            t3 = t1 ^ acc + acc
            g = t2 + t3 & 65535
        if 3 & a > 0:
            t4 = (a & acc) + 3
            a = t4 % 97
            t5 = g // 7 - 14 * acc
            j[g % 8] = t5 % 251
        else:
            j[acc % 8] = (20 - g) % 251
        aux = 0
        while aux < 4:
            t6 = (a >> 4) * (1 ^ 13)
            j[a % 8] = t6 // 7 % 251
            g = (aux + g - 9) % 17
            t7 = j[g % 8] + aux
            t8 = t7 - j[g % 8]
            j[g % 8] = t8 % 251
            aux = aux + 1
    j[a % 8] = (16 | 14) * g % 1009 % 251
    t9 = j[a % 8] >> 1
    t10 = t9 * (g + g)
    w = t10 & (5 + a & g)
    if a + g < 31:
        t11 = g + j[w % 8]
        g = t11 * j[w % 8] % 1009
        s = 0
        while s < 5:
            t12 = j[w % 8]
            t13 = t12 << 4 | 19
            t14 = g // 3 - w
            g = t13 * t14 % 1009
            j[g % 8] = (4 & a) << 2
            s = s + 1
    u = (7 ^ a) * 6
    t15 = a * w - 19
    return t15 * ((g - u) * w) % 97

def f(x):
    c = x - 20 & 20
    t0 = x - 11 & c
    c = fn0(x & c, t0)
    for t in range(39):
        t1 = t - 7 - x
        t2 = t1 - 19 * t // 8
        x = t2 & 262143
        e = 0
        while e < 3:
            t3 = (t | c) * t << 4 ^ x
            x = t3 % 17
            e = e + 1
    if (2 | 19) ^ x <= 48:
        t4 = 3 + c >> 4
        t5 = 5 + 1 & 14
        t6 = (t5 | 19) - c
        x = fn0(t4 % 17, t6 & 32767)
        for g in range(12):
            t7 = g + g << 1 | c
            c = t7 & 4095
            t8 = c + x
            t9 = t8 * (g - 18)
            x = t9 % 251
            t10 = (12 ^ g) + (c ^ x)
            c = (t10 - (x & 2 ^ g)) % 251
    m = 0
    while m < 8:
        t11 = m + 8 << 4 | x
        c = t11 & 65535
        m = m + 1
    t12 = x - 8 & 8191
    t13 = (c >> 1 | 16 - x) + 20
    c = fn0(t12, t13 % 9973)
    nxt = x - 9
    t14 = c ^ nxt ^ nxt
    t15 = (c + c) * 4
    c = t14 & t15
    return (nxt >> 1) % 4093

if __name__ == "__main__":
    arg = 4
    expected = 4091
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
