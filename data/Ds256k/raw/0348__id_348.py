# Auto-extracted from ds_lt256k_500.jsonl
# record_id=348  entry=f  input='18'  output='629'  tokens=98069

def rec(n, a):
    if n <= 0:
        return a
    for m in range(8):
        a = (17 * n + a) % 4093
        t0 = a + n | n
        a = t0 * ((n >> 4) - m) % 97
    t1 = a - 16
    t2 = t1 - a * a
    t3 = 16 & a >> 1
    t4 = t2 + t3 ^ n
    y = t4 % 4093
    t5 = (n // 3 | a) & 16383
    return rec(n - 1, t5)

def fn0(d, m):
    for e in range(4):
        m = (d << 1) - e & 255
        d = (m | d) & 16383
    val = 0
    while val < 11:
        m = (d + d ^ m) % 65521
        val = val + 1
    t0 = (m + d | d) % 97
    d = rec(120, t0)
    aux = 13 ^ m
    t1 = (9 | m) & 2047
    aux = rec(57, t1)
    if d + aux < 1:
        v = 0
        while v < 2:
            t2 = (aux - v) * aux
            m = t2 % 97
            t3 = (11 | m) - d
            d = t3 & 8191
            t4 = m - aux + v
            d = t4 % 97
            v = v + 1
    else:
        t5 = (aux << 4) - m
        m = t5 & 32767
        for acc in range(3):
            d = d - acc & 511
    for cur in range(10):
        t6 = (18 ^ d) & m + cur
        d = (t6 ^ aux * 13 * 1) % 17
        aux = (m // 8 | aux) % 97
        if m | cur >= 31:
            aux = (d + 14 ^ aux) % 17
            t7 = cur - 20 + m
            d = t7 // 8 & 131071
    return aux & d

def fn1(e, g):
    hi = [214, 60, 84, 150, 141]
    for acc in range(6):
        if e // 2 >= 11:
            t0 = (acc | 11) + g
            hi[acc % 5] = t0 % 251
        t1 = acc - 10 + 17
        g = t1 & (acc * acc | e)
    v = (4 ^ g) // 3 ^ g
    hi[e % 5] = v // 7 % 251
    for m in range(5):
        t2 = v ^ hi[g % 5]
        g = (g - 8 | t2) * e % 1009
        t3 = v // 8 - e
        e = t3 * e & 4095
        e = e & 7
    t4 = 19 * hi[g % 5]
    j = t4 - e >> 2
    t5 = g - hi[e % 5]
    t6 = t5 + (j | 13)
    return (t6 | hi[g % 5]) & 32767

def f(x):
    j = [127, 24, 213, 70, 1]
    cur = 0
    while cur < 3:
        for u in range(12):
            x = x & 8191
        cur = cur + 1
    z = 0
    while z < 5:
        buf = 0
        while buf < 19:
            x = x & 1023
            x = ((x | buf) ^ 6) & 1023
            t0 = z ^ j[z % 5]
            j[z % 5] = (t0 | x) % 251
            buf = buf + 1
        if x * x != 21:
            t1 = x + j[z % 5]
            x = (t1 - (8 ^ z)) % 65521
        t2 = (z ^ 9) & j[z % 5]
        t3 = (z * z | 13 + z) ^ t2
        x = (t3 - x) % 65521
        z = z + 1
    w = 20 ^ x
    t4 = x * w & 255
    j[w % 5] = t4 % 251
    t5 = 14 - 19
    t6 = t5 + (w - 9)
    b = t6 ^ x
    for q in range(5):
        t7 = b - j[w % 5]
        w = (b | 16 | t7) % 97
        t8 = j[w % 5]
        x = (t8 + j[x % 5]) % 1009
    t9 = x * 2 & 2047
    t10 = (x | b ^ w) & 511
    w = fn1(t9, t10)
    t11 = x * b % 1009
    t12 = x * b
    t13 = t12 & x // 4
    b = fn1(t11, t13)
    t14 = (w + x) // 6
    d = t14 | x
    t15 = j[x % 5] - 13
    j[d % 5] = (t15 & (b | 6)) % 251
    for lo in range(8):
        t16 = (b | 3) + (d & lo)
        b = t16 % 97
        x = (2 | x) & d
    tmp = w | j[w % 5]
    for a in range(11):
        t17 = (w >> 1) - b
        b = t17 % 65521
        if d - w != 27:
            t18 = 20 - b ^ 12 & w
            j[b % 5] = t18 & 11
        t19 = (w >> 4) - tmp
        tmp = t19 & 32767
    cnt = (14 * b + w) % 1009
    idx = 0
    while idx < 6:
        if w - d == 34:
            t20 = j[x % 5] | d
            t21 = (10 | w) + 9
            t22 = t20 // 4 * t21 % 65521
            j[d % 5] = t22 % 251
        else:
            t23 = x + d - cnt
            cnt = t23 % 1009
        idx = idx + 1
    for aux in range(7):
        j[tmp % 5] = x - d & 16
    return 13 * d % 1009

if __name__ == "__main__":
    arg = 18
    expected = 629
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
