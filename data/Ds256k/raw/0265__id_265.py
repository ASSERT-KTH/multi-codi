# Auto-extracted from ds_lt256k_500.jsonl
# record_id=265  entry=f  input='8'  output='238'  tokens=168725

def rec(n, a):
    if n <= 0:
        return a
    t0 = n + a | a | n >> 2
    cnt = t0 % 4093
    if cnt < 3:
        t1 = a ^ cnt
        t2 = t1 - cnt // 4
        a = t2 % 1009
        t3 = (5 | n) >> 4 | cnt
        cnt = t3 % 1009
    t4 = n + n - a
    return rec(n - 1, t4 & 16383)

def fn0(j, g, a):
    t0 = 12 + j >> 2
    g = t0 + a
    g = a * 15 * g % 4093
    for buf in range(7):
        j = (j - 4) * 16 // 7 % 65521
    j = j + 4
    g = a ^ 19 | 15
    t1 = j ^ a | 9
    return t1 & 4095

def fn1(a, d):
    t0 = a * a
    t1 = t0 * (d - a)
    t2 = (t1 ^ d) & 262143
    t3 = 1 * 15
    t4 = t3 | a ^ 6
    t5 = t4 + a & 2047
    t6 = d + d
    t7 = t6 * (d >> 1)
    d = fn0(t2, t5, t7 % 97)
    if 3 & a == 2:
        t8 = (d + a ^ a) % 65521
        d = rec(85, t8)
        t9 = (a ^ 13) << 1
        d = t9 & a
    t10 = (a << 1) * d
    m = t10 * d & 1023
    res = 0
    while res < 10:
        t11 = d * 20 - 18
        m = t11 - res & 255
        t12 = (20 & 9) - d
        a = t12 - a & 255
        res = res + 1
    for c in range(8):
        a = (a | 8) & 1023
    t13 = m + a & 262143
    t14 = (a ^ m) - d & 65535
    t15 = (a << 4) * a
    m = fn0(t13, t14, t15 % 65521)
    y = 7 + a
    return (d + d ^ d ^ m) & 65535

def f(x):
    t = [708, 923, 584, 46, 652, 125]
    for lo in range(10):
        t[lo % 6] = (lo << 3 << 2) + x
    nxt = 0
    while nxt < 6:
        for q in range(6):
            x = ((nxt ^ 12) + nxt - x) % 9973
            t0 = (nxt & x) + q * x
            t1 = t0 - t[nxt % 6]
            t[q % 6] = t1 % 1009
        nxt = nxt + 1
    for g in range(7):
        for aux in range(29):
            x = (4 ^ g) + x & 2047
            x = (x >> 3) // 5 % 251
        if x >> 4 == 11:
            x = (x | g) & 255
        else:
            t2 = g & 4
            x = t2 & x * x
    t3 = x // 6 >> 4
    t4 = t[x % 6]
    t5 = t4 << 4 ^ 12
    x = fn1(t3 % 9973, t5 & 16)
    for s in range(7):
        for res in range(5):
            t6 = 13 ^ 5
            t7 = t6 & (res ^ 5)
            t8 = t[s % 6]
            t9 = t7 + t8 ^ x
            x = t9 % 9973
            x = 20 - s + x & 1023
            t[x % 6] = 6 * res * x % 251
        x = (x >> 2 | 20) - 6 & 16383
    if t[x % 6] - 19 > 28:
        for a in range(7):
            t10 = x * a + (x ^ a)
            x = t10 & x
            t[a % 6] = (a + x) % 1009
            t11 = x * t[x % 6]
            x = t11 // 6 % 4093
    else:
        x = 5 << 1 ^ x
    t12 = 19 ^ x ^ 1 + 20
    hi = t12 & t[x % 6]
    idx = x >> 4
    for p in range(12):
        t13 = hi >> 2 >> 4
        t[p % 6] = (t13 | idx + hi - 3) % 1009
        tmp = 0
        while tmp < 4:
            t[tmp % 6] = tmp & hi
            tmp = tmp + 1
    if x * x > 31:
        idx = t[hi % 6] ^ x
        v = 0
        while v < 7:
            t[x % 6] = (idx ^ v | 9) % 1009
            v = v + 1
    else:
        if 3 + hi >= 20:
            t14 = t[hi % 6]
            t15 = t[hi % 6]
            t16 = x + t14
            t17 = t[idx % 6]
            t18 = hi & 14
            t19 = t16 & hi - t15
            t20 = t18 & (t17 & hi)
            x = t19 ^ t20
        else:
            t[idx % 6] = (idx ^ 3) * x % 251
            hi = idx >> 1
        for acc in range(5):
            t21 = idx * t[x % 6]
            t22 = t21 - x * t[x % 6]
            idx = t22 % 97
            t23 = t[idx % 6] + 6
            t24 = (5 ^ idx) - acc
            t[idx % 6] = (t24 ^ t23 << 2) % 1009
            t25 = 20 ^ x | x >> 3
            t[idx % 6] = (4 - 6 - 13 - t25) % 1009
    for cnt in range(10):
        t26 = t[idx % 6]
        t27 = t26 * 10 ^ hi
        t28 = cnt - x ^ cnt
        x = t27 * t28 & 131071
    t[idx % 6] = 14 & x ^ 16
    t29 = x % 97 - hi
    return t29 % 251

if __name__ == "__main__":
    arg = 8
    expected = 238
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
