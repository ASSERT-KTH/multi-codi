# Auto-extracted from ds_lt256k_500.jsonl
# record_id=226  entry=f  input='20'  output='16294'  tokens=94838

def rec(n, a):
    if n <= 0:
        return a
    a = (a - 12) % 251
    t0 = (18 ^ n) & n * n
    t1 = t0 + a & 16383
    return rec(n - 1, t1)

def fn0(g, m, d):
    aux = [925, 699, 611, 382, 295, 903]
    tot = 0
    while tot < 2:
        if m | g < 38:
            t0 = d - m - 13
            aux[tot % 6] = (t0 + 12) % 1009
            t1 = d - m
            t2 = t1 * (7 + d)
            aux[d % 6] = t2 % 65521 % 1009
        tot = tot + 1
    t3 = (m - d) * m % 97
    d = rec(113, t3)
    d = g // 4 ^ d
    d = g - 5
    prv = 0
    while prv < 6:
        g = (prv | m) % 9973
        prv = prv + 1
    if d >> 3 <= 25:
        t4 = 19 - m ^ g
        g = t4 - d
        acc = 0
        while acc < 8:
            t5 = 3 - g ^ 3
            aux[d % 6] = t5 % 1009
            t6 = m + d + 18 + acc
            g = t6 & 131071
            acc = acc + 1
    aux[m % 6] = g % 97
    return m * g % 65521

def f(x):
    v = [29, 66, 45, 92, 151]
    nxt = 0
    while nxt < 940:
        x = nxt & x & nxt
        nxt = nxt + 1
    if x * 18 == 26:
        t0 = v[x % 5]
        x = t0 * v[x % 5]
    else:
        for w in range(6):
            t1 = v[x % 5] - x
            t2 = x - v[w % 5]
            t3 = t1 - x - t2 % 17
            x = t3 & 1023
            t4 = (w ^ 9) - w + x
            v[w % 5] = t4 % 251
            t5 = v[x % 5]
            t6 = w & x
            t7 = t6 + (16 - t5)
            v[x % 5] = t7 * w % 251
        t8 = v[x % 5]
        t9 = x & 6
        x = t9 & (t8 & x)
    for g in range(11):
        if (9 ^ 18) - x > 10:
            v[g % 5] = (g - x) % 251
        else:
            t10 = v[g % 5]
            t11 = t10 + v[x % 5]
            x = t11 & x * g
            t12 = g + g | 20
            v[x % 5] = (t12 + x) % 251
        t13 = v[x % 5]
        t14 = (t13 - g) * x
        v[x % 5] = (t14 & 2047) % 251
    z = 7 | 14 | x
    if z // 4 <= 53:
        if 4 * z >= 33:
            z = x * x * 20 % 1009
        t15 = v[z % 5] - z
        z = z - 4 + t15 - 5
    t16 = (z & x) - z * 12
    buf = 20 - 2 + 16 + t16 & 262143
    t17 = buf * z * 15 >> 3
    return t17 & 16383

if __name__ == "__main__":
    arg = 20
    expected = 16294
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
