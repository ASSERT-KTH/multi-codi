# Auto-extracted from ds_lt256k_500.jsonl
# record_id=452  entry=f  input='14'  output='640'  tokens=194106

def fn0(j, a, m):
    w = [32, 59, 65, 59, 33]
    if 15 & m >= 2:
        m = a - m
    t0 = w[a % 5]
    t1 = (a + j) * t0
    a = t1 % 9973
    for p in range(10):
        a = a >> 4 & 65535
    if j | m != 52:
        for lo in range(7):
            t2 = w[lo % 5] << 4
            j = (t2 >> 4) + j & 4095
    val = 0
    while val < 11:
        a = (j + a) % 65521
        val = val + 1
    m = m | 6
    a = j - 11 | j
    if a - 16 != 50:
        m = a & 6
        t3 = w[j % 5]
        t4 = t3 + a >> 2
        a = t4 + 18
    t5 = w[m % 5]
    return (j * 14 ^ t5) & 65535

def f(x):
    t = [105, 233, 141, 222]
    j = x * x
    t0 = (11 | 9) + 10 - 18
    t[j % 4] = (t0 | j) % 251
    t1 = (x ^ 14) & 131071
    t2 = j * x ^ x
    x = fn0(x % 17, t1, t2 & 32767)
    for w in range(7):
        t3 = (2 << 4) - x
        j = (t3 + w) % 1009
        if j ^ 15 < 13:
            t[w % 4] = (8 - w ^ x) % 251
            t4 = j & x
            t5 = t4 & (w & 19)
            j = (t5 ^ x) & 1023
        b = 0
        while b < 27:
            t6 = (2 & 14) - j
            x = (t6 | b) & 1023
            j = (7 << 3) * (j - 7) & 1023
            t7 = j - 2
            t8 = w - j << 3
            t9 = t7 - (j & 8)
            t10 = (t8 | t9) - x
            x = t10 % 1009
            b = b + 1
    t11 = x - 6
    t12 = t11 * (x - j)
    t[x % 4] = t12 % 17
    t13 = (x - 12) * j * j
    t[x % 4] = t13 % 17
    t14 = j * t[j % 4] >> 1
    return t14 % 1009

if __name__ == "__main__":
    arg = 14
    expected = 640
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
