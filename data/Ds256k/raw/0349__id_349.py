# Auto-extracted from ds_lt256k_500.jsonl
# record_id=349  entry=f  input='6'  output='978'  tokens=127533

def fn0(b, m, a):
    cur = m - 12 - (m & 4)
    for z in range(8):
        t0 = 7 - b ^ z
        cur = t0 & 262143
        b = (a * a ^ b) % 9973
        m = ((19 & a) - cur | z) & 8191
    idx = 0
    while idx < 10:
        m = (b - 19 | idx) & 131071
        idx = idx + 1
    t1 = cur // 7
    acc = t1 | 18 ^ b
    p = acc + cur
    a = 1 + b
    t2 = (acc ^ 6 ^ acc) >> 2
    return t2 % 1009

def fn1(m, c):
    val = [229, 111, 247, 216, 152, 178, 45, 198]
    for tot in range(7):
        c = (m ^ 10 | c) & 511
        y = 0
        while y < 5:
            val[tot % 8] = (c + tot) % 251
            m = ((m | 13) + tot) % 97
            val[y % 8] = (16 + c + c + c) % 251
            y = y + 1
    for acc in range(4):
        p = 0
        while p < 3:
            c = ((m | acc) >> 4 | p) % 4093
            t0 = (19 + c) * (m - 1)
            c = t0 >> 2 & 131071
            c = (c - p) % 97
            p = p + 1
    t1 = val[m % 8]
    m = t1 >> 2 ^ m
    t = 0
    while t < 2:
        m = (m | 2) + c << 1 & 131071
        c = (4 + m | c) % 4093
        t = t + 1
    if val[m % 8] & 11 == 3:
        for hi in range(2):
            t2 = hi << 4 ^ m
            val[c % 8] = t2 % 251
            t3 = 19 - hi - val[hi % 8]
            c = (t3 ^ m) & 16383
            t4 = m * val[m % 8]
            val[hi % 8] = t4 % 97
    else:
        t5 = c + m - 6
        m = t5 - m
    j = 0
    while j < 11:
        if c - m >= 14:
            val[j % 8] = 8 * m % 97
            t6 = (c >> 1 ^ m) * j
            val[c % 8] = t6 % 4093 % 251
        j = j + 1
    t7 = (c - m >> 4) // 8
    return t7 % 97

def f(x):
    d = (x << 2) - 9
    for tmp in range(10):
        for y in range(9):
            t0 = d & 4
            t1 = t0 - d * y
            d = t1 % 251
            d = ((y & 11) + 11 | d) & 2047
            t2 = d // 3 & tmp
            x = (t2 | y) & 255
        for s in range(11):
            x = (x << 1) % 251
        for res in range(35):
            x = (1 - tmp | x) % 65521
    v = 0
    while v < 9:
        if v - x > 24:
            x = v * x * v & 1023
            x = (d + 4 - 12 + x) % 65521
        if (v ^ 8) + d > 11:
            t3 = (3 & x) + d
            x = t3 & 4095
            d = d & 3
        v = v + 1
    e = (20 + 4 << 1) + d
    t4 = (e ^ d) << 4
    t5 = t4 - e & 255
    t6 = (15 + x) % 17
    x = fn1(t5, t6)
    t7 = (16 + d) * e + 9
    return t7 % 65521

if __name__ == "__main__":
    arg = 6
    expected = 978
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
