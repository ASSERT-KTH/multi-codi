# Auto-extracted from ds_lt256k_500.jsonl
# record_id=141  entry=f  input='10'  output='150'  tokens=182695

def rec(n, a):
    if n <= 0:
        return a
    if a // 7 >= 62:
        a = (a - n) % 251
        a = ((n >> 3) - a) % 251
    else:
        t0 = 6 * a + a // 7
        a = t0 % 251
    t1 = n * a + (n - a)
    return rec(n - 1, t1 & 8191)

def fn0(e, m):
    j = [55, 95, 39, 14, 5]
    e = m ^ e
    t0 = 17 | e | 15
    e = t0 - j[e % 5]
    m = j[m % 5] & m
    if 13 & m <= 13:
        for aux in range(11):
            t1 = (e | 6) + 2
            j[aux % 5] = (t1 << 2) % 97
            t2 = aux + aux + m
            j[m % 5] = t2 % 97
            t3 = (aux - 18) * (14 + m) >> 4
            e = t3 % 17
    else:
        for hi in range(9):
            e = e % 9973 + e & 131071
            j[m % 5] = ((m + 1) // 5 ^ 16) % 97
            m = m % 9973
        if e ^ m == 45:
            t4 = e >> 3 & 262143
            e = rec(89, t4)
        else:
            t5 = (m ^ e) & e
            m = t5 + e
    return (e - 9) % 9973

def f(x):
    if x ^ 3 != 26:
        t0 = (x & 6) * x
        x = t0 - x
        for p in range(9):
            t1 = 13 * p >> 1
            x = (t1 + x) % 65521
    else:
        x = x - 16 + (x - 5) + x
    m = 11 - x
    t2 = m * x
    t3 = t2 | (14 | m)
    t4 = (m ^ 2) % 251
    m = fn0(t3 % 65521, t4)
    s = 0
    while s < 6:
        for v in range(3):
            t5 = s - 8 ^ x
            x = t5 & 131071
        s = s + 1
    acc = 0
    while acc < 11:
        t6 = (18 ^ 11) + m
        m = t6 & 255
        t7 = acc - 18 + 10
        t8 = t7 - (x | 17) // 4
        x = t8 & 65535
        acc = acc + 1
    u = x + x
    t9 = (12 ^ u) - u & 1023
    m = rec(119, t9)
    cur = 0
    while cur < 8:
        for y in range(10):
            t10 = (x << 3) - m
            m = t10 % 251
            t11 = (y ^ 8) * u * y
            x = t11 % 4093
            t12 = 7 - cur ^ 11 * 4
            u = (t12 ^ x | y) % 65521
        for tmp in range(11):
            t13 = (x ^ tmp) * x + u
            x = t13 % 251
        m = (cur - 18 - u) % 251
        cur = cur + 1
    prv = x - 9 << 2
    return ((prv | 2) + m) // 6 & 131071

if __name__ == "__main__":
    arg = 10
    expected = 150
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
