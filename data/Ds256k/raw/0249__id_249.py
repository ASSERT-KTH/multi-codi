# Auto-extracted from ds_lt256k_500.jsonl
# record_id=249  entry=f  input='1'  output='56'  tokens=150863

def rec(n, a):
    if n <= 0:
        return a
    c = 0
    while c < 11:
        a = (17 - c ^ a) % 17
        c = c + 1
    t0 = (n - a) * 20 & 131071
    return rec(n - 1, t0)

def fn0(j, b):
    if j * b == 8:
        b = (15 + b >> 4) - j
        t0 = (j - b) % 17
        b = rec(91, t0)
    else:
        g = 0
        while g < 10:
            t1 = 2 + j + (g + b) << 2
            b = t1 % 17
            j = (14 ^ g | b) % 9973
            t2 = (11 ^ b) // 4
            b = (t2 + b) % 9973
            g = g + 1
    w = b % 17
    t = w * 11 | b // 7
    if b ^ t <= 53:
        for a in range(12):
            j = b + a & 511
    t3 = w - t ^ w + 17
    e = t3 & b
    tmp = (e - b ^ 10) & b
    t = rec(106, w & j)
    b = (w | 5) + (e ^ b)
    return (t << 3) % 251

def fn1(d, c):
    v = [980, 460, 837, 91, 996]
    c = (c & 13) + 20 + d
    j = 0
    while j < 2:
        t0 = (7 & j) - d * c
        d = ((d + j) % 4093 | t0) % 4093
        t1 = 17 & j | 18 - 14
        v[j % 5] = (t1 | d) % 1009
        t2 = v[j % 5] * j + c
        d = t2 & 65535
        j = j + 1
    c = c & 20
    return (c | 12) + d & 1023

def f(x):
    for q in range(3):
        if q * x >= 55:
            t0 = q ^ 15
            t1 = (2 | q) ^ x
            t2 = t0 | 16 * x
            x = t1 + t2 & 8191
        else:
            x = ((x - q) // 8 - q) % 97
            t3 = 17 - (q + x)
            t4 = q + x - x
            x = (t3 ^ t4) % 251
        for v in range(13):
            x = (q << 2) + x & 131071
            x = x * v % 97
            x = (x ^ v) * v & 65535
    t5 = (14 ^ x) % 251
    t6 = x * x & 262143
    x = fn0(t5, t6)
    nxt = x | 6
    p = 0
    while p < 8:
        if nxt & p >= 6:
            nxt = x & nxt & 19
            x = (nxt - p + 11) % 97
        else:
            nxt = x - nxt & 4095
        t7 = (p << 4 >> 4) - nxt
        x = t7 % 251
        x = p + p - x & 2047
        p = p + 1
    for buf in range(11):
        t8 = buf + buf - x
        nxt = t8 & 255
        t9 = 10 * x + (nxt - 12)
        x = ((7 & 17) << 2 ^ t9) % 251
        t10 = (x << 1 ^ x) - buf
        nxt = t10 % 9973
    idx = x // 3 // 5 >> 3
    t = idx * idx * (7 * x) % 251
    return (1 & 14) + x - t & 255

if __name__ == "__main__":
    arg = 1
    expected = 56
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
