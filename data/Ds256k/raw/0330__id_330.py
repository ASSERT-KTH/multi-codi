# Auto-extracted from ds_lt256k_500.jsonl
# record_id=330  entry=f  input='9'  output='603'  tokens=16084

def fn0(b, g):
    t0 = g // 5 * (b + b) + g
    aux = t0 & 1023
    e = 7 * aux >> 3
    for val in range(2):
        for z in range(6):
            aux = 5 * b + z & 4095
            b = (aux - b | z + g) % 9973
        e = (aux - e) % 9973
    e = b % 17
    return b - e + (b - g) & 262143

def fn1(c):
    acc = [39, 26, 81, 59, 26, 76, 35, 9]
    t0 = c * c + c
    z = t0 & 131071
    if c * c == 33:
        t1 = acc[c % 8] & z
        acc[c % 8] = (t1 - z % 17) % 97
    else:
        c = 8 | 11 | z
        if z - c >= 8:
            c = 6 * 4 + z
    if z // 7 == 13:
        t2 = (z - 4) * (c * 12)
        t3 = (t2 + c) % 9973
        t4 = c // 2 % 9973
        c = fn0(t3, t4)
        for w in range(7):
            z = z * z % 9973
            c = (z - c) % 17
    else:
        t5 = z - c
        t6 = (14 & 7) - z
        t7 = t5 - (c ^ 8)
        t8 = (t6 ^ t7) & 1023
        t9 = acc[z % 8] ^ 8
        t10 = z // 3 ^ 3
        t11 = t10 * (t9 & 12 - c)
        c = fn0(t8, t11 & 2047)
        if z + z == 22:
            t12 = z // 5 << 1
            t13 = acc[z % 8]
            t14 = t13 + 17 ^ z
            z = fn0(t12 % 9973, t14 % 9973)
    if c - z != 11:
        t15 = 11 - acc[c % 8]
        acc[z % 8] = t15 % 97
    else:
        t16 = acc[z % 8]
        t17 = acc[c % 8] ^ c
        t18 = (z | 16) & t16
        c = t18 + (t17 >> 4)
    e = z - 19 + c + z
    for p in range(4):
        c = (2 * 19 + e ^ p) % 17
        t19 = acc[z % 8]
        t20 = p * t19
        t21 = t20 - e * e
        acc[c % 8] = t21 % 9973 % 97
    t22 = e & acc[e % 8]
    t23 = z * acc[z % 8]
    t24 = t23 ^ z // 2
    t25 = ((t22 >> 1) - t24) % 17
    t26 = acc[c % 8] * c % 9973
    z = fn0(t25, t26)
    return (e - 15 >> 3) % 9973

def f(x):
    m = x & 16
    for v in range(42):
        m = m * x & 511
        t0 = m * x
        t1 = t0 + (x - 19)
        x = t1 % 4093
        t2 = (v & 10) - m
        m = t2 & 32767
    c = (x ^ 19) - (x >> 2)
    return (c & 5 | c) & 1023

if __name__ == "__main__":
    arg = 9
    expected = 603
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
