# Auto-extracted from ds_lt256k_500.jsonl
# record_id=388  entry=f  input='13'  output='65488'  tokens=171282

def fn0(b, g):
    prv = g | b
    t0 = g + 5
    t1 = t0 * (g * prv)
    t2 = (b | 6) ^ g
    cur = (t1 - t2) % 1009
    t3 = cur >> 1 >> 1
    v = t3 + (cur // 3 - prv)
    c = b + prv - prv
    s = 0
    while s < 2:
        for a in range(2):
            t4 = c // 8 | prv % 17
            t5 = (11 * prv - cur ^ t4) - a
            b = t5 % 97
        for z in range(11):
            t6 = 18 + g
            t7 = t6 - (cur >> 3)
            v = t7 * v & 65535
        s = s + 1
    t8 = b // 7 + (11 ^ 3)
    v = t8 - (prv - 19 ^ cur)
    return ((cur ^ prv) & g) % 17

def fn1(g):
    d = g + g
    t0 = (2 + d) % 251
    t1 = 15 - 13 | g
    t2 = (t1 | (d - 20) // 8) % 4093
    g = fn0(t0, t2)
    t3 = (g | 4) ^ g * d
    buf = t3 & 4095
    y = (buf + d) // 2
    if d - y < 64:
        t4 = d - 9 ^ 9
        t5 = d | 6 | buf & 3
        y = fn0(t4 & 2047, t5 % 4093)
        buf = buf | 14
    res = g // 5 - d
    return (d >> 4) % 251

def f(x):
    if x | 12 <= 17:
        x = 8 * x - (x ^ 14)
    else:
        x = 5 + x & x & x
    if x // 4 == 64:
        t0 = 14 & x | x ^ 4
        t1 = (t0 + (x & 18)) % 251
        t2 = x + 7 & 16383
        x = fn0(t1, t2)
        x = x // 4 << 1
    else:
        x = (x >> 3) // 7 + x
    e = 0
    while e < 11:
        x = x + x & 32767
        x = x // 3 & 2047
        e = e + 1
    t = 0
    while t < 6:
        z = 0
        while z < 6:
            t3 = z * z - (z - 4)
            x = t3 - (x - 7 << 1) & 131071
            x = 6 & x
            x = x * z % 65521
            z = z + 1
        t4 = (t - 8) * t
        x = (t4 ^ x) % 251
        t = t + 1
    t5 = (x | 17) & 6
    t6 = (t5 - x) % 65521
    t7 = (x ^ 17) + x * x & 16383
    x = fn0(t6, t7)
    for lo in range(8):
        t8 = lo - 13 - x + lo
        x = t8 & 16383
    t9 = (x ^ 13) % 65521
    c = t9 ^ (x ^ 7) // 2
    hi = 0
    while hi < 17:
        t10 = hi - x
        x = t10 & hi + 13
        t11 = x - 8 & x
        x = (t11 + (8 - x) * hi) % 65521
        for g in range(12):
            t12 = (x * x - x) // 3 | g
            c = t12 % 251
            c = (x ^ 3) - c & 511
        hi = hi + 1
    if c * 3 >= 40:
        x = c * x & 8191
        x = (x * x >> 1) % 251
    if x << 4 == 7:
        t13 = (c * c >> 2) // 7
        x = t13 & 131071
    else:
        t14 = c // 5 * c
        x = (t14 ^ c) % 251
        c = fn1((c + 4) % 65521)
    t15 = c ^ 16 | 9 - x
    d = t15 & 4095
    return ((12 << 1) - c) % 65521

if __name__ == "__main__":
    arg = 13
    expected = 65488
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
