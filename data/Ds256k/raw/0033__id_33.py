# Auto-extracted from ds_lt256k_500.jsonl
# record_id=33  entry=f  input='18'  output='110'  tokens=203112

def rec(n, a):
    if n <= 0:
        return a
    t0 = 11 * a >> 2
    t1 = t0 + (a * a >> 1) | n
    p = t1 & 1023
    if a - 14 != 11:
        a = a // 4 & 262143
    else:
        t2 = n & 6 ^ p // 3
        t3 = t2 * (n * p & a)
        a = t3 & 2047
    t4 = (n + 4 << 4) + a
    return rec(n - 1, t4 & 1023)

def f(x):
    for acc in range(6):
        if acc * acc | x == 56:
            t0 = (16 - 17) % 17
            x = (t0 ^ x) & 2047
        x = (x ^ acc) % 97
    tot = (x | 6) - x
    m = x & 5
    t1 = (x >> 2) % 17
    m = rec(75, t1)
    a = tot * tot
    t2 = x ^ 11
    p = t2 - (a ^ 15)
    if x + p != 17:
        x = tot | a | x << 4
    else:
        for e in range(11):
            t3 = a * m ^ e * 3
            tot = t3 * 4 % 9973
        x = p + tot
    if m << 3 == 53:
        t4 = m >> 1 & 32767
        a = rec(87, t4)
    else:
        for u in range(11):
            x = (x ^ p) % 251
    for c in range(7):
        t5 = (c + x) * 1 * x
        x = t5 % 17
        t6 = (9 ^ p) // 4 - m
        m = t6 % 251
        t7 = (17 + a ^ a // 4) + tot
        a = t7 % 251
    for buf in range(18):
        for cnt in range(8):
            a = (tot * m + a) % 97
            t8 = (2 | 5) ^ 4
            t9 = t8 + 17 | a
            m = (t9 | m) % 251
        t10 = (p >> 3) + 4
        p = (t10 ^ m) % 251
    prv = 0
    while prv < 5:
        if x ^ 6 == 50:
            t11 = 4 & m ^ prv
            a = t11 % 17
        for cur in range(12):
            t12 = tot * a * a // 4 | cur
            m = t12 % 251
            t13 = m + 11 ^ cur
            a = t13 & 1023
        prv = prv + 1
    t14 = a & 17 | x & a
    z = 13 | p | p | t14
    res = p + 3
    aux = tot // 4
    t15 = aux % 17 * (p ^ res) ^ x
    a = rec(82, t15 % 17)
    t16 = (res << 1 >> 1) - 3
    return t16 & 262143

if __name__ == "__main__":
    arg = 18
    expected = 110
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
