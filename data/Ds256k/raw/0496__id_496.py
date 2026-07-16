# Auto-extracted from ds_lt256k_500.jsonl
# record_id=496  entry=f  input='6'  output='49355'  tokens=184494

def fn0(a, d, e):
    y = [209, 240, 74, 100]
    d = 4 + d >> 2
    e = e >> 2
    d = e * a % 97
    t0 = y[e % 4]
    t1 = y[a % 4]
    t2 = t0 + d
    t3 = t2 * (t1 + e)
    return t3 & 2047

def fn1(c, d):
    y = [30, 44, 0, 76, 80]
    p = 0
    while p < 7:
        e = 0
        while e < 2:
            c = (e - c) // 5 & 1023
            y[c % 5] = (c - d) % 97
            t0 = 1 + y[c % 5]
            c = t0 + (p & c) & 65535
            e = e + 1
        p = p + 1
    t1 = y[d % 5]
    t2 = c + t1 + 14
    y[d % 5] = t2 % 97
    a = c - 19
    if d ^ 13 != 7:
        if c + d > 0:
            d = c % 4093 // 4
    b = 0
    while b < 6:
        t3 = (b ^ d) - a + c
        c = t3 % 251
        idx = 0
        while idx < 10:
            t4 = y[a % 5]
            y[c % 5] = t4 >> 3
            y[b % 5] = (idx + 3 + a) % 97
            idx = idx + 1
        d = c * b & 1023
        b = b + 1
    t5 = a // 7 * y[c % 5]
    return t5 & 2047

def f(x):
    y = 20 | x
    e = (x ^ 9) & x
    for cnt in range(3):
        if cnt ^ e != 18:
            t0 = cnt + 11 & cnt * x
            t1 = (cnt - e - x) * t0
            y = t1 % 65521
        else:
            e = e * y % 1009
            t2 = 4 << 2
            t3 = t2 | cnt - e
            y = (t3 >> 2) % 65521
        u = 0
        while u < 84:
            y = (y - 11) % 65521
            t4 = y * x ^ u
            e = t4 % 1009
            t5 = u - y
            t6 = t5 ^ (9 | 6)
            x = t6 & 131071
            u = u + 1
    tmp = 0
    while tmp < 7:
        if e * y <= 24:
            t7 = tmp * x ^ (20 ^ e)
            e = t7 & (17 ^ x) + e
            e = (tmp << 1) * x % 1009
        else:
            t8 = y >> 4 | tmp & 20
            t9 = t8 + (20 | x | x)
            e = t9 & 255
        tmp = tmp + 1
    for lo in range(11):
        t10 = lo * 2 | x ^ y
        e = t10 & 32767
        for b in range(2):
            e = ((1 | y) ^ e) & 16383
    cur = x // 6
    buf = 0
    while buf < 3:
        y = (cur ^ x | e) * buf & 4095
        t11 = buf ^ x ^ 5
        e = (t11 ^ y) % 1009
        buf = buf + 1
    nxt = (cur & y) + (x | y)
    q = 0
    while q < 9:
        for v in range(4):
            e = q + x + e & 1023
        t12 = cur % 1009 - 9
        t13 = t12 - (e - 16) * 11 - q
        x = t13 & 65535
        q = q + 1
    return (x - e - 8 * e) % 65521

if __name__ == "__main__":
    arg = 6
    expected = 49355
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
