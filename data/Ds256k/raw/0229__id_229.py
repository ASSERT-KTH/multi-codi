# Auto-extracted from ds_lt256k_500.jsonl
# record_id=229  entry=f  input='7'  output='0'  tokens=164521

def rec(n, a):
    if n <= 0:
        return a
    t0 = n * a >> 3
    p = (t0 ^ n) % 4093
    a = (n // 7 | p) % 97
    t1 = a // 7 & 32767
    return rec(n - 1, t1)

def fn0(j, b, m):
    t0 = (m << 1) % 4093
    m = rec(39, t0)
    t1 = 2 * m >> 3
    g = t1 - j
    if g % 97 == 10:
        for aux in range(2):
            t2 = aux - m
            t3 = t2 | aux & 5
            m = t3 % 97
            t4 = aux + aux ^ m + b
            j = (t4 ^ aux) & 1023
            g = (j * m - g) % 4093
        j = b // 4
    else:
        if g // 3 >= 23:
            t5 = 20 + m << 4
            m = rec(67, t5 % 4093)
            t6 = (j - m) % 4093
            t7 = b - 6 | m
            g = t6 & t7
        if m * g > 33:
            b = b * m * 16 & 255
            g = g & m | g
        else:
            t8 = b % 4093
            t9 = t8 * (15 | g)
            m = rec(78, t9 % 97)
            t10 = (20 * 7 ^ j) % 97
            j = rec(93, t10)
    t11 = b - g & j
    w = t11 >> 3
    t12 = (j | 18) & 131071
    m = rec(67, t12)
    t13 = g * m >> 2 | 9
    return t13 % 97

def fn1(a):
    t0 = a // 4 ^ a
    nxt = t0 + a
    t1 = a + a >> 1
    tmp = t1 * nxt % 1009
    t2 = ((nxt | a) ^ a) * 7
    a = rec(85, t2 % 65521)
    m = 19 * a % 65521
    s = tmp + tmp
    t3 = 3 * 10 + m
    t4 = (a ^ 16) >> 4
    t5 = (m << 4) % 65521
    nxt = fn0(t3 & 4095, t4 & 262143, t5)
    if 8 + 16 + a > 33:
        s = s ^ a ^ (nxt ^ m)
        t6 = nxt % 9973 | m
        nxt = t6 >> 1
    t7 = tmp + 19 & 32767
    nxt = rec(68, t7)
    return (a % 65521 | m) % 65521

def f(x):
    b = x - 12 | x * x
    aux = 0
    while aux < 17:
        p = 0
        while p < 8:
            x = (p ^ b) % 251
            p = p + 1
        aux = aux + 1
    t0 = (b + x) % 9973
    x = rec(41, t0)
    t1 = x * 15 ^ x // 5
    acc = t1 & b * 14 * x
    d = 0
    while d < 4:
        for e in range(5):
            t2 = ((acc ^ 8) << 2) - e
            x = t2 % 9973
            b = b >> 3 & b
        cur = 0
        while cur < 12:
            acc = ((b >> 4) + acc) % 1009
            t3 = x - b | cur
            acc = t3 % 9973
            b = b & cur
            cur = cur + 1
        d = d + 1
    if b | acc != 0:
        acc = 15 + acc & 511
        x = b * x % 1009
    else:
        t4 = b // 5 + 1
        x = t4 * b
    a = (acc ^ b) * (b - x) % 1009
    t5 = x // 4 - a
    x = fn1(t5 & 255)
    return (acc ^ a) & x

if __name__ == "__main__":
    arg = 7
    expected = 0
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
