# Auto-extracted from ds_lt256k_500.jsonl
# record_id=463  entry=f  input='16'  output='208'  tokens=173302

def rec(n, a):
    if n <= 0:
        return a
    c = n & a
    t0 = (c | 6) >> 2 | n
    z = t0 % 1009
    t1 = (z ^ n) << 2 << 4
    t2 = (t1 ^ a) & 511
    return rec(n - 1, t2)

def f(x):
    acc = 0
    while acc < 8:
        if 4 & x != 4:
            t0 = acc + 9 | acc
            x = (t0 ^ (x << 2) + 5) & 8191
        for y in range(10):
            t1 = acc & 8 ^ 11
            x = (t1 + x) % 251
        x = (16 - x) % 17
        acc = acc + 1
    q = 17 | x | 1 - x
    if x - q != 63:
        q = q // 6
    else:
        q = (x >> 4 ^ x * q) >> 4
        t2 = q + q + (x << 4)
        q = t2 | x
    for d in range(6):
        x = (x ^ d) & 255
        q = (x // 7 + (q + x)) % 251
        t3 = x - 4 - x + x
        x = t3 & 1023
    t4 = (x + x) * (x & 15)
    t5 = (t4 ^ x) % 9973
    q = rec(58, t5)
    v = 0
    while v < 11:
        hi = 0
        while hi < 30:
            q = (20 - x | hi) & 2047
            x = (hi + v & v) - x & 1023
            x = x * hi & 255
            hi = hi + 1
        q = (x // 3 << 4) - v & 511
        v = v + 1
    return (x - 13 ^ (q ^ 3)) % 65521

if __name__ == "__main__":
    arg = 16
    expected = 208
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
