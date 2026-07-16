# Auto-extracted from ds_lt256k_500.jsonl
# record_id=204  entry=f  input='16'  output='189'  tokens=138409

def rec(n, a):
    if n <= 0:
        return a
    if n * 5 + a >= 35:
        t0 = a * 11 + (a - 8)
        a = t0 & a
    if n ^ a == 25:
        t1 = n // 2
        t2 = n + 4 | 1
        t3 = t1 ^ (a ^ 16)
        a = t2 * t3 % 17
    else:
        a = ((a | n) ^ a) % 17
        t4 = a + a ^ n
        a = t4 * n & 1023
    t5 = n >> 2 | a
    a = t5 % 17
    t6 = ((20 | n) - a << 4) % 9973
    return rec(n - 1, t6)

def fn0(m, d, b):
    for y in range(4):
        for c in range(7):
            t0 = (y & m) * d
            m = t0 & 65535
            b = (d + c) % 251
            t1 = 18 - b - d
            d = t1 & 8191
        t2 = y - d >> 2 >> 1
        m = t2 % 4093
        t3 = (m - d) * d
        m = (t3 | m) % 9973
    buf = ((b << 2) - m * d) % 251
    if m // 7 != 11:
        m = m - buf - b
    t4 = ((m & d) << 4 >> 1) % 65521
    b = rec(103, t4)
    t5 = buf // 2 // 3 & 1023
    m = rec(90, t5)
    for prv in range(9):
        t6 = (b ^ d) - buf | m
        m = t6 & 511
        buf = (b - buf) % 4093
        t7 = b << 3 ^ d - 1
        buf = (t7 | buf) % 4093
    for cnt in range(12):
        for tmp in range(9):
            t8 = 9 - cnt | m
            b = t8 - tmp & 1023
            m = (d | m) & 32767
        t9 = cnt + cnt ^ b
        d = t9 & 255
        b = (3 << 4) * d - b & 8191
    nxt = d // 4
    t10 = (b | buf) // 7
    return t10 & 32767

def fn1(d):
    lo = [195, 132, 41, 5, 584, 383, 24]
    for hi in range(2):
        t0 = (hi + d) * d
        t1 = t0 - ((11 ^ hi) + d)
        d = t1 & 65535
    if (11 << 4) - d < 23:
        for res in range(8):
            t2 = d - 4 + res
            d = t2 % 4093
            t3 = (d & 16) - lo[res % 7]
            d = (t3 | res) % 65521
    else:
        for tmp in range(3):
            t4 = lo[d % 7] & tmp
            d = (t4 | d + tmp) % 4093
    c = 0
    while c < 4:
        if c + d < 16:
            t5 = lo[c % 7]
            t6 = 4 * t5 * d
            d = t6 % 65521
            t7 = lo[c % 7] - 13 ^ d
            lo[c % 7] = t7 % 1009
        else:
            d = (d ^ 15 | c) & 2047
        c = c + 1
    j = d + d
    if j - 8 == 30:
        t8 = j + j + j
        t9 = t8 + (j | d) * j & 262143
        j = rec(96, t9)
        if 18 | d >= 5:
            t10 = d - j
            t11 = t10 + (d ^ 16)
            d = t11 >> 2
            t12 = j + j
            d = t12 ^ (j ^ 3)
    if d // 6 == 21:
        if 18 | d == 1:
            t13 = lo[d % 7]
            t14 = j - d & t13
            t15 = lo[d % 7]
            d = t14 + t15
        else:
            t16 = lo[d % 7]
            j = t16 - (9 ^ 10)
            j = 4 & j
    else:
        aux = 0
        while aux < 11:
            t17 = (aux - d) // 3 + aux
            j = t17 & 255
            j = (d - j) % 65521
            aux = aux + 1
        p = 0
        while p < 4:
            t18 = lo[p % 7]
            t19 = 17 * d * t18 ^ p
            lo[j % 7] = (t19 & 131071) % 1009
            p = p + 1
    t20 = d + d + (j - d)
    return t20 & j

def f(x):
    j = [20, 50, 16, 95, 27, 10, 24]
    if 19 - x < 34:
        for tmp in range(4):
            t0 = tmp ^ 6 ^ x
            x = t0 % 97
            t1 = x - tmp + (x ^ 3)
            x = (x & 16) - t1 & 131071
    else:
        x = 15 - 16 + x
    v = x ^ 1
    if v // 5 <= 6:
        v = v + x
        if x // 6 != 23:
            t2 = j[v % 7]
            j[x % 7] = (v // 8 ^ t2) % 97
            v = v * v
        else:
            t3 = j[x % 7] - 20
            t4 = 1 - 11 & x - 12
            t5 = t4 ^ t3 * (v * x)
            x = t5 % 97
            t6 = x * v << 4
            t7 = t6 ^ j[x % 7]
            x = t7 % 17
    else:
        for cur in range(3):
            t8 = 16 & cur | j[cur % 7]
            x = (t8 - x) % 17
            t9 = (cur - x) // 8
            t10 = j[v % 7]
            x = (t9 ^ t10) % 9973
        x = 7 * x & x * x
    t11 = x * x - 20 ^ x
    idx = t11 % 97
    t12 = 11 & 16 ^ v
    buf = t12 % 97
    t13 = (buf ^ 12) % 97
    x = rec(91, t13)
    t14 = (v ^ buf) * (x + 8)
    z = t14 % 17
    c = 18 * 15 - z
    lo = 0
    while lo < 30:
        for aux in range(6):
            t15 = x // 5 ^ v
            v = t15 % 97
        x = (x >> 2 | (idx | 2)) % 97
        lo = lo + 1
    t16 = 5 - j[v % 7] + 16
    a = t16 + 13
    t17 = (x ^ buf) // 6
    return (t17 - (buf - 18 + c)) % 251

if __name__ == "__main__":
    arg = 16
    expected = 189
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
