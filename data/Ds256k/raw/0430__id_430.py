# Auto-extracted from ds_lt256k_500.jsonl
# record_id=430  entry=f  input='18'  output='8036'  tokens=62301

def fn0(e):
    y = e - 6
    if e - 6 <= 48:
        e = e - y
        cnt = 0
        while cnt < 2:
            t0 = (9 | cnt) - 1 + e
            e = t0 % 4093
            t1 = y % 4093
            t2 = t1 - (12 ^ y)
            y = t2 % 17
            t3 = (y // 4 + cnt) * y
            e = t3 % 9973
            cnt = cnt + 1
    else:
        for m in range(3):
            e = e - m - y & e
        y = (y >> 1) // 7 - y
    for w in range(8):
        y = (e // 2 - y) % 9973
        for u in range(6):
            e = (w + y | e) & 262143
    t4 = (12 ^ 18) + 9
    res = t4 * y & 511
    return res + y & y

def fn1(a, c):
    m = [995, 15, 562, 872, 905, 862]
    prv = c ^ 16
    a = c ^ 9
    p = 0
    while p < 10:
        a = (a % 65521 - 6) * a % 97
        p = p + 1
    buf = 0
    while buf < 2:
        t0 = (1 - a | a) + buf
        c = t0 % 17
        buf = buf + 1
    m[a % 6] = (a + prv ^ 3 * c) % 1009
    prv = fn0((m[a % 6] << 2) % 65521)
    t1 = m[prv % 6]
    t2 = m[c % 6]
    t3 = t2 << 1
    t4 = 1 + c ^ t1
    t5 = t3 & c - 3
    a = t4 - t5
    if c + prv >= 0:
        t6 = (c ^ 12) * a
        prv = t6 % 65521
        c = c | a
    return (prv | a) & 32767

def f(x):
    a = [984, 924, 254, 141, 181, 294, 956]
    t0 = x * x * (x - 14)
    x = fn0((x << 1 ^ t0) % 4093)
    t1 = a[x % 7] * 7 - x
    m = t1 & x
    t2 = a[x % 7] & m ^ x
    m = t2 << 4 & 16383
    for v in range(8):
        for d in range(28):
            t3 = a[v % 7] | m
            a[m % 7] = t3 // 5 % 1009
        t4 = (m | v) & v + x | v
        x = t4 % 4093
        t5 = (a[v % 7] >> 2) - x
        m = t5 & 16383
    return m * m % 9973

if __name__ == "__main__":
    arg = 18
    expected = 8036
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
