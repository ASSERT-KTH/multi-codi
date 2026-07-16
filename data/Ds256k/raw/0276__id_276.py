# Auto-extracted from ds_lt256k_500.jsonl
# record_id=276  entry=f  input='4'  output='1008'  tokens=225109

def rec(n, a):
    if n <= 0:
        return a
    a = 12 & a
    for s in range(10):
        a = (5 | a) % 9973
        t0 = (n << 1 | a ^ n) * n
        a = t0 & 8191
    t1 = (20 - 2 ^ a) & 255
    return rec(n - 1, t1)

def fn0(c, b):
    if b // 6 >= 39:
        if c >> 1 < 31:
            t0 = (c | b) % 17
            c = rec(89, t0)
        t1 = c - 18 << 3 & 262143
        c = rec(95, t1)
    else:
        for buf in range(6):
            t2 = buf * c | c
            b = (t2 ^ buf) & 1023
    if (16 ^ 11) + b > 16:
        b = ((c << 4) + c) % 17
    else:
        for v in range(4):
            t3 = (v - b) * c
            c = t3 // 7 & 16383
            b = (c * c % 251 + v) % 251
            t4 = c % 17 - v ^ c
            b = t4 % 251
    d = 0
    while d < 10:
        t5 = (8 & c) * (c << 4)
        t6 = b * d + (c - b)
        b = (t5 | t6) % 251
        c = (c - d) % 251
        t7 = (d - b) // 2 + b
        c = t7 % 251
        d = d + 1
    t8 = 1 + 4 ^ b
    c = rec(40, t8 % 17)
    t9 = ((b ^ c) - (12 | c)) % 17
    b = rec(46, t9)
    return 4 * (c + c) // 3 % 1009

def f(x):
    x = rec(98, x & 8191)
    for hi in range(7):
        for a in range(10):
            t0 = (a + x & a) * a
            x = t0 % 17
    u = x + x - (5 + x) + x
    if u // 4 >= 50:
        x = (x ^ 9) & u ^ u
        u = 3 * 11 - (u | 7)
    d = 0
    while d < 9:
        t1 = (u << 2 ^ 8) - x
        x = t1 % 65521
        prv = 0
        while prv < 10:
            x = 2 - u + u - x & 511
            prv = prv + 1
        t2 = u * d
        t3 = t2 * (x & 10)
        x = t3 & 8191
        d = d + 1
    w = u - 17 + u
    for t in range(9):
        for v in range(4):
            t4 = (u ^ x) - (u - 11)
            u = (t4 | t) & 511
        t5 = (t + t << 2) // 5
        w = (t5 ^ u) % 1009
        t6 = u & t
        t7 = t6 & (u & x)
        w = (t7 ^ x) & 32767
    tmp = 2 - 16 ^ x
    t8 = 7 + tmp >> 4
    return (t8 + w) % 1009

if __name__ == "__main__":
    arg = 4
    expected = 1008
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
