# Auto-extracted from ds_lt256k_500.jsonl
# record_id=262  entry=f  input='20'  output='0'  tokens=199539

def rec(n, a):
    if n <= 0:
        return a
    a = ((a - n >> 2) - n) % 97
    t0 = (4 ^ n) * 14 - a
    a = t0 & 32767
    t1 = ((a & 10) - a) % 251
    return rec(n - 1, t1)

def fn0(c, e):
    d = [82, 35, 68, 21, 29, 14, 36, 87]
    tmp = (e >> 1) + c
    if tmp - 11 < 21:
        e = (tmp + e) // 7 // 3
        if d[e % 8] + 10 <= 32:
            t0 = c - 15 - 2
            e = t0 & (tmp | 10) - c
            t1 = (c ^ 17) * (c * 19)
            d[tmp % 8] = (t1 & 32767) % 97
    else:
        t2 = (20 ^ e) & tmp * c
        e = tmp - c + e + t2
        for hi in range(11):
            tmp = ((c + e >> 1) - tmp) % 1009
    z = ((7 ^ e) - 7) % 1009
    prv = 0
    while prv < 4:
        tmp = (z | c | tmp) & 511
        z = (e - tmp) * prv % 65521
        for u in range(6):
            d[e % 8] = prv * c % 97
            d[e % 8] = e // 2 % 97
            d[tmp % 8] = (z * 10 + prv) % 97
        prv = prv + 1
    lo = e + tmp
    if lo * e >= 43:
        t3 = d[lo % 8]
        lo = 1 + 15 - t3
    else:
        t4 = lo * 19 >> 4 << 1
        c = t4 & 2047
    return (e // 6 // 8 ^ tmp) & 4095

def fn1(j):
    cur = [92, 90, 37, 13, 85, 57, 96, 58]
    t0 = (j >> 1 ^ j + j) & 1023
    t1 = (j + 17) % 1009
    j = fn0(t0, t1)
    buf = j >> 3
    t2 = cur[j % 8]
    buf = t2 * 17
    for y in range(8):
        t = 0
        while t < 10:
            j = 4 * 6 * j & 131071
            t3 = cur[t % 8] - t ^ t
            buf = (t3 % 17 ^ buf) % 251
            cur[buf % 8] = t * buf % 97
            t = t + 1
    j = (j | buf) // 3
    j = (j ^ 4) >> 4
    t4 = (buf ^ 8) * cur[j % 8]
    return t4 * 10 % 1009

def f(x):
    c = x ^ 8
    nxt = (c & x) - 4
    res = (c << 1) * (c * nxt)
    c = fn1(c + 10 & res & nxt)
    tot = (x ^ 5) + nxt
    hi = (c | nxt) ^ tot
    for m in range(2):
        t0 = 18 * c
        t1 = t0 * (hi | 15)
        nxt = (t1 + m) % 251
        hi = (tot - res + hi) % 251
        t2 = (tot & 13) * (nxt ^ 9)
        res = (t2 + res) % 17
    nxt = fn1((14 + 1 ^ nxt) & 255)
    val = 0
    while val < 9:
        if tot ^ nxt <= 28:
            x = c // 4 - val & 4095
        else:
            c = c % 17
            tot = ((20 + x) // 5 - tot) % 17
        if hi + res == 44:
            nxt = ((x // 5 >> 2) + val) % 251
            x = ((18 ^ hi) & res | val) % 17
        else:
            nxt = nxt // 6 % 251
            t3 = 10 << 3
            t4 = t3 ^ val - 3
            tot = (t4 | tot) % 251
        val = val + 1
    for cur in range(7):
        t5 = (18 - res ^ 6) - x
        x = t5 % 251
        t6 = hi & nxt & 13 - c
        x = (t6 | x) & 32767
        for cnt in range(19):
            t7 = c * res | cnt
            x = t7 % 17
    for z in range(10):
        for p in range(7):
            t8 = res + x >> 3
            t9 = t8 + c - p
            hi = t9 % 251
        t10 = tot // 2 + (z << 1)
        t11 = c + c - x + t10
        hi = t11 % 17
    t12 = 16 * res % 251
    return t12 * c & 65535

if __name__ == "__main__":
    arg = 20
    expected = 0
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
