# Auto-extracted from ds_lt256k_500.jsonl
# record_id=485  entry=f  input='5'  output='8'  tokens=141687

def rec(n, a):
    if n <= 0:
        return a
    d = (a - n) % 97
    q = n - a & 2047
    t0 = (12 + 19 + a) % 9973
    return rec(n - 1, t0)

def fn0(b, j):
    tot = [216, 126, 172, 22, 28, 227]
    t0 = (b - j) // 7
    e = t0 | (18 | b) >> 4
    for aux in range(11):
        for m in range(12):
            tot[aux % 6] = b // 2 % 251
            t1 = e ^ tot[j % 6]
            tot[aux % 6] = (t1 >> 2) % 251
            t2 = 8 * 19 - j
            e = t2 - m & 4095
        d = 0
        while d < 9:
            t3 = tot[aux % 6] * aux - b
            j = (t3 - j) % 65521
            d = d + 1
    if 17 * j != 1:
        t4 = tot[b % 6]
        t5 = t4 | tot[j % 6]
        t6 = (j | 9) ^ 6
        j = t6 + (t5 ^ (b | 10))
    t = 0
    while t < 3:
        t7 = b * tot[e % 6]
        e = t7 & 16383
        e = 8 + t + b + t & 511
        if j % 4093 != 35:
            t8 = (j + j) // 7
            b = (t8 + t) % 4093
            j = (t + e) % 4093
        t = t + 1
    for p in range(8):
        t9 = j >> 4 ^ b
        b = t9 % 4093
    for q in range(10):
        for res in range(5):
            b = (10 + b) % 65521
            t10 = (q + q | j) + res
            e = t10 & 1023
            t11 = (q & b) << 4
            t12 = t11 - (j + res + res)
            tot[b % 6] = t12 % 251
        t13 = j - 13 | q
        e = t13 & 255
    y = e + e & (j & b)
    a = b % 4093 - b
    t14 = j * a + a // 2
    return (t14 - a * b // 7) % 65521

def f(x):
    e = [674, 242, 606, 156, 802, 515]
    b = 0
    while b < 6:
        t0 = b - 8 ^ e[x % 6]
        x = t0 & 65535
        if b ^ x < 34:
            t1 = b & 1 ^ x
            x = t1 % 4093
        else:
            t2 = 17 ^ b
            t3 = t2 - (x | b)
            e[b % 6] = (t3 + b) % 1009
        t4 = (e[x % 6] ^ 2) << 4
        x = t4 & 65535
        b = b + 1
    t5 = x ^ 4
    t6 = t5 - (x | 3)
    x = rec(45, t6 % 4093)
    t7 = x & 8
    t8 = t7 + (x - 11)
    e[x % 6] = t8 % 1009
    t9 = x * x * x
    t10 = t9 | e[x % 6]
    z = t10 & 32767
    v = 0
    while v < 7:
        t11 = e[x % 6]
        t12 = t11 + e[v % 6]
        t13 = (v | e[v % 6]) * 7
        z = (x & 4 & t12 ^ t13) & 1023
        t14 = e[v % 6]
        t15 = z & t14
        t16 = t15 * (x - v)
        x = t16 % 17
        v = v + 1
    for aux in range(5):
        t17 = aux & 11
        t18 = t17 - 17 * 18
        z = (t18 ^ x) % 17
    prv = 0
    while prv < 12:
        e[x % 6] = (19 + 16 - x) % 1009
        for lo in range(8):
            z = ((19 + x) * x | lo) & 32767
            t19 = e[x % 6]
            e[lo % 6] = (t19 - lo) % 1009
            e[lo % 6] = prv * x % 1009
        if x * 20 < 22:
            t20 = prv - 19 + 12 ^ z
            x = t20 & 2047
            t21 = e[x % 6] >> 4
            e[prv % 6] = (t21 - z * 4) % 1009
        prv = prv + 1
    return (z >> 2) % 17

if __name__ == "__main__":
    arg = 5
    expected = 8
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
