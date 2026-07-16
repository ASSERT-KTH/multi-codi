# Auto-extracted from ds_lt256k_500.jsonl
# record_id=416  entry=f  input='10'  output='46'  tokens=153112

def rec(n, a):
    if n <= 0:
        return a
    t0 = n - a >> 4
    a = (t0 + a) % 9973
    t1 = n - 9 >> 1 >> 3
    t2 = t1 + a & 255
    return rec(n - 1, t2)

def fn0(c):
    for lo in range(11):
        t0 = lo + lo + 3 + lo
        c = t0 + c & 8191
    for idx in range(6):
        for z in range(9):
            t1 = z - 14 | c
            c = t1 & 131071
    for q in range(4):
        if c + 5 >= 53:
            c = (q + c) * q & 1023
        c = (q ^ c) & 8191
    p = 0
    while p < 3:
        c = (p & c) + p & 262143
        p = p + 1
    t2 = c * c - 13
    y = t2 & 8191
    w = (9 << 1) - y
    u = y >> 2
    t3 = (3 - 17) * w * y % 65521
    y = rec(112, t3)
    return (w >> 1) % 251

def fn1(c, b, m):
    aux = [43, 144, 195, 57]
    for prv in range(12):
        m = (m - 8) % 9973
        if c - 11 == 2:
            t0 = m // 2 * (20 & b)
            c = t0 - prv & 16383
            aux[c % 4] = (m << 4) % 9973 % 251
        else:
            t1 = (b | 3 | c // 8) >> 1
            m = (t1 + m) % 9973
        nxt = 0
        while nxt < 11:
            t2 = aux[b % 4]
            t3 = b * t2 % 9973
            aux[b % 4] = t3 % 251
            t4 = c + m & m
            t5 = c // 5 * c
            t6 = (t4 & t5) - nxt
            b = t6 % 251
            nxt = nxt + 1
    t7 = aux[m % 4]
    m = c - t7 >> 3
    d = 0
    while d < 8:
        t8 = c ^ aux[d % 4]
        m = t8 >> 1 & 4095
        w = 0
        while w < 4:
            b = c - m + (m + b) & 511
            w = w + 1
        u = 0
        while u < 10:
            aux[c % 4] = (b - 7) % 251
            u = u + 1
        d = d + 1
    return (m ^ b) & 131071

def f(x):
    for c in range(2):
        if c ^ x == 24:
            t0 = c - 4 | x + c
            t1 = c | 14 | 15 * x
            x = (t0 + t1) % 4093
    buf = (x ^ 5) & x
    t2 = x >> 4
    t3 = t2 | 14 << 3
    x = fn0(t3 % 4093)
    prv = buf // 6
    for a in range(86):
        t4 = (x | 11) + buf
        t5 = t4 + (prv * x >> 2)
        buf = t5 % 97
        x = (buf + a) % 4093
        j = 0
        while j < 4:
            x = (a + prv) * j & 65535
            j = j + 1
    return (buf * prv + buf) % 4093

if __name__ == "__main__":
    arg = 10
    expected = 46
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
