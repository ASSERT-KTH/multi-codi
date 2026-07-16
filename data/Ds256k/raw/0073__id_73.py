# Auto-extracted from ds_lt256k_500.jsonl
# record_id=73  entry=f  input='9'  output='0'  tokens=138661

def rec(n, a):
    if n <= 0:
        return a
    t0 = (a >> 2) + n
    t = t0 % 17
    t1 = ((t | n) - a) % 1009
    return rec(n - 1, t1)

def f(x):
    t0 = (x | 20) % 17
    x = rec(47, t0)
    t1 = 13 * x - x
    p = t1 & (x | 7) - x
    res = 1 - p
    t2 = x % 17 * p
    t3 = t2 + res & 255
    res = rec(28, t3)
    t4 = (p | 5) // 7
    e = t4 * x & 511
    idx = 0
    while idx < 12:
        t5 = (x & e & res >> 2) >> 4
        x = t5 & 131071
        for u in range(4):
            t6 = u * x << 1
            res = (t6 ^ res) % 97
        t7 = res * idx + e
        res = t7 % 17
        idx = idx + 1
    t8 = (e << 3) * p * e & 131071
    p = rec(27, t8)
    s = (5 << 2 << 4) + p
    t9 = p * e + p % 251 + 4
    hi = t9 % 251
    g = 0
    while g < 9:
        t10 = 6 - e >> 3
        hi = (t10 ^ hi) % 17
        t11 = 1 * p * 14
        p = t11 & 255
        for tot in range(12):
            t12 = g + p << 3
            hi = (t12 + (hi * 5 ^ hi)) % 251
            t13 = g * (hi - tot) * hi
            p = t13 & 131071
        g = g + 1
    cnt = e - res ^ 7
    return (x * 10 & 17 ^ e) % 17

if __name__ == "__main__":
    arg = 9
    expected = 0
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
