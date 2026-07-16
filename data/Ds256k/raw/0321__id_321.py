# Auto-extracted from ds_lt256k_500.jsonl
# record_id=321  entry=f  input='12'  output='31'  tokens=168058

def fn0(j, m):
    e = 2 * m + (j | 4)
    t0 = e + j - e
    j = t0 + m
    m = j * e % 251
    j = m & 16 | e
    for c in range(10):
        m = (j >> 3) * m & 4095
        t1 = m * m - c
        e = t1 & 2047
        t2 = j - e + 18 * j
        t3 = 2 * e ^ c ^ t2
        m = t3 % 251
    m = 14 * e & (e | j)
    for nxt in range(6):
        lo = 0
        while lo < 9:
            t4 = (2 << 2) + nxt - m
            m = t4 & 262143
            lo = lo + 1
    return 11 * m - e & 131071

def fn1(b, g, j):
    hi = [354, 422, 736, 279, 366, 972, 613, 434]
    for val in range(10):
        b = ((val | 4) ^ g) % 97
    t0 = (g ^ 15) - b * b
    nxt = t0 * j % 97
    cur = j % 97
    if j * b >= 3:
        t1 = (7 | cur) << 2
        nxt = t1 - cur
    for acc in range(9):
        m = 0
        while m < 12:
            t2 = hi[j % 8] | acc
            t3 = t2 & 15 + g
            hi[j % 8] = (t3 ^ (acc | 13) + nxt) % 1009
            b = (j - acc | b) & 32767
            m = m + 1
        t4 = (cur - 19) * g
        t5 = hi[acc % 8]
        b = (t4 + t5) % 97
    return (g + 12 + nxt) % 17

def f(x):
    if x & 11 < 5:
        x = x + 7 << 2
    if x * 20 > 31:
        if 15 - x < 57:
            x = x + x | x
        acc = 0
        while acc < 7:
            x = acc + x & 262143
            x = (acc | x) & 16383
            t0 = 4 | 12 | x
            x = t0 % 251
            acc = acc + 1
    else:
        x = x % 97 - x
    for hi in range(9):
        if x <= 64:
            x = (12 | x) & 2047
            t1 = 13 - hi
            t2 = t1 - 3 * x
            x = t2 // 3 & 511
    t3 = x * x * 9
    tot = t3 // 8 & 8191
    if x ^ 4 < 3:
        t4 = (x + tot) % 1009
        t5 = (9 | tot) + tot
        t6 = (t5 ^ (19 ^ tot) + tot) % 251
        tot = fn0(t4, t6)
    val = 0
    while val < 8:
        t7 = val * tot + tot
        tot = (t7 - tot) % 97
        t8 = (17 << 3) * (val - 2) >> 4
        tot = t8 - x & 16383
        val = val + 1
    t9 = x << 3 & tot
    t10 = t9 // 6 % 97
    t11 = ((x & 7) * tot >> 4) % 251
    x = fn0(t10, t11)
    for cur in range(147):
        x = ((x | 13) ^ cur) << 3 & 16383
        t12 = 6 * tot ^ x
        tot = t12 % 97
    t13 = (tot ^ x | x) % 97
    t14 = (tot ^ x) + (x - tot)
    t15 = (x ^ 2) % 251
    tot = fn1(t13, t14 & 511, t15)
    t16 = (x + x) * (17 * x) - tot
    m = t16 & 511
    t17 = tot - m + tot
    v = t17 * (m & 11) % 1009
    u = x ^ 8
    prv = m | 17
    if v - 18 == 45:
        for res in range(12):
            t18 = res - 4 - m >> 1
            x = t18 & 65535
            m = (prv // 2 | res) & 131071
            t19 = v * u >> 3 ^ m
            m = t19 % 97
    else:
        v = prv // 3
        buf = 0
        while buf < 3:
            t20 = buf - tot & x * x
            prv = (prv - x) // 8 & t20
            buf = buf + 1
    t21 = tot // 4 | v & x
    return t21 - 3 & 131071

if __name__ == "__main__":
    arg = 12
    expected = 31
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
