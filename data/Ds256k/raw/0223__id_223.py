# Auto-extracted from ds_lt256k_500.jsonl
# record_id=223  entry=f  input='3'  output='21'  tokens=51059

def rec(n, a):
    if n <= 0:
        return a
    for u in range(3):
        a = a + n >> 2 << 4 & 131071
        t0 = 11 + a + a
        a = t0 % 9973
        for aux in range(12):
            t1 = a % 251
            t2 = t1 - (aux ^ 16)
            a = t2 % 17
            t3 = (a >> 1) + a
            a = t3 % 9973
    t4 = (n ^ 14) - (18 + a)
    a = t4 % 251
    return rec(n - 1, a & n)

def fn0(c, m, j):
    t = [61, 11, 74, 58, 67, 34]
    t0 = m + j
    t1 = (7 | 19) + c
    t2 = t0 + (m - c)
    res = t1 + t2
    t3 = c * 8 >> 1
    t4 = t[j % 6]
    t5 = (t3 - t4) % 97
    m = rec(26, t5)
    t6 = j >> 1 & j
    c = rec(58, t6)
    cnt = m - 2
    t7 = (c + 4) // 3
    e = t7 >> 1
    for acc in range(10):
        t[res % 6] = (cnt + e) % 97
        t8 = t[c % 6] - 8
        t9 = t[acc % 6]
        m = ((t8 & j) + t9) % 97
        t10 = (j ^ m) - m // 5
        t11 = (res + e >> 1) * t10 - acc
        c = t11 & 255
    for cur in range(2):
        cnt = (c * 9 | (cnt | m)) & 2047
        if cur - e > 13:
            t12 = (13 ^ 11) - j
            t[e % 6] = t12 % 97
        else:
            j = (cur ^ 7) * (c + cnt) & 262143
    return (e + e) % 97

def fn1(e, g):
    if 17 + e == 48:
        t0 = e % 97
        t1 = t0 * (g * 4)
        e = t1 & 4095
        w = 0
        while w < 9:
            g = g % 1009
            t2 = (e & 9) - w
            g = (t2 + (g + g - e)) % 9973
            g = e + w & 8191
            w = w + 1
    if e % 9973 == 50:
        t3 = e - 1 & 131071
        e = rec(95, t3)
        g = g - e
    else:
        e = (11 & e) - 1 - e
        g = e % 97 - (g - 18)
    t4 = (g + 12) * e // 8
    v = t4 % 9973
    e = (e + 3) // 8 | v
    t5 = e << 2 ^ v
    g = t5 & 65535
    return (g * v % 97 ^ 12) % 97

def f(x):
    prv = x
    for e in range(11):
        x = (e + prv) % 9973
        prv = (x ^ 17 ^ e) & 65535
    res = x ^ 12 | prv
    y = x + x ^ prv
    for tot in range(284):
        t0 = tot + 13 + prv
        y = (t0 + (y // 6 ^ res)) % 65521
    return res // 6 & 16383

if __name__ == "__main__":
    arg = 3
    expected = 21
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
