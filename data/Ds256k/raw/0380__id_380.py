# Auto-extracted from ds_lt256k_500.jsonl
# record_id=380  entry=f  input='14'  output='1386'  tokens=220857

def rec(n, a):
    if n <= 0:
        return a
    t = (20 & n ^ a + a) & 1023
    t = (t | n) % 65521
    a = (a & n ^ 1) & 4095
    t0 = a // 2 + (t << 4)
    t1 = (t0 + (t | 14) * a) % 4093
    return rec(n - 1, t1)

def fn0(e, d):
    t0 = e // 8
    b = t0 | d - 4
    t1 = (e | b) * d & e
    b = rec(48, t1)
    cur = d ^ e | 13
    q = 0
    while q < 6:
        d = (d ^ q) & 262143
        t2 = (b ^ 18) // 7 ^ 19
        d = (t2 | q) % 1009
        q = q + 1
    acc = 8 - d
    for v in range(7):
        res = 0
        while res < 11:
            t3 = (v & cur) * 4
            t4 = cur + e + cur
            cur = (t3 | t4) % 1009
            acc = (b - 9 + v ^ acc) & 2047
            res = res + 1
        t5 = (b << 2) * (10 | cur)
        b = t5 & 1023
        b = (14 ^ cur | b) & 262143
    t6 = d - e
    t7 = 6 << 4 & e
    t8 = t6 - (b + b)
    s = t7 + t8
    t9 = (e + acc) * (d | e)
    s = rec(81, t9 % 1009)
    return (acc * b ^ 9) % 4093

def f(x):
    c = [494, 6, 969, 360, 549]
    p = x
    hi = 7 | x
    t0 = (hi & 19) * (x + p)
    t1 = t0 ^ (hi ^ p) << 3
    c[hi % 5] = t1 % 1009
    if x * p != 33:
        t2 = c[x % 5]
        p = (p + p) * t2
    else:
        t3 = 20 + p >> 2
        t4 = 9 * hi ^ x
        x = t3 - t4
    t5 = hi | x
    t6 = t5 - x * p
    z = t6 & 32767
    c[x % 5] = ((hi & 11) + z << 2) % 1009
    t7 = z | 4
    cur = t7 - z % 4093
    lo = 0
    while lo < 2:
        t8 = c[cur % 5] + 1 + cur
        cur = (t8 - (8 * 4 + 15)) % 17
        hi = (hi | 4) % 4093
        t9 = hi - 20 + lo
        x = t9 & 2047
        lo = lo + 1
    t10 = 5 * 4 - p & 16383
    t11 = (p ^ 16) + 4 - hi
    z = fn0(t10, t11 % 17)
    t = 0
    while t < 7:
        c[x % 5] = (t - 16 - 12 + z) % 1009
        cur = cur - x & 4095
        t = t + 1
    for acc in range(6):
        t12 = (cur + p) % 4093
        hi = (t12 ^ hi) % 9973
    d = z + x >> 4
    for b in range(5):
        if z ^ cur >= 55:
            x = (20 - x) % 17
        else:
            c[p % 5] = (z >> 4) % 1009
        if z - 16 == 50:
            t13 = 5 - hi & d
            t14 = t13 * c[p % 5]
            c[cur % 5] = t14 % 9973 % 1009
        t15 = (b + 9 ^ 15) + hi
        x = t15 % 17
    t16 = p * 12 ^ z * hi
    val = t16 % 17
    for aux in range(4):
        for tmp in range(5):
            c[p % 5] = x & aux
            t17 = c[x % 5] + val >> 1
            c[val % 5] = t17 * d % 4093 % 1009
            x = (p + 12 ^ tmp) % 9973
    for j in range(169):
        t18 = 4 - 5 - d ^ hi
        hi = t18 & 255
    v = c[z % 5] + 6
    u = x ^ d
    if p * val <= 61:
        if z | cur == 5:
            hi = (18 ^ 19) - cur
            u = z * v % 4093
        else:
            c[u % 5] = (x - u) % 1009
            x = 5 * 6 | x
    return (x | v) % 4093

if __name__ == "__main__":
    arg = 14
    expected = 1386
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
