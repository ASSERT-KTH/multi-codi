# Auto-extracted from ds_lt256k_500.jsonl
# record_id=414  entry=f  input='15'  output='227'  tokens=212737

def fn0(b, m):
    z = [175, 402, 464, 86, 908]
    lo = (6 - 8) * (m | 20)
    res = 0
    while res < 3:
        t0 = b // 8 ^ lo
        b = t0 & 4095
        res = res + 1
    g = m % 97 & m
    lo = (6 - lo) // 8
    if lo ^ g >= 36:
        t1 = (g ^ m) - 3 << 4 & 2047
        z[b % 5] = t1 % 1009
    t2 = z[b % 5]
    t3 = (g ^ lo) + t2
    b = t3 % 97
    b = 13 ^ 12 | m << 3
    b = m - b
    t4 = z[g % 5]
    t5 = ((g ^ 2) - t4) // 2
    return t5 % 4093

def f(x):
    c = 0
    while c < 12:
        for g in range(8):
            x = ((20 ^ g) - x) % 9973
            x = x + g & 8191
        x = (x * c | x) % 9973
        c = c + 1
    if 10 - x <= 44:
        x = x << 3 | x
        x = x ^ 16 ^ 8
    p = (x ^ 12) * x + x & 8191
    t0 = p & 1
    t1 = t0 - x * x
    t2 = x + p + x
    q = t1 + t2 & 511
    t3 = (8 + 5 << 4 ^ p) % 251
    t4 = x + p
    t5 = t4 | p + 20
    p = fn0(t3, t5 & 8191)
    for idx in range(11):
        if 16 * p >= 64:
            t6 = q % 251 ^ idx
            p = t6 % 251
            t7 = x // 4 - idx
            q = t7 & 16383
        else:
            t8 = x * p + 10
            t9 = t8 << 2 | q
            q = t9 & 8191
            t10 = (11 - p) // 4
            q = t10 - idx & 65535
        b = 0
        while b < 2:
            t11 = (16 ^ q) + x + b
            p = t11 % 9973
            b = b + 1
    for z in range(67):
        for t in range(2):
            t12 = (q - z) // 4
            t13 = (t12 << 3) - x
            x = t13 % 65521
            p = p >> 1 & 8191
        if x << 1 >= 17:
            p = (x & 13) + z & 4095
            t14 = (p ^ 7) - x
            t15 = t14 ^ q * 1 + x
            x = t15 % 9973
    for m in range(8):
        if 12 * m - q == 50:
            t16 = q + q - 3
            t17 = t16 & q | m
            x = t17 & 255
            x = (m * p - q) % 251
        t18 = (7 ^ m) - 15
        x = t18 - p & 2047
    for e in range(5):
        x = (x ^ e) // 5 >> 1 & 2047
    for a in range(5):
        t19 = q // 8 + (p >> 1) + x
        x = t19 % 251
        t20 = (p << 2 >> 4) + a
        q = t20 & 32767
        t21 = (x | 13) >> 1
        q = (t21 + q) % 65521
    t22 = 16 * q & (x | q)
    return (x & q) * p * t22 % 251

if __name__ == "__main__":
    arg = 15
    expected = 227
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
