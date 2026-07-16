# Auto-extracted from ds_lt256k_500.jsonl
# record_id=119  entry=f  input='15'  output='1280'  tokens=225803

def f(x):
    tmp = (6 + x) * x
    for a in range(7):
        t0 = (20 | a) ^ 19 + x
        x = t0 % 97
        w = 0
        while w < 2:
            x = 4 + x & 65535
            x = (w - x) % 97
            w = w + 1
    q = tmp + tmp
    for p in range(9):
        for e in range(11):
            t1 = 11 * e + tmp
            t2 = (q | tmp) // 6
            q = t1 * t2 & 255
            t3 = x * tmp ^ e
            t4 = x * p ^ 20
            q = (t3 | t4) & 4095
            x = (x & e) - tmp & 511
        tmp = (5 & p) - (11 + q) & 511
        if x * tmp > 11:
            t5 = x * p | q - tmp
            t6 = t5 + (tmp + x << 3)
            x = t6 % 65521
            tmp = (2 + p | q) % 65521
    v = (x | tmp) + tmp % 9973
    t7 = v + q
    t8 = t7 + q * v
    j = t8 & 65535
    if x & tmp <= 53:
        lo = 0
        while lo < 9:
            t9 = v - 2 - v + lo
            x = t9 % 97
            t10 = (q << 1) // 2
            t11 = (v + x) // 6
            v = (t10 ^ t11) % 97
            lo = lo + 1
    d = j & q
    acc = tmp - d & tmp
    if j + acc > 36:
        j = acc * x & 2047
        for cur in range(5):
            q = (cur * 5 - 17 ^ v) & 16383
            t12 = v & x | cur
            q = t12 % 97
    res = (16 * v - 2) % 97
    u = q - acc
    if tmp ^ j < 33:
        res = 1 + 2 - q
    for y in range(7):
        tmp = (d >> 1 ^ tmp) & 65535
    for buf in range(10):
        t = 0
        while t < 11:
            v = v // 8 & 131071
            tmp = (v ^ x) - t & 255
            t = t + 1
        d = d // 4 % 65521
    b = (x * q | x) & 16383
    val = 0
    while val < 2:
        for s in range(2):
            t13 = (j & 5) + q
            q = t13 & 1023
            t14 = u - 3 & v - acc
            d = (t14 - s) % 9973
            t15 = (tmp ^ s ^ v * val) + q
            v = t15 % 65521
        for cnt in range(9):
            acc = (acc - res) % 9973
            t16 = tmp + q
            t17 = t16 ^ d - val
            d = t17 % 9973
            u = (u ^ 14) & 18
        val = val + 1
    return 4 * acc & acc

if __name__ == "__main__":
    arg = 15
    expected = 1280
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
