# Auto-extracted from ds_lt256k_500.jsonl
# record_id=314  entry=f  input='19'  output='9'  tokens=259690

def fn0(b, a, e):
    v = a - b >> 2
    t0 = (4 | v) // 7
    c = t0 // 3
    v = ((e - c) * a | b) % 97
    e = (17 - e & a) - v
    e = a + a
    b = v // 5
    e = a << 1
    e = a ^ c
    t1 = c ^ v
    t2 = t1 + (c + c)
    return t2 // 2 & 8191

def fn1(d, g):
    t0 = g * d - g
    cnt = t0 & (g - 10) // 2
    if d * cnt != 54:
        if g + d == 13:
            t1 = cnt ^ 4
            t2 = t1 - (9 + g)
            t3 = d * 20 % 17
            t4 = 10 + cnt ^ 9
            d = fn0(t2 % 17, t3, t4 % 17)
            g = d - 15
    else:
        t5 = cnt + cnt + d * 16
        g = t5 % 17
    t6 = d * cnt + (g - d)
    u = t6 // 6 % 9973
    j = (u & cnt) * 11 >> 1
    lo = 0
    while lo < 7:
        t7 = (cnt + d >> 1 >> 2) - lo
        u = t7 % 17
        c = 0
        while c < 7:
            t8 = lo - u & lo
            j = (t8 + j) % 17
            c = c + 1
        lo = lo + 1
    t9 = (d ^ u ^ d) & 32767
    t10 = (g & 8) + g >> 2
    t11 = (d - j) * 5
    t12 = t11 + (6 | cnt | g)
    u = fn0(t9, t10 % 17, t12 & 65535)
    for aux in range(4):
        for v in range(6):
            u = (d - j | v) % 9973
            t13 = (10 + cnt | g * cnt) + u
            u = t13 % 9973
            u = (u + d) % 9973
        for s in range(2):
            t14 = (7 | j) - s
            j = t14 % 17
            t15 = 19 - cnt + s
            j = t15 % 9973
        t16 = cnt + aux - (u + 16)
        d = t16 & 16383
    t17 = d - u & 1
    t18 = g // 4 ^ j
    q = t17 | t18
    t19 = (d ^ 8) >> 1 << 1
    return (t19 - j) % 17

def f(x):
    t0 = x - 2
    t1 = x * 16 & 3
    t2 = t0 - (x + x)
    aux = t1 ^ t2
    if x & aux == 14:
        if aux | 15 >= 31:
            t3 = (aux - 4 << 2) // 3 % 65521
            t4 = (x ^ aux) & 255
            t5 = aux ^ 13 | (x | 15)
            t6 = t5 // 5 & 65535
            x = fn0(t3, t4, t6)
        x = x * aux >> 2 & 2047
    buf = (x * 14 + x + x) % 97
    q = buf // 5
    for lo in range(4):
        for idx in range(3):
            t7 = lo * 20 >> 2
            t8 = lo - 6 + aux
            t9 = t7 * t8 ^ q
            q = t9 & 131071
    t10 = ((aux - x) * q ^ aux) & 4095
    t11 = buf | 2
    t12 = 16 ^ x
    t13 = t11 - buf * buf
    t14 = t12 - (1 - buf)
    t15 = (t13 - t14) % 97
    t16 = (aux << 2) // 7
    t17 = t16 + (aux + 12 | q) & 2047
    q = fn0(t10, t15, t17)
    t18 = buf & 1 | buf
    t19 = buf * buf << 2
    val = t18 - t19
    m = 0
    while m < 12:
        for p in range(7):
            t20 = x + p ^ val // 8
            x = t20 % 4093
            t21 = (aux & p) * (val * m) ^ m
            aux = t21 % 4093
            x = (x + p) * m & 511
        for cur in range(4):
            t22 = 8 * q // 4
            aux = (t22 | aux) % 65521
        m = m + 1
    z = 0
    while z < 7:
        a = 0
        while a < 8:
            t23 = (aux | 16) ^ x - 19
            buf = (t23 | buf) & 8191
            t24 = val * aux + (a + z)
            buf = (t24 | buf) & 131071
            a = a + 1
        for y in range(6):
            t25 = (val | 8) % 65521 + y
            buf = t25 & 255
        z = z + 1
    j = buf >> 3
    return (buf + j) % 97

if __name__ == "__main__":
    arg = 19
    expected = 9
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
