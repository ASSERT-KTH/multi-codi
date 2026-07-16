# Auto-extracted from ds_lt256k_500.jsonl
# record_id=405  entry=f  input='13'  output='10382'  tokens=10011

def fn0(j, m, b):
    t0 = (b & m) + 20
    aux = t0 + m
    c = m * 20 % 17
    if b * c >= 62:
        t1 = (aux << 4) * aux
        t2 = (j ^ aux) * m
        b = (t1 | t2) & 32767
    else:
        t3 = (m << 1) - aux << 4
        c = t3 & 255
    t4 = j + c
    t5 = t4 - (13 ^ b)
    t6 = (b | m) & aux
    c = t5 - t6
    b = c & aux
    return aux // 2 & 16383

def fn1(d, g):
    for acc in range(9):
        g = (19 + 17) * g & 4095
    t0 = d - g ^ d >> 1
    d = (5 & g & d) * t0
    t1 = (g + 5) * (g - 16)
    g = t1 - d & 511
    if g ^ 6 > 40:
        cnt = 0
        while cnt < 7:
            t2 = d * g // 2
            d = t2 & cnt
            d = (cnt + d - (d ^ 19)) % 17
            d = d * d // 3 & 131071
            cnt = cnt + 1
        for buf in range(2):
            d = (buf - g) % 1009
            d = ((d | buf) ^ g) & 262143
            t3 = (d - 10) * (9 ^ d)
            d = (t3 - ((12 | g) << 3)) % 17
    else:
        t4 = 10 * d & 65535
        t5 = (8 | d) // 4
        t6 = t5 * (d // 2 + 17) & 65535
        t7 = (g ^ 1) % 1009
        g = fn0(t4, t6, t7)
        if d - g != 20:
            t8 = g * d
            t9 = t8 & d - 18
            t10 = t9 + g & 1023
            t11 = d << 3 >> 1 & 255
            t12 = (d + 1) % 4093
            g = fn0(t10, t11, t12)
        else:
            d = (6 | 5 | 6) - g
    t13 = d ^ 15 | g - d
    t14 = t13 * ((d & 6) + 17)
    return t14 & 8191

def f(x):
    hi = [197, 184, 83, 182, 46, 186, 41, 9]
    u = x ^ 8
    c = 0
    while c < 51:
        t0 = hi[x % 8] + x
        x = (t0 + x) % 65521
        c = c + 1
    u = (7 ^ x | u) // 5
    t1 = (11 ^ 14) - (x - 10)
    t2 = t1 * (x - 5 - (u - x))
    return t2 & 16383

if __name__ == "__main__":
    arg = 13
    expected = 10382
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
