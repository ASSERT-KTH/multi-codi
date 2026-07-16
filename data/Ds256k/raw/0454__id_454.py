# Auto-extracted from ds_lt256k_500.jsonl
# record_id=454  entry=f  input='20'  output='280'  tokens=126457

def f(x):
    lo = [163, 121, 174, 109, 183]
    if x - 17 > 25:
        t0 = x - 2 ^ (x ^ 6)
        x = (x - 20 & x) - t0
    m = 18 & x & x
    if m + x != 15:
        if x + 13 != 40:
            m = x - lo[m % 5] >> 4
            m = 13 * x
    else:
        t1 = lo[x % 5]
        t2 = (t1 >> 4) * m
        lo[m % 5] = t2 % 251
        x = (11 ^ m) // 8 - x
    if m ^ 12 != 11:
        t3 = m - x
        t4 = t3 * (8 + 3)
        t5 = (10 - m) % 1009
        m = t4 - t5
        m = m * m % 4093
    else:
        x = (m - 5) * 14 - 7
    if lo[m % 5] * m == 19:
        for res in range(5):
            t6 = lo[x % 5] - res
            t7 = lo[res % 5] - x
            t8 = (m | 12) >> 4
            t9 = (t6 | t7) * t8 & 511
            lo[res % 5] = t9 % 251
            t10 = lo[m % 5] & x
            lo[m % 5] = t10 & x
        t11 = lo[x % 5]
        x = t11 + 15
    else:
        t12 = x + 13 - (x + x)
        lo[x % 5] = t12 * x % 1009 % 251
    x = x - 13
    for cnt in range(90):
        for g in range(2):
            lo[x % 5] = (19 + lo[x % 5]) % 251
            t13 = 18 - cnt - cnt ^ cnt | x
            x = t13 % 1009
        t14 = 20 << 1
        t15 = t14 * (1 + 4)
        t16 = t15 >> 4 | m
        x = (t16 ^ x) & 16383
    if m + m <= 5:
        x = (x << 1 >> 3) - x
    t17 = 5 - x
    t18 = t17 - x // 2
    t19 = lo[m % 5]
    return t18 + t19 & 2047

if __name__ == "__main__":
    arg = 20
    expected = 280
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
