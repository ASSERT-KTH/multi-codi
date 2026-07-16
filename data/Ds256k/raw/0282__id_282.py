# Auto-extracted from ds_lt256k_500.jsonl
# record_id=282  entry=f  input='6'  output='4016'  tokens=161547

def rec(n, a):
    if n <= 0:
        return a
    u = n + a & n * n
    t0 = (u - n + a) % 97
    return rec(n - 1, t0)

def fn0(g, d, j):
    buf = [67, 136, 237, 72, 45]
    for val in range(8):
        t0 = buf[d % 5]
        t1 = 3 + d + t0
        d = t1 % 251
    if buf[d % 5] + j <= 62:
        t2 = buf[j % 5]
        t3 = buf[g % 5]
        t4 = 5 ^ g
        t5 = t4 ^ t2 - t3
        buf[d % 5] = t5 % 251
    d = g << 2
    if g % 9973 == 17:
        buf[j % 5] = d // 8 // 8 % 251
        g = (d - g) * d % 1009
    else:
        t6 = (j + 8) * (j * g)
        j = t6 % 97
    t7 = d - 6 | g
    d = t7 + buf[g % 5]
    return (2 * 19 - 8 | j) % 9973

def fn1(c, a, j):
    j = 4 << 2 ^ a
    if a // 4 <= 50:
        z = 0
        while z < 11:
            t0 = a * a // 5 - z
            j = t0 % 4093
            z = z + 1
        c = (c ^ j) % 97
    for prv in range(8):
        t1 = (a >> 4 | c) + j
        c = t1 % 97
        for cur in range(5):
            t2 = (c << 1) * a
            j = (t2 ^ j & cur) % 4093
            t3 = 12 - 16
            t4 = t3 & cur << 3
            a = (t4 + c) % 1009
    if a - 9 < 50:
        j = (j | a) & (1 & 7)
        t5 = (c & 11) * (a ^ 16)
        t6 = t5 ^ (c ^ 18) + c
        j = t6 % 1009
    else:
        for tmp in range(11):
            t7 = j - 6 ^ 12
            c = (t7 - tmp) % 4093
            t8 = (c | tmp) % 251 - j
            c = t8 & 16383
    t9 = j * c * (a >> 2) >> 2
    a = t9 & 4095
    return (c ^ j) + a & 65535

def f(x):
    y = 6 | x
    if y - x <= 43:
        t0 = 8 + 6 ^ 10
        t1 = (x << 2) * 8
        x = t0 + t1
        if x & 16 < 14:
            t2 = x % 17 ^ y ^ y
            x = rec(66, t2 % 17)
            x = x + x >> 4
        else:
            t3 = (11 ^ y) & x * y
            t4 = (t3 + (x << 3) * y) % 9973
            t5 = (y & 10 ^ x) << 2
            t6 = y * x << 1
            x = fn0(t4, t5 & 1023, t6 % 4093)
            t7 = y * y & 4095
            y = rec(32, t7)
    else:
        for q in range(9):
            y = y - 6 & 1023
            t8 = 7 * q - 4
            y = t8 - x & 255
            x = (y - x << 3 ^ q) % 4093
    t9 = x * x // 8
    cnt = t9 % 17
    val = 0
    while val < 12:
        if val - x > 63:
            t10 = (y + x ^ y + y) + val
            cnt = t10 % 17
            t11 = y + y - y
            x = (t11 + x) % 4093
        else:
            t12 = x % 4093 * (y ^ 10) // 6
            y = t12 % 97
            t13 = val * cnt // 3
            y = t13 * y & 255
        val = val + 1
    t14 = (y - 15) % 97
    t15 = (y ^ x) % 17
    t16 = (2 - y) % 4093
    y = fn1(t14, t15, t16)
    aux = 0
    while aux < 78:
        t17 = ((y ^ 19) >> 1) - y
        x = (t17 | x) & 32767
        if y * aux != 47:
            cnt = (y | 11) + cnt & 255
        else:
            y = (cnt ^ aux) % 9973
            t18 = cnt + y
            t19 = aux + x
            t20 = t18 * (cnt ^ 18)
            t21 = t19 ^ 9 + 19
            cnt = (t20 | t21) % 9973
        aux = aux + 1
    res = 0
    while res < 9:
        t22 = 9 + cnt + (cnt | y)
        x = (t22 >> 1) + x & 2047
        x = x // 7 & 262143
        res = res + 1
    p = y + y
    t23 = p // 8
    t = t23 ^ p - 13
    for e in range(5):
        t24 = (cnt // 8 >> 3) % 97 + t
        t = t24 & 131071
    t25 = p % 97 >> 1
    t26 = (t25 - (y + 5 ^ x)) % 97
    p = rec(92, t26)
    for prv in range(8):
        cnt = (y * x - prv) % 97
    t27 = t // 3 & 131071
    t28 = t * x | y
    t29 = (6 - cnt) // 2
    t30 = (t28 ^ t29) & 511
    t31 = (x - p - 7 * 16) % 4093
    x = fn0(t27, t30, t31)
    t32 = p - t + (t + t)
    t33 = t * p & x - 1
    t34 = t32 * t33 % 97
    t35 = y >> 4
    t36 = t35 + (t >> 4)
    t37 = (y ^ 3) * p
    t38 = (t37 + 14) % 9973
    cnt = fn1(t34, t36 & 255, t38)
    t39 = y * 6 + (16 ^ y)
    tmp = t39 | (17 ^ cnt) - t
    if cnt + 19 <= 25:
        t40 = cnt - 20 & 4095
        t41 = (16 ^ y) >> 4
        t42 = (t41 + 16) % 17
        t43 = (11 ^ p) & 4095
        tmp = fn1(t40, t42, t43)
    t44 = (tmp + t) * (cnt >> 2) | t
    d = t44 % 4093
    t45 = tmp * cnt - (p ^ tmp)
    t46 = t45 - ((p | d) & t)
    return t46 & 65535

if __name__ == "__main__":
    arg = 6
    expected = 4016
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
