# Auto-extracted from ds_lt256k_500.jsonl
# record_id=460  entry=f  input='5'  output='10'  tokens=128699

def fn0(a, e, b):
    c = [48, 170, 124, 150]
    if a * 4 != 32:
        b = b ^ e
    else:
        for tmp in range(4):
            t0 = c[b % 4]
            t1 = (b & a) // 6
            t2 = t0 // 4 + 17
            b = (t1 | t2) % 1009
            c[e % 4] = (a - b) % 251
            t3 = c[tmp % 4] - 15 | b
            e = t3 % 17
    t4 = c[a % 4]
    e = t4 + e
    t5 = a | c[e % 4]
    t6 = (e >> 3) * (a & e)
    t7 = (e | 20 | t5) + t6
    a = t7 & 65535
    tot = 0
    while tot < 11:
        b = (e * a - e | tot) % 4093
        for idx in range(10):
            t8 = idx + 3 - b
            b = t8 % 97
            c[e % 4] = (a << 2) % 251
        tot = tot + 1
    e = b - 19 ^ e
    for q in range(11):
        t9 = (e ^ a) + b
        b = t9 & 8191
    a = 4 + e
    return e - a & 511

def fn1(d, e, g):
    v = [11, 80, 139, 110, 96, 29, 44]
    for hi in range(5):
        t0 = hi - 14 - 11 + 13 - g
        e = t0 % 4093
    for j in range(10):
        e = (d // 8 - j) % 97
        for b in range(6):
            g = (b * b | g) % 4093
    t1 = v[d % 7]
    tot = e * t1 & 262143
    for aux in range(6):
        for cnt in range(11):
            t2 = (4 + e) * v[d % 7]
            v[e % 7] = t2 * ((g + e) // 8) % 97
            t3 = v[cnt % 7]
            e = (t3 + g) % 4093
        t4 = (e - 18) * v[tot % 7]
        tot = t4 & 255
        v[e % 7] = (g >> 1) % 251
    return (tot + g ^ d) & 8191

def f(x):
    tot = x * x - (x << 1)
    t = x & tot
    m = tot & 13 & tot * t
    t0 = m + m & 8191
    t1 = 18 - t - (m + 9)
    t2 = tot * x % 4093
    t = fn0(t0, t1 % 4093, t2)
    t3 = (x + t) * t
    e = t3 & 4095
    for j in range(3):
        t4 = (10 ^ j) + e - e
        x = t4 % 4093
        p = 0
        while p < 8:
            t5 = 13 * tot + m
            m = t5 % 9973
            p = p + 1
        cur = 0
        while cur < 48:
            t6 = 11 ^ t | tot ^ j
            t7 = t6 - (cur ^ 6 ^ e)
            e = t7 & 16383
            cur = cur + 1
    t8 = t // 6
    t9 = t8 * (m + 20)
    u = t9 % 9973
    return (tot | u) % 17

if __name__ == "__main__":
    arg = 5
    expected = 10
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
