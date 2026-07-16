# Auto-extracted from ds_lt256k_500.jsonl
# record_id=400  entry=f  input='12'  output='204'  tokens=248186

def rec(n, a):
    if n <= 0:
        return a
    tmp = 0
    while tmp < 10:
        a = (a + 9 + (n >> 1)) % 9973
        tmp = tmp + 1
    t0 = a & n | n
    t1 = t0 * (n * 4 * a)
    return rec(n - 1, t1 & 1023)

def fn0(m, a, d):
    p = a ^ m
    prv = 0
    while prv < 4:
        if a & d >= 0:
            m = (a // 2 - m) % 4093
        else:
            a = m + a & 8191
            t0 = 15 * d + a
            a = t0 % 4093
        for q in range(3):
            t1 = p // 7 << 2
            t2 = t1 + 11 - q
            m = t2 & 2047
            t3 = m + 7 + a
            t4 = t3 - 6 ^ p
            p = t4 % 4093
        t5 = 10 + p ^ prv
        m = t5 % 4093
        prv = prv + 1
    a = a % 251 * 12
    d = a - m
    return (a & p) + p & 255

def fn1(b, m):
    e = [85, 41, 8, 6, 3, 47, 65, 64]
    for t in range(5):
        t0 = (t ^ m) >> 1
        b = t0 % 4093
        if b >> 4 <= 62:
            e[t % 8] = b // 5 % 97
            b = (t * 19 ^ b) & 16383
    t1 = m % 4093 | e[m % 8]
    t2 = e[m % 8]
    t3 = (8 ^ m) + t2 & 65535
    t4 = (3 * 4 ^ m) % 4093
    m = fn0(t1 & 16383, t3, t4)
    t5 = 9 << 4 | 9
    q = t5 << 2 | b
    t6 = (b + q) * m
    q = t6 * (m - q << 4) % 4093
    m = (b ^ 4) << 3
    j = 0
    while j < 3:
        e[q % 8] = (j + m) % 97
        j = j + 1
    t7 = (7 * m << 4 ^ b) - q
    return t7 & 4095

def f(x):
    for idx in range(8):
        if idx - x > 10:
            t0 = 1 * idx * 11
            x = t0 - x & 32767
            t1 = idx * idx + x
            x = t1 & 511
        x = x * 11 - idx & 1023
    if x + 16 >= 32:
        if x ^ 16 < 25:
            t2 = (x | 14) & x - 15
            x = t2 * x & 65535
            t3 = 17 + x
            t4 = t3 + (x - 4)
            x = rec(108, t4 % 1009)
        else:
            x = (x - 3) // 6
            t5 = (x ^ 3) * 1 % 17
            x = rec(111, t5)
        nxt = 0
        while nxt < 9:
            x = nxt * 12 & x
            t6 = 17 * nxt
            t7 = t6 - 16 * x
            x = t7 % 17
            x = x >> 4 & 16383
            nxt = nxt + 1
    for z in range(6):
        for v in range(3):
            x = (x - 13) % 1009
        x = (x * x + x) % 17
        for m in range(89):
            x = (x | 16) & 2047
    t8 = x + x
    t9 = t8 * (11 ^ x)
    t10 = (t9 | 18) % 1009
    t11 = (x + 5) // 4
    t12 = x + x & 17
    t13 = (t11 | t12) & 511
    x = fn1(t10, t13)
    for buf in range(8):
        x = buf - x & 32767
        x = (buf | x) >> 4 & 8191
    j = x >> 1
    t14 = (j + x) // 7 % 9973
    t15 = (x | j | j * x) * x
    t16 = j + 3 ^ x * j
    t17 = t16 * j & 2047
    x = fn0(t14, t15 & 262143, t17)
    t18 = (x - 11) * (x * 14) - j
    aux = t18 & 16383
    tmp = (aux ^ j) >> 1 << 3
    q = 0
    while q < 11:
        j = (q + 10 ^ x) & 255
        t19 = 13 & tmp | q
        aux = t19 & 2047
        q = q + 1
    if (6 << 2) - j != 27:
        for lo in range(5):
            x = (j - 17 + tmp | x) & 2047
    else:
        if aux - x >= 31:
            t20 = 17 * x
            t21 = 18 ^ 13
            t22 = t20 - (tmp & x)
            t23 = t21 - (j - 10)
            t24 = (t22 ^ t23) % 1009
            j = rec(106, t24)
            t25 = aux ^ tmp | 15 - x
            t26 = (tmp & 17 | tmp) * t25 & 32767
            t27 = (6 ^ tmp) & 32767
            x = fn1(t26, t27)
        else:
            aux = x - aux
    prv = (x + x) // 5 >> 4
    return prv + j + (x + aux) & 255

if __name__ == "__main__":
    arg = 12
    expected = 204
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
