# Auto-extracted from ds_lt256k_500.jsonl
# record_id=128  entry=f  input='16'  output='405'  tokens=239997

def rec(n, a):
    if n <= 0:
        return a
    if n ^ 6 ^ a != 33:
        a = (10 & 16) * n - a & 1023
    else:
        a = (n // 7 ^ a) % 9973
        t0 = n + a
        t1 = t0 - 8 * a
        a = t1 % 1009
    t2 = a << 1 >> 1
    return rec(n - 1, t2 & 2047)

def fn0(d, b, m):
    tot = [2, 93, 93, 82, 49, 62, 20]
    cur = d * 9 * d % 4093
    if cur * 11 >= 55:
        tot[b % 7] = (b - 10) % 97
    else:
        b = 15 & d
        t0 = tot[cur % 7]
        t1 = t0 & tot[m % 7]
        b = (b << 2 ^ t1) % 4093
    w = 0
    while w < 11:
        e = 0
        while e < 11:
            tot[d % 7] = (m - cur | 14) % 97
            b = (18 - m - w ^ e) % 9973
            t2 = tot[cur % 7] >> 3
            tot[b % 7] = (t2 + ((b | w) - cur)) % 97
            e = e + 1
        if d + 16 == 3:
            t3 = (d & 3) - b >> 4
            b = t3 % 251
            t4 = tot[d % 7]
            t5 = (1 + cur) % 251
            t6 = b // 3 * t4
            t7 = t5 ^ t6 ^ m
            m = t7 & 16383
        else:
            t8 = (2 - b >> 1) % 251 - d
            d = t8 % 251
        w = w + 1
    for hi in range(2):
        t9 = d & b
        m = t9 & 11 * hi
        b = (cur * b * 14 | 1) & 511
    if cur ^ 14 == 58:
        t10 = tot[m % 7] - 9
        b = 19 + d + t10
    t11 = 12 - tot[b % 7] + cur
    return t11 & 511

def fn1(b, m, g):
    tot = [283, 177, 179, 333, 483, 284]
    t0 = g - tot[m % 6]
    t1 = b * b - t0 + g
    prv = t1 & 32767
    t2 = 17 | tot[b % 6]
    t3 = (t2 >> 1) % 9973
    t4 = prv | b | prv
    t5 = g * tot[g % 6]
    t6 = (t5 // 5 + prv) % 97
    b = fn0(t3, t4 & 16383, t6)
    t7 = g - b + g
    g = t7 ^ tot[m % 6]
    for p in range(11):
        t8 = 15 - p - g
        tot[p % 6] = t8 % 1009
        t9 = (m | 5) + g
        g = t9 % 9973
    t10 = prv - tot[b % 6]
    return t10 - (g ^ m) & 8191

def f(x):
    t = [829, 231, 690, 130, 597, 676]
    lo = x + x | 5
    c = x & 14
    t0 = t[lo % 6] >> 2
    t1 = (t0 | lo - c) >> 2
    t2 = (16 + 10 + x ^ lo) % 4093
    t3 = t[lo % 6] * 8
    t4 = (x + c) * t3 << 1
    lo = fn0(t1 & 262143, t2, t4 & 16383)
    cnt = c * 18 * (lo * x) % 251
    for cur in range(719):
        t5 = (cnt + cnt) * 8
        t[cnt % 6] = (t5 ^ x) % 1009
    return (lo ^ cnt) % 1009

if __name__ == "__main__":
    arg = 16
    expected = 405
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
