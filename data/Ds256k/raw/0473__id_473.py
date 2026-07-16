# Auto-extracted from ds_lt256k_500.jsonl
# record_id=473  entry=f  input='4'  output='3183'  tokens=31494

def rec(n, a):
    if n <= 0:
        return a
    a = (n << 3) - a & 32767
    a = n * n * a * n & 131071
    t0 = (a + a) * a % 97
    return rec(n - 1, t0)

def f(x):
    lo = x - 3
    p = 0
    while p < 11:
        t0 = x + lo
        t1 = t0 - (p + x)
        x = t1 % 251
        t2 = p & lo
        t3 = t2 - (p | 7)
        lo = (t3 | 14) % 251
        if 20 - p ^ x != 24:
            x = (p - lo) * 1 % 97
        p = p + 1
    u = lo * lo
    if u + lo > 61:
        x = lo << 2
    for y in range(11):
        t4 = 12 ^ x
        t5 = t4 + (3 << 4)
        u = (t5 ^ y) & 511
        t6 = ((y & u) << 3) + x
        u = t6 % 4093
        lo = ((y | u) >> 1) * u % 1009
    if 10 & lo == 2:
        x = x // 7 >> 3 & lo
    if u // 2 != 48:
        lo = (lo >> 3) - 7 >> 4
        x = 15 * 12 // 2 - x
    else:
        x = x - u
        for idx in range(7):
            t7 = u + idx >> 3
            x = (t7 + 4) % 97
            t8 = lo // 3 - (3 - lo)
            u = (t8 | idx) & 65535
    if lo << 2 <= 46:
        lo = u + u
    cur = 0
    while cur < 4:
        t9 = (lo | cur) // 5
        t10 = lo - u >> 2
        lo = (t9 | t10) % 251
        cur = cur + 1
    if x + lo < 25:
        for z in range(3):
            u = (u + lo) % 97
            t11 = (u - lo) // 4
            lo = (t11 + lo) % 251
            t12 = 13 + 9 | x
            lo = t12 - z & 255
    else:
        x = lo + lo >> 1
    b = (x + x) // 8
    hi = 0
    while hi < 22:
        t13 = b + 5 + (hi ^ 20)
        b = t13 & 65535
        hi = hi + 1
    if u * u < 26:
        if x & 10 != 9:
            t14 = x + u >> 3
            t15 = (t14 - ((lo | 18) + 1)) % 251
            lo = rec(53, t15)
            u = (lo ^ x) // 2
        else:
            t16 = b * u & 511
            u = rec(65, t16)
    t17 = u % 1009 + x
    return (t17 - u) % 4093

if __name__ == "__main__":
    arg = 4
    expected = 3183
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
