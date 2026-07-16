# Auto-extracted from ds_lt256k_500.jsonl
# record_id=396  entry=f  input='2'  output='9727'  tokens=14855

def fn0(c, a, d):
    cur = 6 & a ^ c
    val = 6 - c - 2
    t0 = a - c + (cur >> 2)
    t1 = t0 * (val - cur + 9)
    a = t1 % 1009
    c = 6 & 16 ^ c
    if c - 1 > 17:
        c = c - 19 >> 2
    else:
        d = val ^ 16
    t2 = d ^ 2 | 15 ^ cur
    return t2 % 9973

def fn1(b):
    w = [502, 848, 377, 372, 895, 433, 241]
    c = 0
    while c < 5:
        t0 = w[b % 7]
        t1 = 2 * b
        t2 = t1 + (c + t0)
        t3 = w[b % 7]
        b = t2 * t3 & 511
        t4 = c + c | b
        b = t4 & 131071
        c = c + 1
    g = (b >> 1) - b
    b = 15 * 6 >> 3 ^ b
    if 17 * g == 48:
        t5 = (16 ^ g) * b % 251
        t6 = (20 * 15 - g) % 9973
        t7 = w[b % 7] - g
        t8 = (t7 - (16 << 4)) % 65521
        g = fn0(t5, t6, t8)
    else:
        for hi in range(3):
            t9 = ((b | g) ^ hi) + b
            w[hi % 7] = t9 % 1009
    g = 13 ^ g
    q = 0
    while q < 5:
        for m in range(8):
            t10 = 18 << 2 ^ g
            b = (t10 | b) % 65521
            t11 = (g * b >> 2) + m
            g = t11 & 16383
        t12 = w[q % 7] * 1
        t13 = t12 * (q ^ 10) >> 3
        g = (t13 + b) % 9973
        g = g & q
        q = q + 1
    t14 = g - b & 15 * b
    t15 = b >> 2 ^ (g | b)
    b = (t14 ^ t15) & 511
    t16 = (b | g) & 32767
    t17 = g // 3 % 9973
    t18 = g * b % 65521
    b = fn0(t16, t17, t18)
    return (g // 5 + g * b) % 65521

def f(x):
    v = x & 8
    if x ^ 7 != 14:
        t0 = v + x
        t1 = x & 13
        t2 = t0 | x << 2
        t3 = t1 * (x * x)
        v = t2 | t3
        x = x + v
    else:
        t4 = v * x + v
        x = (t4 - x) % 65521
        if x + x == 3:
            t5 = (v << 1) % 251
            t6 = (x + v + x) * 17 & 65535
            t7 = 11 - v - x
            t8 = t7 >> 3 & 32767
            v = fn0(t5, t6, t8)
            t9 = x + x & 131071
            t10 = (v | 15) & 16383
            t11 = x * v % 9973
            x = fn0(t9, t10, t11)
        else:
            t12 = x - 8 + (x >> 2)
            t13 = (7 & x) * x >> 2
            t14 = (x | 8) & 511
            x = fn0(t12 % 65521, t13 % 9973, t14)
            v = (x + v) * x & 32767
    s = x - v >> 1 ^ x
    t15 = 6 - v << 2
    t16 = v // 4 << 3
    t = t15 * t16 % 9973
    t17 = x ^ 6 ^ t
    for buf in range(18):
        t = (9 * x ^ t) & 32767
        if s | 3 > 51:
            t18 = s - 20 | buf
            t = t18 % 9973
            t19 = (s - x) * t
            s = t19 & 255
        else:
            t20 = (17 ^ t) * (x << 3)
            x = t20 & 1023
        t21 = (s // 2 >> 4) + v
        v = t21 & 255
    return t17 % 9973

if __name__ == "__main__":
    arg = 2
    expected = 9727
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
