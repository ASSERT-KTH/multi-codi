# Auto-extracted from ds_lt256k_500.jsonl
# record_id=415  entry=f  input='19'  output='16'  tokens=260994

def rec(n, a):
    if n <= 0:
        return a
    a = (n | a) % 97
    a = (a ^ n) + a & 32767
    t0 = (19 - n ^ a) & 1023
    return rec(n - 1, t0)

def fn0(m, j):
    u = [32, 51, 83, 73, 39, 1, 86]
    for z in range(5):
        m = ((j | z) ^ z & 18) & 1023
    for y in range(8):
        t0 = j + j & y
        j = t0 * (4 ^ y) % 251
        for hi in range(3):
            j = (u[m % 7] ^ j) % 97
            u[y % 7] = j * y % 97
        aux = 0
        while aux < 11:
            t1 = 17 + u[m % 7]
            t2 = m // 8 % 17
            t3 = t2 ^ t1 - (1 & aux)
            u[y % 7] = t3 % 97
            t4 = m - aux ^ j // 3
            j = t4 % 251
            m = (y & j ^ aux) & 8191
            aux = aux + 1
    t5 = u[j % 7] - m
    t6 = t5 + (j & m) ^ j
    u[m % 7] = t6 % 97
    w = (j ^ u[j % 7]) >> 4
    for b in range(8):
        u[j % 7] = (j - 18) % 97
        j = (b ^ u[j % 7]) & 262143
        for c in range(11):
            t7 = 7 - u[w % 7]
            t8 = t7 - u[b % 7] * w
            t9 = t8 * (m << 3 | w * c)
            u[w % 7] = t9 % 17
            t10 = (u[c % 7] & m) << 1
            u[b % 7] = t10 % 97
    if m ^ w > 58:
        w = (j | 9) >> 4 >> 4
    return (w | 6) % 251

def fn1(b, a, e):
    t0 = b + e >> 1
    t1 = t0 - (8 + e) * b
    a = rec(36, t1 & 511)
    for lo in range(5):
        if a - 5 != 38:
            t2 = lo * b - a
            t3 = t2 * (a * e ^ 12)
            e = t3 % 1009
            t4 = (e >> 2) // 4
            b = t4 + b & 511
        t5 = 7 * a + (a + e)
        e = t5 % 1009
        a = (e >> 2) - lo & 255
    for g in range(7):
        t6 = 10 + 17
        t7 = t6 - (e - g)
        a = t7 & 8191
    a = a - b - (10 - e)
    if 13 + b >= 13:
        j = 0
        while j < 3:
            a = (a ^ j) % 1009
            b = (17 & 7) - a + j & 262143
            a = (j + j - e // 7) % 17
            j = j + 1
    e = e ^ 13
    t8 = e * b | 16
    return t8 * a & 131071

def f(x):
    p = 0
    while p < 3:
        x = x - p & 1023
        for buf in range(8):
            x = (5 | x) % 97
            x = ((buf & 11) - x) % 97
        hi = 0
        while hi < 9:
            t0 = (hi ^ 10) * p ^ p
            x = (t0 | x) % 97
            hi = hi + 1
        p = p + 1
    t1 = x | 16
    b = t1 * (x >> 1)
    for w in range(14):
        b = (w + b) % 17
        t2 = ((w ^ x) + 4) * x
        x = t2 % 17
        for cnt in range(11):
            b = b & 18
    t3 = b - 2 - 1 * x
    v = (x | 15) >> 4 ^ t3
    for q in range(6):
        t4 = q | 7 | x
        v = t4 & 1023
        v = v // 3 // 6 % 97
    c = v - b
    for z in range(10):
        for y in range(7):
            t5 = (x - y) // 4 + 13
            b = t5 & 2047
            t6 = 20 - v + b
            b = t6 & 8191
            b = (3 & v) + y & 65535
    for d in range(11):
        b = (d & 7 | b & d) & 32767
    j = v - x + (13 | x) - 8
    u = c - v
    cur = b * 18
    g = u - 13 ^ cur
    t7 = (j >> 2) * (9 + c) + v
    t8 = (5 << 1) - g
    c = fn0(t7 & 16383, t8 % 1009)
    m = 1 - x ^ (c ^ u)
    return (2 + c) % 97

if __name__ == "__main__":
    arg = 19
    expected = 16
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
