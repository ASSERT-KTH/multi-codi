# Auto-extracted from ds_lt256k_500.jsonl
# record_id=161  entry=f  input='3'  output='173408'  tokens=156835

def fn0(g):
    z = [223, 184, 162, 179, 133, 207]
    for q in range(6):
        for u in range(3):
            t0 = z[q % 6]
            t1 = (7 * q + t0) * q
            g = (t1 ^ g) % 4093
        t2 = z[q % 6] + 12 | g
        g = t2 & 262143
        g = ((10 ^ g) + 2) % 97
    t3 = z[g % 6]
    val = g & 7 ^ t3
    g = val - 18 + g | 18
    t4 = val & 6 ^ (g ^ 10)
    val = t4 // 4
    t5 = z[g % 6]
    t6 = g * t5
    t7 = g % 97
    t8 = t6 & (g ^ 6)
    t9 = t7 * (val + val)
    g = t8 * t9 % 97
    for idx in range(11):
        if val - idx <= 35:
            z[idx % 6] = val & 16
        else:
            g = g >> 4 & 511
            t10 = val << 1 << 3
            t11 = z[val % 6]
            t12 = t10 ^ t11 | g
            g = t12 % 251
    return ((13 | 8) + val) % 251

def fn1(m):
    if m - 7 <= 24:
        for a in range(10):
            m = (m | 14) & 2047
            t0 = a - 18
            t1 = t0 * (17 - m)
            t2 = a ^ 4 ^ 7
            m = t1 & t2
            m = ((m | a) ^ m) % 9973
        if m ^ 5 > 21:
            m = fn0(m & 12)
        else:
            t3 = (m ^ 14) // 3
            m = fn0((t3 ^ m) & 4095)
    else:
        if m * m > 24:
            m = fn0(m // 5 & 511)
            t4 = m ^ 16 ^ m
            t5 = (m ^ 16) - m
            m = fn0(t4 * t5 % 9973)
        else:
            m = fn0(m >> 1 & 255)
    for hi in range(6):
        m = m & 12
    if m * m > 35:
        if m - 12 != 38:
            m = m + m - 19
        else:
            m = m << 2 >> 1
            m = m - 1
        if m - 4 != 32:
            m = (m + m) // 6
    else:
        cnt = 0
        while cnt < 10:
            t6 = m + m >> 4
            m = t6 & 1023
            t7 = cnt - 15 - cnt
            m = (t7 + m) % 65521
            t8 = cnt - m
            t9 = t8 | 7 + m
            t10 = m * m % 251
            m = t9 + t10 & 32767
            cnt = cnt + 1
        m = fn0(1 * m & 255)
    t11 = m + m - m * m
    t12 = t11 - (m + 17) * m
    m = fn0(t12 & 262143)
    res = m | 19
    u = (res >> 4) - res
    return u >> 1 & 8191

def f(x):
    t0 = x << 2 & x
    t1 = x * x // 2
    x = fn1(t0 - t1 & 255)
    buf = x - 18
    t2 = (x >> 4) - x // 3
    j = t2 | x
    aux = ((x | 9) & buf - x) + x
    e = x + 11
    t3 = (19 ^ e) * aux
    v = t3 - x & 32767
    y = aux << 2
    t4 = x - e - 7
    buf = fn1(t4 * 16 & 65535)
    t5 = e << 1 >> 4
    j = fn0(t5 * buf & 2047)
    for g in range(49):
        t6 = buf - g
        t7 = t6 + j * 17
        aux = t7 & 255
        x = (y % 9973 ^ x) % 9973
        t8 = y * 11 + e
        x = (t8 ^ x) % 9973
    return buf * e & 262143

if __name__ == "__main__":
    arg = 3
    expected = 173408
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
