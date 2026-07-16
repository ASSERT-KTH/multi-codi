# Auto-extracted from ds_lt256k_500.jsonl
# record_id=63  entry=f  input='4'  output='24'  tokens=164469

def fn0(j):
    tmp = [8, 17, 24, 13]
    if j % 1009 == 38:
        j = j - 16 ^ j
        for v in range(11):
            t0 = 6 | tmp[v % 4]
            j = (t0 - j) % 65521
            t1 = v - tmp[j % 4]
            t2 = v - j - (v ^ 18)
            tmp[j % 4] = (t1 & t2) % 97
    else:
        for m in range(12):
            t3 = tmp[j % 4] << 4
            j = t3 & 8191
            j = 6 * j & 262143
            j = (m & j) + m + 14 & 262143
        j = j // 5 >> 3 >> 4
    t4 = (17 & j) - j << 4
    e = t4 & 255
    nxt = 19 + j
    e = j | e
    for y in range(5):
        t5 = nxt - tmp[nxt % 4] | y
        e = t5 % 9973
        t6 = 2 + nxt
        t7 = e + y & nxt
        t8 = t6 | j * y
        e = (t7 - t8) % 17
        t9 = j // 4 - nxt
        nxt = t9 & 511
    t10 = tmp[nxt % 4]
    t11 = tmp[j % 4]
    t12 = tmp[nxt % 4]
    t13 = t10 >> 1
    t14 = t13 ^ t11 & t12
    j = t14 + e
    j = 2 * tmp[j % 4]
    return ((j | e) >> 4) % 9973

def fn1(e, j):
    tot = (e ^ j) & 6 | e
    t0 = (e + e) * e ^ tot
    nxt = t0 % 17
    for w in range(6):
        for val in range(3):
            t1 = (w ^ nxt) + (11 - w) | val
            e = t1 % 97
            nxt = (nxt + 20) % 97
            j = (w - val << 3 | nxt) % 97
        t2 = tot * e ^ nxt + j
        nxt = t2 % 17
        for u in range(7):
            t3 = 19 * 8 + nxt + tot
            tot = t3 % 97
            t4 = e * e ^ u
            j = t4 & 255
    j = fn0((e | j) * tot % 4093)
    t5 = 14 * 17 | 19
    e = fn0((t5 + tot) % 17)
    t6 = tot % 4093 | (12 | e)
    return t6 & 262143

def f(x):
    hi = x & 13
    t0 = x ^ 6
    t1 = t0 + (3 - 11)
    t2 = t1 * hi & 8191
    x = fn1(20 & hi, t2)
    t3 = x & hi | x - 18
    idx = t3 & x * 17 - x
    for t in range(31):
        idx = (16 ^ t | hi) % 97
        g = 0
        while g < 7:
            t4 = idx - t >> 4
            x = (t4 ^ x) & 8191
            g = g + 1
        if hi - 3 >= 4:
            t5 = (19 | 13) + 18
            t6 = t5 ^ x | idx
            idx = t6 & 262143
    x = fn0(hi + idx & 131071)
    q = (x * x & 4) - idx
    t7 = q ^ 14 ^ q - x
    t8 = t7 | q >> 1 >> 4
    hi = fn1(x & 6, t8 % 97)
    t9 = (x ^ hi) // 3
    return t9 + idx & 255

if __name__ == "__main__":
    arg = 4
    expected = 24
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
