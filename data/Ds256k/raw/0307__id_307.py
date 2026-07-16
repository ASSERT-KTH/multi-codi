# Auto-extracted from ds_lt256k_500.jsonl
# record_id=307  entry=f  input='14'  output='127'  tokens=198270

def fn0(g, c):
    for y in range(6):
        for aux in range(4):
            t0 = g + y | c
            g = t0 % 1009
            t1 = g // 4 | y
            g = t1 % 4093
        t2 = y + 2 - g
        c = t2 % 1009
    m = (c - 15) // 3
    val = (m | g) - (g ^ 13)
    t3 = 17 - val | 3 * val
    g = t3 // 7 % 4093
    c = (1 - val) * 4 * m % 4093
    t4 = (c * g ^ 7) << 1
    c = t4 & 131071
    v = 0
    while v < 11:
        t = 0
        while t < 6:
            g = (g ^ t) % 1009
            t5 = m % 1009 >> 2 | g
            g = t5 & 8191
            t6 = ((val ^ 5) << 4) * g
            val = t6 % 1009
            t = t + 1
        t7 = (c << 3) - c + m
        m = t7 & 2047
        if 2 ^ m < 44:
            t8 = (11 * 11 << 3 >> 2) + g
            val = (t8 | v) & 32767
            g = (12 ^ val) + v & 131071
        else:
            c = (m ^ g ^ v) & 131071
            t9 = val - c - (15 << 3)
            t10 = t9 - 2 * 19 * (v ^ 11)
            c = t10 & 16383
        v = v + 1
    return val + g & 65535

def f(x):
    if 11 + x != 22:
        t0 = x * 18 * 14
        t1 = (x | 12) - 19
        t2 = (t0 - t1) % 17
        t3 = (x + x) % 251
        x = fn0(t2, t3)
    else:
        x = x - 7
    if 1 ^ x < 29:
        t4 = x - 11
        t5 = t4 + (19 ^ x)
        t6 = x * x * (x - 7)
        x = fn0(t5 % 251, t6 & 32767)
        x = x ^ 6
    t7 = (x >> 2) % 251 >> 1 & 8191
    t8 = x // 5 & 2047
    x = fn0(t7, t8)
    z = (x >> 1) * x % 251
    if z >> 1 <= 53:
        x = (z + z) * (z ^ 2)
        x = x * z << 2 & 4095
    t9 = (8 | 3) << 1
    z = t9 - (x & 10 ^ z)
    a = 0
    while a < 92:
        z = ((x >> 3) + z) % 251
        if a - x <= 62:
            t10 = (14 | 18) - z | a
            x = t10 % 251
        a = a + 1
    t11 = (z << 4) // 3
    return t11 % 251

if __name__ == "__main__":
    arg = 14
    expected = 127
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
