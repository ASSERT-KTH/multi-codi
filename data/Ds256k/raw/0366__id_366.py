# Auto-extracted from ds_lt256k_500.jsonl
# record_id=366  entry=f  input='10'  output='331'  tokens=19242

def fn0(m, j):
    c = [49, 1, 10, 77, 39, 27, 33, 67]
    if j ^ m > 19:
        t0 = j * j & m
        j = t0 + m
        for q in range(10):
            t1 = (m | q) // 5 >> 2
            c[q % 8] = t1 % 97
            t2 = c[m % 8] | 5
            m = t2 % 1009
    hi = (j + j) * 18 & 16383
    a = 0
    while a < 5:
        m = ((1 * 5 ^ j) - m) % 4093
        a = a + 1
    if j - m > 46:
        if 15 & j == 10:
            t3 = 6 - hi ^ m
            t4 = 16 * hi + 16
            m = t3 * t4 % 17
            m = hi ^ j ^ j
    else:
        t5 = hi + j << 2
        j = t5 * 4 % 97
    prv = j * 3
    tot = j & prv
    t6 = m - prv >> 2
    return t6 + m & 8191

def f(x):
    j = [218, 163, 91, 20, 221, 216, 171]
    for a in range(18):
        if a - x == 15:
            t0 = a << 3 | x
            x = t0 % 65521
        else:
            t1 = 3 - j[a % 7] << 4
            x = (t1 ^ x) % 97
    for cur in range(9):
        t2 = cur ^ 16
        t3 = t2 & cur + cur
        t4 = t3 & cur | x
        x = t4 & 16383
        x = x // 4 % 65521
        for q in range(2):
            t5 = q + cur
            t6 = t5 & x + 2
            x = (t6 | 16) % 97
    if 14 & x < 9:
        t7 = 5 + j[x % 7]
        t8 = (x + x | t7) << 3
        x = t8 & 4095
    d = x + x
    t9 = 6 - d - d
    t10 = 15 ^ x | 19 & x
    x = fn0(t9 & 16383, t10 & 32767)
    t11 = x + 14 ^ d
    return t11 & 511

if __name__ == "__main__":
    arg = 10
    expected = 331
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
