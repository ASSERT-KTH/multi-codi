# Auto-extracted from ds_lt256k_500.jsonl
# record_id=449  entry=f  input='1'  output='0'  tokens=178232

def fn0(g, m):
    idx = (m - g) // 8 + g
    for b in range(4):
        cnt = 0
        while cnt < 8:
            idx = (idx + m) % 9973
            t0 = g - 15 - (19 + cnt) - g
            g = t0 & 255
            t1 = 19 * g
            t2 = t1 & (14 ^ idx)
            g = t2 & cnt
            cnt = cnt + 1
    if m + m == 52:
        if m + m <= 18:
            t3 = m - 10 ^ 7
            t4 = (idx & g) << 1
            idx = t3 - t4
            t5 = (g | idx) + g * g
            m = t5 % 9973
        else:
            idx = (g >> 4) - (9 | idx)
        for nxt in range(10):
            m = (nxt + m) * g % 251
    else:
        for t in range(5):
            t6 = (5 | g) + m
            m = t6 % 251
            idx = (idx // 7 - 4) % 251
    c = (idx ^ 3) >> 4
    for lo in range(3):
        if c * c <= 54:
            g = (m + idx ^ lo) % 9973
        t7 = lo & c
        t8 = t7 + (g - m)
        t9 = (3 | idx) + g
        m = t8 - t9 & 131071
    for u in range(12):
        t10 = 7 - c + u + 3
        g = t10 % 1009
    t11 = m * g
    t12 = 18 | g | 1
    t13 = t11 | g * idx
    prv = t12 + t13 & 1023
    t14 = (13 - 16) * (1 + g) | c
    return t14 & 131071

def f(x):
    res = [116, 119, 174, 53, 208, 1, 187]
    t0 = res[x % 7] * 15
    t1 = x * res[x % 7]
    t2 = x + x | t0
    d = t2 - t1 * 17
    t3 = 11 + x ^ d
    acc = t3 | (d - 19) // 3
    t4 = res[x % 7] - 16
    t5 = x - d & t4
    t6 = t5 - res[x % 7]
    t7 = (acc ^ 13 ^ acc) & 16383
    x = fn0(t6 & 131071, t7)
    for j in range(6):
        t8 = (d ^ acc) * 18 * d
        d = t8 % 97
        if 15 - x == 61:
            res[acc % 7] = (8 ^ d) % 251
        t9 = x * 6 << 3
        x = t9 % 97
    t10 = d & x | acc
    aux = t10 >> 2
    t = d << 3
    t11 = x % 65521
    t12 = t11 & (d ^ acc)
    cur = t12 ^ 2
    t13 = d // 2 % 251
    t14 = res[aux % 7]
    t15 = acc & t
    t16 = t15 | d & t14
    d = fn0(t13, t16 % 251)
    for idx in range(6):
        t17 = res[acc % 7] + 17
        aux = t17 - idx & 65535
        for p in range(16):
            t18 = 8 + idx + p - t
            d = t18 % 97
            acc = acc << 3 & 16383
            t19 = 20 + idx - (p * p + 2)
            res[aux % 7] = ((t19 ^ t) & 1023) % 251
    return (18 ^ cur) & 16383

if __name__ == "__main__":
    arg = 1
    expected = 0
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
