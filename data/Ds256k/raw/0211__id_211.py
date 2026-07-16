# Auto-extracted from ds_lt256k_500.jsonl
# record_id=211  entry=f  input='20'  output='27'  tokens=259938

def rec(n, a):
    if n <= 0:
        return a
    w = (n - a) % 97
    t0 = w * n - (n | w)
    t1 = (t0 + a) % 97
    return rec(n - 1, t1)

def fn0(e, g):
    idx = [223, 35, 84, 44, 158, 178, 169, 80]
    y = g * 4 - (2 - e)
    s = 0
    while s < 4:
        if 15 * 6 | e < 49:
            idx[y % 8] = (g >> 1) % 251
            idx[e % 8] = 8 * g % 251
        t0 = (4 ^ 11) + e ^ s
        g = t0 & 4095
        s = s + 1
    y = y - 10
    e = g - e
    t1 = (idx[g % 8] >> 1) + 2
    g = t1 & g
    t2 = (y << 2) - (g | 14)
    y = t2 & 65535
    cur = 0
    while cur < 10:
        if 12 ^ e == 16:
            t3 = e - cur
            t4 = t3 - (g ^ y)
            idx[e % 8] = t4 % 251
        else:
            t5 = (16 | e) & g
            y = (t5 + cur) % 97
            t6 = e - cur << 2
            e = t6 % 97
        cur = cur + 1
    t7 = (g >> 1) % 97
    e = rec(88, t7)
    t8 = e * 2 - 14 * e
    return (t8 | y) % 97

def f(x):
    t0 = x * x % 17
    x = rec(98, t0)
    for s in range(7):
        t1 = 4 * s * (s - 11)
        t2 = (t1 | (19 & 3) * s) + x
        x = t2 % 65521
        x = (s | 7) & x
        if s + 13 ^ x >= 61:
            t3 = (8 & x) - (x - 10)
            x = (t3 << 1) % 17
            t4 = x + s | 13 & 8
            x = ((1 | s) ^ t4) & 8191
        else:
            x = x >> 2 & 32767
    t5 = x % 65521 | x << 1
    t6 = ((x >> 3 << 4) + t5) % 65521
    t7 = (x ^ 7) & x
    x = fn0(t6, t7)
    m = x >> 1
    t8 = 13 + 7 << 4
    acc = t8 | x
    t = 0
    while t < 456:
        t9 = 11 + x + m
        m = t9 % 17
        t = t + 1
    t10 = acc * 15 + (acc + m)
    tot = t10 + m & 32767
    t11 = acc - x & 16383
    t12 = (m ^ 19) % 1009
    acc = fn0(t11, t12)
    tmp = 10 - acc + 12
    t13 = (m + acc) % 65521
    tmp = rec(113, t13)
    for hi in range(12):
        acc = ((19 | tmp) - acc) % 17
    t14 = (acc << 3) // 5
    z = (t14 ^ tot) & 255
    t15 = 10 + 9 | acc
    t16 = 9 + tmp >> 4
    v = t15 - t16
    return (2 ^ 8 | v) & 16383

if __name__ == "__main__":
    arg = 20
    expected = 27
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
