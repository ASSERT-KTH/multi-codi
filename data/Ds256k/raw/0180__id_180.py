# Auto-extracted from ds_lt256k_500.jsonl
# record_id=180  entry=f  input='4'  output='1782'  tokens=104274

def rec(n, a):
    if n <= 0:
        return a
    if a + n == 7:
        t0 = n ^ 12 ^ n & a
        a = t0 % 4093
        for p in range(6):
            a = (n * p | a) & 131071
    t1 = 1 << 3
    t2 = t1 - (a + 15)
    a = t2 % 9973
    t3 = (a - n) % 9973
    return rec(n - 1, t3)

def f(x):
    u = 0
    while u < 7:
        x = (x * u << 3) % 97
        t0 = (u | 4) << 3
        t1 = t0 + u | x
        x = t1 & 2047
        x = (x * x << 1) - u & 255
        u = u + 1
    for buf in range(245):
        x = (buf - 16) * x % 65521
        if buf ^ 1 ^ x != 47:
            x = ((17 & buf) + x) % 9973
    t2 = x // 6 % 97
    x = rec(33, t2)
    lo = x * x % 97
    t3 = 13 - x ^ lo - 19
    t4 = (t3 ^ x) % 9973
    lo = rec(51, t4)
    t5 = x * 16
    t6 = t5 - (17 | x)
    t7 = (x >> 4) // 6
    val = t6 & t7
    t8 = 4 - x
    t9 = t8 * (val >> 2)
    acc = (t9 | val) % 9973
    t10 = (x - 14) % 1009
    acc = rec(87, t10)
    s = 7 - val - 10 | lo
    if val // 7 == 6:
        t11 = s * val >> 1
        s = t11 // 8 & 2047
    t12 = (lo >> 4) % 1009
    x = rec(24, t12)
    return (x | lo) & 2047

if __name__ == "__main__":
    arg = 4
    expected = 1782
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
