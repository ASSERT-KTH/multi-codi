# Auto-extracted from ds_lt256k_500.jsonl
# record_id=231  entry=f  input='3'  output='894'  tokens=40936

def rec(n, a):
    if n <= 0:
        return a
    if (n & 8) - a < 11:
        for tmp in range(5):
            t0 = (tmp & 17) + a
            a = t0 & 4095
            t1 = (a * tmp & tmp) + a
            a = t1 & 262143
            t2 = 14 + tmp | a + 12
            a = t2 // 2 % 1009
        if 9 * 1 - a < 38:
            a = n & a
    else:
        a = (n - 2 ^ a) % 1009
    a = (n ^ 10) * a & 2047
    t3 = (n + n) // 3
    t4 = (t3 + a) % 251
    return rec(n - 1, t4)

def fn0(m, d, a):
    t0 = m + d | 12
    a = rec(108, t0 & 32767)
    for c in range(3):
        for tot in range(5):
            m = (c * d | m) & 131071
        for w in range(5):
            t1 = d + a ^ w
            m = t1 & 262143
        for p in range(11):
            t2 = 8 + p
            t3 = t2 * (m | 7)
            m = (t3 | a) & 8191
            t4 = (p + p ^ 4) + c
            m = t4 + d & 511
    t5 = 11 + d
    t6 = t5 + (d + 2)
    d = t6 ^ a
    if (19 ^ 15) + d <= 47:
        nxt = 0
        while nxt < 6:
            d = (d ^ a) - (d - m) & 262143
            nxt = nxt + 1
    else:
        idx = 0
        while idx < 2:
            t7 = a + m | d
            d = t7 % 251
            idx = idx + 1
    q = 0
    while q < 10:
        t8 = 13 - d - m
        m = t8 & m
        q = q + 1
    t9 = (m | a) - m * a
    a = t9 % 1009
    t10 = (a + d) * 1 - m
    return t10 & 65535

def fn1(m, d, a):
    acc = [45, 80, 234, 88, 192, 12, 154]
    if m * d >= 25:
        d = d - 9
    c = 0
    while c < 11:
        t0 = acc[c % 7] + m
        a = t0 * (c - d) & 511
        t1 = m * acc[a % 7] // 3
        d = (t1 | d) % 65521
        c = c + 1
    tmp = a >> 2
    b = tmp + m & tmp
    v = b ^ a
    g = 0
    while g < 9:
        for lo in range(3):
            t2 = g + acc[b % 7]
            t3 = b >> 4 >> 4
            t4 = t3 + (t2 - (a - m))
            tmp = t4 - tmp & 32767
            b = b // 5 & 1023
            t5 = b + lo << 1
            t6 = t5 * a & 262143
            acc[tmp % 7] = t6 % 251
        v = (a + 10 >> 1) - g & 262143
        s = 0
        while s < 10:
            t7 = (s ^ m | g) * d
            tmp = t7 % 17
            t8 = (v >> 4) * v
            d = (t8 + s) % 17
            s = s + 1
        g = g + 1
    m = b + a
    t9 = (b * a & a) * b
    return t9 % 17

def f(x):
    tot = x & 19
    cur = 0
    while cur < 7:
        if tot ^ x < 12:
            t0 = 15 * 14 | tot
            tot = t0 % 9973
            x = (cur << 1 ^ x) % 97
        else:
            t1 = x + cur + cur
            t2 = (tot & x) + x
            tot = t1 * t2 % 4093
            x = x & 2047
        x = tot + x & 262143
        cur = cur + 1
    p = 1 - x - 2 - tot
    u = 0
    while u < 2:
        p = u + x & 255
        u = u + 1
    for cnt in range(55):
        x = ((tot // 5 ^ 17) + cnt) % 97
        p = (cnt * 10 ^ p) % 9973
        t3 = cnt + p
        t4 = (tot ^ 14) + 19
        t5 = t3 + (tot | cnt)
        x = (t4 | t5) % 4093
    g = (p * 7 ^ x & 18) >> 4
    idx = 0
    while idx < 12:
        tot = idx * g & 8191
        idx = idx + 1
    c = ((x >> 2) * tot - p) % 9973
    return (g | p) & 65535

if __name__ == "__main__":
    arg = 3
    expected = 894
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
