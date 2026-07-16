# Auto-extracted from ds_lt256k_500.jsonl
# record_id=250  entry=f  input='5'  output='13'  tokens=167054

def rec(n, a):
    if n <= 0:
        return a
    t0 = (n & a) << 3
    t = t0 // 3 % 251
    if t * n <= 50:
        t = (9 * n ^ t) % 65521
    return rec(n - 1, n & a)

def fn0(m, c, g):
    for idx in range(8):
        q = 0
        while q < 10:
            m = c + m & 262143
            q = q + 1
        t0 = m // 2 >> 3
        t1 = t0 | m | g
        g = t1 % 4093
    t2 = (m | c) - m * 6
    g = t2 << 3 & 511
    if c >> 4 != 48:
        for j in range(5):
            t3 = g * 15 << 1
            g = t3 >> 4 & 1023
            t4 = (j + 6) * 16
            t5 = (g & c) - j
            c = t4 * t5 % 65521
        for u in range(8):
            c = (m * 11 + m - c) % 4093
            g = u + g & 2047
            g = (c | g) % 65521
    else:
        if m << 4 == 6:
            g = (c - 1 & (m ^ 2)) + 1
    if g >> 2 != 15:
        c = (m ^ 9) << 4 & 1023
        t6 = (g - c ^ g) * g % 65521
        g = rec(60, t6)
    else:
        t7 = c + 4 ^ m * g
        m = rec(77, t7 % 4093)
        t8 = (m - 6) % 65521
        g = t8 * g % 65521
    for cur in range(7):
        c = g // 7 + c & 65535
        g = (cur * cur | c) & 32767
        if g // 6 >= 38:
            m = g * c - cur & 32767
            m = (cur + g) % 65521
        else:
            c = (3 ^ 20 | g) - c & 32767
            t9 = (14 | m) + g
            m = t9 - m & 255
    for tot in range(4):
        c = 15 * c % 65521
    g = (c | 16) - g
    return (g - m) % 65521

def fn1(c, b, a):
    aux = 0
    while aux < 8:
        c = c * aux & aux
        a = c & aux
        aux = aux + 1
    for s in range(10):
        for buf in range(11):
            b = (s + a - b) % 251
            c = (18 + 1 | c) & 65535
            t0 = s & a - s
            b = (t0 - buf) % 251
    if c + b >= 55:
        q = 0
        while q < 11:
            t1 = c + q
            t2 = t1 + c % 9973
            c = (t2 - b) % 251
            q = q + 1
        y = 0
        while y < 7:
            t3 = b & c
            t4 = t3 | b * y
            b = t4 << 2 & 1023
            t5 = a - b - y
            c = t5 & 4095
            y = y + 1
    else:
        c = b // 8
        t6 = (9 ^ 1) << 4
        b = t6 ^ c
    c = a ^ b | 5
    c = (a * a | a) % 9973
    c = b ^ 18 ^ b % 9973
    return (5 + b >> 2 ^ 5) % 9973

def f(x):
    res = [14, 47, 94, 40, 45, 28, 55, 7]
    c = 0
    while c < 10:
        t0 = res[c % 8]
        t1 = t0 * res[c % 8]
        x = (t1 ^ c | x) & 255
        x = ((x << 3) * c >> 4) % 17
        t2 = (res[c % 8] & 1) - x
        x = t2 % 4093
        c = c + 1
    q = 3 ^ x
    aux = x * x // 6 & x
    t3 = res[aux % 8]
    t4 = aux // 8 + aux
    t5 = (5 & q) - t3
    lo = t4 | t5
    res[aux % 8] = (18 + aux) % 97
    b = (aux >> 4) * aux << 4 & 2047
    if b - x <= 25:
        if q - lo < 36:
            t6 = q + lo + aux
            q = t6 >> 3
            aux = x // 8
        else:
            t7 = res[aux % 8]
            res[lo % 8] = (aux - t7) % 97
        t8 = (b | lo) - q
        x = t8 * (4 + lo << 1) % 17
    else:
        t9 = res[b % 8]
        t10 = t9 // 5
        t11 = t10 * (x >> 4)
        t12 = (q + 11) * (b >> 4) & 8191
        t13 = (x + 13 | aux) & 255
        x = fn0(t11 % 17, t12, t13)
    t14 = res[q % 8] % 17
    a = (t14 & q) + b
    for j in range(46):
        z = 0
        while z < 3:
            t15 = (z + 8) * (a * 8) // 7
            lo = t15 % 4093
            z = z + 1
        if aux | 13 != 59:
            t16 = a // 4 | lo
            lo = t16 & 16383
            t17 = (8 & a) - a
            t18 = t17 - res[b % 8]
            q = (t18 | q) % 17
    t19 = res[lo % 8]
    p = t19 - x ^ b
    acc = 0
    while acc < 12:
        x = q & acc
        t20 = res[acc % 8] // 3 - q
        b = t20 % 17
        t21 = res[aux % 8] + acc
        x = (4 & 1) * t21 & 32767
        acc = acc + 1
    t22 = (a // 2 + (b - q)) * b
    return t22 % 17

if __name__ == "__main__":
    arg = 5
    expected = 13
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
