# Auto-extracted from ds_lt256k_500.jsonl
# record_id=113  entry=f  input='4'  output='1959'  tokens=84451

def rec(n, a):
    if n <= 0:
        return a
    if a // 8 < 30:
        a = ((a | n) >> 2) % 1009
    cur = 0
    while cur < 2:
        for nxt in range(6):
            t0 = (a | n) - nxt
            a = (t0 | 11) % 65521
        a = n + n + a & 8191
        a = (a | n) & 8191
        cur = cur + 1
    t1 = n // 8 * a & 131071
    return rec(n - 1, t1)

def fn0(d, m):
    t0 = (m | 5) ^ d
    m = rec(30, t0 & 65535)
    t1 = (m ^ 6) - m - d
    d = rec(31, t1 % 17)
    for j in range(5):
        t2 = j * j - 4 + d
        m = t2 % 17
        if d * j == 52:
            t3 = m * d - m
            d = (t3 | d) & 1023
            m = j + d & d
    t = 0
    while t < 8:
        y = 0
        while y < 7:
            t4 = (t ^ y) + 10 * d
            m = (d // 7 << 3) + t4 & 2047
            t5 = t + y
            t6 = d * m + t
            t7 = t5 + (m ^ 6)
            m = (t6 | t7) & 65535
            y = y + 1
        t8 = d % 17 + (m << 1)
        d = t8 % 251
        t = t + 1
    d = (10 - d ^ d) & m
    t9 = d * d ^ (20 ^ m)
    t10 = (d - m) * m & t9
    m = rec(39, t10)
    m = m * d & 262143
    t11 = d * m * (d | 19) >> 2
    m = t11 & 2047
    return (d + m) % 97

def f(x):
    cnt = [139, 215, 182, 220, 110, 150]
    if x + x < 13:
        if 20 - x >= 35:
            t0 = (11 - 19) * 1 - 13
            cnt[x % 6] = t0 ^ x
        else:
            t1 = (x ^ 15) << 3
            x = t1 + (x << 3) // 5
        t2 = cnt[x % 6]
        t3 = cnt[x % 6]
        t4 = x | t2
        t5 = t4 - x * t3
        cnt[x % 6] = t5 % 251
    else:
        t6 = cnt[x % 6]
        t7 = cnt[x % 6]
        t8 = t6 * x
        t9 = t8 ^ (x | t7)
        x = t9 >> 4
    for val in range(620):
        x = (3 + x) % 65521
    t10 = 12 ^ cnt[x % 6]
    prv = (x ^ 12 ^ t10) + 5
    t11 = cnt[prv % 6]
    q = 18 * 13 & t11
    res = (9 | prv) + prv
    q = prv | 13
    if x * q < 57:
        cur = 0
        while cur < 8:
            t12 = x ^ cnt[res % 6]
            t13 = t12 * (cnt[prv % 6] | cur)
            t14 = (x & prv) + (7 ^ res) ^ t13
            cnt[q % 6] = t14 % 97
            cur = cur + 1
        q = res + 14 | res
    else:
        for a in range(4):
            t15 = res // 8 + a
            t16 = res >> 2 ^ prv
            cnt[x % 6] = (t15 - t16) % 251
            res = (a - 17 ^ x) % 97
    t17 = cnt[res % 6]
    t18 = (res | 18) + 6
    t19 = t18 ^ (6 * 13 | t17)
    q = t19 % 97
    t20 = prv - 8 - res
    return t20 % 65521

if __name__ == "__main__":
    arg = 4
    expected = 1959
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
