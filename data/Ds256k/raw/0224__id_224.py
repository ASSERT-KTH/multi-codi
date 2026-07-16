# Auto-extracted from ds_lt256k_500.jsonl
# record_id=224  entry=f  input='14'  output='0'  tokens=50094

def rec(n, a):
    if n <= 0:
        return a
    for z in range(8):
        if n - z | a < 41:
            a = (z | a) % 17
            t0 = (z | 14) ^ a
            a = t0 & 16383
        else:
            t1 = (z << 3) + n | a
            a = t1 % 65521
    t2 = n * 1 >> 4
    t3 = (t2 - a) % 65521
    return rec(n - 1, t3)

def fn0(j, d):
    res = (j ^ 11) // 5 // 4
    d = res + res
    res = j * j & d
    res = j << 2
    for acc in range(10):
        for val in range(8):
            res = ((8 ^ j) + val) % 1009
        if (acc & 12) - res < 9:
            d = 11 * 5 * d % 65521
            d = (j | d) & 8191
        else:
            t0 = 20 | 6
            t1 = t0 & j - 2
            t2 = t1 + res - d
            d = t2 % 65521
            t3 = 7 * d ^ acc
            res = t3 % 65521
    res = j // 6
    t4 = (d << 3) + (d + res) ^ d
    return t4 % 65521

def fn1(d, m):
    nxt = 0
    while nxt < 12:
        for y in range(2):
            t0 = m >> 3 ^ d
            d = t0 % 251
            t1 = (12 ^ y) * 2
            t2 = (t1 ^ nxt) - m
            m = t2 % 97
            t3 = y - 7
            t4 = nxt & 12
            t5 = t3 | (d | 5)
            t6 = t4 * (nxt & 17)
            d = t5 + t6 & 4095
        u = 0
        while u < 4:
            t7 = (nxt - m) * d // 2
            m = t7 % 17
            u = u + 1
        if nxt + d < 28:
            t8 = (nxt + nxt) * nxt
            m = (t8 - d) % 17
            t9 = m * d * 17
            m = (t9 - d) % 17
        nxt = nxt + 1
    s = m % 251
    t10 = m * s ^ m % 251
    t11 = d // 7 & 255
    d = fn0(t10 % 251, t11)
    p = 0
    while p < 12:
        m = p + s & 255
        m = (p + s) * d // 2 % 17
        d = m * m - p & 255
        p = p + 1
    acc = 0
    while acc < 7:
        idx = 0
        while idx < 2:
            s = s - d >> 1 & 255
            t12 = d >> 4 | s
            s = t12 & 2047
            d = ((idx ^ s) - idx) % 17
            idx = idx + 1
        t13 = d // 4 | m
        m = t13 & 511
        acc = acc + 1
    for cnt in range(12):
        for tot in range(4):
            t14 = s % 251 % 97
            s = (t14 - cnt) % 97
            m = (18 + s ^ tot) & 16383
    return s * s % 97

def f(x):
    v = [821, 805, 734, 257]
    aux = 12 - (x & 15)
    if aux ^ 5 == 32:
        aux = 3 * 16 + x
    else:
        t0 = 8 * aux
        t1 = x * 20
        t2 = t0 + (x ^ 11)
        t3 = t1 + (aux ^ 7)
        aux = t2 - t3
        x = (6 & aux) << 4
    val = (aux ^ x) + x
    for z in range(8):
        a = 0
        while a < 7:
            t4 = 1 + val + (x - aux)
            v[a % 4] = t4 % 1009
            a = a + 1
        if v[aux % 4] << 2 < 40:
            t5 = (11 & z) << 3
            v[aux % 4] = (t5 | aux) % 1009
            aux = aux // 3 & 8191
        for lo in range(12):
            t6 = (4 ^ val) + (z ^ val) | x
            x = t6 & 16383
    t = aux ^ x
    t7 = v[val % 4]
    idx = 7 - t7 - t
    t8 = idx >> 4 ^ val
    x = t8 // 2
    t9 = v[x % 4] + aux
    return t9 & (8 & x)

if __name__ == "__main__":
    arg = 14
    expected = 0
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
