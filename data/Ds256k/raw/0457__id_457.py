# Auto-extracted from ds_lt256k_500.jsonl
# record_id=457  entry=f  input='14'  output='0'  tokens=132787

def rec(n, a):
    if n <= 0:
        return a
    a = (n | a) % 65521
    hi = 0
    while hi < 3:
        a = (hi & 9 | a) & 262143
        hi = hi + 1
    t0 = (n ^ 12) - 8 - a
    return rec(n - 1, t0 % 17)

def f(x):
    t0 = (5 ^ x) * x & 2047
    x = rec(78, t0)
    t1 = ((x - 1 | 5) ^ x) % 65521
    x = rec(82, t1)
    g = x * x & 8191
    s = x ^ g ^ x
    t2 = s ^ x
    t3 = t2 - (g + g)
    e = t3 * x % 65521
    for z in range(10):
        w = 0
        while w < 7:
            t4 = g * w + 1 + 16
            e = t4 & 16383
            e = (x & w) - z & 1023
            w = w + 1
        e = z * x & 4095
    if g - e >= 27:
        for res in range(7):
            t5 = g * e & e
            s = (t5 ^ s) % 9973
            s = g // 4 - (7 - s) & 1023
            t6 = (g << 2) * s
            t7 = t6 + (s >> 2) % 9973 - e
            e = t7 % 65521
        x = s & 17
    for b in range(8):
        g = (b - e - b) % 4093
        e = (g & e) // 4 % 9973
        g = (e << 1 | b) & 511
    for acc in range(12):
        for lo in range(4):
            t8 = (acc + 18 << 2) * acc | e
            x = (t8 ^ lo) & 8191
        t9 = 20 ^ x
        t10 = t9 ^ 13 * acc
        s = t10 & 16383
    t11 = x * s + 5
    u = t11 % 17
    return 18 * e * (x ^ 10) % 9973

if __name__ == "__main__":
    arg = 14
    expected = 0
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
