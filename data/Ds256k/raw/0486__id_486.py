# Auto-extracted from ds_lt256k_500.jsonl
# record_id=486  entry=f  input='10'  output='3972'  tokens=211434

def fn0(d, e, a):
    y = [39, 147, 199, 208, 91]
    if d + 2 < 11:
        for w in range(3):
            t0 = 18 * 12 + a + w
            e = t0 % 4093
            t1 = a % 65521 >> 1 << 3
            d = (t1 ^ w) & 65535
        s = 0
        while s < 6:
            y[e % 5] = (10 + d) % 251
            s = s + 1
    else:
        t2 = e - y[e % 5]
        d = t2 * d * e % 65521
    t3 = (e ^ a) >> 4
    y[d % 5] = (t3 - d // 3 // 6) % 251
    for b in range(12):
        for aux in range(3):
            y[a % 5] = (a + 5) % 251
            t4 = a * 7 - (18 - 5)
            y[aux % 5] = (t4 * d & 16383) % 251
            t5 = (6 | e) & (7 & d)
            a = (t5 * b | aux) % 4093
        t6 = b << 2 << 4 ^ e
        a = t6 & 65535
        for m in range(4):
            t7 = (16 | y[a % 5]) + d
            t8 = 10 + 9 - y[d % 5]
            d = t7 - t8 & 32767
            t9 = m - 11 | a
            a = t9 & 2047
            t10 = (e & d) - (2 - b)
            a = (t10 ^ a) & 16383
    t11 = (d << 3) // 7
    y[e % 5] = (t11 >> 1) % 251
    e = (e | d) ^ a << 1
    a = y[e % 5] + 19
    t12 = y[d % 5]
    y[e % 5] = (a | t12) % 251
    t13 = e // 2 - y[e % 5]
    return t13 - e & 262143

def fn1(j):
    p = [554, 156, 941, 71, 426, 363]
    lo = (j & 3) - j % 1009
    for idx in range(5):
        for res in range(2):
            p[res % 6] = (18 * 3 - j >> 3) % 1009
            t0 = p[idx % 6] - res ^ 15
            t1 = t0 * ((3 & j) + (lo & 13))
            p[res % 6] = t1 % 1009
            p[j % 6] = j // 3 % 1009
    p[j % 6] = j * 6 % 1009
    t2 = lo - p[lo % 6]
    e = ((15 | j) + t2) * 5
    for y in range(7):
        t3 = lo | 3
        t4 = t3 * (j * y)
        e = t4 % 65521
        val = 0
        while val < 5:
            p[j % 6] = (17 + lo) % 1009
            p[j % 6] = (y * 2 | e) % 1009
            t5 = p[y % 6] // 2 - j
            lo = (t5 - val) % 17
            val = val + 1
    tmp = lo // 7 * j * 3 % 65521
    if p[e % 6] ^ 5 < 43:
        if e % 17 == 12:
            t6 = 20 % 17 - j
            p[j % 6] = t6 % 1009
            t7 = lo // 4 ^ tmp | lo
            p[e % 6] = t7 % 1009
        else:
            t8 = lo % 17 - (lo - tmp)
            j = t8 & (tmp + j | j)
            t9 = j & p[j % 6]
            p[tmp % 6] = (t9 + lo) % 1009
    else:
        t10 = (p[j % 6] ^ e) & tmp
        t11 = t10 * (lo + j >> 3) & 16383
        p[e % 6] = t11 % 1009
        p[lo % 6] = (lo & 5) << 1
    return e + j & 262143

def f(x):
    for v in range(4):
        for s in range(99):
            t0 = x ^ v
            t1 = t0 - (s + s)
            x = t1 & 131071
            t2 = (x ^ v) - s
            x = t2 % 4093
            t3 = (x ^ 8 ^ v) << 2
            x = t3 & 511
        t4 = (5 << 1) - x
        x = t4 % 65521
        prv = 0
        while prv < 3:
            x = (x ^ prv) // 2 % 65521
            prv = prv + 1
    aux = x & 17 ^ 9
    e = (x * aux ^ x) % 65521
    u = (x + x & e) % 9973
    t5 = (18 ^ 6) & (2 | x)
    return (t5 - e) % 4093

if __name__ == "__main__":
    arg = 10
    expected = 3972
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
