# Auto-extracted from ds_lt256k_500.jsonl
# record_id=440  entry=f  input='6'  output='54'  tokens=247997

def fn0(m, b, e):
    for val in range(6):
        t0 = 10 * val | e
        e = t0 & 4095
    for cur in range(10):
        t1 = (m >> 1) * (cur ^ m) - m
        b = t1 & 255
        b = (m * m ^ b) & 1023
        for v in range(2):
            t2 = b - cur >> 2
            m = (t2 + v) % 251
            t3 = e % 9973 & m ^ 8
            m = t3 & 4095
            e = (e + b) % 4093
    t4 = 7 - b
    t5 = t4 | b - 9
    lo = t5 << 1
    m = lo | m
    if m | e >= 9:
        t6 = lo ^ e
        t7 = t6 - (e ^ 19)
        m = t7 + 5
        m = 2 * b
    else:
        if (3 ^ 11) - m == 26:
            m = lo % 9973
        else:
            m = e ^ lo
            t8 = lo - 12
            t9 = t8 * (b - lo)
            b = t9 & 511
        e = 14 * 15 ^ m
    if 1 + b >= 24:
        t10 = m * m + e // 5 - lo
        lo = t10 & 65535
        for a in range(12):
            e = ((lo ^ 15) - e) % 65521
            e = 8 + b - e & 8191
            b = b * 3 & 511
    t11 = (13 ^ b) * m
    return (t11 | lo) & 65535

def fn1(b):
    cnt = [85, 92, 89, 58, 69, 28]
    t0 = b | 8
    t1 = t0 * (13 * b)
    t2 = b * b & b
    t3 = cnt[b % 6] & 255
    b = fn0(t1 % 1009, t2, t3)
    t4 = cnt[b % 6]
    m = 17 | t4 | b
    if m + 17 <= 33:
        t5 = m * cnt[m % 6] // 8
        m = (t5 + cnt[b % 6]) % 1009
        p = 0
        while p < 6:
            t6 = m & b ^ p
            t7 = t6 | cnt[p % 6]
            m = t7 % 65521
            cnt[b % 6] = (m ^ 3) % 97
            t8 = m + b
            cnt[p % 6] = t8 & (18 & 14)
            p = p + 1
    else:
        b = m - 18
    e = m | 20
    return m // 4 + m & 65535

def f(x):
    if x - 19 <= 17:
        x = (x | 19) - 7
        if x & 12 > 7:
            x = x * x // 3
            t0 = x * x + 4
            t1 = t0 << 1 & 8191
            t2 = x * x * x
            x = fn0(t1, x & 262143, t2 & 262143)
        else:
            x = x ^ 5
            x = (x - 7) * x & 511
    else:
        for c in range(2):
            t3 = (c << 3) * c
            t4 = (c | 12) << 4
            t5 = (t3 ^ t4) - x
            x = t5 % 9973
    for v in range(8):
        for nxt in range(2):
            t6 = v + v
            t7 = t6 | x >> 2
            x = t7 & 32767
            x = v * 10 + x & 262143
            t8 = nxt - 2 - nxt * x
            x = t8 - x & 16383
        hi = 0
        while hi < 3:
            t9 = v - x - (5 - x)
            x = t9 & 8191
            t10 = x * x ^ v
            t11 = (hi & x) * v
            x = t10 * t11 % 1009
            hi = hi + 1
        for d in range(12):
            x = (v | x) % 1009
            x = (15 | v) + x & 131071
            t12 = x >> 2 ^ d
            x = (t12 + 15) % 9973
    prv = x + x
    for cur in range(6):
        res = 0
        while res < 5:
            t13 = res - cur << 3
            prv = (t13 + x) % 1009
            x = (16 | x) & 4095
            t14 = prv // 8 * cur
            x = (t14 - x) % 9973
            res = res + 1
    for w in range(8):
        t15 = prv - w
        prv = t15 & prv >> 4
        t16 = (x - 5) * (prv - x)
        x = t16 & 4095
        if w * x >= 50:
            prv = (3 ^ w) - prv & 262143
    p = x // 5 + 16 & x
    t17 = (p << 4) * prv
    j = t17 % 9973
    idx = j >> 1
    t18 = j * j ^ 16
    t19 = t18 // 8 % 17
    t20 = (p | idx) * prv * j
    t21 = ((prv << 2) + j) % 1009
    x = fn0(t19, t20 % 9973, t21)
    lo = 0
    while lo < 47:
        x = (x | idx) % 1009
        lo = lo + 1
    for z in range(8):
        if p - j <= 27:
            t22 = x // 3
            t23 = t22 & j - p
            j = t23 // 5 % 1009
        if p & z != 0:
            prv = (p >> 3) + prv & 65535
            x = (j << 3 ^ 19 | x) & 8191
        t24 = (prv | idx) + j | z
        x = t24 % 9973
    for aux in range(6):
        for t in range(9):
            t25 = (p ^ 5) + j + aux
            idx = (t25 | idx) & 16383
            t26 = (6 ^ prv) * p
            idx = (t26 - idx) % 17
            x = (10 * idx | x) & 32767
    b = j * 8 - (x - j)
    return x & j

if __name__ == "__main__":
    arg = 6
    expected = 54
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
