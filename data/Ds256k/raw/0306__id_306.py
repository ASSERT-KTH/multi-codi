# Auto-extracted from ds_lt256k_500.jsonl
# record_id=306  entry=f  input='12'  output='0'  tokens=103247

def fn0(b, a):
    cnt = [78, 0, 76, 49, 77, 39, 37, 12]
    m = a - 13
    t0 = m * m * b
    lo = t0 & 2047
    tot = 0
    while tot < 3:
        t1 = 15 ^ 10 | lo
        lo = t1 % 65521
        y = 0
        while y < 9:
            t2 = b + lo - m
            m = t2 % 9973
            y = y + 1
        for hi in range(7):
            t3 = tot | b
            t4 = t3 + m * b
            lo = (t4 | hi) & 16383
            t5 = 9 - cnt[tot % 8]
            t6 = t5 - cnt[lo % 8]
            cnt[m % 8] = (tot * hi ^ tot ^ t6) % 97
            m = (tot | lo | m) % 9973
        tot = tot + 1
    j = lo ^ b
    if j + m < 57:
        j = (m | j) + (lo >> 3) >> 2
    t7 = cnt[lo % 8] * a
    lo = (t7 | m >> 4) % 65521
    t8 = j - 16 | b + lo
    t9 = t8 - cnt[a % 8]
    cnt[m % 8] = t9 % 97
    t10 = lo ^ cnt[lo % 8]
    a = t10 ^ b + m
    t11 = lo + cnt[b % 8]
    return (lo >> 2 | t11) % 65521

def f(x):
    for y in range(2):
        buf = 0
        while buf < 101:
            x = (19 - buf - (x ^ buf)) % 1009
            t0 = y * 14 << 4
            t1 = t0 ^ (buf & y) << 1 | x
            x = t1 & 4095
            x = (x - y) % 17
            buf = buf + 1
        t2 = (y | 18) ^ x
        t3 = x // 8 >> 1
        x = t2 & t3
        if x % 1009 <= 20:
            x = (8 - 6 | x) % 251
        else:
            x = x << 4 & 65535
            x = (y - 1 - x ^ 18) % 17
    c = 13 * x
    tmp = x + x
    tmp = fn0(8 & c, tmp & 19)
    q = tmp * c % 17
    x = (x >> 2) * c % 17
    t4 = q & 10
    tmp = t4 - (q - tmp)
    return (c ^ x ^ c) & 32767

if __name__ == "__main__":
    arg = 12
    expected = 0
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
