# Auto-extracted from ds_lt256k_500.jsonl
# record_id=0  entry=f  input='10'  output='15'  tokens=205667

def fn0(e):
    a = [844, 803, 684, 640, 1, 626, 505]
    tmp = 0
    while tmp < 7:
        t0 = e % 9973 + 16
        e = t0 + tmp & 65535
        t1 = a[tmp % 7]
        t2 = (t1 ^ e) + e
        e = t2 % 17
        t3 = (18 ^ e) // 7
        e = (t3 ^ tmp) % 4093
        tmp = tmp + 1
    if a[e % 7] - 6 > 54:
        for w in range(4):
            a[e % 7] = (e | w) % 1009
            t4 = w - 1 | e
            e = t4 & 511
            t5 = a[e % 7]
            t6 = (e ^ t5) - e
            a[e % 7] = t6 % 1009
    for idx in range(4):
        t7 = (6 + 17 << 3) * e
        e = t7 % 251
        e = idx - e & 16383
    a[e % 7] = (e - 2) % 1009
    tot = e * e // 6 & e
    for acc in range(8):
        t8 = e // 4 & (tot | 4)
        e = (e * e + 17 | t8) & 1023
    return 12 + 2 + tot >> 1 & 131071

def f(x):
    m = 0
    while m < 36:
        for d in range(8):
            x = (m * 11 + x) % 1009
            t0 = x // 7 ^ 3
            t1 = t0 + x * m * d
            x = t1 % 17
        z = 0
        while z < 6:
            x = x % 97
            t2 = m * x | m * 16
            x = (t2 + z) % 1009
            t3 = (x + m) % 17 * x
            x = t3 & 131071
            z = z + 1
        x = 17 & x
        m = m + 1
    for tot in range(9):
        x = (tot * x | x) & tot
        t4 = (x | tot) * tot
        x = t4 << 4 & 255
    tmp = x + x
    t5 = tmp * x + x
    s = (t5 | (tmp - x) // 6) & 131071
    c = (s & 13 | 4) * tmp
    if s << 1 < 5:
        y = 0
        while y < 2:
            tmp = (y ^ x) % 97
            x = (c << 1 << 4 | x) % 1009
            t6 = x * 8 ^ s
            s = t6 & 1023
            y = y + 1
        for lo in range(12):
            t7 = s & tmp
            t8 = t7 - (s + c)
            t9 = t8 >> 3 ^ x
            x = t9 & 511
            s = (tmp >> 2 ^ s) % 17
            x = (c + lo) % 17
    else:
        for res in range(9):
            t10 = (c >> 3) * (3 << 1) ^ x
            x = t10 & 1023
            c = (c - res) % 1009
            c = (c | s) % 17
        c = tmp ^ x
    t11 = (2 + 13) * tmp
    return t11 & 255

if __name__ == "__main__":
    arg = 10
    expected = 15
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
