# Auto-extracted from ds_lt256k_500.jsonl
# record_id=444  entry=f  input='6'  output='3364'  tokens=131867

def rec(n, a):
    if n <= 0:
        return a
    t0 = (a ^ 20 ^ 11) + n
    s = t0 % 9973
    s = (17 & n ^ a) & 511
    t1 = (a % 97 | n >> 1) >> 3
    a = t1 % 97
    t2 = (18 << 3 | 3) + a & 65535
    return rec(n - 1, t2)

def fn0(d, b, c):
    t0 = (d << 1) % 251
    d = rec(47, t0)
    u = 0
    while u < 3:
        b = (d * d + u) % 9973
        u = u + 1
    b = rec(95, c % 9973)
    t1 = (c ^ d) * (c % 9973)
    z = t1 % 9973
    t2 = d % 251 - z
    return t2 % 9973

def fn1(m, c, d):
    t0 = 20 - 15 | m >> 1
    t1 = d * c + (m + m)
    d = rec(67, t0 & t1)
    aux = 0
    while aux < 2:
        t2 = c // 5 + (d - m) + aux
        d = t2 & 8191
        for prv in range(12):
            d = (13 + prv + 3 - d) % 97
            t3 = (aux + c) * (m // 7)
            d = (t3 - prv) % 97
        aux = aux + 1
    if 13 - 17 - c >= 38:
        p = 0
        while p < 2:
            t4 = 8 ^ p
            t5 = t4 | d + m
            c = t5 >> 3 & 16383
            t6 = p ^ d
            t7 = t6 - (m >> 1)
            m = t7 & 4095
            c = (m // 4 + c) % 97
            p = p + 1
    else:
        nxt = 0
        while nxt < 11:
            d = (11 ^ 6) * d % 97
            t8 = 13 * 19 + (d - c)
            t9 = t8 ^ (m & nxt) - c
            m = t9 & 511
            nxt = nxt + 1
    t10 = (m << 4) * (d ^ 19)
    t11 = 1 * m * (d ^ c)
    t12 = (t10 | t11) & 1023
    t13 = (c | 6) * 20 % 17
    t14 = c - m & 4095
    c = fn0(t12, t13, t14)
    t15 = (d & c) * d // 3
    m = t15 % 17
    d = c ^ m
    t16 = 14 * d * (c | d)
    return t16 % 97

def f(x):
    if (14 ^ 11) + x != 29:
        for nxt in range(9):
            x = ((1 ^ nxt) - nxt) * x & 1023
            t0 = (x ^ 16) >> 3
            x = t0 & 511
    cnt = (x ^ 9) + x | 9
    for c in range(8):
        cnt = (x * 3 // 7 | cnt) & 1023
        t1 = x + cnt - 2 | cnt
        x = t1 & 4095
    cur = (x ^ 1) >> 2
    cnt = (cur - 1) * (x >> 1) & 8191
    s = 0
    while s < 382:
        t2 = (s ^ 5) * s >> 4
        x = (t2 + x) % 9973
        cnt = (cur >> 4) + s & 511
        s = s + 1
    return (cur ^ x) & 262143

if __name__ == "__main__":
    arg = 6
    expected = 3364
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
