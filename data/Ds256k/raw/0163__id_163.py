# Auto-extracted from ds_lt256k_500.jsonl
# record_id=163  entry=f  input='4'  output='14'  tokens=197117

def rec(n, a):
    if n <= 0:
        return a
    t0 = (n | a) - (a + a)
    a = t0 * ((13 ^ 5) + n) % 97
    t1 = n // 8 | a
    return rec(n - 1, t1 % 97)

def fn0(d, m, g):
    buf = [67, 217, 145, 149, 21, 12]
    y = 0
    while y < 6:
        if d * 15 == 31:
            m = g & m
        else:
            m = ((d ^ 6) - y) % 65521
            t0 = m - d ^ g
            buf[m % 6] = (t0 ^ buf[g % 6]) % 251
        y = y + 1
    t1 = (d - 16 ^ 17) & 32767
    g = rec(35, t1)
    if d - 10 != 24:
        g = 5 * d + g
    else:
        t2 = (d | 14) << 2
        buf[g % 6] = t2 % 251
        t3 = buf[g % 6] >> 3
        t4 = ((d & g) + t3) * g
        d = t4 % 4093
    for lo in range(11):
        t5 = 17 ^ 15 ^ lo
        g = (t5 + d) % 65521
        t6 = 15 * 3 - g ^ d
        d = t6 % 4093
        d = (lo - d) % 4093
    b = g ^ 10
    aux = (19 - 9) * 19 + g
    t7 = buf[d % 6] * d - m
    g = t7 * 4 & 8191
    t8 = (b ^ buf[g % 6]) // 7
    t9 = t8 + (m ^ b ^ 11 & b)
    return t9 & 1023

def f(x):
    m = [180, 115, 88, 244, 99, 16, 218, 9]
    v = x ^ 17
    for a in range(11):
        g = 0
        while g < 49:
            t0 = m[a % 8] & x
            t1 = a - 11 ^ g
            x = (t1 + (t0 & a)) % 17
            m[x % 8] = (9 | v) + g >> 4
            g = g + 1
        v = a * v % 65521
    t2 = x - 10 & x
    t3 = (v | 10) % 65521
    t4 = 19 & x
    t5 = t4 & (x | v)
    x = fn0(t2, t3, t5)
    idx = (v // 5 << 4) % 17
    t6 = (x - 13) * x
    return (t6 ^ idx) % 17

if __name__ == "__main__":
    arg = 4
    expected = 14
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
