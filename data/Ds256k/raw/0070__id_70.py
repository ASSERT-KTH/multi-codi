# Auto-extracted from ds_lt256k_500.jsonl
# record_id=70  entry=f  input='16'  output='94'  tokens=258419

def rec(n, a):
    if n <= 0:
        return a
    t0 = n - 14
    t1 = t0 | n ^ 1
    b = (t1 ^ a) & 131071
    for u in range(11):
        b = (a + n | b) % 4093
        t2 = (n ^ u) * (b % 4093)
        b = t2 // 4 % 9973
    t3 = ((19 | a) + n - 17) % 97
    return rec(n - 1, t3)

def fn0(e):
    z = [30, 17, 59, 30, 47, 46, 17, 89]
    if e * z[e % 8] >= 46:
        for p in range(7):
            t0 = z[e % 8]
            t1 = 13 & p
            t2 = t1 * (e | t0)
            e = t2 >> 2 & 2047
            t3 = e * 3 ^ e
            e = (t3 << 4) % 251
        if z[e % 8] - 7 == 51:
            t4 = e - 6 >> 3
            t5 = t4 & e - 12 - e
            z[e % 8] = t5 % 97
            e = e * e % 251
    cur = (e // 8 ^ 4 - 8) + e
    t6 = 8 - z[e % 8]
    prv = (t6 ^ e + 1) << 2
    t7 = (z[cur % 8] + 16) % 251
    e = rec(30, t7)
    t8 = 7 - 6 + 7
    cur = t8 ^ prv
    e = e * e // 7 % 251
    w = 0
    while w < 5:
        e = (cur & 8 ^ w) % 251
        w = w + 1
    s = 0
    while s < 6:
        for res in range(9):
            t9 = 13 + res + cur
            cur = t9 & 32767
        v = 0
        while v < 10:
            t10 = cur ^ 16 ^ 3 | v
            prv = t10 & 32767
            v = v + 1
        s = s + 1
    t11 = z[cur % 8] + e
    return t11 % 251

def fn1(d, a):
    tot = 0
    while tot < 2:
        a = (a ^ 10) % 97
        tot = tot + 1
    t0 = d & 14
    t1 = t0 ^ a + d
    t2 = (t1 | d) & 1023
    a = rec(42, t2)
    for idx in range(8):
        if d % 1009 == 11:
            a = (idx ^ d) * (d // 2) % 97
            t3 = (idx - 20 | d << 1) + d
            d = t3 & 131071
        else:
            a = (a & 11) - idx & 1023
            t4 = idx - 7
            t5 = t4 | a >> 3
            a = t5 & d
    w = 0
    while w < 3:
        t6 = 14 - w + w ^ w
        d = (t6 ^ d) % 1009
        w = w + 1
    for tmp in range(11):
        t7 = tmp - 3 - d
        a = t7 % 97
    t8 = a * a
    t9 = t8 - (14 - a)
    return t9 - 9 & 511

def f(x):
    lo = [223, 74, 227, 42, 45, 143]
    if x | 8 == 28:
        for p in range(2):
            t0 = x - 14
            lo[p % 6] = t0 | x + x
    else:
        x = x << 2
        if x << 1 != 60:
            lo[x % 6] = (x >> 4) * x % 251
            lo[x % 6] = x ^ 4
    if x | 1 <= 59:
        for aux in range(4):
            x = (x + x) * x & 262143
            t1 = x | lo[x % 6]
            t2 = t1 + (x + aux) >> 4
            lo[aux % 6] = t2 % 251
    g = (x >> 3) - 13
    for q in range(5):
        cnt = 0
        while cnt < 7:
            t3 = (lo[q % 6] & 12) - x
            lo[q % 6] = (t3 + q) % 251
            t4 = (x & g) * (g & q) - 18
            x = t4 & 16383
            t5 = g * g + cnt
            t6 = 3 + g >> 2
            t7 = (t5 - t6) % 1009
            lo[g % 6] = t7 % 251
            cnt = cnt + 1
    for cur in range(8):
        t8 = g * cur | g >> 4
        x = t8 & 32767
    tot = 0
    while tot < 5:
        t9 = lo[tot % 6]
        t10 = lo[x % 6]
        t11 = x >> 1
        t12 = (5 | t9) * t10
        t13 = t11 + (tot | 11)
        g = t12 * t13 % 1009
        t14 = (g | x) - tot >> 3
        x = t14 & 511
        tot = tot + 1
    if x & 6 == 3:
        for d in range(9):
            t15 = (d | g) // 4
            lo[g % 6] = (t15 >> 3) % 251
            lo[g % 6] = g // 8 * d // 6 % 251
            t16 = lo[g % 6]
            t17 = t16 >> 1 ^ x
            x = t17 & 8191
    else:
        t18 = x * g & 9
        g = t18 + (g + g) // 7
    nxt = 0
    while nxt < 16:
        t19 = x - 11
        t20 = t19 ^ (g ^ nxt)
        g = (t20 + x) % 1009
        g = (nxt << 3 | x) % 1009
        g = (x ^ 20 | nxt) & 65535
        nxt = nxt + 1
    t21 = lo[x % 6]
    t22 = lo[x % 6]
    t23 = (x | t21) ^ t22
    c = t23 - g
    t24 = 6 + g + c
    u = t24 - c
    for z in range(7):
        u = ((c >> 3) % 97 ^ z) & 131071
    for s in range(10):
        u = (x // 2 ^ s) & 16383
    for idx in range(11):
        t25 = lo[c % 6] * x
        t26 = ((20 - x | t25) - 10) % 1009
        lo[x % 6] = t26 % 251
        u = u // 3 % 1009
    t27 = lo[c % 6]
    t28 = t27 * c + g
    m = t28 % 1009
    j = x >> 3
    c = fn0(x // 8 & 131071)
    t29 = (u << 4) - 8
    t30 = t29 * (j % 97 // 3)
    b = t30 % 97
    for buf in range(12):
        if 15 & b < 15:
            lo[m % 6] = (x % 1009 + 16 | 2) % 251
            t31 = u + j ^ 3
            lo[b % 6] = (t31 - ((b >> 3) + j)) % 251
        if 1 + u > 8:
            lo[m % 6] = (3 - g) % 251
            t32 = (20 + x >> 4) + b
            b = t32 % 97
        else:
            lo[x % 6] = (m * buf | 3) % 251
    hi = 0
    while hi < 11:
        if 8 + g <= 37:
            t33 = lo[hi % 6]
            t34 = lo[u % 6]
            t35 = t33 - hi
            t36 = t35 * (x & t34)
            lo[m % 6] = t36 % 251
            t37 = hi ^ 9
            t38 = t37 + (16 << 3)
            j = (t38 | m) % 1009
        hi = hi + 1
    t39 = lo[u % 6]
    t40 = b * j
    t41 = lo[x % 6]
    t42 = x & t41
    t43 = t40 | x - t39
    t44 = t42 & x >> 1
    return (t43 | t44) % 97

if __name__ == "__main__":
    arg = 16
    expected = 94
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
