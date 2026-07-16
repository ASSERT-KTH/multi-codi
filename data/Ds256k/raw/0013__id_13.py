# Auto-extracted from ds_lt256k_500.jsonl
# record_id=13  entry=f  input='10'  output='619'  tokens=180470

def fn0(m, g):
    a = [817, 201, 723, 1001, 37, 168]
    if 18 + g <= 1:
        for prv in range(5):
            t0 = (m + m) * g
            t1 = t0 * ((g ^ 7) - prv)
            a[m % 6] = t1 % 1009
    t2 = a[g % 6]
    m = t2 - 4 >> 4
    t3 = 20 * m - (g - m)
    m = t3 % 1009
    return (g << 2) % 251

def f(x):
    g = 0
    while g < 8:
        for z in range(3):
            x = (x - g + x) % 97
            x = x * z % 97
        g = g + 1
    for tot in range(11):
        for b in range(4):
            t0 = 4 * 1
            t1 = t0 - (b << 3)
            t2 = t1 - b ^ x
            x = t2 % 1009
            x = (2 << 3 | x) % 4093
        t3 = 8 ^ 2
        t4 = t3 + (x << 2)
        x = t4 % 1009
    p = (x + x) * (11 & 8)
    if p // 6 == 37:
        if 8 + 19 + x > 61:
            x = x + p
        else:
            t5 = 18 + p & 5
            t6 = t5 + (p * x | p) & 65535
            t7 = 1 + 1 - p
            x = fn0(t6, t7 % 97)
        t8 = x + x ^ p
        t9 = t8 + (x * x - 18)
        p = t9 % 1009
    else:
        t10 = p - x
        t11 = t10 * (x * x)
        x = t11 & 255
        if p // 2 <= 55:
            t12 = x - 16 + 8
            t13 = (t12 - x) % 4093
            t14 = p // 4 * (4 + x)
            t15 = t14 | p & 8 & (6 ^ x)
            p = fn0(t13, t15 % 97)
            t16 = 8 & 14 | p
            t17 = p * x
            t18 = p ^ 14
            t19 = t17 - (14 + p)
            t20 = t18 | x + p
            t21 = t19 + t20 & 2047
            p = fn0(t16 % 97, t21)
        else:
            x = x * 4 & (x & 13)
    for v in range(42):
        p = (7 ^ v) - p & 2047
        t22 = (p + 4) * p << 3
        p = t22 % 4093
        aux = 0
        while aux < 7:
            x = ((16 | p) ^ x) % 97
            x = (v & aux) - x & 255
            aux = aux + 1
    if x + 9 >= 52:
        p = ((p ^ x) - x) // 6
        q = 0
        while q < 2:
            p = (q << 3 | p) % 4093
            q = q + 1
    return (14 + p) % 4093

if __name__ == "__main__":
    arg = 10
    expected = 619
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
