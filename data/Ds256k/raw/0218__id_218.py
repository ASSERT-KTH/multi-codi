# Auto-extracted from ds_lt256k_500.jsonl
# record_id=218  entry=f  input='1'  output='21'  tokens=24125

def fn0(d, g, a):
    q = [73, 59, 28, 104, 214, 114, 47]
    if q[a % 7] & g <= 5:
        g = (a + 9) % 9973
    else:
        d = g + d - 11
    m = g & 8
    if 19 ^ d < 56:
        m = a - 16 + d
        d = g >> 2 << 1 & m
    else:
        t0 = (a + a) * (18 | a)
        a = (t0 + d) % 9973
        tmp = 0
        while tmp < 12:
            t1 = m & 13 & g
            t2 = q[g % 7]
            q[d % 7] = (t1 - t2) % 251
            tmp = tmp + 1
    g = (d | a) % 17 & d
    t3 = g + g | d | m
    return t3 % 17

def fn1(a, g):
    t0 = (a - 10) * g
    t = t0 + a & 16383
    c = 8 + 12 + a
    p = 0
    while p < 4:
        if t ^ p == 42:
            t1 = 19 + 1 + c | a
            a = t1 & 255
            t2 = (g ^ 1) - c
            c = t2 & 2047
        t3 = p * 6 * a
        a = t3 * (3 - p - a) % 65521
        p = p + 1
    tmp = (g ^ t) - g // 8
    t4 = (6 + a) % 1009
    t5 = (g - a) * a
    t6 = (t5 >> 2) % 65521
    t7 = ((8 & 6) - (5 & tmp)) % 65521
    g = fn0(t4, t6, t7)
    t8 = (c | t) + g
    return t8 % 17

def f(x):
    t = x & 19
    for p in range(119):
        if p ^ t > 19:
            t0 = (t << 1) - p
            x = t0 % 1009
        else:
            t1 = t - p ^ t * p
            t2 = t1 - (x >> 1 ^ (15 ^ t))
            t = t2 % 4093
    t = t + 7
    return (x >> 1 | t) % 97

if __name__ == "__main__":
    arg = 1
    expected = 21
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
