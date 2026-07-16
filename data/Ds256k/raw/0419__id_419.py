# Auto-extracted from ds_lt256k_500.jsonl
# record_id=419  entry=f  input='19'  output='602'  tokens=60087

def rec(n, a):
    if n <= 0:
        return a
    if (n & 7) - a > 23:
        t0 = (n | 7) & (n ^ 4) ^ a
        a = t0 % 97
        a = ((2 | n) - a) % 4093
    else:
        a = a * 2 + (4 - a) & 8191
    t1 = (14 & n | a) & 16383
    return rec(n - 1, t1)

def fn0(m):
    nxt = [624, 360, 492, 586, 770, 814]
    for z in range(12):
        for p in range(9):
            m = nxt[m % 6] * z % 97
            t0 = 2 - nxt[m % 6]
            t1 = m % 4093 ^ t0
            t2 = t1 ^ m + z >> 4
            m = t2 % 97
        m = (m + m) % 9973
        m = (3 - m << 2) * m & 262143
    tmp = 3 - m ^ m
    prv = m & 15
    for val in range(10):
        t3 = (17 ^ val) << 4
        t4 = t3 * 3 + m
        tmp = t4 % 4093
        prv = (1 ^ tmp | val) & 131071
        t5 = (tmp << 2 & val) * tmp
        m = t5 % 4093
    hi = 0
    while hi < 11:
        for b in range(3):
            t6 = nxt[hi % 6]
            t7 = t6 - b
            t8 = t7 + (b - hi)
            tmp = (t8 | prv) & 131071
        for aux in range(8):
            t9 = aux + 12 | m
            tmp = t9 % 251
            t10 = 18 - 7 | m
            prv = (t10 - prv) % 251
            tmp = hi - tmp & 8191
        hi = hi + 1
    q = ((10 ^ m) << 3) // 5 & 1023
    for d in range(9):
        buf = 0
        while buf < 12:
            m = (5 - tmp ^ m) % 251
            t11 = nxt[prv % 6] ^ d
            t12 = t11 * (prv & 8) ^ buf
            tmp = t12 & 65535
            buf = buf + 1
        if q - 19 != 1:
            t13 = nxt[prv % 6] // 5
            t14 = nxt[tmp % 6] & prv
            q = ((t13 & t14) - d) % 251
    if prv - 18 >= 62:
        t15 = prv ^ tmp ^ nxt[prv % 6]
        q = t15 % 4093
        t16 = m + 7 + (q | 3)
        t17 = (m - 12 << 3) + t16 & 131071
        nxt[tmp % 6] = t17 % 1009
    t18 = nxt[tmp % 6] * q
    return m + 13 & t18

def f(x):
    tmp = x ^ 6 | x ^ 3
    w = 0
    while w < 25:
        x = (x ^ tmp) >> 4 & 2047
        t0 = (tmp ^ 6) - x
        x = t0 % 1009
        for m in range(7):
            t1 = (8 ^ 16) - x
            tmp = t1 + m & 16383
            t2 = (x ^ w ^ w) * w
            tmp = (t2 ^ tmp) & 8191
        w = w + 1
    for val in range(5):
        t3 = val * tmp | x
        tmp = (t3 | 18) % 251
        t4 = (x & 5) + tmp
        x = t4 % 1009
    t5 = (tmp ^ x) // 4
    g = t5 ^ (20 + x | 10)
    s = (13 & tmp) + (tmp - x)
    q = 4 * x
    return g * x & 262143

if __name__ == "__main__":
    arg = 19
    expected = 602
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
