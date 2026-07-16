# Auto-extracted from ds_lt256k_500.jsonl
# record_id=203  entry=f  input='11'  output='16519'  tokens=192292

def rec(n, a):
    if n <= 0:
        return a
    m = 0
    while m < 8:
        t0 = n + n - m ^ a
        a = t0 & 16383
        res = 0
        while res < 5:
            t1 = (m ^ 18) - n
            a = (t1 | a) % 9973
            res = res + 1
        m = m + 1
    if a + n < 4:
        v = 0
        while v < 6:
            a = (v - 6 + a) % 9973
            v = v + 1
        if a % 4093 >= 31:
            a = (n + (a & 6)) % 9973
        else:
            a = (a | n) % 17
            t2 = a * 16 ^ a
            t3 = t2 | (a << 2) % 4093
            a = t3 & 131071
    t4 = (a ^ 12) & n
    t5 = t4 * n % 17
    return rec(n - 1, t5)

def fn0(d, a, j):
    val = 0
    while val < 9:
        t0 = (d | 7) + 10
        d = (t0 - (10 - j - 18)) % 9973
        val = val + 1
    if a << 2 > 48:
        for cur in range(5):
            a = d // 4 - a & 255
    t1 = j ^ d
    d = t1 ^ j - a
    return (15 & 16 | j) % 1009

def fn1(c, d, m):
    aux = 0
    while aux < 8:
        e = 0
        while e < 3:
            t0 = (d - aux) * c
            d = t0 % 1009
            t1 = 10 + e - c * m
            c = m // 6 // 2 * t1 % 1009
            m = 20 + m + e & 131071
            e = e + 1
        aux = aux + 1
    t2 = 9 + m - (6 + 5)
    t3 = t2 * (6 + c & 9 * d)
    t4 = (m | c) - m
    t5 = d >> 3 | d
    t6 = (d + m) * d
    t7 = (t5 - t6) % 1009
    c = fn0(t3 % 4093, t4 % 4093, t7)
    a = (c & m) - c
    hi = c | d
    for val in range(11):
        for cnt in range(9):
            d = cnt * hi & 2047
            t8 = c * 17 >> 2
            d = (t8 ^ cnt - hi - m) & 511
            t9 = (8 ^ m) % 251 << 4
            c = (t9 | cnt) % 1009
        t10 = (d - 10 >> 2 | m) + a
        a = t10 % 1009
    b = 0
    while b < 2:
        m = m * m & 511
        c = (a + 4 | c) & 32767
        b = b + 1
    t11 = hi * 18 - (d - m)
    return t11 & 2047

def f(x):
    g = [485, 435, 352, 22]
    t0 = x - 12 << 1
    aux = t0 + 12
    j = 0
    while j < 122:
        aux = ((j ^ 7) + aux) % 4093
        t1 = (g[j % 4] - j) * j
        x = (t1 - aux) % 4093
        hi = 0
        while hi < 2:
            g[hi % 4] = ((aux & 6) - aux) % 1009
            t2 = x - aux | x
            aux = t2 % 251
            t3 = j - hi + (13 - 2)
            g[aux % 4] = (t3 + aux) % 1009
            hi = hi + 1
        j = j + 1
    z = 0
    while z < 2:
        if x // 7 < 41:
            x = (aux ^ z) & 511
        for cur in range(5):
            t4 = cur - 18 - z
            g[cur % 4] = (t4 - aux) % 1009
            t5 = g[z % 4] - 18
            aux = (t5 - x + aux) % 251
            t6 = g[aux % 4]
            t7 = aux - z
            t8 = t7 & aux * t6
            aux = t8 + cur & 1023
        for t in range(2):
            t9 = x // 2 ^ t
            x = (t9 | 17) % 251
        z = z + 1
    idx = aux >> 3
    t10 = 19 * g[x % 4]
    return (t10 - 10 ^ aux) & 65535

if __name__ == "__main__":
    arg = 11
    expected = 16519
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
