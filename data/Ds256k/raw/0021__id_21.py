# Auto-extracted from ds_lt256k_500.jsonl
# record_id=21  entry=f  input='9'  output='68'  tokens=204146

def rec(n, a):
    if n <= 0:
        return a
    c = 0
    while c < 12:
        if a | c > 16:
            t0 = (n & 16) * n
            a = (t0 | a) & 255
            a = (a >> 1) * a % 4093
        else:
            a = (c ^ a) % 97
            a = 18 * a % 4093
        c = c + 1
    t1 = (n + a) % 65521
    return rec(n - 1, t1)

def fn0(j):
    val = [812, 239, 231, 933, 882, 522, 977]
    res = j >> 1 >> 3
    t0 = 6 & (val[res % 7] & j)
    lo = t0 | res
    prv = res // 5
    if lo // 5 == 64:
        t1 = val[prv % 7]
        lo = lo * t1 % 17
    else:
        res = lo + j
        t2 = (lo & 20) * (res - prv)
        t3 = (15 | j) - 7 ^ t2
        res = t3 & 262143
    t4 = res % 17
    u = t4 - (j | res)
    t5 = prv - val[u % 7] - u
    z = t5 ^ 19
    t6 = (res >> 1) // 7
    return t6 % 1009

def fn1(g, c):
    g = g + g
    if g - 7 <= 7:
        for lo in range(10):
            c = g * g - lo & 65535
            t0 = g % 251 | lo
            c = t0 % 251
            t1 = (c ^ 2) >> 4 | g
            g = t1 % 251
    else:
        t2 = 15 & g
        t3 = g >> 4
        t4 = t2 + (c - 14)
        t5 = t3 & g % 65521
        g = t4 - t5
    for z in range(4):
        g = (c + 19 ^ z) & 1023
        g = (2 ^ g) & 65535
    if g + c <= 27:
        v = 0
        while v < 3:
            t6 = g + c
            t7 = t6 * (c * c)
            c = (t7 + c) % 65521
            g = (2 * 13 + g) % 9973
            t8 = v + c - 11
            c = t8 % 65521
            v = v + 1
        g = (g ^ c) & c
    return c % 65521

def f(x):
    j = (x | 1) - x
    z = 0
    while z < 7:
        j = (x ^ j ^ x ^ z) % 251
        if j ^ z >= 4:
            x = j * x & 8191
        else:
            j = ((z & 13) + j) % 17
        z = z + 1
    lo = j + x & x
    t0 = x + j + x
    s = t0 % 17
    for idx in range(4):
        x = (x // 6 >> 1) % 17
    buf = 0
    while buf < 9:
        t1 = 2 * s - (6 - 20) << 3
        j = (t1 | buf) & 32767
        for p in range(9):
            t2 = (buf ^ j) - 12
            lo = t2 * lo & 4095
        if 19 + s > 1:
            j = (lo // 2 >> 2 | buf) & 2047
            t3 = buf * 10 >> 1
            lo = (t3 - x) % 17
        else:
            t4 = (lo | x) // 6
            lo = t4 % 1009
            t5 = j ^ 17 ^ s
            s = t5 % 17
        buf = buf + 1
    tmp = s * s
    g = 0
    while g < 10:
        s = (j * lo | g) & 131071
        t6 = j - 12 + (tmp ^ 1) | j
        x = (t6 | g) % 251
        g = g + 1
    for val in range(481):
        j = lo * j % 251
    m = tmp // 5
    for hi in range(6):
        for w in range(11):
            lo = (j & 5) - w & 32767
            t7 = (5 ^ s) - 4 << 2 | w
            lo = t7 % 17
            x = x * tmp % 1009
        if (7 & hi) - s == 46:
            s = (10 - 9 | s) % 1009
        else:
            t8 = m + lo - (15 + hi)
            tmp = t8 % 1009
    tot = 0
    while tot < 2:
        for b in range(12):
            t9 = (6 + s) * (lo * x)
            s = t9 & 65535
        tot = tot + 1
    m = fn0((tmp | m) * s % 17)
    res = j * tmp - j & 1023
    x = fn0((j ^ s) % 1009)
    for acc in range(4):
        for a in range(4):
            t10 = (a - s) * (tmp - 17)
            m = (12 + m) // 7 - t10 & 65535
        if lo % 17 >= 14:
            t11 = s * j & acc + 2
            lo = (t11 - s) % 17
            m = (6 * j + m) % 251
        else:
            x = (18 * lo << 3 | x) % 1009
            lo = (m // 2 - res ^ lo) & 255
    return (14 + lo) % 1009

if __name__ == "__main__":
    arg = 9
    expected = 68
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
