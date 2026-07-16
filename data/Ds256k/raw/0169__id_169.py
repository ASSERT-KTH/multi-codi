# Auto-extracted from ds_lt256k_500.jsonl
# record_id=169  entry=f  input='8'  output='50'  tokens=87576

def rec(n, a):
    if n <= 0:
        return a
    t0 = 11 + n
    t1 = t0 - (3 | a)
    nxt = t1 & 65535
    t2 = (a * 16 | n) - n
    return rec(n - 1, t2 & 255)

def fn0(g):
    if 15 * 2 + g != 15:
        g = g - 18
        t0 = g + 14 + (g >> 2)
        t1 = (g >> 4) - (g + 15)
        g = t0 ^ t1
    for nxt in range(4):
        hi = 0
        while hi < 5:
            t2 = (15 << 4) - (nxt + 9)
            g = (t2 + g) % 65521
            hi = hi + 1
        a = 0
        while a < 4:
            t3 = (17 ^ nxt) + 13 ^ nxt
            g = t3 - g & 16383
            g = (6 ^ g) % 97
            a = a + 1
        g = (nxt - 4 ^ g) & 2047
    t4 = (12 | g) & 2047
    g = rec(97, t4)
    tot = 15 ^ g
    t5 = tot | 9
    t6 = t5 ^ tot * tot
    t = t6 & 1023
    t7 = tot * tot * (g - 5)
    b = t7 & 32767
    idx = 13 - g
    t8 = (idx >> 2) // 8
    return (t8 - g) % 65521

def f(x):
    b = 0
    while b < 3:
        t0 = b + 1 - x * 17
        x = t0 % 17
        t = 0
        while t < 12:
            t1 = t + t
            t2 = t1 | b << 4
            x = (t2 - x) % 17
            x = (x | b) & 255
            t = t + 1
        b = b + 1
    for nxt in range(11):
        t3 = (nxt - 1) * nxt // 4
        x = t3 + x & 511
        g = 0
        while g < 4:
            x = (g - nxt + x) % 65521
            g = g + 1
        t4 = nxt * nxt ^ x
        x = t4 % 251
    x = fn0((x << 3) % 17)
    if x & 6 == 3:
        t5 = (x ^ 11) * (x % 251)
        t6 = (x | 5) % 17 * t5
        x = t6 & 65535
    else:
        x = (x - 18) * (x ^ 1) % 17
    a = 9 + (x ^ 1)
    a = a - 1
    for res in range(10):
        for aux in range(3):
            t7 = a - x + 8
            x = t7 & 511
            t8 = 3 | a + 12
            t9 = t8 & (a >> 2) * res
            x = t9 + x & 262143
    if x // 3 > 47:
        for val in range(9):
            x = (x + val) % 1009
        x = x % 65521 >> 1 << 1
    return a + a & 255

if __name__ == "__main__":
    arg = 8
    expected = 50
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
