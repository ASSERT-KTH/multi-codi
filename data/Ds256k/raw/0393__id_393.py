# Auto-extracted from ds_lt256k_500.jsonl
# record_id=393  entry=f  input='20'  output='1001'  tokens=136358

def rec(n, a):
    if n <= 0:
        return a
    if (n >> 3) - a == 16:
        a = (14 * n | a) % 251
        a = (a % 17 | n) & 1023
    else:
        a = (a >> 2 >> 4) - a & 8191
    if a - n != 8:
        for buf in range(2):
            a = (buf * buf + a) % 17
        j = 0
        while j < 6:
            a = (10 + n | a) & 131071
            j = j + 1
    else:
        a = (n + 12 ^ a) % 9973
    a = (20 + 18 | n) * a & 2047
    t0 = n * a + 6
    t1 = t0 * ((16 ^ 13) * a)
    return rec(n - 1, t1 % 17)

def fn0(g):
    u = (g - 10) * 11
    for aux in range(3):
        g = (g + aux ^ aux) & 8191
        tot = 0
        while tot < 6:
            t0 = g - aux - (tot ^ 6)
            t1 = tot * u + tot * aux
            u = t0 * t1 % 1009
            tot = tot + 1
        t2 = aux + u | g & 9
        t3 = t2 + ((g >> 1) - g * u)
        g = t3 % 9973
    t4 = (13 - g | u) % 1009
    g = rec(72, t4)
    t = g - 16 & g + 4
    t5 = (t ^ 2) * (t - u)
    t6 = (g | u) % 17 + t5
    g = rec(73, t6 & 32767)
    q = 0
    while q < 5:
        lo = 0
        while lo < 2:
            t7 = q * q
            t8 = (g >> 2) - lo
            t9 = t7 & g + u
            u = (t8 + t9) % 9973
            lo = lo + 1
        q = q + 1
    for acc in range(8):
        for d in range(5):
            t10 = acc * (g // 8)
            u = (t10 ^ u) % 9973
            t11 = acc & d * acc
            u = (t11 - u) % 9973
        e = 0
        while e < 11:
            t12 = g * 20 - e
            t = t12 % 17
            e = e + 1
    buf = g - 5
    return (u + u) % 97

def fn1(j):
    u = [119, 125, 150, 25, 102]
    b = 3 - j
    if j | b != 39:
        a = 0
        while a < 10:
            t0 = a - 9 << 4
            u[b % 5] = (t0 + b) % 251
            t1 = u[a % 5]
            t2 = t1 + u[j % 5]
            j = t2 % 17
            t3 = a * u[j % 5]
            j = t3 & 16383
            a = a + 1
    for c in range(4):
        u[j % 5] = (j + j) % 251
        j = (j ^ 18) % 1009
        s = 0
        while s < 12:
            t4 = j >> 1 ^ 14 - j
            j = (t4 + ((c ^ 6) << 1)) % 17
            b = s - b & 2047
            t5 = 1 + c - j
            u[s % 5] = t5 % 251
            s = s + 1
    for tmp in range(4):
        if j * j > 64:
            t6 = j + tmp - (tmp - b)
            u[tmp % 5] = t6 % 251
        else:
            j = (4 - tmp | j) % 17
    cnt = 0
    while cnt < 9:
        lo = 0
        while lo < 10:
            u[b % 5] = (b + b) % 251
            b = (17 * j // 5 ^ b) & 255
            u[cnt % 5] = (13 & cnt | b) % 251
            lo = lo + 1
        cnt = cnt + 1
    if 17 * b != 39:
        t7 = b - 18
        t8 = t7 * (b << 2)
        j = t8 % 9973
        if b >> 3 == 44:
            j = j - 11
    t9 = u[b % 5]
    t10 = u[j % 5]
    t11 = t9 - j ^ t10
    return t11 & 32767

def f(x):
    acc = [106, 423, 486, 329, 733]
    w = x + 3 + x
    t0 = x + 4 - (9 + x)
    t1 = x - w + (x + x)
    u = t0 - t1
    x = 14 + u
    if 8 | u >= 6:
        if w * u <= 1:
            acc[u % 5] = 15 - u
            acc[x % 5] = (12 & u) + (u >> 3)
        u = 4 + 6 - x
    if x - w > 24:
        t2 = acc[w % 5] // 7
        t3 = (5 | u) + 2
        w = t3 & t2 * (w | u)
    t = 0
    while t < 136:
        t4 = acc[x % 5]
        t5 = t4 | acc[w % 5]
        x = t5 % 9973
        t6 = acc[w % 5]
        t7 = t6 << 4
        t8 = t7 - (18 ^ w)
        x = (t8 + t) % 9973
        t9 = 18 + t << 2
        x = (t9 ^ (w | 1) + w) % 1009
        t = t + 1
    return u // 3 % 1009

if __name__ == "__main__":
    arg = 20
    expected = 1001
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
