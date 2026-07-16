# Auto-extracted from ds_lt256k_500.jsonl
# record_id=120  entry=f  input='13'  output='5'  tokens=257606

def f(x):
    e = [50, 99, 222, 249]
    hi = 19 + 4 & x
    lo = 0
    while lo < 10:
        t0 = e[lo % 4] - 7
        t1 = lo + 1 ^ hi
        hi = t1 + (t0 | 4) & 131071
        lo = lo + 1
    s = x - 20
    idx = hi
    e[x % 4] = (s << 1) * idx % 251
    tot = s - hi
    t2 = (s - 12) * hi
    u = t2 // 8
    cur = 0
    while cur < 2:
        if idx >> 1 == 62:
            e[cur % 4] = x + 7
            t3 = hi & 11 | cur
            idx = t3 & 32767
        for z in range(3):
            e[idx % 4] = tot // 6 % 251
        cur = cur + 1
    if tot >= 33:
        t4 = e[tot % 4]
        e[tot % 4] = 1 & t4
    else:
        u = hi >> 2 & x
        for b in range(7):
            e[hi % 4] = x + 5
            t5 = s ^ 1
            t6 = t5 + (x - 19)
            s = t6 & 4095
            e[x % 4] = ((b - idx) * x - b) % 251
    nxt = (e[u % 4] & 7) << 1
    for m in range(8):
        a = 0
        while a < 11:
            nxt = 20 - nxt & 2047
            a = a + 1
        if e[nxt % 4] & hi > 25:
            t7 = (m | 20) ^ nxt
            hi = t7 & 8191
            t8 = e[nxt % 4]
            t9 = m & t8
            t10 = t9 * (x + nxt)
            t11 = t10 ^ tot // 5
            e[nxt % 4] = t11 % 251
        t12 = nxt ^ x | x
        nxt = t12 & 11
    prv = (x ^ u) + x
    tmp = 7 << 1 << 3 ^ nxt
    for q in range(12):
        t13 = 20 * 10 & 8 | tmp
        u = (t13 ^ q) & 8191
        for res in range(21):
            x = e[x % 4] % 17
            e[tot % 4] = (hi | x) // 4 % 251
            s = ((16 & 6) * u + res) % 4093
    t14 = (7 ^ hi) // 7
    t15 = e[hi % 4]
    g = t14 + t15
    return (7 ^ tmp) % 17

if __name__ == "__main__":
    arg = 13
    expected = 5
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
