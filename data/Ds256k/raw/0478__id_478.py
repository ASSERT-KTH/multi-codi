# Auto-extracted from ds_lt256k_500.jsonl
# record_id=478  entry=f  input='11'  output='366'  tokens=196193

def fn0(m):
    t0 = m + m
    b = t0 + (m | 10)
    v = m % 17 - b
    c = (13 + m) * b & 2047
    t1 = (b >> 2) * (m + c)
    y = t1 * b % 97
    b = (m + b << 4) % 17
    c = (c + 9 & m - 2) - b
    t2 = b - m >> 2
    return t2 + 1 & 8191

def fn1(b, e):
    g = 0
    while g < 11:
        if e + e >= 24:
            b = e - g & 4095
        b = g + 5 + e & 8191
        g = g + 1
    cnt = 0
    while cnt < 2:
        j = 0
        while j < 4:
            t0 = cnt - (b & 10)
            t1 = t0 * cnt ^ e
            e = t1 % 4093
            t2 = (cnt & e) * (cnt + 12)
            b = (t2 + b) % 97
            t3 = (cnt & 7) + b
            b = t3 * b % 97
            j = j + 1
        t4 = e | 4
        t5 = b * e * 11
        t6 = t4 ^ cnt + cnt
        e = (t5 + t6) % 97
        t7 = e * e + (b ^ 6)
        b = (t7 ^ (14 ^ b) + 12) % 97
        cnt = cnt + 1
    b = b + e ^ e >> 3
    b = (e * 2 ^ b) - b
    return ((e ^ 11) % 4093 ^ b) % 97

def f(x):
    q = (x ^ 20) + (x & 17)
    for u in range(10):
        t0 = q & x | u
        q = (t0 ^ (x | u | u)) & 16383
    for m in range(6):
        t1 = 20 ^ q
        t2 = t1 * (1 * m)
        x = t2 % 4093
        val = 0
        while val < 2:
            q = val * x & 4095
            q = ((m & 3) * x - q) % 4093
            x = (13 + 3 | q | val) & 4095
            val = val + 1
        q = q - m + x & 1023
    c = (q >> 3) + (x - 1)
    cnt = 0
    while cnt < 12:
        x = (cnt - c) % 4093
        q = (15 * cnt | q) % 4093
        c = q + x + cnt & 1023
        cnt = cnt + 1
    t3 = (x | q) + c // 8
    t4 = t3 // 2 % 4093
    c = fn1(c & x, t4)
    aux = 0
    while aux < 22:
        q = (aux + 3 + q) % 9973
        for j in range(5):
            t5 = c + x | j
            q = (t5 | q - x >> 3) % 9973
            q = j & x
        if (14 ^ aux) + x < 24:
            t6 = c - 7 - aux * aux
            c = t6 % 9973
            t7 = x + x & (q ^ aux)
            t8 = t7 ^ aux * c + 20 * aux
            c = t8 & 32767
        aux = aux + 1
    t9 = (c << 4) // 8 ^ c
    t10 = (x >> 2) // 3 % 4093
    c = fn1(t9 & 16383, t10)
    tot = (q << 1) + 14
    prv = 0
    while prv < 6:
        t11 = x % 4093 + prv
        tot = t11 % 9973
        t12 = 1 * 15 + tot ^ x
        x = t12 % 9973
        prv = prv + 1
    b = (12 ^ tot) >> 3
    t13 = (c ^ q) >> 2 | 20
    x = fn0(t13 % 4093)
    g = (tot & b) >> 4
    for s in range(7):
        if 14 * q >= 11:
            t14 = 19 ^ g | g - c
            b = (t14 ^ b) & 511
        else:
            t15 = 13 * s ^ b + s
            q = t15 & 65535
            t16 = 6 - x << 2
            q = (t16 - q) % 9973
    buf = x + 1 >> 4
    t = 13 + q
    t17 = buf * 4 // 7
    t18 = (t17 - buf) % 4093
    t19 = (tot + x) % 4093
    x = fn1(t18, t19)
    t20 = x % 4093 | x * q
    t21 = 9 - buf ^ (18 | q)
    t22 = t20 - t21 & 32767
    t23 = (16 << 1) * b
    buf = fn1(t22, t23 & 255)
    d = (14 * g ^ g) - x
    idx = 0
    while idx < 9:
        t = (((6 ^ q) >> 4) + idx) % 4093
        cur = 0
        while cur < 5:
            t24 = (idx ^ 1) + c - cur
            x = t24 % 9973
            t25 = (13 + x ^ buf) // 7
            tot = (t25 ^ cur) % 4093
            cur = cur + 1
        idx = idx + 1
    return (10 | d) & 262143

if __name__ == "__main__":
    arg = 11
    expected = 366
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
