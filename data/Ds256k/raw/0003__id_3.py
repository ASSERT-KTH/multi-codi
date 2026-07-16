# Auto-extracted from ds_lt256k_500.jsonl
# record_id=3  entry=f  input='4'  output='9'  tokens=114304

def rec(n, a):
    if n <= 0:
        return a
    if a >> 1 <= 38:
        a = (a << 4) * (a * 11) & 262143
    else:
        idx = 0
        while idx < 10:
            a = (idx * 20 | a) % 1009
            a = a - idx & 65535
            t0 = (idx - 15) * n
            t1 = a >> 4 >> 2
            a = t0 + t1 & 255
            idx = idx + 1
        a = (n ^ 5 ^ a) % 1009
    res = n - a & 255
    t2 = (res - a) * 8
    return rec(n - 1, t2 % 65521)

def f(x):
    w = [81, 33, 42, 17, 44, 12, 78]
    w[x % 7] = (x & 12) + x
    m = 0
    while m < 12:
        for hi in range(7):
            t0 = 5 - x
            t1 = t0 ^ 11 + x
            x = t1 % 65521
            t2 = w[x % 7] + 6 - m
            x = t2 % 4093
            t3 = (hi ^ 8) & hi
            t4 = (x - 16) // 7
            x = (t3 + t4) % 65521
        t5 = w[x % 7]
        t6 = 13 + t5 >> 1
        t7 = (x ^ 6) & x
        x = t6 & t7
        m = m + 1
    p = 0
    while p < 6:
        g = 0
        while g < 6:
            t8 = g << 2 | (6 | g)
            w[x % 7] = ((t8 | 7) + x) % 97
            x = (p + x + p) % 65521
            t9 = x ^ 2 ^ (p ^ g)
            x = t9 & 65535
            g = g + 1
        p = p + 1
    for aux in range(4):
        x = (aux + x | x * 11) % 17
        t10 = (10 ^ 7) * (x % 17)
        w[aux % 7] = t10 & 16
    t11 = (x >> 4 & x >> 1) % 4093
    w[x % 7] = t11 % 97
    tot = 0
    while tot < 12:
        x = x + tot & 2047
        t12 = w[x % 7]
        t13 = w[tot % 7]
        x = t12 & t13 & tot
        tot = tot + 1
    t14 = w[x % 7]
    idx = (x ^ 1) + t14
    return (x & idx ^ 9) & 511

if __name__ == "__main__":
    arg = 4
    expected = 9
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
