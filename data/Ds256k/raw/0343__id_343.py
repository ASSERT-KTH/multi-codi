# Auto-extracted from ds_lt256k_500.jsonl
# record_id=343  entry=f  input='14'  output='3729'  tokens=211703

def fn0(m, b):
    w = b % 97
    d = (5 - b) // 3
    if w + b > 19:
        d = 13 - 12 ^ d >> 1
        if d | b != 1:
            b = (b << 2) + d
    else:
        t0 = m + m & w // 2
        t1 = t0 - (b + 11) * (b // 7)
        d = t1 % 97
    t2 = m + 7
    cur = t2 - (d | w)
    m = (w * m ^ 7) & 262143
    return (cur - 9 ^ 20) % 97

def f(x):
    if x > 12:
        t0 = x ^ 9 ^ x - 7
        x = t0 + x
    tot = x + x - x
    s = tot - 2 + x
    for cnt in range(8):
        t1 = 3 * tot & 7
        x = (t1 ^ x) & 8191
        for tmp in range(8):
            s = (tmp - cnt | x) % 9973
            s = tmp * x * 5 % 9973
        t2 = s // 8 * (tot & 9)
        tot = t2 - x & 16383
    m = 0
    while m < 5:
        t3 = (2 | m) - tot
        x = t3 & 32767
        tot = ((tot & x) << 2) % 4093
        m = m + 1
    nxt = (s >> 4 >> 2) - tot
    for cur in range(5):
        for d in range(3):
            x = (d - s - 13) % 9973
        t4 = s * 19 >> 3
        t5 = t4 + (x ^ 5) * nxt | cur
        tot = t5 & 131071
    for u in range(9):
        t6 = 5 + tot
        t7 = t6 - (x & u)
        s = t7 & 2047
        t8 = s * tot + s
        tot = t8 * x & 8191
    j = 17 * x + 6
    for a in range(13):
        t9 = nxt // 7 + (tot + tot) | x
        j = (t9 | a) % 4093
        e = 0
        while e < 2:
            t10 = (nxt >> 2) * 17 // 2 ^ e
            j = t10 % 9973
            t11 = a * x - j
            j = t11 & 4095
            e = e + 1
        for v in range(10):
            t12 = (j >> 3) - s | j | v
            nxt = t12 & 4095
    for idx in range(8):
        buf = 0
        while buf < 8:
            j = ((j & x) + x) % 4093
            t13 = s // 4 - nxt
            nxt = t13 & 32767
            j = (9 + j & nxt) + nxt & 4095
            buf = buf + 1
    t14 = 19 + nxt - x // 5
    t15 = t14 + (18 - x ^ j)
    return t15 % 9973

if __name__ == "__main__":
    arg = 14
    expected = 3729
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
