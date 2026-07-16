# Auto-extracted from ds_lt256k_500.jsonl
# record_id=467  entry=f  input='10'  output='5704'  tokens=243560

def rec(n, a):
    if n <= 0:
        return a
    a = (a | n) % 9973
    for b in range(3):
        t0 = (b ^ a) * (20 ^ b)
        a = t0 % 9973
        t1 = (9 * n | n + b) * n
        a = t1 - a & 16383
    t2 = (n << 2 >> 3) + n ^ a
    return rec(n - 1, t2 & 4095)

def fn0(c):
    idx = ((c & 5) + c) // 4
    c = (13 | c) ^ c
    for e in range(3):
        t0 = idx * idx
        t1 = t0 | idx & 2
        c = t1 - c & 262143
        c = 8 & c
    t2 = 4 * 1 | c
    idx = rec(88, t2 & 511)
    return (idx ^ 17) & 4095

def f(x):
    t0 = x * x - x
    idx = t0 + x * x
    t1 = idx - 19 + (x & idx)
    j = t1 * (idx // 3 ^ x)
    t = (idx + j >> 4) * x & 511
    if t - 12 >= 21:
        t = (j + idx) // 6
    t2 = x + 11 - 1
    e = t2 - (x ^ 5)
    if 11 - t > 20:
        e = fn0(13 - 2 - j & 8191)
    else:
        x = fn0((e - idx) * (x | t) & 8191)
        if 14 + x == 14:
            j = idx * 19
            t3 = x - j + (7 + idx)
            t4 = t3 - (11 - x) * (e ^ j)
            e = t4 & 4095
    for z in range(531):
        j = (z + idx) % 97
    t5 = j & e
    t6 = t5 ^ t // 7
    t = rec(102, t6 & 16383)
    hi = x // 5
    for val in range(7):
        t = e * hi + (val + e) & 8191
    t7 = (t ^ hi) + (x | 12)
    return (j * 16 & x) + t7 & 65535

if __name__ == "__main__":
    arg = 10
    expected = 5704
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
