# Auto-extracted from ds_lt256k_500.jsonl
# record_id=183  entry=f  input='14'  output='0'  tokens=142547

def rec(n, a):
    if n <= 0:
        return a
    t0 = (a * 17 >> 3) - n
    lo = t0 % 4093
    t1 = (9 * lo >> 3 ^ a) & 2047
    return rec(n - 1, t1)

def fn0(d):
    b = [222, 505, 981, 969, 200, 95]
    t = d - 19 - d
    a = 0
    while a < 7:
        d = b[d % 6] // 8 & 255
        t0 = 1 + d - 13
        t = (t0 ^ t) & 65535
        t1 = d >> 4 ^ t * d
        b[d % 6] = t1 % 4093 % 1009
        a = a + 1
    t2 = 2 + 4 + t
    nxt = t2 ^ ((t | 9) ^ d)
    e = 0
    while e < 8:
        t3 = e - 3 - 14
        b[t % 6] = (t3 ^ d) % 1009
        e = e + 1
    for j in range(9):
        d = (j * nxt % 251 | 5) & 1023
        t4 = 14 & j | nxt
        t = t4 & 511
        t5 = b[d % 6] + nxt
        t6 = j & d ^ j
        t = (t6 - (t5 + 18)) % 4093
    return nxt >> 1 & 255

def fn1(e, j):
    j = e + 7
    t0 = (e * j ^ e - 1) & 255
    j = rec(118, t0)
    e = e + e
    t1 = e - 20
    t2 = t1 + (j - e)
    j = t2 >> 1
    return e - j & 255

def f(x):
    z = (5 * x ^ x) >> 2
    t0 = z * x + x & 511
    t1 = z * 9 & 8191
    z = fn1(t0, t1)
    z = fn0((x | 4) & 2047)
    q = 0
    while q < 9:
        cnt = 0
        while cnt < 11:
            z = ((x | 4) - cnt) % 1009
            cnt = cnt + 1
        x = 14 * x % 1009
        for prv in range(9):
            t2 = 10 & z | prv
            z = t2 % 1009
            t3 = x - prv
            t4 = z // 2 * prv
            t5 = t3 + (prv | 4)
            x = t4 - t5 & 1023
            z = (19 + q | z) & 16383
        q = q + 1
    for cur in range(8):
        t6 = z + z
        t7 = t6 * (x + x)
        x = t7 & 16383
    if x // 4 <= 14:
        x = x // 3 << 1
        x = x >> 4 | x
    else:
        z = 3 - x
        if z * x > 47:
            x = z + x
        else:
            z = 9 - x >> 4
    if x * z != 64:
        z = z + 1
    else:
        t8 = 16 << 3 << 2
        x = (t8 >> 4) + x
    t9 = (z | 16) * (z + z)
    p = t9 % 4093
    v = p + p
    c = 0
    while c < 6:
        t10 = x // 7
        t11 = t10 + (x + p)
        v = t11 - c & 4095
        t12 = 9 + c - p
        z = t12 % 1009
        c = c + 1
    t = x * z >> 4 & 4095
    t13 = 11 + (v << 2)
    t14 = (t13 | p) % 17
    t = rec(72, t14)
    t15 = (13 ^ p ^ x) * x
    return t15 & 255

if __name__ == "__main__":
    arg = 14
    expected = 0
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
