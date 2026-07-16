# Auto-extracted from ds_lt256k_500.jsonl
# record_id=378  entry=f  input='18'  output='2'  tokens=170907

def fn0(a, d, m):
    for cur in range(4):
        if a & m < 30:
            t0 = cur + m << 1
            d = t0 % 97
            t1 = (5 ^ a) - d
            a = t1 & 65535
        t2 = a >> 2
        t3 = t2 + (d ^ 7)
        d = t3 % 4093
        m = (a * d ^ m) % 97
    for j in range(5):
        for b in range(7):
            t4 = 17 & a ^ d
            d = t4 % 1009
        if d + a < 18:
            t5 = (19 & d) + a
            a = t5 & 65535
        else:
            t6 = 13 - m
            t7 = t6 * (d ^ m)
            m = (t7 >> 4) % 251
            a = (a << 2 ^ d) * 11 & 1023
    for tmp in range(10):
        for q in range(4):
            t8 = q * tmp * 9 + d
            m = t8 % 251
        for s in range(3):
            t9 = (17 - a | d ^ 15) + a
            d = t9 % 251
    aux = (d + a) % 1009
    t10 = d * d + (aux + a) + 9
    w = t10 % 251
    t11 = a * 18 * w
    m = t11 & aux
    return w - 16 & 1023

def fn1(j, d):
    s = d - j
    z = 0
    while z < 9:
        d = (j & 8) - z & 4095
        t0 = s * j
        t1 = t0 ^ z - 9
        d = t1 % 4093
        z = z + 1
    j = (d - j) * j % 4093
    nxt = 0
    while nxt < 7:
        t2 = nxt & j | 2 - s
        d = t2 & 16383
        if nxt - 7 ^ d <= 55:
            j = (nxt - 16 + j) % 4093
            t3 = (7 ^ d) - (d | 20)
            j = (t3 - 10 | j) % 251
        t4 = j >> 2
        t5 = t4 ^ (s | j)
        d = (t5 - d) % 251
        nxt = nxt + 1
    if 2 * s >= 26:
        t6 = (15 | d | j) << 4
        d = t6 & 255
    s = s - j & j
    tmp = 0
    while tmp < 6:
        p = 0
        while p < 8:
            t7 = ((17 ^ 14) << 2) + d | s
            s = t7 % 251
            j = (10 - 5 - j) % 251
            p = p + 1
        tmp = tmp + 1
    t8 = 15 * 2 + s
    return t8 % 251

def f(x):
    if 13 + x < 3:
        x = x << 1 | x
        x = x * x % 97 >> 4
    t0 = x * 18 * (x ^ 10)
    s = t0 - x
    nxt = s & x ^ x >> 3
    t1 = 5 - x & 255
    t2 = s % 9973 // 8
    t3 = (s + x ^ x) & 4095
    x = fn0(t1, t2 % 97, t3)
    a = nxt & s & (s & x)
    t4 = 18 + 10 ^ s
    for acc in range(9):
        x = ((acc ^ nxt) << 1) % 9973
        t5 = 17 - s | a
        a = t5 & 255
        for c in range(39):
            t6 = (10 + acc) * 10 + x
            s = (t6 + c) % 97
            s = (acc * 6 + x | s) % 9973
    return t4 % 97

if __name__ == "__main__":
    arg = 18
    expected = 2
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
