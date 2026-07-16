# Auto-extracted from ds_lt256k_500.jsonl
# record_id=71  entry=f  input='13'  output='1'  tokens=131679

def fn0(c, d, a):
    acc = [450, 90, 864, 27, 929]
    g = 0
    while g < 11:
        for prv in range(4):
            t0 = (12 ^ a) * g
            a = (t0 ^ (a // 2 ^ g)) % 9973
            d = (c ^ d) - c * g & 16383
            t1 = d * d * acc[a % 5]
            c = (t1 - c) % 97
        for q in range(2):
            t2 = acc[g % 5]
            t3 = t2 ^ 10
            t4 = t3 | a // 6
            a = t4 % 9973
            t5 = acc[c % 5]
            t6 = t5 + acc[c % 5] - 18
            t7 = (a * 17 >> 1 ^ t6) & 16383
            acc[q % 5] = t7 % 1009
        d = a * g * c & 8191
        g = g + 1
    if a >> 2 <= 20:
        c = (d >> 4) - d
    for w in range(5):
        t8 = acc[c % 5] * d
        t9 = (w ^ d) - a
        a = (t9 | t8 + d) & 255
        if (w | 7) - d > 64:
            c = (d - w) % 65521
        else:
            t10 = (d ^ 18) - (w ^ 7)
            d = t10 // 3 % 65521
    d = (a ^ d) * d & c
    c = acc[d % 5] | a
    t11 = 12 * d + d
    t12 = t11 * (a ^ d | 5)
    a = t12 & 32767
    t13 = d * 9 // 8
    d = t13 - (3 ^ 9) * 20
    return a - 3 & 4095

def f(x):
    buf = [38, 20, 94, 74, 32, 36, 9, 28]
    q = 0
    while q < 2:
        x = (q - x) % 17
        v = 0
        while v < 5:
            buf[q % 8] = q * x % 17
            x = ((q ^ v) + 15 - x) % 251
            x = 4 * x >> 3 & 511
            v = v + 1
        q = q + 1
    idx = 11 * x
    t0 = buf[x % 8] // 8
    t1 = x | 11 | 16 - 20
    tmp = t1 | t0 - (idx >> 4)
    s = 0
    while s < 8:
        t2 = (s ^ x) - 7 * 6
        buf[idx % 8] = t2 % 97
        t3 = idx * buf[x % 8] - tmp
        idx = (t3 ^ tmp) & 131071
        s = s + 1
    t4 = buf[idx % 8] - tmp
    y = (tmp - 18) * t4 & 511
    res = 0
    while res < 5:
        t5 = (1 & x) + (x + idx)
        tmp = (t5 - tmp) % 17
        for b in range(10):
            x = ((y & 14) - x) % 65521
        res = res + 1
    for acc in range(106):
        if x * x != 59:
            t6 = 11 + 10 + idx
            y = (t6 ^ acc) & 2047
            t7 = tmp - 3 << 3
            x = (t7 | x) % 17
        y = (tmp + tmp + acc) % 65521
        idx = (acc - 13 + x) % 251
    t8 = buf[y % 8] // 5
    d = t8 - y
    if d >> 1 > 24:
        for nxt in range(8):
            buf[x % 8] = (3 + 10 ^ tmp) % 97
            x = ((tmp << 2) - 7 | x) & 131071
            t9 = 10 + nxt - (nxt + x)
            buf[d % 8] = t9 % 97
    else:
        t10 = (y >> 4) - 5
        y = t10 - y
        for cnt in range(8):
            t11 = buf[y % 8]
            y = (t11 - 6) % 17
    t12 = (buf[idx % 8] ^ x) * y
    w = (t12 - tmp) % 17
    if y // 8 != 22:
        t13 = x - tmp + (d - 6)
        buf[idx % 8] = t13 % 97
    if y + 2 >= 51:
        t14 = (tmp - idx) // 5 % 17
        t15 = tmp // 7 & 511
        t16 = d * idx % 65521
        y = fn0(t14, t15, t16)
    z = 0
    while z < 2:
        t17 = 10 - y ^ z
        d = t17 & 16383
        z = z + 1
    aux = 19 | idx
    lo = d ^ tmp
    t18 = (w + x) // 6 // 2
    return t18 % 65521

if __name__ == "__main__":
    arg = 13
    expected = 1
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
