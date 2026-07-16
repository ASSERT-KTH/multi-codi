# Auto-extracted from ds_lt256k_500.jsonl
# record_id=193  entry=f  input='13'  output='0'  tokens=255534

def rec(n, a):
    if n <= 0:
        return a
    d = (n & 5 ^ a) % 97
    t0 = (12 + n << 2) + n
    z = (t0 | a) & 511
    t1 = a >> 2 & 255
    return rec(n - 1, t1)

def f(x):
    for nxt in range(12):
        y = 0
        while y < 3:
            x = 7 * x >> 2 & 32767
            t0 = (8 | y) + (y + nxt)
            x = (t0 & 1 ^ x) % 251
            x = (y - x - x) % 97
            y = y + 1
    v = 0
    while v < 10:
        for m in range(5):
            x = 6 * x & 65535
            x = (m - v ^ x) - x & 262143
        if v - 3 + x >= 51:
            t1 = (x >> 2) * x | x
            x = t1 % 251
        if (v ^ 7) + x >= 60:
            t2 = x // 8 * 12
            x = (t2 - v) % 251
            t3 = (1 ^ x) >> 2
            t4 = t3 ^ v + v - v
            x = t4 & 511
        else:
            t5 = x * 7 % 9973 << 3
            x = t5 & 65535
            t6 = 6 + v
            t7 = t6 + (x + x)
            x = t7 & 131071
        v = v + 1
    t8 = ((x | 19) + x) % 97
    x = rec(91, t8)
    t9 = (x * x | x) & 9
    x = rec(94, t9)
    for s in range(3):
        x = (x >> 4) * s % 9973
    t10 = x * x * x
    t11 = (t10 - x) % 97
    x = rec(47, t11)
    e = 19 - 2 - 7 + x
    aux = x | 2
    for u in range(6):
        for cur in range(12):
            t12 = e + 3 | x
            x = t12 & 1023
            t13 = cur * e - x
            t14 = t13 + (x ^ 4) * e
            aux = t14 & 16383
            e = (cur & u) - x & 4095
        x = u - 9 - e & 262143
    t15 = x - 12 - aux * x
    aux = rec(29, t15 % 251)
    lo = 0
    while lo < 20:
        aux = (9 * x + aux) % 97
        if e | lo < 14:
            aux = lo + lo + aux & 65535
            x = aux * lo & 8191
        else:
            e = e - lo & 1023
            e = aux + lo - 16 & 16383
        e = (7 - aux ^ lo) & 2047
        lo = lo + 1
    q = (18 * 4 >> 3) - aux
    z = q - 3
    t16 = ((12 ^ 1) - z * e) % 251
    z = rec(79, t16)
    t17 = (q + x) // 6
    q = rec(83, t17 % 9973)
    j = z ^ x ^ x // 2
    g = (13 & x) - q - j
    t18 = z & 10 & x - 3 ^ z
    return t18 % 9973

if __name__ == "__main__":
    arg = 13
    expected = 0
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
