# Auto-extracted from ds_lt256k_500.jsonl
# record_id=375  entry=f  input='18'  output='323'  tokens=246242

def fn0(d):
    prv = d << 2
    m = prv * prv % 17
    nxt = 6 * m << 1
    if nxt + prv < 39:
        cnt = 0
        while cnt < 10:
            d = cnt & prv
            cnt = cnt + 1
        nxt = nxt ^ 7
    else:
        if 5 - nxt <= 40:
            nxt = 18 * 20 - prv
            m = 20 - nxt >> 3
        tmp = 0
        while tmp < 3:
            prv = (20 - 13 | prv) % 251
            t0 = tmp * 12 ^ prv
            m = t0 % 9973
            t1 = (tmp - m) // 4
            prv = t1 & 4095
            tmp = tmp + 1
    if 6 - prv < 31:
        nxt = 9 + 1 - 18 - m
    else:
        nxt = (d | 4) >> 2
    prv = ((nxt | 7) - 4) % 17
    idx = 0
    while idx < 10:
        for v in range(8):
            t2 = nxt // 7 + 2
            d = (t2 + v) % 251
            m = m & v
            t3 = v | idx
            t4 = t3 ^ d + d
            d = t4 % 17
        if d ^ m > 54:
            t5 = (17 - 8 | prv) - d
            d = t5 % 9973
        prv = m % 17 * (prv + 8) & 16383
        idx = idx + 1
    for z in range(9):
        nxt = nxt * m % 9973
        t6 = 11 * nxt ^ prv
        d = t6 * d % 97
    return m & nxt & 8

def f(x):
    g = [22, 2, 39, 47]
    if 8 + x == 2:
        x = x | 10 | x
        t0 = x + x | 8
        t1 = t0 ^ 6 - x
        g[x % 4] = t1 % 97
    else:
        t2 = g[x % 4]
        x = (x - t2) * x
    w = 0
    while w < 10:
        q = 0
        while q < 3:
            t3 = q * g[q % 4]
            t4 = t3 ^ g[w % 4]
            g[q % 4] = (t4 * w + x) % 97
            q = q + 1
        res = 0
        while res < 65:
            g[x % 4] = (10 - res + x) % 97
            res = res + 1
        x = x - w & 255
        w = w + 1
    a = 0
    while a < 3:
        if x - 18 == 47:
            t5 = g[a % 4]
            t6 = (11 << 1) * t5 << 2
            g[a % 4] = (t6 ^ x) % 97
            t7 = 1 * 18 - x
            g[x % 4] = t7 % 97
        else:
            t8 = ((1 ^ 5) + (a - 15)) * x
            g[x % 4] = t8 % 97
        x = (x >> 3) // 7 // 3 & 32767
        a = a + 1
    if x - 7 != 9:
        for idx in range(9):
            g[idx % 4] = (x | idx) % 97
            g[x % 4] = idx & x
        for m in range(6):
            x = (m ^ 14) + x & 32767
    if x * x == 42:
        for c in range(8):
            g[c % 4] = (c * 17 ^ x) % 97
            t9 = (11 << 4) + (c - 1) & c
            x = (t9 - x) % 9973
            t10 = x + x ^ c ^ c
            x = t10 % 1009
    else:
        x = x - 14 + x
        x = fn0((13 << 2) * x % 1009)
    if x // 5 <= 64:
        t11 = x << 4 ^ x
        x = (t11 - ((20 ^ x) << 3)) % 1009
    e = x - 11 << 1
    t12 = x - g[e % 4]
    t13 = e // 6 - 1
    g[x % 4] = (t13 + (t12 + e // 6)) % 97
    for cnt in range(4):
        for buf in range(9):
            x = (x >> 1 >> 4) % 97
            x = (13 - x) * e & 32767
            t14 = (cnt ^ 12) + cnt
            t15 = t14 + e + x
            x = t15 % 1009
        t16 = ((x | 20) << 1) * x - cnt
        e = t16 % 4093
        t17 = x // 6 >> 3
        x = (t17 + cnt) % 97
    g[x % 4] = (x + x - x) % 97
    val = x & e
    nxt = 0
    while nxt < 11:
        t18 = val % 9973 - e
        e = t18 % 9973
        if x ^ nxt > 62:
            x = (((1 & e) << 2) - nxt) % 4093
        t19 = x // 3 + val - e
        e = t19 & 4095
        nxt = nxt + 1
    t20 = g[x % 4]
    t21 = e + e
    hi = t21 - (t20 ^ x)
    t22 = e + 13 & 20 << 3
    acc = t22 - 7
    lo = (acc * x - e * x) % 9973
    return 2 + e & 8191

if __name__ == "__main__":
    arg = 18
    expected = 323
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
