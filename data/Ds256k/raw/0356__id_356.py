# Auto-extracted from ds_lt256k_500.jsonl
# record_id=356  entry=f  input='9'  output='32'  tokens=210849

def rec(n, a):
    if n <= 0:
        return a
    buf = (n + a) * (a * n) % 4093
    t0 = a >> 3 | n * a
    t1 = t0 + (n * n + (buf - n))
    return rec(n - 1, t1 & 4095)

def fn0(a, e, g):
    t0 = (12 + (e ^ 7)) * a
    e = rec(87, t0 % 9973)
    if g >> 4 == 52:
        e = 15 - a
    t1 = e >> 3
    t2 = t1 | e ^ a
    t3 = g + e ^ g
    t4 = t2 * t3 & 4095
    a = rec(48, t4)
    w = 0
    while w < 2:
        g = g // 4 % 9973
        t5 = w * (20 * w) - g
        a = t5 % 9973
        tmp = 0
        while tmp < 4:
            t6 = (5 + e) * (a * g)
            t7 = t6 - ((6 ^ e) & g - w)
            a = t7 & 16383
            tmp = tmp + 1
        w = w + 1
    if e * e < 44:
        if g % 9973 > 38:
            t8 = (12 ^ g) + (a - 18)
            e = rec(41, t8 & 255)
            t9 = e * a - e
            g = (t9 ^ ((e | g) ^ g)) & 16383
    return (g * e >> 3) // 2 & 255

def f(x):
    prv = [272, 626, 1003, 347, 991, 791]
    t0 = 3 - 1
    t1 = x | 13
    t2 = t0 * (x | 3)
    t3 = t1 - x * 6
    y = t2 - t3
    for aux in range(5):
        t4 = x * prv[x % 6]
        y = (t4 ^ aux) % 9973
        t5 = x + 18 + aux
        prv[y % 6] = t5 * 10
        t6 = x * 16 // 5
        x = t6 + x & 255
    t7 = prv[x % 6] - y
    prv[x % 6] = (t7 - (x - y)) % 1009
    a = 11 * y & x
    for idx in range(32):
        for q in range(5):
            prv[a % 6] = (q + y) % 1009
            prv[x % 6] = q * a % 1009
            t8 = prv[y % 6] ^ q
            prv[idx % 6] = (10 | a) * t8 % 1009
        t9 = (x & 14) + x
        a = (t9 - idx) % 65521
        t10 = prv[y % 6]
        t11 = t10 - idx
        t12 = t11 * (idx * a)
        y = t12 % 9973
    u = 0
    while u < 11:
        a = (a >> 4) % 9973
        prv[u % 6] = 1 * x
        t13 = x * prv[y % 6] * a
        y = (t13 ^ u) % 9973
        u = u + 1
    t14 = (a & y) * x % 9973
    prv[a % 6] = t14 % 1009
    res = (y - 9 & x) + y
    s = y + 5
    t15 = a // 8 % 9973
    t16 = prv[res % 6]
    t17 = s + x
    t18 = t17 * (t16 // 4)
    t19 = t18 * s % 65521
    t20 = prv[a % 6]
    t21 = prv[s % 6]
    t22 = s - t20
    t23 = t22 ^ t21 + 14
    res = fn0(t15, t19, t23 % 9973)
    b = s * s % 9973
    t24 = prv[b % 6] & res
    return (x & 3 ^ t24) % 65521

if __name__ == "__main__":
    arg = 9
    expected = 32
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
