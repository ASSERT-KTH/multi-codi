# Auto-extracted from ds_lt256k_500.jsonl
# record_id=483  entry=f  input='14'  output='232'  tokens=253418

def fn0(m, g, d):
    a = m >> 3 & m
    for lo in range(12):
        d = (m ^ 19 ^ d) % 1009
        acc = 0
        while acc < 12:
            t0 = m >> 1 | acc
            t1 = d % 65521 | 6
            g = t0 + t1 & 65535
            t2 = 5 + acc & g
            t3 = (1 | acc) << 1
            d = (t2 - t3) % 9973
            acc = acc + 1
    if m + a <= 2:
        m = g & m | m - 7
        if g << 3 < 41:
            t4 = d << 4 << 3
            a = t4 % 65521
            g = 16 + 7 + d
        else:
            a = 10 + d - g
            a = (g & d) - g + g
    hi = 0
    while hi < 4:
        for tot in range(2):
            d = ((a & d) << 1 << 4) % 1009
        t5 = g ^ hi ^ d
        d = t5 >> 3 & 262143
        t6 = a * hi + 19 | hi
        a = t6 % 1009
        hi = hi + 1
    t7 = d // 6
    t8 = d + a >> 2
    t9 = t7 + (g + d)
    nxt = t8 - t9
    for s in range(3):
        m = s - nxt & 262143
    for v in range(6):
        t10 = 12 * m ^ 5 & a
        a = t10 & 262143
    t11 = 5 - 20 | nxt
    return t11 & 255

def fn1(e, g):
    q = [20, 9, 53, 13, 61, 71]
    cur = (g >> 3) - g
    t = 0
    while t < 5:
        t0 = g % 17 * t
        t1 = q[cur % 6]
        g = (t0 + t1) % 17
        cur = e * cur + cur & 2047
        t2 = e // 7 + cur
        cur = t2 % 17
        t = t + 1
    t3 = g * cur & e + 11
    w = t3 - (e + cur ^ e)
    if g * w != 1:
        g = g + e - w
    t4 = 7 + g & 511
    t5 = q[w % 6]
    t6 = t5 * q[cur % 6]
    t7 = (t6 ^ 18 * e) % 9973
    t8 = (w - 14 - cur) % 9973
    g = fn0(t4, t7, t8)
    t9 = q[w % 6]
    t10 = q[e % 6]
    t11 = t9 + w
    t12 = t11 + (t10 ^ cur)
    t13 = cur & 19
    t14 = t13 - (g | w)
    t15 = (g - 6) // 6 & 262143
    g = fn0(t12 % 17, t14 % 17, t15)
    t16 = (g >> 1 << 4) + w
    return t16 & 4095

def f(x):
    acc = [566, 270, 683, 574, 395]
    prv = 0
    while prv < 5:
        if prv ^ x < 23:
            acc[prv % 5] = prv + prv + x | prv
            t0 = acc[prv % 5] & x
            t1 = t0 - acc[x % 5]
            acc[x % 5] = t1 % 1009
        else:
            t2 = acc[prv % 5] // 3
            acc[x % 5] = (t2 + x) % 1009
            t3 = acc[prv % 5]
            t4 = (prv ^ t3) >> 2
            x = (t4 ^ x) % 1009
        t5 = acc[x % 5] + 20
        x = (t5 ^ x | prv) % 4093
        prv = prv + 1
    u = acc[x % 5] & x
    if u * x == 44:
        u = x & 7
        x = x >> 3
    else:
        t6 = acc[u % 5] - u
        t7 = 10 * u & x
        x = t7 + (t6 | x - 18)
    t8 = u * x + u
    d = t8 & 8191
    if d - x > 59:
        t9 = x * u // 3
        t10 = t9 - ((x ^ d) + d)
        d = t10 & 511
    else:
        j = 0
        while j < 11:
            d = d - 17 & 255
            u = (d - 6 - u) % 9973
            x = (u + acc[x % 5]) % 4093
            j = j + 1
    acc[d % 5] = (x - u) % 1009
    hi = (u | 20) - d - d
    y = 0
    while y < 3:
        t11 = x // 4 | y
        hi = t11 % 4093
        y = y + 1
    t12 = d * d + (u >> 4)
    t13 = t12 + (d ^ 10) * (d * 2)
    res = t13 % 1009
    t14 = d * x // 3
    lo = t14 % 1009
    idx = 0
    while idx < 15:
        t15 = d + hi + res
        res = t15 % 4093
        acc[u % 5] = lo - 1 >> 1
        lo = (lo - hi) % 4093
        idx = idx + 1
    z = 0
    while z < 8:
        acc[hi % 5] = (d & u) % 1009
        u = (z - u | u) % 97
        z = z + 1
    q = (res ^ d) - 10
    for tot in range(10):
        t16 = acc[lo % 5]
        t17 = t16 * hi % 4093
        q = t17 + q & 16383
        u = (d * lo * res | tot) & 8191
        for tmp in range(2):
            lo = (res // 5 + tmp) % 9973
            t18 = acc[x % 5] >> 3
            u = (t18 - tmp) % 97
    t19 = u // 3 + (lo | hi)
    t20 = d + 1
    t21 = t20 | u * res
    t22 = t21 * u & 255
    u = fn1(t19 % 1009, t22)
    if u + lo < 60:
        q = hi << 2 >> 2
    else:
        q = 2 * res
        t23 = acc[d % 5] >> 1
        t24 = (q ^ lo) << 4
        hi = t24 - (t23 | d & x)
    t25 = 12 + 9
    t26 = t25 * (u ^ d)
    return t26 & 2047

if __name__ == "__main__":
    arg = 14
    expected = 232
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
