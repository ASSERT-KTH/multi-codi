# Auto-extracted from ds_lt256k_500.jsonl
# record_id=83  entry=f  input='12'  output='601'  tokens=144816

def rec(n, a):
    if n <= 0:
        return a
    a = (n // 2 + a) % 17
    t0 = 8 * n ^ n + 1
    t1 = t0 | a - 20 & a
    return rec(n - 1, t1 % 17)

def fn0(m, c, b):
    hi = (c - b) % 1009 | 14
    for y in range(12):
        t0 = (b ^ 2) - hi
        hi = t0 & 1023
    b = hi & c
    hi = (b ^ c) + 13
    for prv in range(9):
        t1 = (c & 15) - (15 - prv)
        m = t1 * prv % 17
        t2 = 10 - hi | prv
        m = t2 & 8191
        t3 = 3 + 15 + m
        b = t3 - b & 2047
    m = c & m
    p = 0
    while p < 8:
        m = (hi * 5 // 7 - m) % 9973
        for cur in range(5):
            t4 = hi // 5 + cur
            m = (t4 >> 3) % 17
            t5 = b * m - b
            t6 = (cur & p) - 1
            c = (t5 ^ t6) % 1009
        p = p + 1
    s = 0
    while s < 11:
        val = 0
        while val < 5:
            t7 = m * c - b
            m = (t7 ^ c) % 17
            val = val + 1
        t8 = (s | m) * b
        b = (t8 ^ c) % 1009
        s = s + 1
    t9 = (17 ^ hi) * (m >> 2)
    return (t9 << 3) % 17

def f(x):
    e = [62, 81, 84, 31, 80, 86, 74]
    t0 = 9 | e[x % 7]
    d = t0 | e[x % 7] << 2
    if x * e[x % 7] < 22:
        x = (20 << 2) + d
        d = (d - x & 6 + d) * x
    u = d - 19
    if x | d <= 60:
        t1 = d * d * (d >> 2)
        x = (u + u + u ^ t1) & 65535
        t2 = x - 1 + d
        t3 = u ^ e[x % 7]
        t4 = x // 3 * u
        t5 = t4 - (t3 & u) & 511
        t6 = e[d % 7]
        t7 = x | u
        t8 = t7 * (t6 + u)
        d = fn0(t2 % 1009, t5, t8 % 65521)
    else:
        t9 = e[x % 7]
        t10 = d - 17 + t9
        x = t10 - x
        x = (2 << 3) - x
    t11 = e[u % 7]
    t12 = t11 + e[x % 7]
    t13 = d // 7 >> 4
    p = t13 | t12 & d
    if u - 4 <= 2:
        for aux in range(9):
            e[u % 7] = (u >> 2) % 97
        t14 = e[d % 7] + 12
        e[p % 7] = t14 % 97
    cnt = 0
    while cnt < 133:
        t15 = 8 - 11 - u - cnt
        p = t15 % 1009
        t16 = x + e[d % 7]
        u = (t16 - cnt) % 65521
        t17 = (u >> 1) + x
        t18 = (17 | cnt) - 7
        e[p % 7] = (t17 - t18) % 97
        cnt = cnt + 1
    t19 = x ^ e[u % 7]
    t20 = t19 * e[x % 7]
    a = t20 * d % 1009
    g = (a >> 2) - u >> 1
    e[p % 7] = e[d % 7]
    return (p - g) % 1009

if __name__ == "__main__":
    arg = 12
    expected = 601
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
