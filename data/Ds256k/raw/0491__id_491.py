# Auto-extracted from ds_lt256k_500.jsonl
# record_id=491  entry=f  input='6'  output='7'  tokens=219362

def rec(n, a):
    if n <= 0:
        return a
    w = 0
    while w < 3:
        t0 = n << 2 ^ w
        t1 = t0 // 3 | a
        a = t1 & 511
        if n + a >= 56:
            t2 = w << 1 ^ a
            a = t2 % 65521
        else:
            a = (w + n ^ a) % 9973
            a = ((w + a) // 4 + n) % 65521
        if w - 3 - a > 22:
            t3 = (n ^ 3) + 4
            t4 = (3 | 1) * n
            t5 = (t3 & t4) + a
            a = t5 % 65521
            a = 17 - w + a & 65535
        w = w + 1
    t6 = a * a * (a - 4)
    a = t6 % 9973
    t7 = (n & a) * n
    t8 = t7 * n % 65521
    return rec(n - 1, t8)

def fn0(b, c):
    p = b & 9
    t0 = (p ^ b) - b << 2
    c = rec(50, t0 % 97)
    for hi in range(9):
        p = (p + b) // 4 & 8191
    j = b >> 3
    t = p * b % 97
    if t >> 2 == 20:
        b = p >> 1
        for q in range(12):
            t1 = j - 7 - (4 << 1) | q
            p = t1 % 9973
    if 19 + b > 54:
        for z in range(6):
            t2 = t + t
            t3 = t2 - t * p
            t = t3 & 8191
            b = (b - c) * p % 97
        if b + t >= 14:
            b = j ^ 6
        else:
            t4 = 5 - c ^ p - 6
            t = rec(58, t4 & 8191)
    else:
        t5 = j + p & c
        t6 = t5 - (4 & 2 ^ 1)
        p = rec(61, t6 % 97)
    for nxt in range(12):
        b = (p & t | nxt) % 9973
        t7 = (6 ^ j | b) >> 3
        t = (t7 ^ nxt) % 9973
    t8 = (p & 18) * c * 19
    return t8 & 1023

def fn1(c, e, m):
    y = 0
    while y < 6:
        if e - m <= 4:
            m = (e * e + m) % 65521
            t0 = (y + c) * m
            t1 = t0 | m * c >> 3
            m = t1 & 65535
        y = y + 1
    a = ((e ^ 18) + c * m) % 251
    val = e // 4
    for lo in range(3):
        if 18 - val != 31:
            t2 = (val << 1) - a
            a = t2 & 65535
        else:
            a = (val + val ^ a) & 131071
        a = ((a * 8 ^ 4) - val) % 65521
    z = 9 & m
    t3 = 15 * 7 | c - 15
    t4 = e - c + (c + m)
    m = t3 ^ t4
    t5 = (a + 10) % 65521
    t6 = (1 ^ e | val) % 4093
    m = fn0(t5, t6)
    t7 = (m ^ e) - 9
    return (t7 - val) % 251

def f(x):
    t0 = x - 20 + (15 - x)
    s = t0 | x
    t1 = x + s - (x & 16)
    w = t1 - (s + x + s)
    nxt = (2 ^ x) * (s >> 4)
    prv = s % 17 ^ x
    t2 = prv * nxt // 3
    c = t2 >> 2
    t3 = (nxt << 1) * s % 65521
    t4 = prv << 3 & (prv & c)
    s = fn0(t3, t4)
    for res in range(4):
        t5 = prv * prv | res
        w = t5 // 2 & 262143
        t6 = w * 7 * (prv - 15)
        c = t6 - ((w ^ res) + s) & 65535
        buf = 0
        while buf < 25:
            s = ((prv ^ c) * buf + 19) % 65521
            buf = buf + 1
    return (x | nxt) * w % 17

if __name__ == "__main__":
    arg = 6
    expected = 7
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
