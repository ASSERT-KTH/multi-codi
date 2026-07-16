# Auto-extracted from ds_lt256k_500.jsonl
# record_id=109  entry=f  input='14'  output='2225'  tokens=71834

def fn0(j):
    v = j * j % 4093
    tot = 0
    while tot < 2:
        if tot + 18 | v <= 8:
            j = (tot + v) % 1009
        else:
            v = (tot + j + 16) % 4093
            v = (j ^ tot) & 255
        tot = tot + 1
    for hi in range(5):
        j = j >> 3 & 8191
        t0 = 12 * hi * (j >> 1)
        j = t0 % 4093
    for idx in range(8):
        t1 = 7 * (13 + v) + 1
        j = (t1 - j) % 1009
        v = (idx << 1 | v) % 4093
    t2 = (j & 16) * (j + v)
    b = t2 % 4093
    if 4 - b >= 42:
        v = j // 6
        v = ((j & b) >> 4) + v
    if b & v <= 64:
        t3 = j + v
        v = t3 + (v ^ b)
        b = 2 - b
    else:
        v = j - 17
        if v | 1 >= 24:
            b = v & 8
    prv = v & 20
    t4 = ((v << 4) + (prv | 2)) // 8
    return t4 & 131071

def f(x):
    hi = [108, 56, 156, 227, 222]
    tot = 11 & hi[x % 5]
    t0 = hi[x % 5]
    t1 = x - 12 ^ t0
    nxt = t1 + 3
    t2 = tot - x
    acc = t2 * (x - tot)
    if 12 ^ nxt >= 45:
        x = nxt ^ hi[x % 5]
        nxt = nxt - 3
    else:
        t3 = hi[x % 5]
        t4 = 14 - 19
        nxt = t4 | t3 << 3
        if 13 | nxt <= 58:
            t5 = hi[nxt % 5]
            t6 = t5 - 1 | x
            hi[x % 5] = t6 % 251
            t7 = hi[nxt % 5]
            hi[tot % 5] = (acc + t7) % 251
    x = fn0((x ^ 4) % 4093)
    t8 = nxt - acc ^ 18
    hi[x % 5] = (t8 - (tot + 6 << 3)) % 251
    t9 = tot + acc
    t10 = x * tot | 4
    t11 = t9 - (acc + tot)
    lo = t10 * t11 & 255
    res = lo | 5
    t12 = hi[x % 5]
    t13 = (t12 >> 1) * x
    for p in range(8):
        for g in range(9):
            t14 = hi[x % 5]
            t15 = lo - t14 - tot
            x = (t15 - g) % 4093
            t16 = p + tot + hi[lo % 5]
            hi[tot % 5] = t16 % 251
    return (t13 - tot) % 9973

if __name__ == "__main__":
    arg = 14
    expected = 2225
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
