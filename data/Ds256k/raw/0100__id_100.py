# Auto-extracted from ds_lt256k_500.jsonl
# record_id=100  entry=f  input='20'  output='8334'  tokens=175338

def fn0(d, m, a):
    cnt = [132, 77, 80, 54]
    if m + 6 == 39:
        t0 = 5 | cnt[a % 4]
        a = t0 ^ 14 + a ^ a
        cnt[m % 4] = m * d % 4093 % 251
    else:
        m = m + d
        cnt[a % 4] = (a - d) % 251
    for u in range(9):
        for acc in range(10):
            t1 = acc * u | m
            cnt[d % 4] = t1 % 251
        cnt[m % 4] = (9 ^ a) % 251
        for tot in range(11):
            t2 = tot + u | u ^ tot
            a = (t2 ^ a) % 9973
            t3 = cnt[a % 4]
            t4 = m * 3 | tot
            t5 = t4 | t3 + 3
            cnt[d % 4] = t5 % 9973 % 251
    d = (a * 15 - d) % 9973
    a = m + 19
    if 8 + d < 25:
        t6 = d * cnt[d % 4]
        a = (d ^ m) & t6
    else:
        for nxt in range(7):
            cnt[nxt % 4] = ((a - nxt) % 4093 + m) % 251
            cnt[nxt % 4] = (m << 1) // 6 % 251
            t7 = (d & nxt) - m
            t8 = m + 10 ^ 19
            cnt[m % 4] = (t7 ^ t8) % 251
    t9 = cnt[m % 4] + m
    m = (17 - a | t9) >> 2
    a = a * 9 & 32767
    return (a + 14 >> 4) % 4093

def fn1(m):
    lo = [238, 173, 196, 120, 141]
    y = 0
    while y < 8:
        for b in range(4):
            t0 = 4 ^ 20
            t1 = t0 - (m + 20)
            lo[y % 5] = t1 % 251
            m = (b + y | m) % 97
        m = (m - 17) % 4093
        y = y + 1
    t2 = m ^ 17 | m // 7
    w = t2 - m
    t3 = lo[m % 5]
    t4 = lo[m % 5]
    q = w - t3 ^ t4
    for s in range(11):
        nxt = 0
        while nxt < 12:
            t5 = lo[m % 5] >> 4
            m = t5 + m * 20 & q
            t6 = 15 ^ lo[nxt % 5]
            lo[q % 5] = (t6 - w) % 251
            t7 = 7 + s | m
            t8 = t7 * (nxt * m ^ 7)
            lo[s % 5] = t8 % 65521 % 251
            nxt = nxt + 1
    t9 = 3 ^ lo[q % 5]
    t10 = t9 + 12 * q
    t11 = t10 * lo[q % 5]
    lo[w % 5] = t11 % 65521 % 251
    t12 = lo[q % 5]
    t13 = 12 - m | t12
    return t13 % 4093

def f(x):
    b = [334, 713, 513, 540]
    tmp = 0
    while tmp < 10:
        g = 0
        while g < 9:
            x = x * tmp % 9973
            b[g % 4] = (g - tmp + x) % 1009
            x = (x ^ 17) % 9973
            g = g + 1
        if tmp ^ x > 2:
            t0 = b[tmp % 4]
            t1 = b[x % 4]
            t2 = t0 + t1
            b[x % 4] = t2 & (tmp & x)
        tmp = tmp + 1
    m = 5 - x
    j = 0
    while j < 8:
        m = x * j % 9973
        for idx in range(11):
            x = (idx * 2 & m | 5) & 511
        t3 = b[x % 4] >> 1
        t4 = t3 | b[x % 4] * m
        m = 9 * 20 + m & t4
        j = j + 1
    buf = 0
    while buf < 470:
        x = (17 - m | x) & 2047
        buf = buf + 1
    tot = 0
    while tot < 4:
        t5 = b[m % 4]
        t6 = x + x
        t7 = t6 & (t5 ^ 10)
        x = t7 // 7 & 2047
        t8 = (m << 3) - m * x << 1
        x = t8 & 262143
        b[m % 4] = (x >> 3) // 8 % 1009
        tot = tot + 1
    if 1 - x >= 22:
        if 7 - b[x % 4] != 54:
            x = (m + 17 | 4) - x
        else:
            t9 = 16 + b[x % 4]
            b[x % 4] = (t9 | m >> 2) % 1009
    if 7 ^ m > 25:
        b[x % 4] = (m * m + m) % 9973 % 1009
    nxt = m + x
    return (x - 18) * (20 | nxt) % 9973

if __name__ == "__main__":
    arg = 20
    expected = 8334
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
