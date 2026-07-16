# Auto-extracted from ds_lt256k_500.jsonl
# record_id=372  entry=f  input='19'  output='439'  tokens=240081

def rec(n, a):
    if n <= 0:
        return a
    t0 = a // 5 ^ 19 - 7
    u = t0 + n & 32767
    for cnt in range(6):
        t1 = (5 | n) ^ cnt
        a = (t1 + a) % 9973
        t2 = 1 - u | cnt
        a = t2 % 4093
    t3 = (n * n ^ a) % 97
    return rec(n - 1, t3)

def fn0(m, c, d):
    cnt = [17, 177, 229, 226, 213, 106]
    cnt[m % 6] = (d - c) % 251
    for buf in range(11):
        t0 = buf + c
        t1 = t0 - 8 * m
        c = t1 % 9973
        t2 = c + d >> 4
        d = t2 % 65521
        val = 0
        while val < 7:
            m = ((val << 3) - c) % 65521
            t3 = d - cnt[d % 6]
            c = (t3 + c) % 65521
            t4 = (buf & m) - d | c
            c = t4 & 262143
            val = val + 1
    for prv in range(4):
        t5 = m & cnt[c % 6]
        t6 = cnt[d % 6]
        t7 = (d ^ prv) & t6
        m = (t5 + m ^ t7) & 32767
        t8 = m // 7 ^ prv
        c = t8 % 65521
    cnt[m % 6] = (m - d) % 251
    u = 0
    while u < 5:
        hi = 0
        while hi < 10:
            d = (c | 7) - hi & 255
            t9 = 4 * d * u - 7 - hi
            c = t9 % 9973
            t10 = cnt[u % 6] * u
            cnt[c % 6] = (t10 * (c | u) & 262143) % 251
            hi = hi + 1
        d = (m - u) * d & 511
        for acc in range(8):
            t11 = cnt[d % 6] << 2
            cnt[d % 6] = (t11 << 4) // 6 % 251
        u = u + 1
    t12 = cnt[c % 6]
    t13 = t12 // 8
    t14 = t13 - c * d
    t15 = (d ^ c) % 9973
    d = (t14 - t15) % 65521
    t16 = cnt[c % 6]
    t17 = m & 8 | t16
    d = t17 >> 3
    b = 0
    while b < 9:
        idx = 0
        while idx < 3:
            c = (idx ^ 20 ^ m) & 255
            t18 = b ^ cnt[m % 6]
            m = (t18 ^ 5 ^ 10) % 9973
            d = (b ^ d) % 9973
            idx = idx + 1
        b = b + 1
    t19 = (m & d) + 15
    return t19 & 1023

def fn1(d, m, g):
    for nxt in range(7):
        t0 = g * nxt * d // 2
        d = t0 % 1009
        for q in range(12):
            t1 = 3 - g ^ g ^ 16
            d = (t1 - d) % 4093
            g = (d % 1009 - g) % 9973
        t2 = m % 1009 - nxt
        d = t2 & 262143
    t3 = (d | m) % 4093
    g = rec(27, t3)
    for lo in range(12):
        t4 = m * d // 4 + g
        g = t4 % 9973
    t5 = (d & 8) + (m | 4)
    t6 = t5 * (g // 4 - (g ^ 4))
    g = t6 % 97
    d = 18 + m & d % 4093
    for cnt in range(5):
        t7 = 13 * 5 ^ m
        g = t7 + g & 262143
        t8 = 15 + cnt ^ d
        g = t8 % 1009
        for y in range(11):
            t9 = d - m >> 2
            g = t9 - (y * y - cnt) & 65535
            t10 = y | cnt
            t11 = t10 | g // 2
            d = t11 * cnt & 16383
            t12 = g - 6 - d - cnt
            g = t12 & 511
    t13 = (g << 4 ^ (d | m)) + d
    t14 = ((m | d) >> 2) % 4093
    t15 = m * d % 9973
    d = fn0(t13 % 1009, t14, t15)
    t16 = 3 ^ d
    t17 = t16 ^ 5 * d
    return t17 % 4093

def f(x):
    val = x + x
    t0 = val + x - x
    buf = t0 + (13 & val & val)
    nxt = 1 ^ 9 ^ buf
    for p in range(4):
        for tot in range(11):
            val = ((p | 5) ^ val) % 1009
        for w in range(7):
            nxt = 3 * w & x * 19
            t1 = (w - buf) * p << 2
            val = t1 & 8191
            t2 = 2 + 18 + buf & buf
            x = (t2 ^ w) % 1009
        for g in range(2):
            t3 = (p * nxt >> 3) - val
            val = t3 & 131071
            nxt = (buf + val - nxt) % 65521
            t4 = (g - 11 | 5) - buf
            val = t4 % 65521
    t5 = (nxt + val) * (val << 2)
    j = t5 - 6 & 8191
    d = j // 3 * buf
    z = 0
    while z < 44:
        t6 = (j & val) + 20 * val
        j = t6 & 65535
        if d & nxt <= 10:
            j = (1 ^ z) - nxt & 131071
            j = (d * 20 ^ z) % 17
        t7 = d % 17 * nxt
        t8 = t7 ^ x | z
        val = t8 % 17
        z = z + 1
    if val - x != 16:
        d = (d + j - d) % 65521
    else:
        if val // 7 != 33:
            t9 = (val | x) % 65521
            t10 = (val | 18) << 3
            t11 = (t10 | j) & 255
            t12 = (17 ^ nxt) & 262143
            j = fn0(t9, t11, t12)
        else:
            t13 = (x >> 4 << 2 | d) & 262143
            t14 = (d * buf - (val - 10)) % 1009
            t15 = x // 8 % 65521
            j = fn0(t13, t14, t15)
            d = (d + x - buf) // 7
    if nxt - j != 56:
        val = 6 * x
        t16 = (buf ^ 16) + val // 6
        t17 = (t16 ^ (val | 16) + buf) % 65521
        t18 = (val ^ nxt ^ val) & 32767
        t19 = (d ^ x) & 65535
        d = fn0(t17, t18, t19)
    else:
        e = 0
        while e < 3:
            t20 = 14 - nxt - (nxt >> 1)
            t21 = (t20 & nxt // 3 - buf) + j
            j = t21 & 131071
            x = (val // 4 - e) % 17
            t22 = 12 - 7
            t23 = t22 | buf ^ val
            t24 = t23 // 5 - e
            x = t24 & 32767
            e = e + 1
    q = (x + j) // 2 + val
    t25 = x * q - j
    t26 = 1 * nxt * 12
    return (t25 ^ t26) % 1009

if __name__ == "__main__":
    arg = 19
    expected = 439
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
