# Auto-extracted from ds_lt256k_500.jsonl
# record_id=287  entry=f  input='9'  output='0'  tokens=253716

def rec(n, a):
    if n <= 0:
        return a
    if n * a == 12:
        t0 = 3 ^ 19
        t1 = t0 + a // 8
        a = t1 // 2 % 4093
    else:
        if a + n > 61:
            a = (n * 17 | a) & 131071
            a = a * a % 65521
        a = a - n & 255
    t2 = n * a ^ (n | a)
    tot = t2 & 131071
    a = n & a
    t3 = n + n | a
    return rec(n - 1, t3 % 4093)

def fn0(c, m, d):
    t0 = (c & 16) - m
    t1 = t0 * (d * 19 | m)
    res = t1 & 2047
    if d - res > 22:
        t2 = (d >> 4) % 17
        m = rec(46, t2)
    else:
        if res | 10 < 30:
            t3 = res + 1 | 10 * 1
            t4 = (t3 + d) % 251
            c = rec(46, t4)
            t5 = (c | 9) & 5
            c = t5 - 11
    d = ((m - c) * m | 14) % 17
    m = c & 10 ^ d
    if c * m > 4:
        if m >> 1 != 39:
            t6 = (15 + res) % 251
            c = rec(32, t6)
        else:
            t7 = (5 ^ m) % 251
            m = rec(56, t7)
            t8 = d * c % 251
            m = rec(120, t8)
        c = (11 << 3) - c
    d = 6 * m - c
    t9 = 14 * res << 2
    return t9 % 251

def f(x):
    p = [136, 939, 410, 40, 725]
    e = (x ^ 19) * (x - 18)
    t0 = e - p[x % 5] + e
    t1 = ((x | 1) + (x - e)) % 4093
    t2 = e & x ^ x
    t3 = (t2 - e) % 9973
    x = fn0(t0 % 9973, t1, t3)
    w = 20 - e - x
    for buf in range(8):
        t4 = p[x % 5] & w
        w = (t4 + (7 - e)) % 97
        if 19 * p[x % 5] <= 6:
            t5 = (w + e) * (e ^ buf)
            p[buf % 5] = t5 & 511
            t6 = w + 11 | buf
            w = t6 % 4093
        else:
            t7 = p[buf % 5] - e
            x = (t7 ^ (6 | x)) % 65521
        x = ((buf | 6) ^ w) % 65521
    nxt = w * x & 16383
    if 5 + e > 11:
        e = w // 7
        e = e * 12
    else:
        tmp = 0
        while tmp < 5:
            t8 = p[nxt % 5]
            t9 = (w & e) * t8
            p[nxt % 5] = (t9 ^ 4) % 97
            p[e % 5] = (5 + e) % 1009
            tmp = tmp + 1
        t10 = nxt * w % 97
        t11 = (w * e | e) & 8191
        t12 = nxt * w << 1 & 2047
        w = fn0(t10, t11, t12)
    for tot in range(9):
        val = 0
        while val < 61:
            p[e % 5] = (x + tot ^ 2) % 1009
            val = val + 1
    t13 = 8 * w & 8 * 17
    return t13 * (e + nxt & nxt) & 255

if __name__ == "__main__":
    arg = 9
    expected = 0
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
