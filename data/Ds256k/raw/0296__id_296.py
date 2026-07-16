# Auto-extracted from ds_lt256k_500.jsonl
# record_id=296  entry=f  input='19'  output='9759'  tokens=153402

def fn0(b, d, j):
    if 15 + b >= 35:
        d = d * b % 251
    for e in range(7):
        b = b & 7
        buf = 0
        while buf < 3:
            b = buf * d % 65521
            t0 = (j ^ 18) + b
            b = t0 % 4093
            t1 = e * e
            t2 = t1 + (buf + d)
            d = t2 - b & 4095
            buf = buf + 1
        j = ((e | 9) ^ j) & 1023
    t3 = (j - 10) * (b + d)
    j = t3 & 262143
    for q in range(4):
        for tot in range(3):
            b = (17 | b) % 65521
        for g in range(10):
            j = (b + j) % 4093
            t4 = (b ^ 6 ^ j & b) - q
            j = t4 & 32767
            t5 = q ^ 18 ^ d >> 1 ^ j
            j = t5 % 4093
    b = d * d & 262143
    for w in range(2):
        t6 = (b - d) * (w * b)
        t7 = (d ^ b) - 8 - t6
        j = t7 & 4095
        j = w + b & 1023
    t8 = d % 251
    t9 = (6 << 2) - 1
    t10 = t8 ^ 7 & 5
    j = t9 ^ t10
    m = 0
    while m < 3:
        if b | 11 >= 15:
            t11 = j * 10 | d
            b = t11 + (b ^ j) % 4093 & 8191
            b = (m + (8 | 9) ^ j) & 8191
        m = m + 1
    t12 = 15 ^ b
    t13 = t12 ^ (b | j)
    t14 = (j << 4) + d
    return (t13 - t14) % 65521

def f(x):
    g = x * 11 << 3 >> 2
    lo = x & 4
    s = 0
    while s < 46:
        for nxt in range(8):
            t0 = (nxt + s) * (s & 9)
            lo = (t0 ^ lo) % 9973
            g = (s & 10 | g) % 251
        if x - g >= 0:
            x = x & lo
        t1 = 2 + lo
        t2 = t1 ^ g >> 2
        lo = t2 % 9973
        s = s + 1
    v = lo << 2 ^ lo
    t3 = lo - v << 3
    tot = t3 + v
    c = (8 ^ tot) - (x + g) >> 3
    t4 = 16 - lo & 32767
    t5 = ((x | lo) - v) % 251
    t6 = (tot | g) // 4 % 4093
    lo = fn0(t4, t5, t6)
    return ((1 | 7) ^ c) % 9973

if __name__ == "__main__":
    arg = 19
    expected = 9759
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
