# Auto-extracted from ds_lt256k_500.jsonl
# record_id=465  entry=f  input='4'  output='65'  tokens=35193

def rec(n, a):
    if n <= 0:
        return a
    t0 = 13 * n | a
    tmp = t0 & 255
    t1 = a + tmp - 15
    tmp = t1 % 97
    t2 = (tmp - 19) // 3 - a & 255
    return rec(n - 1, t2)

def fn0(g, a):
    for tot in range(9):
        t0 = ((a & tot) - tot) * a
        g = t0 & 65535
        g = ((6 ^ a) & a ^ tot) % 97
    for s in range(5):
        if 5 & a != 2:
            g = (g ^ 6) >> 3 & 2047
        t1 = s + a
        t2 = t1 - 18 * s
        g = t2 + 13 & 262143
        t3 = s + a + s
        a = t3 * s & 1023
    for idx in range(9):
        t4 = (a >> 1) // 6
        a = t4 & 4095
    buf = (12 - g) // 5
    e = 0
    while e < 12:
        t5 = (10 - e) * e
        buf = (t5 ^ a) & 4095
        if 5 - 20 ^ g > 6:
            g = (15 * a | e) & 262143
            a = (buf - g + e) % 251
        t6 = (buf + g) // 2
        a = (t6 | a) % 97
        e = e + 1
    nxt = 0
    while nxt < 4:
        t7 = a ^ g ^ buf
        buf = t7 & 4095
        if nxt - buf > 12:
            buf = buf + buf & 255
        if 14 ^ g == 26:
            g = ((17 | a) - g) % 97
        nxt = nxt + 1
    y = 0
    while y < 9:
        t8 = y + buf
        t9 = t8 * (buf >> 3)
        t10 = 16 - g ^ buf
        buf = t9 * t10 % 4093
        y = y + 1
    return (buf ^ a) * a & 65535

def f(x):
    j = [245, 154, 104, 157, 238, 228, 125]
    v = (11 - x & x) - x
    if j[v % 7] + j[v % 7] != 37:
        if v + x != 4:
            x = 14 & x
            t0 = v * x + v
            j[v % 7] = t0 % 251
        for tot in range(3):
            j[v % 7] = x * v % 251
    cur = j[x % 7] + v
    t1 = j[v % 7]
    x = t1 + v
    if cur * x < 63:
        for y in range(6):
            t2 = 7 ^ j[v % 7]
            t3 = t2 + j[cur % 7]
            cur = t3 & 1023
    else:
        for p in range(7):
            j[p % 7] = (p & cur) * (cur << 4) % 251
            t4 = j[v % 7]
            x = (t4 | x) & 511
            t5 = j[v % 7] << 1
            j[v % 7] = t5 % 251
        v = ((7 ^ 4) + x) // 5
    for e in range(7):
        t6 = j[cur % 7] << 4
        t7 = v ^ e ^ x
        v = t7 + (t6 - x) & 8191
        for a in range(23):
            j[e % 7] = (3 - cur) % 251
    if j[cur % 7] * cur < 58:
        t8 = x + v
        cur = t8 + cur * x
        for c in range(6):
            t9 = j[x % 7]
            t10 = x + t9 >> 2
            x = (t10 << 1) % 9973
            t11 = j[c % 7]
            t12 = (14 ^ t11) - x
            t13 = x // 4 ^ v
            j[c % 7] = (t12 + t13) % 251
            cur = ((c << 4) + v) % 65521
    else:
        x = v + v
    t14 = (cur ^ 8) + j[x % 7]
    return (t14 >> 2) % 65521

if __name__ == "__main__":
    arg = 4
    expected = 65
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
