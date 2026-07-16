# Auto-extracted from ds_lt256k_500.jsonl
# record_id=438  entry=f  input='17'  output='32'  tokens=15519

def rec(n, a):
    if n <= 0:
        return a
    t0 = n * n // 5 ^ a
    g = t0 % 1009
    if 20 - n | g >= 29:
        d = 0
        while d < 9:
            t1 = (d | g) + 17
            g = t1 & 511
            t2 = n - a - d
            g = t2 & 16383
            t3 = (d ^ 19) - d | a
            a = t3 % 17
            d = d + 1
        for p in range(8):
            g = g << 3 & 32767
            t4 = 14 << 1 & p
            t5 = t4 - p + g
            a = t5 % 17
    else:
        t6 = n * 18 - g
        a = t6 % 1009
    t7 = (5 & 18) - (8 ^ g)
    t8 = t7 ^ (a | g) >> 2
    return rec(n - 1, t8 % 17)

def fn0(d, j, g):
    t0 = (9 + j) % 65521
    j = rec(55, t0)
    if g * g == 3:
        j = (j - d) % 9973
    else:
        t1 = j * 2
        t2 = t1 ^ 9 & g
        t3 = t2 + j & 255
        j = rec(36, t3)
    t4 = g * g | d << 3
    tot = (t4 + d) % 9973
    s = 0
    while s < 6:
        g = (g ^ 16) % 65521
        if s - tot > 3:
            tot = (20 + j ^ tot) % 65521
            t5 = tot + j ^ s
            g = t5 & 131071
        else:
            j = ((g ^ 11) + s) % 9973
        s = s + 1
    t6 = d + tot + d << 4
    hi = t6 % 97
    t7 = (d | 5) * (j - 11)
    nxt = t7 % 9973
    for res in range(2):
        for b in range(9):
            g = (res * res | nxt | b) & 16383
            t8 = (tot << 1) + res + nxt
            nxt = t8 % 9973
        t9 = d + nxt - res
        j = t9 % 9973
    t10 = d + j + (nxt + g) & 4095
    g = rec(71, t10)
    return (hi - 18) % 97

def f(x):
    if 17 ^ x > 25:
        x = x ^ 15
        for tot in range(2):
            x = (x - 1) % 251
            x = (x ^ tot) & 1023
            t0 = (tot * 5 & (13 ^ x)) + 7
            x = t0 % 65521
    res = 0
    while res < 40:
        t1 = ((res | 19) - (x >> 1)) * x
        x = t1 & 4095
        res = res + 1
    for cur in range(3):
        x = ((x << 1) + 12) % 251
        z = 0
        while z < 4:
            t2 = z + (19 ^ z)
            t3 = t2 * (z - 6 + 14)
            x = (t3 + x) % 251
            z = z + 1
    t = 0
    while t < 4:
        x = (t * t - x) % 251
        for y in range(5):
            x = (y + x << 3) % 251
            x = x * x % 65521
        t = t + 1
    hi = 4 | x
    return 7 * 11 - hi & 255

if __name__ == "__main__":
    arg = 17
    expected = 32
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
