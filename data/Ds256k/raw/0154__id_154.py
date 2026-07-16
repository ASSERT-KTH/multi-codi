# Auto-extracted from ds_lt256k_500.jsonl
# record_id=154  entry=f  input='5'  output='3995'  tokens=161324

def rec(n, a):
    if n <= 0:
        return a
    t0 = n + n
    t1 = t0 + (18 + 2)
    s = (t1 + a) % 97
    t2 = a // 6 % 4093
    return rec(n - 1, t2)

def fn0(c, g, m):
    for b in range(9):
        m = ((b << 1) - g) % 97
        g = b + c & m
    g = m * c % 65521
    c = g - c + m
    for idx in range(2):
        if 12 + m == 22:
            m = (c - m ^ c) % 97
            c = (g >> 1 ^ idx ^ m) & 511
        else:
            t0 = (m ^ idx) + g + g
            g = t0 & 8191
            c = (g << 2 ^ c) % 65521
    t1 = (c + 19) % 97
    c = rec(109, t1)
    c = (3 << 3) + g
    c = 8 - m
    return (m ^ g) % 4093

def f(x):
    hi = 8 * x
    for w in range(594):
        t0 = (hi + hi) * w
        x = t0 // 6 & 2047
    res = 0
    while res < 5:
        hi = (res + 12 | hi) & 511
        res = res + 1
    t1 = 2 & x
    x = t1 - (hi ^ x)
    if x * hi != 43:
        x = 5 ^ x ^ 5
        t2 = (hi ^ 13) & 32767
        t3 = hi % 97 + 14
        t4 = (hi >> 2) - x & 4095
        hi = fn0(t2, t3 & 32767, t4)
    t5 = hi // 3 % 9973
    t6 = hi - x + hi
    t7 = (t6 >> 2) % 4093
    t8 = (x ^ 7) % 9973
    hi = fn0(t5, t7, t8)
    t9 = (hi ^ 18) * 8
    t10 = (t9 >> 1) % 9973
    t11 = 4 - x & 65535
    t12 = hi & 5 | x
    hi = fn0(t10, t11, t12 % 9973)
    if hi & x < 47:
        for b in range(2):
            hi = (hi >> 3) % 9973
    else:
        for cur in range(4):
            t13 = (x & 1 & 18) - cur
            hi = t13 % 9973
            t14 = (7 | 18) ^ hi
            x = (t14 | cur) % 9973
        hi = (x + hi) * 15 & 4095
    t15 = x // 6 // 3
    return (t15 | hi) % 4093

if __name__ == "__main__":
    arg = 5
    expected = 3995
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
