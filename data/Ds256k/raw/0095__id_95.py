# Auto-extracted from ds_lt256k_500.jsonl
# record_id=95  entry=f  input='9'  output='22848'  tokens=141295

def fn0(j):
    z = 0
    while z < 12:
        j = (4 << 4) + j & 255
        z = z + 1
    if j + j == 64:
        for hi in range(5):
            j = (hi + j) % 1009
    cur = 20 * j % 4093
    lo = cur + j
    if lo + j >= 63:
        c = 0
        while c < 12:
            lo = (lo + j) % 1009
            t0 = (lo | 8) * (c ^ lo)
            j = (t0 ^ lo) & 4095
            t1 = (j ^ c) + (cur - 13) - lo
            cur = t1 & 16383
            c = c + 1
        cur = 20 + 10 - j
    if lo >> 4 <= 31:
        cur = 5 | lo
        cur = 12 | cur
    buf = 0
    while buf < 3:
        t2 = 8 - 16 | j - lo
        j = t2 % 97
        buf = buf + 1
    lo = (cur + cur ^ lo) & 8191
    return (lo ^ j) % 97

def fn1(m):
    for d in range(7):
        nxt = 0
        while nxt < 7:
            t0 = d * nxt + m
            m = t0 & (m & nxt) - nxt
            t1 = (nxt | 4) + 7
            t2 = t1 | (19 + nxt) * m
            m = t2 & 16383
            nxt = nxt + 1
        cur = 0
        while cur < 4:
            m = (cur + m + 17) % 1009
            t3 = cur + 7 & d | m
            m = t3 & 8191
            cur = cur + 1
        if 2 - d - m < 14:
            t4 = (d & 18) * (m + m)
            m = t4 & 65535
        else:
            t5 = d * d + (2 ^ m) - d
            m = t5 & 32767
            m = m % 9973
    t6 = m - 3
    t7 = t6 + (m >> 2)
    g = t7 ^ m
    if g - m > 17:
        t8 = (m & 4) + m
        g = t8 + g
        w = 0
        while w < 2:
            t9 = w * w * g
            g = t9 >> 1 & 1023
            t10 = 17 * m | m
            m = t10 & 2047
            t11 = 18 - 3 | (w | m)
            g = t11 & 131071
            w = w + 1
    hi = (g >> 1) - 5 + g
    for v in range(4):
        for s in range(6):
            g = ((17 - v) * v + g) % 1009
            g = hi & g
        t12 = v - 15 << 3
        t13 = t12 * v + hi
        hi = t13 % 9973
    t14 = 18 * m
    t15 = m - 5
    t16 = t14 * (hi - g)
    t17 = t15 - hi // 8
    return (t16 | t17) % 9973

def f(x):
    for tot in range(889):
        t0 = x + tot + 11
        x = t0 & 4095
    z = x * x
    j = x | 13
    x = fn1((x + z) % 65521)
    if x - 10 != 24:
        x = j >> 4
        t1 = j - z
        t2 = z - 6
        t3 = t1 + (x ^ j)
        t4 = t2 ^ j + x
        j = t3 * t4 % 65521
    else:
        z = fn0((z + 2) % 1009)
        z = fn1(10 * 6 & x)
    return z * j * x & 32767

if __name__ == "__main__":
    arg = 9
    expected = 22848
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
