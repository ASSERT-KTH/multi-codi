# Auto-extracted from ds_lt256k_500.jsonl
# record_id=65  entry=f  input='20'  output='82'  tokens=99263

def fn0(d, a):
    t0 = (d ^ a) * a
    e = t0 & d
    for tot in range(7):
        for idx in range(5):
            t1 = e - 5 + (idx - e)
            d = t1 * (18 << 3) & 8191
            t2 = (tot << 2) * (idx + a)
            t3 = t2 * (e - 12 << 2)
            e = t3 & 262143
    cnt = (e | 7) // 5
    s = 0
    while s < 12:
        a = s + d & 16383
        if s + d <= 24:
            t4 = d >> 3 ^ cnt
            cnt = (t4 + cnt) % 97
            t5 = (e | d) & s
            e = (t5 ^ cnt) & 511
        else:
            cnt = cnt % 1009
            t6 = s * cnt * (cnt * s)
            a = t6 & 255
        s = s + 1
    tmp = cnt // 6
    p = d * cnt & 4095
    if (19 | 10) ^ d == 16:
        a = 13 + 2 + 2 ^ tmp
    else:
        t7 = 19 - tmp
        t8 = t7 - (d - e)
        e = t8 - p
        b = 0
        while b < 8:
            t9 = (a >> 1) * cnt
            tmp = (t9 ^ tmp) % 97
            t10 = cnt + tmp + b
            p = t10 * 18 % 1009
            b = b + 1
    return (12 - p) % 1009

def fn1(m):
    j = 0
    while j < 7:
        m = j - 18 - m & 16383
        j = j + 1
    b = m | 4
    if b & 6 >= 4:
        for val in range(12):
            t0 = (b ^ 3) - b >> 3
            b = t0 % 1009
    else:
        t1 = m - 1 & 20
        t2 = m // 2 + (b + b) >> 3
        b = fn0(t1, t2 % 17)
        for t in range(7):
            t3 = t * m ^ m
            b = (t3 + b) % 17
            m = m // 6 // 7 & 2047
            t4 = m * t & 12
            b = (t4 | b) % 1009
    if b - 5 > 9:
        for p in range(9):
            m = (m | 18) + b & 8191
    else:
        if b >> 3 < 35:
            t5 = m // 5 % 1009 >> 4
            b = fn0(t5 % 251, m & b)
            m = m * m % 1009
    t6 = (m ^ 17) & 2047
    t7 = (b & m) >> 1
    t8 = m * m - b
    t9 = t7 - t8 & 2047
    b = fn0(t6, t9)
    return (b ^ m) + m & 65535

def f(x):
    y = (x + 17) * (x & 12) * 14
    nxt = (y | x) + y
    t0 = x + x | 8
    nxt = t0 ^ y
    nxt = x & nxt
    for m in range(14):
        t1 = nxt ^ m | y
        y = t1 % 9973
        for t in range(9):
            nxt = (m | nxt) % 9973
            t2 = m ^ 4
            t3 = t2 & nxt * 14
            t4 = t3 ^ m ^ y
            y = t4 & 32767
            t5 = (14 ^ 11) + nxt - y
            y = t5 % 9973
        t6 = 4 | 20
        t7 = t6 & y // 4
        y = t7 * 1 % 9973
    return ((nxt << 1) + x) % 9973

if __name__ == "__main__":
    arg = 20
    expected = 82
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
