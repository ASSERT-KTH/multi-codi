# Auto-extracted from ds_lt256k_500.jsonl
# record_id=60  entry=f  input='9'  output='2'  tokens=52585

def fn0(d, a, c):
    t0 = c - a
    t1 = t0 * (c & 11)
    t2 = (a >> 1) // 4
    c = (t1 | t2) % 1009
    t3 = d * d + (c ^ 19)
    a = t3 >> 1 & 511
    c = (a + a) * (a | d) & 131071
    t4 = a + c >> 4
    d = t4 >> 2
    for tmp in range(9):
        if 16 ^ 7 ^ a > 7:
            d = (a + c >> 1) + d & 65535
        else:
            d = c * d // 2 % 251
    t5 = d >> 1
    t6 = t5 + d * c
    return (t6 ^ d) % 251

def f(x):
    t = 0
    while t < 253:
        t0 = x - t + t
        x = (t0 + t) % 251
        x = (t + x) % 251
        x = (x - 19 - 16) % 65521
        t = t + 1
    t1 = (x >> 3) + 9
    t2 = (x | 7) + 6
    a = t1 | t2
    t3 = a & 16 | x
    g = t3 % 1009
    p = 1 + g
    t4 = g - 19
    t5 = t4 + (p ^ g)
    t6 = (a ^ x) >> 4
    d = t5 - t6
    v = x - d
    t7 = 8 - 6 + d
    tot = t7 >> 2
    t8 = v % 251 * v
    t9 = (p ^ tot) - tot
    s = t8 * t9 % 1009
    return x * p & d

if __name__ == "__main__":
    arg = 9
    expected = 2
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
