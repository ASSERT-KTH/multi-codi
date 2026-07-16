# Auto-extracted from ds_lt256k_500.jsonl
# record_id=442  entry=f  input='10'  output='32736'  tokens=114204

def f(x):
    idx = 0
    while idx < 4:
        for nxt in range(12):
            x = (idx ^ x ^ nxt * idx) % 65521
            t0 = (17 << 3) - nxt * 13 | 6
            x = (t0 ^ x) % 1009
            t1 = x - 1
            t2 = t1 + (idx + idx)
            x = t2 % 65521
        t3 = idx & 14
        t4 = t3 & idx * x
        t5 = 15 + x - idx
        x = (t4 ^ t5) % 65521
        idx = idx + 1
    t6 = x * x // 8
    z = (t6 ^ x) % 65521
    tmp = x + z << 2 ^ 4
    if x << 2 != 45:
        a = 0
        while a < 12:
            tmp = (x ^ tmp) % 65521
            a = a + 1
    s = 0
    while s < 12:
        z = (s & 19 ^ x) & 65535
        z = (z ^ 1) % 1009
        s = s + 1
    if tmp + z > 12:
        t7 = 12 * 6 * x
        z = t7 % 1009
    d = (tmp >> 1) * tmp & 131071
    t8 = (z | 9) << 4
    e = (t8 - z) % 1009
    cur = 14 - 17 - (6 - x)
    hi = (cur + 4) % 65521
    buf = (17 + hi) * z % 65521
    if d + buf > 35:
        cur = e * x & 511
        t9 = (d ^ 20) * 19
        d = t9 + z % 65521 * x & 16383
    b = 0
    while b < 12:
        for lo in range(3):
            t10 = ((d & z) >> 1) // 4
            cur = t10 + cur & 2047
            tmp = ((cur * x | x) - tmp) % 65521
            t11 = (lo + b) * e
            cur = t11 % 65521
        b = b + 1
    w = hi * d & x
    for c in range(8):
        t12 = (buf & tmp) * d
        w = t12 - c & 511
        if 4 ^ cur != 20:
            hi = (c + z - 14) * cur & 4095
            t13 = (hi + 10 << 2) - z + cur
            cur = t13 & 4095
        else:
            buf = (d - buf << 1 >> 3) % 65521
            t14 = d & z & tmp >> 1
            x = (t14 ^ x) & 511
        t15 = z - 12 | w
        w = t15 % 65521
    if e - x != 33:
        y = 0
        while y < 7:
            t16 = (w >> 4) * (14 - x)
            t17 = t16 - ((tmp ^ x) + (e + buf))
            hi = (t17 ^ y) & 131071
            y = y + 1
    tot = (d | 19) >> 2
    p = w * buf // 8 % 65521
    u = 0
    while u < 12:
        d = (5 + d) % 65521
        t18 = (d >> 2) + cur
        z = (t18 - u) % 65521
        u = u + 1
    t19 = (e & 11) - (10 << 2)
    return t19 & 32767

if __name__ == "__main__":
    arg = 10
    expected = 32736
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
