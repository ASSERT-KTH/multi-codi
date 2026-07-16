# Auto-extracted from ds_lt256k_500.jsonl
# record_id=297  entry=f  input='7'  output='101'  tokens=225673

def rec(n, a):
    if n <= 0:
        return a
    for acc in range(8):
        if acc - n - a == 16:
            t0 = (11 ^ n) - n
            t1 = 5 * a % 65521
            a = (t0 ^ t1) % 4093
        else:
            t2 = acc - 9 ^ acc
            t3 = t2 * n - a
            a = t3 % 17
    t4 = (n * n + 14 ^ a) % 65521
    return rec(n - 1, t4)

def fn0(c, g, j):
    for idx in range(12):
        t0 = 12 * g * (c // 6) ^ 14
        j = (t0 | j) & 32767
        if g * idx != 8:
            c = c - j & 255
            g = (g & j) % 97
        else:
            t1 = 11 ^ j
            t2 = t1 & 18 * 9
            c = (t2 ^ c) & 8191
    t3 = (g ^ 18) % 9973
    c = rec(79, t3)
    nxt = ((j ^ g) - g) * j & 1023
    t4 = (g >> 4) // 7 % 97
    nxt = rec(102, t4)
    if j // 8 != 42:
        hi = 0
        while hi < 8:
            t5 = 10 - hi - g
            c = t5 & 32767
            hi = hi + 1
    t6 = (j << 4) - (g | c)
    return (t6 - nxt) % 1009

def fn1(m):
    b = m & 4 & 5 ^ m
    acc = m - 17 - b << 2
    b = (b | acc) + b & 8191
    t0 = m - 15 ^ acc
    m = t0 % 4093
    return b - 19 & 1023

def f(x):
    if x | 10 == 13:
        if 19 ^ x < 17:
            x = x - 6
    if x - 10 > 25:
        t0 = 14 - x - x
        x = t0 - x
        x = x - 12 >> 2
    for acc in range(8):
        t1 = (3 << 2) - x
        x = t1 & 8191
    for t in range(8):
        prv = 0
        while prv < 5:
            x = x % 9973
            prv = prv + 1
        t2 = t << 3 | x
        x = t2 & 65535
        x = (x % 9973 - x) % 1009
    t3 = (18 | x) & 262143
    x = rec(107, t3)
    p = x * 13
    for b in range(60):
        if x % 9973 == 57:
            p = (p + p) % 1009
            t4 = (x ^ b) * 11
            p = t4 + (b ^ 13) * x & 262143
        x = (p + p | p | b) % 1009
        t5 = (p >> 3) + p ^ b
        x = t5 & 65535
    for tmp in range(6):
        t6 = x - 13 - (4 ^ p)
        p = t6 % 1009
    return 10 + p & 262143

if __name__ == "__main__":
    arg = 7
    expected = 101
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
