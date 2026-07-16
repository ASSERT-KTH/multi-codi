# Auto-extracted from ds_lt256k_500.jsonl
# record_id=209  entry=f  input='1'  output='1005'  tokens=216886

def rec(n, a):
    if n <= 0:
        return a
    t0 = n << 3 ^ 4
    g = (t0 + a) % 1009
    t1 = g // 4 | n
    cnt = t1 & 2047
    for e in range(3):
        g = cnt - 9 - g & 131071
    return rec(n - 1, a % 251)

def fn0(m, g):
    t0 = (m % 97 | m) % 9973
    g = rec(47, t0)
    t1 = ((1 << 4) - m) % 97
    g = rec(85, t1)
    b = (g + m) * 7 & 3
    for prv in range(3):
        a = 0
        while a < 2:
            t2 = (b | 19) + (a + prv)
            t3 = t2 * (g - b - (16 & b))
            m = t3 & 131071
            b = (g | b) - (15 + m) & 262143
            a = a + 1
    if b * 13 < 35:
        for t in range(5):
            t4 = t + t ^ (m ^ 7)
            m = (b - g - b + t4) % 4093
            g = ((t & 4) + g ^ t) & 32767
        for aux in range(6):
            t5 = (4 * g ^ aux) * 5
            b = t5 & 2047
    d = 12 - m ^ g
    t6 = (d - 5) // 5 + d
    return t6 & 8191

def fn1(a):
    z = [75, 3, 46, 19, 9]
    t0 = z[a % 5]
    t1 = a - 14
    t2 = t1 - (t0 + 13)
    t = t2 >> 1
    j = 0
    while j < 6:
        t3 = z[t % 5] & t
        t4 = z[t % 5]
        t5 = (t3 >> 1 | t4) + j
        a = t5 & 16383
        j = j + 1
    aux = 4 - t
    m = 0
    while m < 3:
        a = (m ^ aux) >> 4 & 4095
        t6 = 12 + m
        t7 = t6 ^ m + aux
        t = t7 // 2 & 32767
        m = m + 1
    t8 = a + 3
    t9 = aux * aux
    t10 = t8 ^ aux + 3
    t11 = t9 + 14 * 7
    t12 = (t10 | t11) & 131071
    z[aux % 5] = t12 % 97
    t = a - t - aux
    if 2 - 5 | a < 61:
        aux = a & t
    else:
        t = t + aux
    t = t - a
    t13 = (aux & 15) + z[a % 5]
    return (t13 - z[t % 5]) % 17

def f(x):
    d = x * x
    z = x - 15
    for s in range(1082):
        d = (d | z) % 1009
        d = (z + d) % 4093
    t = x - 20
    res = (16 ^ 20) + t
    idx = x + x
    t0 = 18 + 2
    t1 = t0 + (x + 7)
    t2 = (t1 - 17) % 1009
    x = fn0(res & idx, t2)
    return 20 + d & 4095

if __name__ == "__main__":
    arg = 1
    expected = 1005
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
