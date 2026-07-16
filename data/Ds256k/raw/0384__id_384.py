# Auto-extracted from ds_lt256k_500.jsonl
# record_id=384  entry=f  input='15'  output='0'  tokens=172681

def fn0(g, m, j):
    for cur in range(12):
        if (7 | 16) - g <= 57:
            t0 = g - 17 - (cur + 14)
            m = t0 * cur & 2047
        for y in range(8):
            j = (18 + y - g) % 9973
        if 20 * 1 ^ g == 31:
            j = (m + m | cur) & 1023
    for z in range(4):
        j = (m >> 1 | 4) - z & 2047
    t1 = 7 << 2 | g
    j = t1 >> 4
    g = 8 * 19 & g
    t2 = j + j
    j = t2 + (g ^ 1)
    g = (5 << 3) + m
    if g + j != 61:
        m = (g | m) * m % 1009
    else:
        t3 = 5 * j
        t4 = t3 - (j - 8)
        g = t4 & 511
        t5 = m * 5
        t6 = t5 & g - 2
        t7 = 19 - j + g
        g = t6 ^ t7
    return j + m & 8191

def fn1(j):
    for nxt in range(4):
        for e in range(4):
            t0 = nxt * nxt - nxt * 11
            j = t0 - j & 255
            j = (7 - e ^ j) & 255
            t1 = (4 | j) * (nxt * nxt)
            j = t1 + e & 8191
        for p in range(3):
            t2 = 15 + j + (p - nxt)
            j = t2 & p
            t3 = (nxt | 7) * p
            j = (t3 ^ j) % 97
            j = (nxt - j) // 8 & 1
    t4 = 7 - 16 ^ j
    t5 = (5 | j) & 255
    t6 = (17 - j) % 97
    j = fn0(t4 & 131071, t5, t6)
    tot = j * 14
    for cnt in range(4):
        t7 = tot + 15
        t8 = t7 | tot * cnt
        j = t8 % 1009
        a = 0
        while a < 2:
            t9 = cnt * cnt - tot - cnt + a
            j = t9 % 1009
            tot = (cnt - tot) % 1009
            a = a + 1
    j = j << 1 ^ 7
    j = tot - 17
    return tot + j & j

def f(x):
    e = [304, 685, 596, 766, 916, 527]
    u = (17 + x) * 10
    t0 = e[u % 6] ^ 7
    t1 = (u << 2) + u
    g = t1 - (t0 - x)
    if e[x % 6] | g <= 38:
        g = u + g
    else:
        j = 0
        while j < 3:
            t2 = e[x % 6] - u
            e[g % 6] = t2 % 1009
            t3 = x + e[x % 6]
            e[u % 6] = t3 % 1009
            j = j + 1
        if e[x % 6] & g == 19:
            u = 19 + u
            t4 = e[g % 6] | u
            u = t4 ^ (u ^ g) ^ g
    t5 = e[g % 6]
    t6 = 3 << 2
    t7 = t6 ^ t5 * u
    a = t7 & 16383
    t8 = (4 + u) * (g << 2)
    g = fn1(t8 + 1 & 8191)
    t9 = e[u % 6]
    t10 = (t9 ^ u) // 2
    t11 = e[u % 6]
    u = fn1((t10 ^ t11) & 1023)
    e[u % 6] = ((19 ^ u) & x) << 3
    for s in range(11):
        for idx in range(12):
            e[g % 6] = (u << 3) % 1009
            g = (g & s) * (g | a) % 1009
        t12 = 7 - e[s % 6] ^ g
        u = t12 & 65535
        e[a % 6] = (a >> 1) % 1009
    q = (7 ^ 12) + a
    m = g ^ 10
    c = 0
    while c < 4:
        if e[u % 6] | c == 25:
            t13 = (c & 4 | 13) - a
            g = t13 % 1009
            t14 = g * e[x % 6]
            g = (t14 // 7 + c) % 1009
        m = m + m & 8191
        c = c + 1
    if g + m >= 33:
        for res in range(6):
            t15 = m + u
            t16 = t15 * (5 + 7)
            t17 = (res ^ 19) - 8
            x = (t16 ^ t17) % 97
            e[res % 6] = (a >> 4) % 1009
    else:
        if g // 3 == 46:
            e[u % 6] = ((3 ^ g) >> 4) % 1009
            e[g % 6] = x ^ 7
        a = x + e[a % 6]
    tot = (9 | 8) ^ m
    m = fn1((g ^ u) & 16383)
    t18 = u - e[tot % 6]
    return t18 * (g >> 4) % 1009

if __name__ == "__main__":
    arg = 15
    expected = 0
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
