# Auto-extracted from ds_lt256k_500.jsonl
# record_id=402  entry=f  input='20'  output='3'  tokens=47000

def fn0(d, m):
    v = m | 3
    for idx in range(11):
        t0 = (13 ^ 8) & (13 ^ idx)
        t1 = 20 & m | v | t0
        m = t1 % 97
    nxt = 7 & d
    res = v // 3
    buf = 0
    while buf < 3:
        for hi in range(6):
            t2 = res * 15 & (res ^ 19)
            t3 = t2 + ((res | 19) - buf)
            v = t3 + hi & 262143
        buf = buf + 1
    p = 15 ^ v
    t4 = res // 3 ^ res
    d = t4 * nxt
    d = (d + v + p) % 1009
    return (nxt ^ 3 ^ 16) % 17

def fn1(d, b, c):
    lo = [118, 202, 170, 200, 239]
    if d + c > 15:
        t0 = (18 + 14) * lo[d % 5]
        d = t0 >> 2
        t1 = b >> 3 & b << 2
        t2 = d - lo[c % 5]
        t3 = (1 - b & t2 ^ 20) & 131071
        b = fn0(t1, t3)
    else:
        if c - 13 > 49:
            t4 = lo[c % 5]
            b = t4 - d
            t5 = lo[c % 5] ^ b | c
            lo[c % 5] = t5 % 251
        else:
            c = d % 97 + 8
        d = 13 & 19 | c >> 3
    t6 = lo[b % 5]
    t7 = 6 + t6 & 511
    t8 = d - 15
    t9 = t8 + 11 * b
    t10 = (b - c) % 251
    t11 = (t9 - t10) % 9973
    c = fn0(t7, t11)
    t = lo[d % 5] & d
    t12 = lo[d % 5] - c << 2
    t = t12 >> 2
    t13 = b * 4 - (d ^ b)
    return (t13 ^ t) % 97

def f(x):
    prv = [29, 32, 87, 72]
    prv[x % 4] = prv[x % 4] * x % 97
    m = x & 20 & x
    for s in range(174):
        if prv[x % 4] != 8:
            prv[s % 4] = (10 + s) * m % 97
    for aux in range(11):
        m = (x ^ 17 ^ aux) % 97
    buf = 15 - prv[x % 4] ^ m
    for acc in range(12):
        if prv[m % 4] + 6 != 30:
            t0 = 8 - prv[acc % 4]
            prv[x % 4] = t0 & (19 & 20) | x
        buf = (buf - 20 | acc) % 17
    g = x - m
    hi = g + g
    prv[g % 4] = (hi << 4) % 97
    t1 = prv[buf % 4] | buf
    u = buf & 2 ^ t1
    b = 0
    while b < 7:
        u = (g + m >> 2 | u) & 131071
        x = hi - 11 & m + x
        if m + buf <= 59:
            hi = ((m & x) + b) % 97
        else:
            x = (6 + x) % 17
        b = b + 1
    v = g * m * hi % 97
    t2 = prv[x % 4]
    t3 = t2 >> 1
    res = t3 * (buf - g)
    t4 = (u & hi) * prv[m % 4]
    t5 = t4 * (res + v - x) & 65535
    prv[v % 4] = t5 % 97
    for nxt in range(12):
        t6 = prv[x % 4]
        t7 = (14 - t6) * m
        t8 = res * res ^ m
        prv[v % 4] = (t7 & t8) % 97
        t9 = x * prv[nxt % 4]
        t10 = 13 - 4 | t9 | x
        prv[g % 4] = t10 % 97
        x = (res | m | nxt) & 16383
    t11 = (10 | 1) - m
    w = t11 + 5
    prv[u % 4] = m & res
    c = buf >> 1
    t12 = prv[c % 4] ^ res
    t13 = prv[c % 4] & 17
    t14 = t13 ^ buf & prv[v % 4]
    t15 = (t12 ^ prv[u % 4]) & t14
    prv[v % 4] = t15 % 97
    t16 = 14 ^ m
    t17 = t16 * (u - w)
    return t17 // 8 % 17

if __name__ == "__main__":
    arg = 20
    expected = 3
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
