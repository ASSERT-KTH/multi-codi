# Auto-extracted from ds_lt256k_500.jsonl
# record_id=293  entry=f  input='15'  output='767'  tokens=151526

def fn0(e, g):
    lo = 0
    while lo < 6:
        for v in range(5):
            e = e % 251
            e = ((lo ^ v) * g ^ e) % 251
            g = (lo * v - g) % 9973
        lo = lo + 1
    nxt = 12 * e * g % 251
    buf = 0
    while buf < 4:
        g = nxt + g & 8191
        t0 = g % 251
        t1 = t0 | 19 + nxt
        t2 = (buf | 6) - t1
        nxt = t2 % 251
        buf = buf + 1
    if g ^ e < 10:
        b = 0
        while b < 6:
            g = g * g % 9973
            nxt = (b ^ g) >> 2 & e
            t3 = g * 5 ^ nxt & b
            g = t3 & 2047
            b = b + 1
        nxt = ((6 + g) * e ^ 10) & 1023
    a = (nxt >> 2 & nxt) >> 2
    t4 = g * a % 9973 * a
    d = t4 & 1023
    return e & d

def f(x):
    for u in range(6):
        x = (8 ^ 16) + x & 511
        x = (x ^ u) % 4093
        for j in range(2):
            x = (20 - u | x) & 2047
    lo = x << 1
    buf = 0
    while buf < 239:
        t0 = 8 - buf
        lo = t0 & (1 | lo)
        if x - buf != 34:
            lo = (x - lo) % 4093
            t1 = (5 ^ buf) + (buf - lo)
            x = t1 & 255
        else:
            lo = buf + (lo - 2) & 262143
        x = x - 12 & 2
        buf = buf + 1
    t2 = x * 14 | 8
    t3 = 20 * lo - 15
    m = t2 - t3
    for cur in range(12):
        lo = (18 - cur + cur | lo) & 65535
    acc = lo >> 4
    hi = lo << 1
    c = 11 << 1 | hi
    if c + hi >= 0:
        t4 = (c ^ acc) & 511
        t5 = 6 * x % 4093
        lo = fn0(t4, t5)
        g = 0
        while g < 3:
            x = (12 * hi + g) % 1009
            t6 = (acc & 2) - lo | x
            x = t6 % 1009
            t7 = lo * acc - 13
            hi = (t7 ^ g) % 65521
            g = g + 1
    if x + lo <= 48:
        for y in range(9):
            c = x * hi - c & 2047
            m = (m ^ 1) & 32767
        hi = lo * x % 65521
    else:
        if hi * acc >= 42:
            t8 = c + lo - 19
            hi = t8 ^ acc
            t9 = lo * m * acc % 65521
            t10 = 13 * hi & 8191
            c = fn0(t9, t10)
    for nxt in range(2):
        e = 0
        while e < 4:
            t11 = x & 17
            t12 = t11 - (e + 17)
            x = t12 - c & 255
            lo = (nxt & 1) + hi + lo & 255
            e = e + 1
        if 17 - m != 41:
            t13 = (18 - 6) * m - c + x
            x = t13 & 255
            t14 = nxt - hi
            t15 = nxt - hi
            t16 = t14 ^ nxt << 1
            t17 = t15 ^ (hi | c)
            c = (t16 - t17) % 4093
        else:
            lo = (c + 5 - lo) % 65521
        if hi + 8 != 4:
            t18 = (lo ^ 5) - hi
            m = t18 + m & 2047
        else:
            c = m * m // 3 & nxt
    t19 = x + hi - lo // 4 | x
    return t19 % 65521

if __name__ == "__main__":
    arg = 15
    expected = 767
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
