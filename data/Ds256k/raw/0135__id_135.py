# Auto-extracted from ds_lt256k_500.jsonl
# record_id=135  entry=f  input='15'  output='2'  tokens=108498

def fn0(e, c, b):
    t0 = b * c - 16
    v = t0 & 262143
    t1 = v | e
    t2 = t1 ^ c & b
    v = t2 // 7
    e = b // 5 ^ 18
    hi = 0
    while hi < 6:
        tot = 0
        while tot < 10:
            e = (3 * tot ^ 9 ^ b) & 2047
            c = ((11 | v) // 6 | c) % 4093
            t3 = (v + c) // 4
            b = (t3 - tot) % 4093
            tot = tot + 1
        for tmp in range(9):
            t4 = b * c * 7
            v = t4 + v & 65535
        hi = hi + 1
    t5 = (13 * b ^ e) // 2
    v = t5 % 65521
    for aux in range(7):
        t6 = 19 ^ e
        t7 = e + v ^ 11
        t8 = t6 ^ aux * c
        v = (t7 ^ t8) % 4093
        t9 = v % 65521 // 3
        e = (t9 + aux) % 65521
    t10 = e & c ^ v
    c = t10 % 65521
    t11 = 17 ^ b ^ v
    return t11 & 255

def fn1(g, b):
    d = [879, 492, 98, 151, 238, 428, 323]
    g = b ^ 1 ^ 13 + g
    t0 = (b | g) - 2 & g
    t1 = b + 7 ^ (17 ^ g)
    t2 = t1 + b & 16383
    t3 = b * 11 % 251
    g = fn0(t0, t2, t3)
    g = b * b & 1023
    d[b % 7] = (10 | g) % 1009
    t4 = 10 ^ b
    t5 = b | 2
    t6 = t4 - (6 - b)
    t7 = t5 * (b + b)
    return (t6 | t7) & 255

def f(x):
    for val in range(6):
        c = 0
        while c < 8:
            t0 = x ^ 7 ^ c
            x = t0 & 16383
            x = x - c << 4 & 2047
            t1 = 1 + x - x
            x = t1 + (x * val | x) & 262143
            c = c + 1
        for buf in range(4):
            x = (buf - 16 | x) % 4093
            x = (buf | x) % 4093
    idx = 0
    while idx < 3:
        if idx - 7 + x != 42:
            t2 = 6 * 7
            t3 = idx - x + 19
            t4 = t2 | x // 4
            x = (t3 ^ t4) % 4093
        else:
            t5 = (idx + idx << 2) - idx
            x = (t5 + x) % 97
            t6 = (idx & 11) - x
            x = t6 % 9973
        for aux in range(11):
            x = ((x & idx) + aux) * idx & 2047
            t7 = (idx ^ 2) * x
            x = t7 % 17
        idx = idx + 1
    t8 = (x - 4) * (2 - x) * x
    w = t8 & 8191
    if w | x >= 11:
        x = x | 14
    for acc in range(74):
        w = x * 2 - acc & 32767
        w = (x + x + acc) % 97
        t9 = w - 18 | w
        x = (t9 ^ x) % 4093
    for q in range(8):
        res = 0
        while res < 7:
            x = (w | res) // 6 & 8191
            res = res + 1
        t10 = x * w
        t11 = t10 | q * 8
        x = t11 % 17
    for s in range(2):
        t12 = (w ^ x) * s
        x = (t12 - (x - s << 4)) % 97
    hi = x - 10
    t = 0
    while t < 5:
        t13 = t ^ 4 | w
        hi = t13 % 97
        x = w * t + t & 65535
        if hi >> 4 == 34:
            t14 = (x >> 3 ^ 12 - w) + t
            hi = t14 & 511
        t = t + 1
    d = x // 5
    prv = (x << 4) % 17
    b = 3 + x
    j = d >> 3
    t15 = w // 8 + prv
    return t15 % 17

if __name__ == "__main__":
    arg = 15
    expected = 2
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
