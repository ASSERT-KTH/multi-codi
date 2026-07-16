# Auto-extracted from ds_lt256k_500.jsonl
# record_id=91  entry=f  input='5'  output='302'  tokens=254533

def rec(n, a):
    if n <= 0:
        return a
    cnt = (a * a >> 1) + n & 16383
    t0 = ((a | cnt) - n) * 9
    aux = t0 % 17
    t1 = (11 ^ 8) + (n * 15 - n)
    aux = t1 - a & 32767
    t2 = (18 ^ a) % 97
    return rec(n - 1, t2)

def fn0(a, c, e):
    e = (c | 5) // 6 & 3
    nxt = 0
    while nxt < 2:
        t0 = (a & 7) - c
        t1 = (e - 8) // 2
        e = t0 + t1 & 8191
        nxt = nxt + 1
    t2 = (c >> 4) * c
    t3 = 16 * c // 7
    t4 = (t2 - t3) % 97
    c = rec(21, t4)
    if a | 18 > 10:
        for d in range(9):
            t5 = (15 | a) + 6 << 2
            a = t5 % 97
            t6 = e - d >> 3 >> 3
            a = t6 & 131071
            a = (2 + a) % 251
        t7 = (c >> 2 | c ^ e) * e
        e = t7 % 97
    else:
        e = e - a - a
        c = e | 10 | c
    a = e + 10
    if a - 15 > 23:
        t8 = (2 + c << 2) // 4 & 262143
        c = rec(41, t8)
    c = (c | 8 | e) + 3 & 131071
    prv = 0
    while prv < 5:
        t9 = a + a - a
        t10 = t9 ^ (a ^ 1) // 2
        a = t10 & 32767
        prv = prv + 1
    return c & 15

def fn1(b):
    val = [70, 311, 912, 705, 862, 270, 333, 230]
    if 8 | b == 53:
        p = 0
        while p < 2:
            b = p * b & 511
            t0 = p - 13 ^ b
            b = t0 & 65535
            p = p + 1
    d = 0
    while d < 12:
        b = (b ^ 10) & 1023
        d = d + 1
    t1 = b // 2 % 17
    t2 = b // 5 * 5
    t3 = b + 11 + 10
    t4 = b + val[b % 8] & 32767
    b = fn0(t1, t2 & t3, t4)
    t5 = val[b % 8] - b & b
    t6 = (t5 - 4) % 17
    b = rec(68, t6)
    hi = 0
    while hi < 6:
        if hi * b > 44:
            val[b % 8] = (b + hi ^ b) // 7 % 1009
            val[b % 8] = (hi * 18 | b) % 1009
        for g in range(5):
            t7 = b & 8 | g
            val[g % 8] = t7 * hi
        hi = hi + 1
    prv = 0
    while prv < 3:
        t8 = val[prv % 8]
        t9 = (4 + t8) // 2
        b = t9 + b & 32767
        if prv - val[prv % 8] + b < 5:
            b = b + prv & 8191
        else:
            t10 = val[b % 8] | 20
            b = (17 ^ 14) * t10 & 1023
            t11 = val[b % 8] - prv
            val[b % 8] = ((t11 ^ b) - prv) % 1009
        q = 0
        while q < 9:
            t12 = (2 * prv | prv) ^ b
            b = t12 & 65535
            q = q + 1
        prv = prv + 1
    t13 = (b | 16) // 4
    t14 = t13 // 3 & 255
    b = rec(104, t14)
    for w in range(12):
        nxt = 0
        while nxt < 2:
            t15 = w + w | b
            val[b % 8] = t15 % 1009
            b = w - b & 32767
            t16 = (1 + nxt | 6 * b) + nxt
            b = t16 % 17
            nxt = nxt + 1
    t17 = val[b % 8]
    t18 = b + b | t17
    return t18 & 4095

def f(x):
    hi = [68, 47, 45, 83, 50]
    for res in range(4):
        x = res - x & 9
        x = ((15 * x | x) << 1) % 1009
    for aux in range(88):
        for c in range(9):
            hi[aux % 5] = (x + 18) % 97
            t0 = c * 12 + x
            x = t0 % 97
        t1 = hi[x % 5]
        t2 = t1 // 6 * aux
        x = t2 % 1009
    p = 2 ^ x
    t3 = hi[p % 5]
    t4 = x * p
    t5 = (p ^ 16) - t3
    t6 = t4 - p // 3
    q = (t5 ^ t6) & 32767
    s = 7 - p
    t7 = hi[s % 5] - 3 >> 4
    tot = t7 - 20
    if p >> 3 == 42:
        for acc in range(9):
            t8 = x + tot - hi[tot % 5]
            hi[acc % 5] = t8 % 97
            t9 = acc - p ^ acc
            t10 = s // 5 - q
            q = (t9 - t10) % 1009
    if x ^ 9 == 49:
        q = (20 | tot) + 6
    t11 = x - hi[q % 5]
    g = (t11 >> 3) * (7 << 1)
    if p ^ q == 53:
        hi[q % 5] = (x >> 3) * 5 % 97
        for cnt in range(11):
            hi[g % 5] = ((13 ^ s) - g) % 97
            t12 = 8 * q // 5
            t13 = t12 * q | x
            x = t13 & 511
            t14 = (p | 14) // 3 | tot
            tot = t14 & 65535
    else:
        q = (s >> 1 & 19) * p
    t15 = hi[s % 5]
    t16 = hi[x % 5]
    t17 = x - 2
    t18 = q // 6 & t15
    t19 = t17 * (tot | t16)
    v = (t18 | t19) & 511
    for w in range(12):
        t20 = hi[tot % 5]
        t21 = (t20 ^ 20) + w
        g = t21 % 97
        t22 = 8 - s + s
        g = t22 + g & 131071
    t = 0
    while t < 10:
        hi[p % 5] = tot * t % 97
        t = t + 1
    t23 = hi[v % 5] & v
    t24 = tot // 8 & g
    t25 = t24 * ((17 | p) * t23) & 32767
    hi[v % 5] = t25 % 97
    for buf in range(7):
        g = (q % 1009 ^ buf) & 2047
    return (x >> 3 ^ s) & 511

if __name__ == "__main__":
    arg = 5
    expected = 302
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
