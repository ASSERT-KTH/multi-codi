# Auto-extracted from ds_lt256k_500.jsonl
# record_id=68  entry=f  input='13'  output='0'  tokens=62962

def fn0(e):
    v = (e | 2) // 8
    t = e + 6 + (v + v)
    u = 0
    while u < 4:
        v = t + t - v & 8191
        v = (1 & v) + u & 255
        u = u + 1
    y = 0
    while y < 12:
        t0 = e - 12
        t1 = t0 * (y + t)
        e = t1 & 262143
        t2 = (v * y << 4) + v
        v = t2 % 251
        t3 = e * 9 * e
        t4 = (t3 | (13 << 3) * t) ^ v
        v = t4 % 4093
        y = y + 1
    if 6 ^ v == 53:
        e = e & t
        if v * v >= 34:
            v = v % 251
            t5 = (15 - t) * (v + t)
            e = t5 + (t & 9) * v & 32767
        else:
            e = e // 6 * 16 % 9973
    c = e - 5 - e
    m = (9 + c) // 6 + v
    t6 = e % 4093 & e
    return (t6 | c) % 4093

def fn1(g, a):
    cur = a >> 3
    t0 = g * cur >> 2
    e = t0 % 251
    prv = cur * e & 511
    t1 = g % 251 + prv
    prv = (t1 | g * e // 2) % 65521
    g = (g * prv ^ a) & 65535
    for b in range(10):
        t2 = prv + 8 + (cur | e)
        a = t2 * (a * a // 8) % 65521
        v = 0
        while v < 4:
            t3 = cur + 1 & prv
            t4 = cur ^ 13 ^ 19
            t5 = t3 + t4 ^ g
            g = t5 % 65521
            v = v + 1
        for buf in range(3):
            t6 = (b + prv) * e
            t7 = t6 >> 3 ^ cur
            cur = t7 % 65521
            t8 = b - 6 | e & buf
            prv = t8 % 65521
    if cur + g >= 21:
        prv = fn0((e + a ^ g) & 511)
    else:
        if (20 ^ 2) + g != 14:
            g = e * e ^ a
        t9 = (cur >> 1) + a * g >> 3
        prv = t9 & 16383
    prv = fn0(((g | 11) - a) % 97)
    return g * cur & 1023

def f(x):
    j = [10, 21, 52, 86, 5, 87, 85, 36]
    if x & 17 >= 11:
        for acc in range(8):
            x = x + x & 4095
            j[x % 8] = 16 * j[x % 8] % 97
            t0 = (x ^ 17) // 6
            x = t0 & 2047
    else:
        g = 0
        while g < 2:
            x = (x + 20) % 9973
            g = g + 1
    c = x * x & 8191
    d = 0
    while d < 35:
        j[c % 8] = x * 17 % 97
        x = 11 & x
        t1 = j[d % 8]
        t2 = t1 << 3
        t3 = t2 - 16 * c
        c = t3 % 251
        d = d + 1
    for v in range(6):
        if 18 - 1 | c > 26:
            t4 = (c >> 2) // 3
            t5 = (x >> 1) * x
            t6 = t4 * t5 % 251
            j[x % 8] = t6 % 97
        x = (c * 12 | x) & 255
        j[v % 8] = (v - c) % 97
    for buf in range(5):
        t7 = x % 251
        t8 = t7 + (x ^ 12)
        c = (t8 + c) % 9973
    for m in range(8):
        prv = 0
        while prv < 3:
            t9 = x * prv * (8 | c) % 251
            j[c % 8] = t9 % 97
            t10 = j[m % 8]
            t11 = prv - 4
            t12 = t11 * (t10 + x)
            c = t12 % 9973
            t13 = m * prv ^ x
            x = t13 * x & 32767
            prv = prv + 1
    nxt = x // 2
    cnt = (15 | 12) - nxt
    return nxt % 251

if __name__ == "__main__":
    arg = 13
    expected = 0
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
