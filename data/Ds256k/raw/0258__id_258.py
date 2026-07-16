# Auto-extracted from ds_lt256k_500.jsonl
# record_id=258  entry=f  input='11'  output='1792'  tokens=144911

def rec(n, a):
    if n <= 0:
        return a
    t0 = a << 1
    t1 = t0 & a - 17
    t2 = t1 & a ^ n
    prv = t2 & 16383
    if prv ^ 3 != 17:
        t3 = 11 & prv
        t4 = t3 * (prv * 11)
        prv = t4 % 251
    else:
        y = 0
        while y < 9:
            t5 = (prv & 7) * (prv - 16)
            prv = t5 - 8 & 2047
            a = (y - n | prv) % 1009
            t6 = prv - 3 ^ y
            a = t6 % 65521
            y = y + 1
    t7 = (n | a) % 1009
    return rec(n - 1, t7)

def fn0(e):
    g = 0
    while g < 4:
        if g + e <= 20:
            t0 = g << 3
            t1 = t0 + (e + g)
            t2 = 13 + e >> 3
            e = t1 * t2 & 2047
            e = ((e | 6) >> 2) // 8 & 8191
        e = e * 19 // 7 & 1023
        g = g + 1
    t3 = e + e
    t4 = t3 * (e - 20)
    aux = t4 % 251
    m = e | aux
    for q in range(8):
        m = m // 7 % 65521
        for hi in range(10):
            e = (12 ^ q | e) & 255
            m = (aux + e + m) % 97
    cur = e + e - (e ^ m)
    t5 = (cur + aux) * (aux + e)
    t6 = t5 ^ aux - 19 << 3
    res = t6 % 97
    aux = cur & 13
    if m + res >= 48:
        t7 = e * m & 1023
        res = rec(104, t7)
    t8 = (3 | m) >> 3
    return t8 & 32767

def fn1(m, e):
    buf = [319, 526, 38, 500, 991, 813, 542, 721]
    if buf[e % 8] - 20 != 4:
        if e << 2 != 9:
            e = 4 + e
            t0 = buf[e % 8] | 10
            buf[m % 8] = t0 * 16 % 1009
        else:
            t1 = 6 + m ^ e & 5
            e = t1 << 2
            m = m | 8
    else:
        m = 6 * 9 - e
    t2 = e % 9973 - buf[m % 8]
    buf[e % 8] = (17 + m - 18 - t2) % 1009
    buf[e % 8] = (e | 9) % 1009
    for cnt in range(10):
        m = (cnt ^ e) & 8191
        for t in range(5):
            t3 = m & t
            t4 = t3 + (18 | m)
            m = t4 >> 1 & 32767
            t5 = m << 2 | e
            e = t5 % 9973
            t6 = e + buf[m % 8] ^ cnt
            e = ((e & 16) + e ^ t6) % 9973
        e = (cnt + cnt + m) % 1009
    if e - m >= 31:
        if 19 - e == 51:
            e = (e << 2) % 4093
        m = m ^ buf[m % 8]
    else:
        m = m - 5 + e
        t7 = e - m & m - e
        e = (t7 << 3) % 1009
    t8 = e + e & m
    t9 = m + m & 5
    cur = t8 * t9 % 4093
    t10 = buf[e % 8]
    tot = t10 & 5
    return (cur | e) % 4093

def f(x):
    t0 = x + x - x * x
    res = (2 - x ^ 6) + t0
    if 5 - x == 23:
        for cnt in range(11):
            x = ((cnt + cnt) % 17 ^ res) % 17
            x = (res >> 1 ^ (x ^ 8)) & 511
        res = 20 + x
    else:
        for acc in range(3):
            t1 = (res | 17) // 5
            x = (t1 - x) % 17
            res = x + res & 32767
            t2 = (res + x) * (14 & res) // 7
            x = t2 & 4095
        t3 = x | res
        t4 = t3 * (res // 8)
        x = fn0(t4 % 17)
    for u in range(53):
        t5 = (res >> 3) // 6
        x = t5 & x
        res = (x ^ u) & 255
        t6 = x - u >> 4
        x = t6 & res
    res = x + x
    t7 = (18 ^ 20) - res
    t8 = x // 2
    t9 = t8 - 14 * x
    t10 = x ^ 1 ^ res
    t11 = t9 + t10 & 511
    res = fn1(t7 % 17, t11)
    x = (res * x >> 2) + res & 511
    t12 = (res | x) << 2
    return t12 % 65521

if __name__ == "__main__":
    arg = 11
    expected = 1792
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
