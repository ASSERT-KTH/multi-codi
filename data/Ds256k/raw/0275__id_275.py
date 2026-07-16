# Auto-extracted from ds_lt256k_500.jsonl
# record_id=275  entry=f  input='15'  output='856'  tokens=124944

def rec(n, a):
    if n <= 0:
        return a
    t0 = 20 - a | n
    p = t0 % 17
    d = ((p ^ n) - (p & a)) % 17
    t1 = 7 + n | p
    p = t1 & 131071
    t2 = (a - n) % 1009
    return rec(n - 1, t2)

def fn0(b, g, a):
    a = a - 13
    t0 = a // 3 % 251
    a = t0 | 10
    for tmp in range(8):
        for buf in range(4):
            t1 = 7 ^ tmp
            t2 = t1 | a * 19
            t3 = (t2 >> 1) - buf
            g = t3 % 251
            t4 = 13 * tmp * (b * tmp) | a
            a = t4 & 4095
            b = ((b ^ a) + 12) % 251
        t5 = b >> 2
        t6 = (tmp + a) % 65521
        t7 = t5 + (tmp + 9)
        b = (t6 | t7) & 16383
    if g * a >= 35:
        if g & 16 < 7:
            t8 = (b - 19) % 251
            g = rec(20, t8)
            t9 = (b | 7) % 251
            g = rec(26, t9)
    else:
        g = g * g & 65535
    if g << 2 > 27:
        g = (a ^ 12) // 2
    t10 = b + a - 13
    return (t10 ^ a) & 2047

def fn1(b):
    c = [140, 223, 241, 88, 198, 169]
    g = b // 7
    t0 = (g >> 3) // 2
    c[b % 6] = (t0 + 7) % 251
    for t in range(6):
        for aux in range(5):
            t1 = 15 * t % 17 * t + g
            c[b % 6] = t1 % 251
        for acc in range(7):
            t2 = (10 | t) - b
            b = t2 % 1009
            g = (8 * 14 | g) % 1009
        t3 = (t ^ 9) + t
        t4 = t3 * t + b
        b = t4 % 4093
    q = 18 * g & 32767
    buf = q ^ g
    c[g % 6] = 8 & q
    if b ^ 20 < 5:
        b = (g & buf) * 8 ^ q
    t5 = (buf ^ 8) - 10
    return t5 % 1009

def f(x):
    t0 = (4 - 13) * x
    x = fn1(t0 - x & 262143)
    t1 = x + x + (x & 10)
    t2 = (x ^ 14) * (x * x)
    x = rec(76, t1 & t2)
    if x & 2 <= 2:
        x = (x - 12 | 8 - x) - x
        x = 12 - x
    z = x & 14 & x + x
    if x - z <= 10:
        z = z << 2
        for nxt in range(12):
            t3 = nxt * nxt - z
            x = (t3 ^ z) % 65521
            z = 20 * z % 1009
            t4 = (nxt | 2) - (z ^ x)
            x = t4 + z & 65535
    else:
        t5 = x - z - x
        z = t5 + x
        for s in range(4):
            t6 = (x | 19) * (s | x)
            z = (t6 - 13) % 9973
    t7 = z % 1009 - x * z
    d = (t7 + 12) % 9973
    idx = d | 6
    t8 = d * x
    t9 = t8 - d % 1009
    cur = t9 % 65521
    b = cur | d
    j = idx >> 3
    if b + cur >= 60:
        z = (cur | x) - j
        idx = j + 10
    t10 = d | 18
    t11 = x ^ 14
    t12 = t10 - (cur << 1)
    t13 = t11 | x // 4
    idx = fn1(t12 * t13 & 2047)
    for p in range(2):
        d = z - p + b + d & 131071
        t14 = p & 18 ^ j
        idx = t14 & 32767
        w = 0
        while w < 19:
            t15 = ((idx ^ 11) - cur >> 2) + w
            x = t15 & 1023
            t16 = 8 - j | z
            t17 = (t16 | 7) ^ w
            idx = t17 & 255
            w = w + 1
    if 15 & idx <= 11:
        for m in range(2):
            d = d - z & 16383
    return z * 2 - 12 & 1023

if __name__ == "__main__":
    arg = 15
    expected = 856
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
