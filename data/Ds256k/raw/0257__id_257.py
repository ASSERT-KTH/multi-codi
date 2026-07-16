# Auto-extracted from ds_lt256k_500.jsonl
# record_id=257  entry=f  input='14'  output='1'  tokens=169898

def fn0(a):
    s = (a >> 3) // 2
    res = a + a
    j = 0
    while j < 9:
        for m in range(9):
            t0 = (s ^ res) + 20
            s = t0 % 251
            a = (m - 8) * a & 131071
        t = 0
        while t < 7:
            t1 = 14 * a - res - j
            s = (t1 | s) % 251
            t2 = (16 | res) - (t - j)
            a = t2 % 251
            res = ((res - t) % 1009 ^ s) % 4093
            t = t + 1
        s = s // 7 % 1009
        j = j + 1
    t3 = (8 ^ s) + (s | 10)
    return t3 % 1009

def f(x):
    u = x - 2 + x
    for s in range(251):
        x = ((u & 7) - 1 ^ x) & 2047
        if x + u <= 51:
            t0 = u << 4 ^ x - 4
            x = t0 * ((3 & u) * u) % 1009
            u = (20 % 17 | u) & 2047
        t1 = (11 | x) ^ s
        u = t1 & 131071
    e = 0
    while e < 10:
        x = (16 - u | x) % 9973
        e = e + 1
    if 8 - x == 1:
        x = x % 1009
        u = x - 17
    else:
        for buf in range(11):
            x = ((buf * 12 | x) + x) % 17
        u = fn0((20 << 3) // 3 * u % 9973)
    if 6 | u > 49:
        t2 = (u >> 1) * x // 8
        u = fn0(t2 % 17)
    else:
        for y in range(3):
            u = (y + y ^ u) % 9973
            t3 = x - u >> 3
            x = t3 % 9973
            t4 = y * x
            t5 = t4 + (u - x)
            x = t5 % 9973
        u = fn0((((x & u) >> 3) + u) % 1009)
    if u * x <= 35:
        t6 = (u >> 2) * x
        u = t6 % 17
        x = x - 9
    if u & 8 > 0:
        x = ((3 ^ 7) - x) // 4
    else:
        u = (x - u) // 7
        t7 = u + u ^ u - x
        u = (x * x >> 2 ^ t7) % 17
    t8 = x - 17 - (x - 8) + u
    return t8 % 9973

if __name__ == "__main__":
    arg = 14
    expected = 1
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
