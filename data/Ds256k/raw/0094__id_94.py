# Auto-extracted from ds_lt256k_500.jsonl
# record_id=94  entry=f  input='4'  output='351'  tokens=113959

def rec(n, a):
    if n <= 0:
        return a
    acc = n - a & 17
    if n - a < 33:
        for g in range(3):
            acc = 18 * acc & 8191
            t0 = (7 | acc) >> 2
            t1 = (t0 >> 1) + a
            a = t1 & 65535
            acc = (g + g + n) * a % 1009
        for d in range(7):
            a = (n | acc) + d & 2047
            t2 = 4 * 16 >> 4
            t3 = (t2 | acc) + a
            a = t3 & 32767
            a = (a << 3) * (9 ^ d) & 255
    t4 = acc // 6 * n
    tot = t4 % 1009
    t5 = (n & 19 & n) * n
    t6 = (t5 - a) % 1009
    return rec(n - 1, t6)

def fn0(e):
    cnt = 0
    while cnt < 8:
        for nxt in range(8):
            t0 = cnt + cnt
            t1 = t0 * (4 + cnt)
            e = (t1 ^ e) & 65535
        for g in range(2):
            e = (e | cnt) % 65521
        cnt = cnt + 1
    for m in range(6):
        t2 = m & 16 | e
        e = t2 % 65521
    for v in range(10):
        t3 = ((v | 7) - v) * 9
        e = (t3 ^ e) % 97
        e = ((v & 2) + e) % 65521
        t4 = v | 11
        t5 = t4 & v - 17
        e = (t5 + e) % 65521
    prv = 0
    while prv < 11:
        e = prv - 10 + e & 32767
        e = ((prv | 6) ^ e) % 4093
        t6 = (prv << 4) + e
        e = t6 & 255
        prv = prv + 1
    cur = 0
    while cur < 8:
        for lo in range(3):
            e = (e ^ cur) % 4093
        cur = cur + 1
    t7 = 4 ^ e
    t8 = t7 * (e >> 4)
    t9 = e // 2 << 1
    return (t8 + t9) % 65521

def fn1(j, g):
    y = [262, 614, 243, 217, 126, 152, 502]
    j = j % 65521
    g = j ^ g ^ g
    for u in range(9):
        t0 = y[u % 7]
        t1 = u - t0
        t2 = t1 ^ (15 | j)
        j = t2 % 65521
    for v in range(10):
        aux = 0
        while aux < 3:
            t3 = (g ^ y[aux % 7]) & 14
            t4 = y[j % 7] << 2 ^ g
            g = t3 * t4 & 131071
            t5 = g % 65521 | aux
            j = t5 % 97
            aux = aux + 1
        t6 = 7 * v ^ j
        t7 = t6 * ((j ^ 10) * j)
        g = t7 % 97
        t8 = g * g // 7
        y[g % 7] = t8 % 97
    if y[g % 7] - 1 != 9:
        if g + g < 57:
            t9 = y[j % 7]
            t10 = j * g * t9 | j
            j = t10 & 2047
            g = (j - g) % 97
        else:
            t11 = y[j % 7]
            t12 = g * g
            t13 = t12 * (g - t11)
            j = t13 - j & 262143
    t14 = 15 & y[g % 7]
    return (t14 | g) >> 2 & 8191

def f(x):
    lo = [18, 2, 59, 35, 35, 45]
    v = 0
    while v < 12:
        x = (x + v) % 251
        v = v + 1
    if lo[x % 6] > 11:
        x = x | 20
        x = ((x >> 2) - 12) // 4
    for tot in range(4):
        x = (x + 12) % 251
        hi = 0
        while hi < 6:
            t0 = (x - hi | tot) + tot
            x = t0 % 4093
            hi = hi + 1
        for z in range(16):
            t1 = x + lo[x % 6]
            lo[x % 6] = t1 * (z & tot) % 97
    cur = 0
    while cur < 6:
        t2 = cur + cur + x * cur
        t3 = x // 6 - cur - t2
        x = t3 & 8191
        if 3 * cur | x < 3:
            t4 = 19 + x >> 2
            lo[cur % 6] = t4 * 8 % 97
            lo[x % 6] = (x * x & 262143) % 97
        res = 0
        while res < 6:
            t5 = (x - 18) * (3 & cur)
            t6 = t5 | lo[x % 6]
            lo[cur % 6] = t6 % 97
            t7 = x >> 4 | res ^ 8
            lo[cur % 6] = t7 % 97
            t8 = lo[cur % 6] | cur
            x = (t8 >> 1) - x & 16383
            res = res + 1
        cur = cur + 1
    a = 0
    while a < 12:
        t9 = (20 - 2) * (a | 13) + x
        x = t9 & 255
        for nxt in range(9):
            t10 = nxt - lo[a % 6]
            x = (t10 * 20 ^ x) % 4093
        x = (a + 15 ^ x) & 262143
        a = a + 1
    return x * 13 & 131071

if __name__ == "__main__":
    arg = 4
    expected = 351
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
