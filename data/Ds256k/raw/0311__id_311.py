# Auto-extracted from ds_lt256k_500.jsonl
# record_id=311  entry=f  input='18'  output='31'  tokens=95718

def fn0(j, b):
    if j + j == 49:
        t0 = (j + j) * 4
        j = t0 * j % 251
        t1 = (j ^ b) % 9973
        t2 = j * j << 1
        j = (t1 + t2) % 4093
    prv = j ^ 15
    d = 20 | b
    cur = 0
    while cur < 3:
        t3 = 7 + 2 & j - cur
        j = t3 + cur & 4095
        for y in range(10):
            t4 = b * cur | 14 * 5 | j
            j = t4 % 251
        j = j % 1009
        cur = cur + 1
    t5 = 5 * prv * (j + d)
    prv = t5 + (j ^ 17 ^ 15) & 8191
    return (d >> 3) + j & 4095

def fn1(d):
    buf = d + d - d - 5
    t0 = d + d
    t1 = t0 ^ (buf | d)
    q = t1 << 4 & 2047
    aux = q >> 2
    for cnt in range(6):
        t2 = buf * q
        t3 = t2 ^ (14 ^ aux)
        buf = t3 // 6 % 17
        t4 = buf - aux ^ cnt - d
        q = t4 % 17
    t5 = (buf + 17 & d) - d
    return t5 & 16383

def f(x):
    lo = (x * x & x) + x
    w = lo - 14
    for tot in range(21):
        for a in range(4):
            lo = (tot + w | lo) % 251
        w = w * x & 32767
        for acc in range(6):
            x = ((lo >> 4) - acc) % 251
            t0 = 12 - tot
            t1 = acc << 1 << 1
            t2 = t0 - tot * tot
            t3 = t1 - t2 + x
            lo = t3 & 32767
    t4 = 12 * 1 * 6
    x = fn1((t4 | w) & 255)
    t5 = x + 9 << 1 | w
    lo = fn1(t5 & 255)
    w = fn1(((w & x) * x ^ w) & 2047)
    t6 = lo ^ x
    t7 = t6 + (w & lo)
    t8 = x >> 2 >> 2
    t9 = t7 * t8 % 251
    t10 = w + x >> 4
    w = fn0(t9, t10 % 251)
    t11 = lo - w << 1
    return (t11 + (lo << 4 | lo)) % 251

if __name__ == "__main__":
    arg = 18
    expected = 31
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
