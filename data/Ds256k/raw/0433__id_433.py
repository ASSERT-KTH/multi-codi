# Auto-extracted from ds_lt256k_500.jsonl
# record_id=433  entry=f  input='3'  output='61'  tokens=176900

def f(x):
    t = [153, 128, 225, 73, 193, 117, 160]
    t0 = 9 - 12 & (x | 12)
    t[x % 7] = t0 - x
    y = x * x >> 2
    aux = 7 * y >> 3
    d = y & 5
    t1 = 9 - d & (2 & d)
    c = t1 & x - 16 - (x + aux)
    t2 = c * x
    p = t2 - aux // 3
    t3 = 12 - p ^ 1
    nxt = t3 + t[y % 7]
    if aux & x > 6:
        m = 0
        while m < 9:
            d = (x * 8 ^ d) % 97
            t[m % 7] = y * 1
            m = m + 1
        p = 14 ^ 17 ^ y
    else:
        t4 = t[aux % 7]
        t5 = aux << 2
        y = t5 + t4 * p
    if t[p % 7] + 3 < 6:
        for acc in range(5):
            t6 = t[d % 7]
            t[x % 7] = (c - t6) % 251
            t7 = t[d % 7]
            t[y % 7] = (nxt + d - t7) % 251
            t8 = (x - 17) * d
            t9 = t8 & t[nxt % 7]
            aux = (t9 ^ aux) % 97
        for tot in range(9):
            t[c % 7] = (d * d >> 4) % 251
            t10 = t[x % 7]
            t11 = t[tot % 7]
            t12 = (t10 + t11) // 4
            t13 = t[tot % 7]
            nxt = t12 & t13
            t14 = tot - 5
            t15 = t14 ^ y * y
            p = t15 % 1009
    else:
        nxt = (d - y) % 251
    hi = 8 << 1 | nxt
    for cur in range(187):
        if y | aux <= 28:
            t16 = (x ^ d) // 2
            t[d % 7] = (t16 + y) % 251
            aux = (hi * hi | aux) & 32767
        t17 = t[c % 7]
        t18 = t17 << 4 << 1
        t19 = (t18 >> 4) + hi
        hi = t19 & 262143
        d = (d >> 1) % 1009
    t[aux % 7] = ((9 | d) - (14 ^ p)) % 251
    t20 = t[x % 7]
    t21 = 17 | y
    t22 = t21 + (t20 - hi)
    j = t22 + hi
    res = 16 - j
    buf = d // 8 >> 4
    t23 = t[c % 7] >> 4
    return ((t23 | nxt) >> 2) % 97

if __name__ == "__main__":
    arg = 3
    expected = 61
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
