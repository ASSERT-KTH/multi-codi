# Auto-extracted from ds_lt256k_500.jsonl
# record_id=390  entry=f  input='1'  output='91'  tokens=141115

def fn0(m):
    t0 = m << 1 << 1
    idx = t0 * ((m >> 4) + m) % 65521
    t1 = 17 + 4
    t2 = t1 + (m - 11)
    s = t2 // 8
    t3 = 16 + idx
    cur = t3 - (m - idx)
    for y in range(2):
        buf = 0
        while buf < 8:
            t4 = 9 * y
            t5 = t4 | m - cur
            m = t5 & 32767
            buf = buf + 1
        idx = (3 ^ m) * idx % 1009
    tot = 0
    while tot < 10:
        for res in range(9):
            s = ((3 | s) % 97 >> 1) % 97
        g = 0
        while g < 8:
            idx = ((tot ^ 10 | g) ^ idx) & 262143
            t6 = s & tot | 16
            idx = (t6 | idx) % 97
            cur = (s * cur - (idx ^ 14)) % 9973
            g = g + 1
        cur = (cur >> 1) % 65521
        tot = tot + 1
    t7 = cur * m + s
    acc = (t7 >> 3) % 9973
    return (15 - cur) * acc & 262143

def fn1(d):
    aux = [648, 113, 740, 605, 740]
    t0 = (7 ^ d) * d ^ 1
    cnt = t0 & 131071
    buf = cnt // 2
    t1 = aux[d % 5]
    t2 = buf * buf
    t3 = t2 * (t1 // 4)
    w = t3 % 9973
    t4 = 3 + 18
    t5 = 4 - cnt >> 2
    t6 = t4 ^ d % 4093
    acc = t5 * t6 & 1023
    t7 = aux[acc % 5] | 19
    d = (t7 ^ cnt + cnt) + d
    return (cnt + d >> 2) % 4093

def f(x):
    p = [47, 22, 18, 68, 85, 82]
    x = fn0((x ^ 9) % 251)
    g = 0
    while g < 64:
        t0 = (19 + x) // 3
        x = t0 & (g & 11)
        x = ((g | x) >> 4) % 9973
        t1 = p[x % 6]
        t2 = t1 * p[g % 6]
        t3 = t2 & p[x % 6]
        t4 = (g + x) * (g - 15)
        x = (t3 + t4) % 9973
        g = g + 1
    for a in range(10):
        x = x + x & x
        t5 = p[a % 6] >> 4
        t6 = a + a - t5 & a | x
        x = t6 % 251
        if 11 * a | x > 8:
            x = (x & 12) + 3 & 2047
        else:
            t7 = 11 - x << 3
            p[a % 6] = t7 // 7 % 97
    for tmp in range(4):
        t8 = p[tmp % 6]
        t9 = 8 * t8 * 9
        x = t9 - x & 511
        x = x >> 4 & 16383
        for s in range(2):
            t10 = p[s % 6] + tmp
            t11 = t10 * (tmp - 12) - x
            p[x % 6] = t11 % 97
            t12 = 14 & tmp | x
            x = t12 & 2047
            t13 = p[x % 6] ^ x
            x = t13 % 251
    t14 = p[x % 6]
    return (t14 | x) % 9973

if __name__ == "__main__":
    arg = 1
    expected = 91
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
