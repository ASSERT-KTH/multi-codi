# Auto-extracted from ds_lt256k_500.jsonl
# record_id=87  entry=f  input='7'  output='13'  tokens=251542

def rec(n, a):
    if n <= 0:
        return a
    t0 = n * 20 | a
    q = t0 % 17
    t1 = (a ^ 16) + q
    t2 = a - 2 & n
    q = t1 + t2 & 131071
    t3 = (2 ^ a) >> 2 | q
    a = t3 % 97
    t4 = a * n % 17
    t5 = t4 ^ q + n + 9
    return rec(n - 1, t5 & 65535)

def fn0(e, g, j):
    tot = [612, 861, 79, 53, 413]
    t0 = tot[j % 5]
    q = (j & t0) // 7
    z = g >> 3
    tmp = (e >> 4) - 13 - e
    t1 = (tot[g % 5] | 20) // 3
    t2 = e + 17 ^ tot[g % 5]
    g = t1 & t2
    if tmp ^ e <= 46:
        t3 = tot[tmp % 5] + e
        t4 = 20 * 17 - t3
        j = t4 & (tmp & 4) - 3
        if j - tmp >= 55:
            t5 = 14 | tot[z % 5]
            q = tmp % 251 * t5
            t6 = tot[z % 5]
            t7 = tot[j % 5]
            t8 = t6 - z
            t9 = t8 | t7 * 10
            g = t9 & q
    else:
        e = j - g
        for a in range(10):
            t10 = (4 << 4) - e ^ j
            j = t10 & 8191
            z = (8 & a | e) & 2047
            tmp = (q + 4 ^ a) & 2047
    aux = 0
    while aux < 4:
        e = (g * 12 ^ e) % 9973
        aux = aux + 1
    q = 20 * g % 251
    return (q >> 1) % 251

def fn1(m, a, b):
    cur = [156, 170, 213, 214, 49]
    v = b - a >> 1
    c = cur[m % 5] + m
    t0 = cur[v % 5]
    t1 = m - b
    t2 = cur[a % 5]
    t3 = cur[c % 5]
    t4 = t2 ^ b
    t5 = t1 + (t0 + b)
    t6 = t4 * (t3 // 6)
    s = (t5 + t6) % 9973
    a = c - cur[v % 5]
    t7 = s // 7 << 2
    t8 = v * c >> 2
    a = t7 + t8 & 1023
    for j in range(4):
        aux = 0
        while aux < 12:
            t9 = 4 & cur[m % 5]
            t10 = (t9 - (c | b)) * m
            cur[b % 5] = t10 % 9973 % 251
            t11 = c * aux & m >> 2 ^ 8
            cur[v % 5] = t11 % 251
            cur[aux % 5] = (15 * aux - v) % 251
            aux = aux + 1
    t12 = 13 << 4 & v
    return (t12 - (v // 8 | m)) % 65521

def f(x):
    j = [819, 908, 583, 206]
    t0 = (x ^ 6) % 17
    t1 = (j[x % 4] ^ 3) >> 2
    t2 = t1 ^ (x << 3 | x % 17)
    t3 = x * x - 19 & 262143
    x = fn0(t0, t2 & 8191, t3)
    t4 = j[x % 4] ^ x
    t5 = x - 14 - t4
    z = t5 & (1 & x) << 1
    if 18 * x <= 57:
        x = z + x + 8 + x
        t6 = z * 16 + (z | x)
        t7 = t6 & (x ^ z) << 1
        j[x % 4] = t7 % 1009
    else:
        x = 18 * z
    t8 = j[z % 4] & z
    prv = t8 - (x >> 2)
    e = z * j[x % 4]
    for cnt in range(25):
        for b in range(10):
            j[cnt % 4] = (e + cnt) % 1009
            z = 16 * z % 251
            t9 = j[cnt % 4]
            t10 = t9 + j[prv % 4]
            j[x % 4] = t10 % 1009
        t11 = cnt * prv & cnt
        x = (t11 - 18) % 251
        prv = (e + z - prv) % 251
    acc = e - 2 - (z - e)
    t12 = 18 + prv
    t13 = t12 * (z - prv)
    t14 = t13 // 7 & 16383
    t15 = (e - 6) % 17
    t16 = e >> 2 & 65535
    e = fn1(t14, t15, t16)
    if x ^ 18 == 6:
        t17 = j[z % 4]
        t18 = e ^ t17
        t19 = t18 + (e | 12)
        z = t19 // 7
    t20 = j[prv % 4]
    j[e % 4] = (9 * acc | t20) % 1009
    return (13 | z) % 251

if __name__ == "__main__":
    arg = 7
    expected = 13
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
