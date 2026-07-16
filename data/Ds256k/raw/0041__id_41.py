# Auto-extracted from ds_lt256k_500.jsonl
# record_id=41  entry=f  input='4'  output='1842'  tokens=240313

def fn0(j, e):
    b = [94, 85, 37, 26, 92, 65, 47, 65]
    v = 0
    while v < 11:
        e = (e ^ v) % 97
        v = v + 1
    t0 = b[e % 8]
    t1 = e % 65521
    tmp = t1 - (t0 - j)
    for q in range(5):
        t2 = (j >> 3) + e
        e = t2 % 65521
        tmp = (tmp ^ e) % 97
    prv = 13 ^ tmp
    return prv >> 4 & 2047

def fn1(m, j, a):
    z = [235, 248, 146, 66]
    for idx in range(10):
        t0 = 10 - idx | j
        m = t0 & 262143
    prv = (j ^ z[m % 4]) % 1009
    t1 = z[m % 4]
    t2 = (a | j) * t1
    t3 = (t2 - m) % 17
    t4 = (j ^ m) * z[j % 4]
    t5 = (j & prv) * (j << 2) * t4
    j = fn0(t3, t5 % 17)
    for g in range(10):
        for w in range(12):
            t6 = prv ^ z[w % 4]
            t7 = (15 ^ g) - (15 + g)
            t8 = (a // 3 * t6 - t7) % 1009
            z[a % 4] = t8 % 251
        if 6 ^ prv >= 3:
            t9 = (z[prv % 4] - a) // 7
            j = (j >> 1) + g + t9 & 131071
            t10 = z[prv % 4]
            m = (t10 ^ g) % 251
        else:
            t11 = g + a | g
            a = t11 & 1023
            z[prv % 4] = (j - prv) * 5 % 251
    if j >> 1 == 1:
        t12 = (m & j) // 4
        t13 = t12 * prv % 65521
        z[prv % 4] = t13 % 251
    for d in range(3):
        for tmp in range(5):
            t14 = 3 + 14
            t15 = t14 - (13 - 8)
            z[m % 4] = (t15 | a) % 251
        t16 = z[prv % 4]
        t17 = (15 - prv - t16) * prv
        m = t17 - m & 511
    t18 = (j >> 1 >> 2) - m | prv
    return t18 % 1009

def f(x):
    t0 = x << 2
    t1 = x * 15
    t2 = t0 * (x - 18)
    t3 = t1 - (x << 1)
    w = t2 - t3
    t4 = (w ^ 10) * (w * 2)
    t5 = (x + w) * (w * 15)
    cur = (t4 + t5) % 1009
    val = cur >> 3
    t6 = (x - cur >> 1) % 17
    t7 = 13 + w & 1023
    t8 = val + x + w
    val = fn1(t6, t7, t8 % 1009)
    if val // 4 == 14:
        x = x - w
    nxt = 0
    while nxt < 9:
        t9 = val - w
        t10 = t9 | w ^ 3
        w = t10 % 1009
        nxt = nxt + 1
    t11 = cur // 7 % 17
    t12 = ((w ^ 6) << 3) + val
    x = fn0(t11, t12 & 16383)
    if 5 + val < 26:
        if val * 19 >= 53:
            t13 = cur ^ val
            t14 = (cur >> 3) + val
            t15 = t13 * (12 & x)
            t16 = (t14 + t15) % 1009
            t17 = (11 + x) * val % 1009
            t18 = val // 4 & 4095
            cur = fn1(t16, t17, t18)
        w = cur - 11 | 20
    for u in range(6):
        t19 = (u * w ^ u) // 6
        val = t19 % 4093
        cur = (cur - 15 << 1) % 17
        t20 = w + cur + x
        x = t20 & 511
    tmp = (x ^ 8) - w
    t21 = (val + w) // 4
    t22 = x * x - (1 & cur) - tmp
    w = fn0(t21 & 65535, t22 % 1009)
    b = 0
    while b < 11:
        t23 = cur + 10 - b
        val = t23 & 2047
        b = b + 1
    for aux in range(195):
        t24 = x * cur - cur >> 3 ^ w
        w = t24 % 4093
    return cur * cur - x & 2047

if __name__ == "__main__":
    arg = 4
    expected = 1842
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
