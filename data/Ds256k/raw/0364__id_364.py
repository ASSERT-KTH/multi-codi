# Auto-extracted from ds_lt256k_500.jsonl
# record_id=364  entry=f  input='3'  output='831'  tokens=113795

def fn0(c, e):
    if e % 1009 >= 29:
        t0 = (e - c) * e
        e = (t0 - (3 * c ^ c)) % 17
        t1 = 1 * c + c * c
        t2 = t1 * (e * c * c)
        e = t2 & 16383
    j = c ^ e ^ e
    w = 0
    while w < 11:
        j = e - w & e
        m = 0
        while m < 5:
            t3 = c + m
            t4 = t3 - (e - 6)
            e = t4 % 17
            t5 = 17 - c ^ e
            e = t5 & 8191
            m = m + 1
        if j + e > 30:
            c = ((j >> 2) * j + c) % 17
            t6 = (w | 1 | e) // 3
            c = t6 % 17
        else:
            j = (16 * e ^ w) % 1009
        w = w + 1
    j = (j * 19 ^ j) & 262143
    t7 = (c + 19) % 1009 ^ j
    return t7 % 17

def fn1(d, j):
    d = d & 12
    for hi in range(7):
        t0 = 16 - hi ^ hi
        j = t0 * d & 262143
        t1 = 3 + hi & 7
        j = (t1 | j) % 9973
        idx = 0
        while idx < 10:
            t2 = hi * 8 * (j & 20)
            t3 = t2 + (j >> 2) // 5
            d = (t3 | idx) & 1023
            t4 = hi * hi * hi % 97
            d = (t4 | d) % 251
            idx = idx + 1
    for c in range(5):
        t5 = (c ^ 6) + j // 8 | j
        j = t5 & 65535
        if c + 19 - j <= 24:
            j = (d + j) * j % 9973
            t6 = 12 + c - j
            d = t6 & 262143
        else:
            d = c * j & c + d
            d = (c * c | j) % 17
        for t in range(10):
            d = (18 * t | j) % 17
            j = ((t | c) * d >> 3) % 17
    j = j % 9973
    j = j % 9973
    for q in range(9):
        d = (q & d ^ d) & 2047
    t7 = (20 | j) >> 3
    j = t7 * ((j ^ 7) * j) & 32767
    j = j >> 2
    return ((5 ^ 20) + d + j) % 251

def f(x):
    prv = [165, 175, 158, 89, 199]
    nxt = (x | 14) << 2
    for y in range(8):
        nxt = (nxt + x) * y % 4093
        t0 = x & prv[y % 5]
        t1 = y * nxt - (x | 2)
        x = t0 * (nxt + x) - t1 & 131071
        x = (y | nxt) & 262143
    prv[nxt % 5] = (prv[x % 5] + x) % 251
    s = 0
    while s < 10:
        t2 = x << 1 | s
        nxt = t2 % 9973
        nxt = s * nxt % 9973
        t3 = nxt << 1 ^ s
        x = t3 % 9973
        s = s + 1
    for cur in range(10):
        t4 = 2 ^ 9 ^ x
        nxt = (t4 + nxt) % 4093
    z = 0
    while z < 7:
        t5 = z ^ 8
        t6 = t5 & x + nxt
        t7 = prv[z % 5]
        x = t6 + t7 & 1023
        for j in range(9):
            x = ((nxt ^ 15) + x) % 9973
        z = z + 1
    t8 = prv[nxt % 5]
    t9 = x * t8 << 4
    prv[x % 5] = t9 % 9973 % 251
    res = nxt ^ 6
    prv[x % 5] = (x >> 3) % 251
    t10 = prv[res % 5] // 5
    u = t10 + (res - nxt) + x
    t11 = res + prv[nxt % 5]
    prv[res % 5] = t11 % 251
    q = (10 ^ (3 ^ 15)) + u
    for w in range(4):
        t12 = 16 + u + x
        t13 = 7 - q - nxt
        x = t12 * t13 & 255
        cnt = 0
        while cnt < 5:
            res = (q - nxt - cnt) % 4093
            t14 = (x & 14) * u
            t15 = t14 - u & 131071
            prv[cnt % 5] = t15 % 251
            t16 = prv[cnt % 5] // 2 + u
            prv[u % 5] = t16 % 251
            cnt = cnt + 1
    t17 = prv[res % 5]
    e = 10 + t17
    t = 0
    while t < 7:
        if 12 & prv[u % 5] == 3:
            t18 = e * u + (t & nxt)
            prv[res % 5] = (t18 >> 3) % 9973 % 251
        else:
            t19 = 10 * 6 * (res ^ 18)
            e = (t19 ^ t) & 2047
        t = t + 1
    c = 0
    while c < 2:
        t20 = prv[res % 5]
        t21 = (t20 >> 2) + c
        u = t21 & 32767
        val = 0
        while val < 8:
            q = (e // 7 | q) & 131071
            x = (x - c) % 4093
            res = val + prv[nxt % 5] & u
            val = val + 1
        c = c + 1
    lo = e + e - 13 + x
    t22 = prv[q % 5]
    t23 = 10 | t22
    t24 = t23 + (res - q)
    buf = t24 ^ res
    g = 0
    while g < 11:
        x = (6 | u) - g & 65535
        u = buf + u & 2047
        g = g + 1
    return ((res & u) - 3 + buf) % 4093

if __name__ == "__main__":
    arg = 3
    expected = 831
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
