# Auto-extracted from ds_lt256k_500.jsonl
# record_id=318  entry=f  input='15'  output='16372'  tokens=229006

def fn0(g, j, e):
    j = g ^ j
    for y in range(10):
        t0 = (9 ^ 14) + g
        t1 = t0 - (y - 10)
        g = t1 & 131071
    for cnt in range(4):
        t2 = cnt | e
        t3 = t2 | g - cnt
        t4 = 5 + 15 + 4
        e = (t3 | t4) % 251
        t5 = e * cnt
        t6 = t5 - (e ^ 10)
        e = t6 & 262143
        g = (6 & 13) - g & 4095
    e = 8 - 15 ^ e
    for a in range(5):
        g = (e - 20 | g) % 251
        for t in range(2):
            t7 = e >> 4 ^ j
            j = t7 % 251
            t8 = (t | 10) + 14
            g = t8 * (g * t % 17) % 17
        t9 = 5 + a ^ g
        e = t9 & 2047
    return j + 1 & g - e

def f(x):
    if x << 3 == 11:
        if 10 + x > 7:
            x = x ^ 12
        x = 7 & x
    m = x + 12
    t0 = (m | 11) & 4095
    t1 = (17 + 8 ^ m) % 97
    t2 = 8 - m & 4095
    m = fn0(t0, t1, t2)
    t3 = m & 4 | 10 ^ m
    t4 = (m & 14 ^ x) + t3
    t5 = m + m & x
    t6 = (m ^ 8) * (m * 14) // 2
    m = fn0(t4 & 8191, t5, t6 % 97)
    for t in range(7):
        x = t * m % 4093
        cur = 0
        while cur < 2:
            x = (x >> 4) % 97
            cur = cur + 1
        m = (x ^ 18 | t) & 8191
    z = 0
    while z < 12:
        m = x - m & 255
        if m >> 2 != 64:
            t7 = z * x + (x + 3)
            m = t7 // 2 % 97
            x = (x * 11 - 13 - m) % 4093
        if x - 18 == 8:
            m = (m - 20) * x % 251
            t8 = 4 * 16 << 1
            t9 = x - z | 2
            m = t8 * t9 % 65521
        else:
            x = x - z & 131071
        z = z + 1
    x = x & 17 ^ x
    for val in range(4):
        t10 = m & val ^ val * m
        x = t10 % 251
        for g in range(33):
            t11 = val << 2
            t12 = t11 | m // 4
            x = (t12 ^ g) & 4095
            t13 = g ^ val
            t14 = t13 | m + val
            t15 = m ^ x ^ m
            x = t14 - t15 & 511
            m = (val * g - g ^ x) % 4093
        for tmp in range(7):
            m = (val * x >> 4 | tmp) % 65521
    t16 = (m | x) >> 4
    return t16 - m & 16383

if __name__ == "__main__":
    arg = 15
    expected = 16372
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
