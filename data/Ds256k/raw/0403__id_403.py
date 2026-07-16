# Auto-extracted from ds_lt256k_500.jsonl
# record_id=403  entry=f  input='11'  output='899'  tokens=104210

def fn0(g, m):
    t0 = g % 4093
    t1 = t0 - (19 ^ g)
    tmp = t1 + 3
    for j in range(12):
        prv = 0
        while prv < 4:
            g = (prv + tmp) // 7 % 9973
            prv = prv + 1
        acc = 0
        while acc < 3:
            tmp = ((j + g) * m | tmp) & 8191
            t2 = (j - m | m ^ g) // 2
            m = t2 & 1023
            g = (acc * m ^ j) & 131071
            acc = acc + 1
    q = tmp & 5
    if 11 ^ m >= 46:
        tmp = m + tmp
        t3 = g - 18
        t4 = t3 ^ (5 | m)
        tmp = t4 // 5
    else:
        g = ((q | g) ^ g << 3) % 4093
    for z in range(3):
        m = ((q & 16) + m) % 65521
        m = ((g | q) + m) % 9973
    buf = tmp | q
    return g + 19 + buf & 4095

def f(x):
    for m in range(48):
        if (m & 17) + x == 27:
            x = (x ^ 2) - m & 1023
        else:
            t0 = m - 10 ^ x
            x = t0 & 511
            t1 = ((17 & m) + m) * 5
            x = (t1 | x) % 1009
        x = x * m * x + m & 16383
        x = (m + 20 ^ x + 18) & 16383
    if x * x == 11:
        for v in range(12):
            x = ((2 & 1) + x) % 65521
        t2 = (2 << 3) + x
        t3 = ((x & 9) << 1 ^ 12) & 255
        x = fn0(t2 % 65521, t3)
    else:
        if x | 13 > 28:
            t4 = x % 65521 - (7 - x)
            t5 = (t4 ^ x) & 262143
            t6 = (x ^ 6) % 1009
            x = fn0(t5, t6)
            x = 15 + x + 17 - x
    t7 = (x - 12 ^ x) & 65535
    t8 = (x ^ 4) & 4095
    x = fn0(t7, t8)
    z = x - 7 ^ x
    t9 = z * x + x
    t10 = t9 * (x - 14 << 2)
    t11 = 6 & 10 ^ x
    x = fn0(t10 % 65521, t11 & 16383)
    t12 = 5 * z + z
    s = t12 % 1009
    return (s ^ z) * z & 2047

if __name__ == "__main__":
    arg = 11
    expected = 899
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
