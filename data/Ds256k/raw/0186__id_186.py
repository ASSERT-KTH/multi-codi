# Auto-extracted from ds_lt256k_500.jsonl
# record_id=186  entry=f  input='6'  output='0'  tokens=24428

def fn0(c, g):
    idx = (14 + g) % 9973
    cnt = (g & 4) * c
    t0 = g + cnt + 5
    t1 = t0 * (g - 1 + idx)
    g = t1 & 131071
    for q in range(6):
        c = ((7 << 1 << 3) - c) % 251
    return ((idx >> 2) - (c & cnt)) % 251

def fn1(g, c):
    p = 0
    while p < 12:
        g = (g << 2) % 65521
        g = (13 + g) % 251
        t0 = 5 + 2 + (g - p)
        g = t0 & (c | 15) << 3
        p = p + 1
    t1 = (c - 15) % 9973
    t2 = c + 19 & 1023
    c = fn0(t1, t2)
    t3 = (1 | c) & 1023
    c = fn0(t3, c & 1)
    t4 = g * c * g & 511
    t5 = (2 ^ c) % 251
    c = fn0(t4, t5)
    if c * c != 2:
        c = c - 8
        t6 = (g - 8) % 65521
        t7 = (g | 10) << 1 & 2047
        g = fn0(t6, t7)
    idx = 0
    while idx < 4:
        for t in range(5):
            c = 3 + c & 8191
        if 16 | 12 | c != 26:
            c = (c // 3 << 3) % 251
            t8 = g * 5 - (idx - 4)
            c = t8 & 1023
        for cnt in range(6):
            g = (idx & 17) - c + cnt & 32767
            t9 = cnt + idx << 4
            t10 = t9 - (idx & 5) * cnt
            g = (t10 | g) & 2047
            c = (17 * g - cnt) % 9973
        idx = idx + 1
    c = g - 6
    if c - 6 == 26:
        for w in range(5):
            c = c * w % 9973
            t11 = w ^ 17 ^ g
            c = t11 & 4095
    t12 = 11 - 3 - g
    return t12 % 65521

def f(x):
    buf = [230, 96, 15, 101, 194]
    lo = 0
    while lo < 12:
        t0 = buf[lo % 5] + 4
        x = (t0 | x) % 251
        lo = lo + 1
    q = x << 4 & x
    for tot in range(6):
        t1 = 15 - 10 | tot
        q = t1 - x & 8191
    for t in range(4):
        t2 = 4 - q + q
        t3 = t2 - q | x
        x = t3 % 65521
    acc = buf[q % 5] >> 4
    idx = 0
    while idx < 24:
        t4 = q - idx - acc >> 3
        acc = t4 % 251
        x = x << 2 & 131071
        t5 = idx * 15 * q
        t6 = x % 251 + acc
        q = (t5 | t6) & 131071
        idx = idx + 1
    return x & acc

if __name__ == "__main__":
    arg = 6
    expected = 0
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
