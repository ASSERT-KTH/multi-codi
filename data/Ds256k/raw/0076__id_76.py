# Auto-extracted from ds_lt256k_500.jsonl
# record_id=76  entry=f  input='9'  output='5'  tokens=228603

def fn0(m, b, a):
    z = [37, 53, 62, 12, 22]
    t0 = m ^ z[b % 5]
    t1 = a // 7 & b // 7
    z[a % 5] = (t1 & (t0 | m)) % 97
    a = (m & z[b % 5]) * 1
    b = 16 - b ^ b
    t2 = 3 + m
    t3 = b + 14 >> 4
    t4 = t2 + (a - 15)
    m = t3 - t4
    m = z[b % 5] + m
    for idx in range(11):
        b = idx & a
    d = 0
    while d < 4:
        for p in range(11):
            t5 = (6 - m) // 8
            z[p % 5] = t5 % 97
            m = (b * a - p) % 1009
        d = d + 1
    if 8 ^ 7 | b < 5:
        for res in range(8):
            t6 = 8 * m << 2
            z[b % 5] = t6 % 65521 % 97
            b = (res - 18 ^ m) & 511
            z[res % 5] = (m << 3 & 8191) % 97
        for tot in range(6):
            a = m + a + a & 65535
            b = (a + 19 ^ 3 | tot) & 131071
    else:
        for buf in range(3):
            t7 = m * a - (m << 1) >> 4
            b = (t7 + buf) % 65521
        for aux in range(11):
            t8 = b * 18 // 7 // 6
            a = (t8 | a) & 131071
            z[a % 5] = (a // 4 + m) % 97
    return (b ^ 14) & 32767

def fn1(d, j, a):
    s = 16 - a & j
    t0 = j & 7
    t1 = t0 & (s & 18)
    t2 = j - 10 & (3 | a)
    t3 = (10 - j >> 4) % 97
    s = fn0(t1, t2, t3)
    t4 = 10 - d
    t5 = t4 * (d + j)
    d = t5 * a & 1023
    if 7 + j != 54:
        for c in range(6):
            s = (c * s >> 2) % 9973
        u = 0
        while u < 8:
            t6 = (a + u) // 7
            s = t6 % 65521
            a = a // 2 % 9973
            u = u + 1
    t7 = s - d - s & 13
    t8 = a >> 4
    t9 = (s + s) // 5
    t10 = t8 * (d << 4)
    t11 = (t9 ^ t10) % 65521
    t12 = (s + a) % 65521
    j = fn0(t7, t11, t12)
    t13 = 20 + d
    t14 = t13 - (a + 12)
    t15 = (d << 1) % 97
    s = fn0(j & d, t14 % 9973, t15)
    return (j + a | s) & 32767

def f(x):
    acc = [970, 902, 138, 837, 660, 497, 661, 256]
    for j in range(38):
        u = 0
        while u < 11:
            x = (u ^ 10 ^ x) % 4093
            t0 = acc[j % 8]
            t1 = (t0 - x) // 7
            acc[j % 8] = t1 // 2 % 1009
            u = u + 1
    t2 = acc[x % 8]
    t3 = x // 8 + x
    t4 = t2 * x - 14
    acc[x % 8] = t3 * t4 % 17
    t5 = 9 * x % 17
    t6 = x + 11 & 511
    t7 = (3 - x) % 4093
    x = fn1(t5, t6, t7)
    aux = (x | 19) // 4 ^ x
    t8 = (acc[x % 8] >> 2) // 6
    t9 = (t8 & acc[x % 8]) - aux
    return t9 % 17

if __name__ == "__main__":
    arg = 9
    expected = 5
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
