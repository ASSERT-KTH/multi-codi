# Auto-extracted from ds_lt256k_500.jsonl
# record_id=289  entry=f  input='7'  output='2037'  tokens=140074

def fn0(g, c):
    c = 11 ^ g
    c = g % 65521
    g = 10 - g
    for tot in range(12):
        c = (4 * tot ^ g) % 65521
    g = g >> 2
    w = 0
    while w < 4:
        t0 = c & g
        t1 = t0 * (g | 9)
        g = t1 & 32767
        w = w + 1
    t2 = c + c
    t3 = t2 ^ c - g
    return t3 & 262143

def fn1(g, b, e):
    t0 = (e >> 1) * g & e
    t1 = (19 - e) % 4093
    e = fn0(t0, t1)
    t2 = g * g // 4
    t3 = t2 * ((e + e) * g)
    u = t3 & 1023
    g = (g | 18) // 4
    e = u + b
    t4 = g + g
    t5 = t4 - e // 8
    t6 = t5 // 5 - u
    return t6 % 4093

def f(x):
    t0 = x ^ 8 ^ 17 - x
    idx = (7 ^ x | x) * t0
    for tmp in range(8):
        if idx % 4093 < 18:
            t1 = tmp ^ 18
            t2 = t1 * (idx * 11)
            x = t2 & 1023
        else:
            t3 = x >> 4
            t4 = (x | tmp) ^ x
            t5 = t3 * (x | idx)
            idx = (t4 ^ t5) % 9973
        if (tmp ^ 17) + idx != 41:
            x = (idx // 3 << 4) - x & 65535
        else:
            x = (tmp ^ 9 | idx) % 97
    if idx + idx <= 35:
        t6 = 11 * x
        t7 = t6 + (idx ^ x)
        t8 = (16 - idx) % 4093
        x = fn0(t7 & 262143, t8)
        for d in range(10):
            idx = (6 * d & 8 | idx) % 4093
            t9 = (x ^ idx) + x
            x = t9 - x & 1023
            idx = x * d & 65535
    else:
        for u in range(6):
            x = x >> 4 & u
    c = 0
    while c < 7:
        for w in range(19):
            t10 = (c + c) * c | x | w
            idx = t10 % 4093
            t11 = w + w - idx
            idx = t11 & 32767
            idx = x // 2 - idx & 32767
        for buf in range(10):
            x = (c ^ x) // 5 % 97
        if c - 14 - idx >= 8:
            t12 = (4 * 12 & idx >> 4) - x
            x = t12 & 511
            t13 = (1 | 8) + (c ^ 7)
            x = t13 & (1 - idx | idx % 97)
        c = c + 1
    t14 = (idx | 20) >> 4
    t15 = x & idx ^ idx + idx
    t16 = x << 3 & 511
    x = fn1(t14 & x, t15 % 4093, t16)
    if idx - x <= 45:
        t17 = 3 | x
        t18 = t17 + (x + x)
        x = t18 ^ x
    if idx + idx <= 12:
        t19 = idx >> 3 & x
        t20 = t19 * (x * x % 4093) % 4093
        t21 = (idx ^ 20) & 65535
        t22 = idx + 4 >> 2 & 65535
        x = fn1(t20, t21, t22)
        for a in range(7):
            t23 = 1 + 5 ^ 11 | idx | x
            x = t23 & 4095
            idx = a * idx % 4093
    t24 = idx & 11
    t25 = t24 * (idx // 6)
    tot = (t25 | idx) % 4093
    t26 = (x - tot) // 4
    return t26 & 65535

if __name__ == "__main__":
    arg = 7
    expected = 2037
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
