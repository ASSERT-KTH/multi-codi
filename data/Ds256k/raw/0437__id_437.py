# Auto-extracted from ds_lt256k_500.jsonl
# record_id=437  entry=f  input='1'  output='14'  tokens=26328

def rec(n, a):
    if n <= 0:
        return a
    tmp = (a | n) & 131071
    p = ((tmp ^ 7) + n) % 4093
    t0 = (n >> 3) * n | tmp
    p = t0 % 65521
    t1 = (tmp // 7 ^ a) & 262143
    return rec(n - 1, t1)

def fn0(b):
    for w in range(6):
        prv = 0
        while prv < 12:
            b = (17 - b) % 9973
            prv = prv + 1
    if 16 + 14 + b < 46:
        b = 7 - 17 + b
    d = (b + 12) // 3
    if 5 + b >= 38:
        a = 0
        while a < 3:
            b = (a ^ b) // 8 & 131071
            t0 = (8 | d) >> 4
            b = t0 * a % 65521
            a = a + 1
        buf = 0
        while buf < 6:
            d = b + d + (buf + b) & 1023
            d = (buf & 12 ^ 3 ^ b) & 255
            buf = buf + 1
    else:
        t1 = (d | 19) >> 4
        b = t1 - (d + b) // 4
        d = 19 + b
    m = b + d >> 3
    t2 = d * b - (m | 10)
    q = (t2 ^ d) % 17
    t3 = d - m | b
    return t3 & 1023

def fn1(m):
    cnt = [39, 55, 93, 54]
    for tmp in range(11):
        for t in range(2):
            t0 = tmp & 3 ^ tmp
            t1 = tmp + t - 8
            t2 = t0 * t1 - m
            m = t2 % 65521
            t3 = cnt[m % 4]
            t4 = tmp * 14
            t5 = cnt[m % 4]
            t6 = t4 & t * t3
            t7 = (tmp ^ t5) * tmp
            m = t6 + t7 & 16383
    idx = 4 - m
    for g in range(5):
        for z in range(11):
            m = (m + 17) * z % 17
            t8 = cnt[m % 4]
            t9 = t8 // 2
            t10 = t9 | g ^ z
            m = t10 & 2047
            t11 = m % 4093 - idx
            idx = t11 % 65521
        b = 0
        while b < 3:
            t12 = (g | 8) - (g << 4) ^ g
            m = (t12 ^ idx) + m & 255
            b = b + 1
    if m + m == 9:
        if idx + idx == 41:
            m = idx // 3
        for lo in range(7):
            cnt[idx % 4] = m * 1 % 97
    else:
        t13 = idx // 8 - (idx << 4)
        idx = t13 & 511
        idx = m >> 1
    for tot in range(6):
        t14 = cnt[tot % 4]
        t15 = cnt[tot % 4]
        t16 = t14 * 19
        t17 = t16 * (12 - t15)
        cnt[idx % 4] = (t17 | m) % 97
        t18 = cnt[idx % 4] ^ idx
        idx = 19 - idx + t18 & 1023
    t19 = cnt[m % 4]
    t20 = 11 - 18
    t21 = t20 + (m & t19)
    acc = t21 - idx
    t22 = acc + cnt[m % 4]
    cnt[m % 4] = t22 % 97
    return (17 + m ^ acc) % 97

def f(x):
    a = [497, 589, 915, 148]
    idx = x & 20
    t0 = a[x % 4] >> 4 ^ idx
    a[x % 4] = idx & x ^ idx | t0
    a[idx % 4] = idx - 12 & 7
    b = idx + x
    for w in range(158):
        t1 = x + w | x
        idx = (t1 + b) % 17
    return (idx ^ 9) & 16383

if __name__ == "__main__":
    arg = 1
    expected = 14
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
