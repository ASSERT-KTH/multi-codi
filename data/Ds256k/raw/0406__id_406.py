# Auto-extracted from ds_lt256k_500.jsonl
# record_id=406  entry=f  input='11'  output='0'  tokens=242714

def rec(n, a):
    if n <= 0:
        return a
    t0 = (a | 13) & a << 2 ^ n
    nxt = t0 % 17
    t1 = (11 - a) % 1009
    return rec(n - 1, t1)

def fn0(a, e, j):
    j = (e << 4) * 16 & 131071
    nxt = 0
    while nxt < 9:
        j = (nxt - e) % 65521
        t0 = (e | j) - e * 11
        t1 = j * nxt + e | t0
        j = t1 & 255
        t2 = e + j + (e >> 2)
        e = ((a ^ j) // 2 | t2) % 97
        nxt = nxt + 1
    t3 = j * e - (16 + a)
    e = t3 & 255
    t4 = 20 - 14
    t5 = t4 - 16 * 5
    t6 = a + e ^ j
    e = t5 * t6 & 262143
    res = 0
    while res < 8:
        e = (6 & a ^ a | e) % 65521
        a = 16 * e & a
        t7 = a + a
        t8 = t7 & (a ^ e)
        t9 = res - 5 & res
        a = (t8 | t9) % 1009
        res = res + 1
    e = (j * e - a) % 97
    for w in range(12):
        t10 = w - 11 - 7
        j = (t10 + e) % 9973
        t11 = (e // 6 << 3) // 6
        j = (t11 ^ w) % 1009
    t12 = 18 ^ a | 7 - j
    j = rec(41, t12 % 9973)
    t13 = e + 7 ^ e
    t14 = t13 * (e // 8 * 10)
    return t14 & 16383

def f(x):
    acc = 0
    while acc < 4:
        x = (14 + x ^ x) & 4095
        if x >> 1 != 27:
            x = ((17 ^ acc) + 15 + x) % 4093
            t0 = acc * acc * 4 << 4
            x = (t0 ^ x) % 4093
        else:
            x = ((acc | 13) - acc | x) % 9973
        acc = acc + 1
    nxt = 0
    while nxt < 18:
        for d in range(7):
            t1 = (11 | d | d) * 3 ^ x
            x = t1 % 9973
        for g in range(11):
            t2 = g + 2 - g ^ g
            x = (t2 | x) & 262143
        nxt = nxt + 1
    t3 = (6 - x) % 9973
    x = rec(31, t3)
    t4 = x % 4093 * 2 | x
    t5 = (x & 7) - (20 ^ 13)
    x = fn0(t4 % 4093, t5 & 262143, x % 4093)
    for p in range(3):
        for a in range(8):
            x = (a - x) % 4093
            t6 = (x >> 1) + (p | x)
            x = t6 - p & 511
        for e in range(3):
            x = (p * 17 & 4) - x & 8191
    t7 = (11 + x ^ 20) & 131071
    t8 = ((x & 6) + x) % 4093
    t9 = 13 * 15 - x
    x = fn0(t7, t8, t9 % 9973)
    u = x >> 3
    t10 = u // 8 >> 2
    y = t10 * 13
    t11 = x - 12 & 65535
    t12 = x + y & 255
    t13 = u * y & x
    u = fn0(t11, t12, t13)
    if y + y <= 54:
        val = 0
        while val < 9:
            t14 = y + 13 + val
            u = t14 % 4093
            val = val + 1
        t15 = y * y % 4093
        t16 = (14 ^ y) & 2047
        t17 = x // 4 + (9 | 7)
        t18 = t17 | y * y + x
        x = fn0(t15, t16, t18 % 4093)
    else:
        for res in range(6):
            t19 = u // 4 - (x + u)
            x = (x * y * y + t19) % 4093
            t20 = (y | 13) // 7
            y = (t20 ^ 16) % 4093
    prv = (u ^ x) & 16 + x
    if u - x >= 61:
        y = u | 6
    else:
        for buf in range(7):
            prv = (10 ^ prv) - y & x
            prv = (y + x >> 3 ^ prv) % 4093
            u = ((x >> 1) - u) % 9973
        if 18 | x >= 25:
            t21 = (y - prv) * y & 8191
            t22 = (16 ^ prv) % 9973
            t23 = (y << 3) * (12 * u)
            y = fn0(t21, t22, t23 % 9973)
            t24 = x - 15 & 4095
            t25 = u + prv >> 1 & 16383
            t26 = (y ^ x) & 255
            prv = fn0(t24, t25, t26)
        else:
            y = y + y
            y = (11 * y - y) % 9973
    t27 = u << 1 | x
    idx = 2 + y - t27
    if prv + x > 21:
        idx = prv >> 3
    else:
        x = y - prv
        x = idx | x
    cnt = x * y & 8191
    if y * cnt == 30:
        for tmp in range(12):
            t28 = prv + 12 - tmp
            u = t28 & 1023
    return idx & u

if __name__ == "__main__":
    arg = 11
    expected = 0
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
