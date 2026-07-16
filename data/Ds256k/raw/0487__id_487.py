# Auto-extracted from ds_lt256k_500.jsonl
# record_id=487  entry=f  input='15'  output='1232'  tokens=240173

def rec(n, a):
    if n <= 0:
        return a
    t0 = (a | 19) + n
    a = t0 // 5 & 65535
    t1 = (14 << 3) * n
    t2 = t1 - (a * a ^ a) & 16383
    return rec(n - 1, t2)

def fn0(d, c):
    q = [244, 112, 130, 30, 121, 108, 231, 26]
    t0 = c + 8 + 14
    q[d % 8] = t0 % 251
    t1 = c + c >> 4
    d = t1 | c & d ^ d
    t2 = c * c
    t3 = t2 - (12 + c)
    q[c % 8] = t3 % 17
    t4 = q[c % 8]
    t5 = (d | 5) & c
    t6 = (d | t4) >> 1
    q[c % 8] = (t5 - t6) % 251
    t7 = q[d % 8]
    d = (c & 11) * t7
    for lo in range(10):
        c = (c >> 2) % 1009
    t8 = (c | 8) - 14
    t9 = (7 << 3) % 17
    q[d % 8] = (t8 - t9) % 251
    for p in range(7):
        for w in range(6):
            t10 = 19 * c - (p + d) >> 4
            q[p % 8] = t10 % 251
        q[d % 8] = (c - p) % 251
        if c >> 1 != 14:
            c = (p + d) // 2 & 16383
        else:
            d = 19 + d & 4095
            d = (p | 14 | c) & 65535
    return (c << 2) * (19 | 6) & 65535

def fn1(d, m, c):
    prv = [495, 37, 893, 987, 785, 19, 497]
    a = 0
    while a < 6:
        d = m & a
        a = a + 1
    val = 0
    while val < 8:
        t0 = 13 * 12 // 6 // 3
        m = ((t0 ^ c) + val) % 65521
        val = val + 1
    t1 = 6 << 1
    m = t1 ^ d + d
    t2 = prv[d % 7]
    m = 17 + t2
    return (d & c ^ c % 65521) & 511

def f(x):
    cnt = [161, 22, 84, 245, 157, 132, 185, 22]
    if x ^ 8 > 16:
        t0 = x * x * (8 + x) % 17
        t1 = (x - 20) % 9973
        t2 = x * 9 % 251
        x = fn1(t0, t1, t2)
    else:
        x = x << 2
    if x - 6 >= 30:
        b = 0
        while b < 7:
            x = x % 17 & 10 - 5
            b = b + 1
    for e in range(6):
        x = (11 - 3 + x) % 97
    if x + x <= 56:
        for res in range(7):
            t3 = res - 14 + res - x
            x = t3 % 251
            t4 = (res + x) * (x % 97)
            cnt[x % 8] = (x >> 3 >> 4) * t4 % 251
    m = 2 | x
    for aux in range(9):
        for j in range(8):
            t5 = cnt[m % 8]
            t6 = m + m
            t7 = t6 + m * t5
            t8 = aux * j ^ x
            t9 = t7 * t8 & 131071
            cnt[aux % 8] = t9 % 251
    s = 0
    while s < 146:
        t10 = (10 ^ 14) + x
        x = t10 - x & 32767
        s = s + 1
    t11 = x // 5
    t12 = t11 - (x | m)
    a = t12 % 17
    t13 = cnt[a % 8]
    t14 = t13 - a | a
    g = t14 & m
    for prv in range(11):
        m = (g + g - m) // 5 & 511
        g = (a + prv) % 17
        tot = 0
        while tot < 11:
            cnt[g % 8] = (m << 3 & 255) % 251
            t15 = (a | 20) * m
            x = (t15 - tot) % 17
            tot = tot + 1
    idx = 0
    while idx < 8:
        t16 = (g | x) ^ a
        a = t16 % 9973
        t17 = g + x << 3
        x = t17 & 5
        t18 = cnt[idx % 8]
        t19 = idx - t18 >> 1
        m = (t19 - g) % 17
        idx = idx + 1
    t20 = (16 + 1) * m & 32767
    t21 = (12 - g >> 1 ^ g) & 255
    t22 = (14 + m << 3) % 251
    g = fn1(t20, t21, t22)
    t23 = cnt[g % 8]
    t24 = t23 + 1
    t25 = t24 + (x ^ m)
    g = rec(81, t25 % 97)
    return cnt[m % 8] * 14 % 9973

if __name__ == "__main__":
    arg = 15
    expected = 1232
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
