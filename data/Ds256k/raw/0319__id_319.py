# Auto-extracted from ds_lt256k_500.jsonl
# record_id=319  entry=f  input='16'  output='179'  tokens=93511

def fn0(m, j):
    if j & 4 > 4:
        if j | 5 > 45:
            t0 = j & m | (j | 8)
            j = t0 % 97
            j = m >> 1
        c = 0
        while c < 11:
            t1 = (j | 3) // 6
            m = t1 - m & 255
            c = c + 1
    else:
        j = (j * m + j) // 4 % 9973
    lo = (m * j | j) % 9973
    g = 0
    while g < 7:
        if m - j < 42:
            lo = ((j << 3) + g) % 9973
            j = g * 4 & m + lo
        g = g + 1
    val = (lo ^ j) - (lo & m)
    for s in range(11):
        t2 = val - lo - s
        m = t2 % 9973
        t3 = (lo ^ 2) * s
        m = t3 & 255
        w = 0
        while w < 8:
            lo = lo // 5 % 9973
            t4 = 13 * val | w
            val = t4 % 97
            w = w + 1
    t5 = j ^ m ^ j >> 2 | lo
    return t5 % 9973

def fn1(j, a, c):
    buf = a + a - a | j
    val = 13 + buf - j
    val = c - 7 - j ^ j
    if c + c >= 6:
        t = 0
        while t < 11:
            a = (buf ^ t) // 4 % 65521
            t0 = 10 + 15 ^ val
            c = (t0 ^ t) & 511
            t = t + 1
        b = 0
        while b < 12:
            t1 = j * 3 | 10
            a = (t1 - a) % 65521
            t2 = j + a - b
            buf = t2 & 131071
            b = b + 1
    else:
        c = val ^ 12
        g = 0
        while g < 3:
            c = (buf * buf + c) % 4093
            t3 = (j ^ c) * c + 13 | buf
            buf = t3 % 4093
            g = g + 1
    buf = 19 + 10 ^ val
    if c - 11 == 7:
        val = 13 - buf + j
    else:
        if buf * 20 == 18:
            t4 = (c - a - (val ^ 17)) % 97
            t5 = a + a & 131071
            c = fn0(t4, t5)
            j = c % 97 * c & 4095
        else:
            t6 = buf - 14
            a = t6 + (15 & c)
        t7 = a // 5 * a & 65535
        t8 = ((buf * a ^ val) << 3) % 97
        a = fn0(t7, t8)
    t9 = (19 << 4) - val
    return t9 % 65521

def f(x):
    t0 = (x & 20) * (x + x)
    t = t0 + (x - 2 & x)
    a = x ^ t >> 4
    for e in range(362):
        a = ((t & x) - e) % 17
        t1 = (x - t) // 5 ^ a
        a = t1 % 9973
        x = (t + t | e) % 9973
    return (a | 17) % 9973

if __name__ == "__main__":
    arg = 16
    expected = 179
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
