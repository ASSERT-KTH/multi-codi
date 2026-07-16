# Auto-extracted from ds_lt256k_500.jsonl
# record_id=256  entry=f  input='4'  output='1'  tokens=178634

def f(x):
    for aux in range(10):
        x = aux * x & 8191
        t0 = (x ^ 8) - aux
        x = t0 % 9973
        x = (8 - aux | x) & 1023
    g = x ^ 8
    t1 = (g - x) // 8
    d = t1 * (g >> 3 | x) % 1009
    t2 = x >> 4 ^ g
    idx = t2 * x % 9973
    t3 = 6 & x
    t4 = d ^ g
    t5 = t3 & x + idx
    t6 = t4 + (13 + 12)
    s = t5 ^ t6
    for e in range(12):
        j = 0
        while j < 11:
            d = (d - j) % 4093
            t7 = 20 * j + d
            idx = t7 % 65521
            t8 = s // 2 % 4093
            s = (t8 | s) & 262143
            j = j + 1
        t9 = e * s >> 1
        s = t9 % 1009
    if d + 6 != 35:
        d = 4 ^ s
    res = x * d & d
    lo = d % 9973 >> 1
    for prv in range(10):
        t10 = 8 + prv
        t11 = t10 ^ res - idx
        res = (t11 + idx) % 65521
        if g * lo <= 27:
            lo = g * lo % 9973
        else:
            t12 = (idx ^ lo) - g & x
            s = t12 - prv & 511
    t13 = idx * 20 // 3
    a = t13 % 65521
    if 13 - 8 - d != 48:
        a = s | lo
    for y in range(111):
        a = (y ^ 11) * g % 1009
    if x - s == 8:
        t14 = 3 + 10
        t15 = d ^ 5
        t16 = t14 | res * 1
        t17 = t15 & (g & d)
        res = t16 * t17 & 8191
        if x * res <= 36:
            lo = (x - 17 ^ 20 * lo) + idx
            t18 = idx // 6 >> 1
            d = t18 + ((a | 19) + 3)
        else:
            t19 = g // 3 // 2
            idx = t19 % 4093
            t20 = a % 1009 - x
            s = t20 % 4093
    else:
        t21 = idx & x
        t22 = t21 * (a % 9973)
        t23 = (a + res) // 2
        x = (t22 + t23) % 4093
        for v in range(12):
            t24 = 2 * idx | d
            d = t24 & 65535
            a = (11 + idx ^ v) % 65521
    return lo // 2 % 65521

if __name__ == "__main__":
    arg = 4
    expected = 1
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
