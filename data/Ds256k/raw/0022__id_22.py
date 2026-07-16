# Auto-extracted from ds_lt256k_500.jsonl
# record_id=22  entry=f  input='6'  output='15'  tokens=123626

def rec(n, a):
    if n <= 0:
        return a
    val = 0
    while val < 5:
        a = (a - 3) % 65521
        a = n * val - a & 262143
        t0 = (8 ^ n) * (n + n) * val
        a = t0 - a & 2047
        val = val + 1
    for idx in range(8):
        t1 = n & 11 | a ^ idx
        a = ((idx - a & n) + t1) % 9973
        a = (idx & a) - 1 & 20
    t2 = (a - 2) % 9973
    aux = t2 - n & 511
    t3 = (n + a) * n % 9973
    return rec(n - 1, t3)

def fn0(b, c, j):
    for g in range(11):
        t0 = b - j
        t1 = j - b & 3
        t2 = t0 * (b + b)
        j = t1 * t2 % 65521
        c = j * g + 3 & 8191
    t = b // 8
    b = 10 & j
    j = t % 9973
    t3 = ((c | j) + (4 - j)) % 65521
    j = rec(96, t3)
    y = 0
    while y < 9:
        t4 = ((j | y) & y) + b
        j = t4 & 4095
        for prv in range(4):
            t5 = (prv << 2) + (j ^ 12)
            c = t5 % 65521
        b = (7 * b ^ c) - y & 8191
        y = y + 1
    t6 = (t | 15) * 2
    return t6 & 262143

def fn1(j, m):
    nxt = 0
    while nxt < 3:
        t0 = j ^ 15
        t1 = t0 - (nxt ^ 3)
        j = (t1 ^ 12) % 4093
        nxt = nxt + 1
    c = j - m
    tot = 0
    while tot < 4:
        t2 = c >> 3 | tot
        j = t2 % 4093
        a = 0
        while a < 7:
            c = m + a >> 2 & 8191
            a = a + 1
        j = tot - c & 16383
        tot = tot + 1
    for val in range(11):
        b = 0
        while b < 12:
            t3 = c + 2 - b
            j = t3 & 32767
            b = b + 1
        c = (val | 20) & m + 3
        for v in range(12):
            j = (c + c >> 4 | v) % 4093
            t4 = (v - val) * (j // 5)
            m = m * j * val * t4 % 9973
    y = (j >> 3) // 6
    t5 = (14 - c) // 5
    t6 = t5 * ((y & j) + c)
    return t6 & 1023

def f(x):
    p = [64, 22, 5, 27, 89]
    if x > 11:
        x = x & 18
    for res in range(8):
        if res | x <= 0:
            p[x % 5] = res | x
    t0 = p[x % 5] - 9 + x
    acc = t0 * x
    for b in range(249):
        if 2 - x > 18:
            x = (x & 18 ^ x - 6) % 97
        else:
            x = acc - x & 262143
        t1 = 16 + b ^ x % 251
        p[x % 5] = t1 % 97
        p[b % 5] = (acc | 18) % 97
    u = (3 + acc) * x & 1023
    prv = acc - 5
    for v in range(11):
        t2 = p[v % 5]
        acc = t2 & prv
        x = (v - 5 + 11 + u) % 9973
        if prv * x == 49:
            t3 = 12 - v + 16 + x
            u = t3 % 9973
    for e in range(3):
        u = (((acc & u) >> 3) + e) % 9973
        acc = (e | x) & 262143
        if 9 ^ prv == 11:
            t4 = prv + p[e % 5]
            p[x % 5] = t4 % 97 >> 2
            t5 = (x ^ u ^ prv) + 7 | e
            acc = t5 & 16383
        else:
            t6 = (e ^ u ^ prv * u) & 65535
            p[e % 5] = t6 % 97
            t7 = e ^ prv
            t8 = p[x % 5]
            t9 = p[x % 5]
            t10 = prv & t8
            t11 = t7 + (e - 18)
            t12 = t10 ^ t9 - u
            x = t11 * t12 % 97
    w = 10 * u
    z = 0
    while z < 8:
        prv = (x - z ^ w) % 251
        t13 = p[u % 5]
        t14 = (u & 9 ^ t13) + x
        x = t14 % 251
        if 17 * u != 14:
            x = prv * z >> 1 & 1023
        z = z + 1
    t15 = p[x % 5] + 15 | x
    p[prv % 5] = t15 % 97
    buf = w % 251 & x
    hi = u * prv * 10 & 65535
    if w - p[x % 5] <= 6:
        if 6 + hi == 41:
            t16 = 8 ^ p[x % 5]
            t17 = buf - u ^ t16
            t18 = t17 | p[prv % 5]
            p[prv % 5] = t18 % 97
            t19 = p[x % 5] * buf
            t20 = buf - prv - 7 * hi
            p[acc % 5] = (t20 & t19 + 3) % 97
        else:
            t21 = p[buf % 5] ^ w
            t22 = hi - u & x
            t23 = (t22 + t21 * prv) % 9973
            p[acc % 5] = t23 % 97
        for val in range(10):
            t24 = p[hi % 5]
            p[x % 5] = (t24 | w) % 97
    else:
        if u | 10 < 35:
            t25 = p[buf % 5] - 8
            prv = (t25 + (20 ^ hi)) % 251
            t26 = (w | 1) % 9973 >> 1
            t27 = acc - w + 16 & 1023
            hi = fn1(t26 & 65535, t27)
    t28 = p[prv % 5]
    aux = t28 // 3
    if prv ^ p[u % 5] >= 3:
        for m in range(4):
            p[hi % 5] = (13 + buf) % 97
        hi = (prv >> 4) - aux
    t29 = p[hi % 5] * aux
    t30 = t29 * (11 - w)
    t31 = t30 + (x + acc - buf)
    d = t31 & 65535
    nxt = 12 - u
    t32 = (18 | u) % 251
    t33 = p[u % 5]
    idx = t32 + t33
    cnt = (nxt ^ 13) * 19 + hi
    return (17 - nxt | buf - 7) & 8191

if __name__ == "__main__":
    arg = 6
    expected = 15
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
