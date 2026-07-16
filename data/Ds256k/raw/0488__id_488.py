# Auto-extracted from ds_lt256k_500.jsonl
# record_id=488  entry=f  input='11'  output='165'  tokens=103040

def rec(n, a):
    if n <= 0:
        return a
    nxt = (n | a) % 4093
    for y in range(6):
        nxt = (nxt | 1) % 9973
        t0 = (14 - a & 12) + nxt
        nxt = t0 & 511
    t1 = a >> 1
    t2 = t1 * (nxt - 14)
    t3 = t2 // 3 & 2047
    return rec(n - 1, t3)

def fn0(j, m):
    tmp = 0
    while tmp < 10:
        j = tmp * 10 + m & 1023
        if j & tmp != 0:
            j = (tmp + 5 | m) & 511
            j = j + m & 1023
        tmp = tmp + 1
    m = j * 15 & j // 4
    j = m * m % 4093 ^ m
    if j // 8 > 1:
        t = 0
        while t < 2:
            m = (t * 3 ^ j) & 131071
            t0 = j >> 1 | m // 3
            t1 = 20 ^ 14 ^ (j ^ 1)
            m = (t0 - t1) % 97
            t2 = m - t
            t3 = t2 * (j | m)
            m = t3 % 97
            t = t + 1
        j = (j ^ m) // 4
    else:
        t4 = j ^ 1
        t5 = t4 * (8 ^ 7)
        m = t5 & 4095
    m = j % 97 + (6 - j) | 17
    for e in range(6):
        m = (j >> 3 | m) % 97
        m = (4 * e | j) % 4093
    nxt = 0
    while nxt < 9:
        j = (m + j) % 97
        for c in range(12):
            j = j & m
            t6 = m - 4 + m * m
            m = t6 // 3 % 97
            t7 = m * nxt * nxt - m ^ c
            j = t7 & 4095
        nxt = nxt + 1
    buf = 0
    while buf < 2:
        t8 = (m >> 1) * (m & j) + 2
        m = t8 % 97
        buf = buf + 1
    t9 = j - 18
    t10 = t9 - (4 | j)
    return t10 & 262143

def fn1(g, j):
    aux = 0
    while aux < 8:
        for b in range(11):
            t0 = (10 | j) & aux - 4
            j = t0 * 6 % 4093
        t1 = j + aux & j * g
        g = t1 * ((g | 5) >> 4) % 4093
        aux = aux + 1
    t2 = j - 5 - g
    y = t2 + g
    t3 = (y | 9) % 4093
    t4 = (g << 2) // 8 & 65535
    g = fn0(t3, t4)
    d = g * y % 97
    for tot in range(2):
        d = (j & 10) * d & 4095
    t5 = (y - 8) * (9 - j)
    e = t5 & (d >> 1) // 4
    t6 = (7 ^ j) // 5 % 4093
    t7 = 15 * e | j
    j = fn0(t6, t7 % 97)
    return (3 * j ^ y) & 255

def f(x):
    for s in range(5):
        x = s + x & 2047
        x = s << 4 & x
    res = 0
    while res < 1073:
        x = 4 - res + x & 16383
        res = res + 1
    p = (x + x >> 1) + x
    nxt = p + p + p
    nxt = 20 + nxt >> 3
    nxt = p + p + p >> 4
    return p + x - (11 - x) & 2047

if __name__ == "__main__":
    arg = 11
    expected = 165
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
