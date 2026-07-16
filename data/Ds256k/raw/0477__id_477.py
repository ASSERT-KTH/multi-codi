# Auto-extracted from ds_lt256k_500.jsonl
# record_id=477  entry=f  input='9'  output='160'  tokens=217998

def fn0(a, b):
    if b * b > 32:
        if a // 3 != 37:
            b = 5 * a
            t0 = a * b | 5
            b = t0 % 251
        else:
            a = a | 11
        t1 = b * 10
        a = t1 & a * a
    else:
        a = (b * b - b ^ a) % 65521
    b = b + b + a % 251
    for g in range(7):
        if b // 6 <= 64:
            t2 = b % 65521 * (a ^ 2)
            a = ((b - a << 2) + t2) % 65521
            b = (b ^ a) % 65521
        else:
            b = b % 65521
            t3 = g * a | 7
            a = t3 * (7 ^ 15 | b) % 251
        if 5 - a > 38:
            t4 = g ^ 9 ^ a
            b = t4 % 251
            b = ((3 | b) // 4 | g) % 65521
        else:
            t5 = b // 8 << 2 << 4
            a = (t5 | a) & 4095
            a = a * g % 251
        t6 = g - 14 - 6
        t7 = (1 ^ g) * 19
        t8 = t6 + t7 + b
        b = t8 % 65521
    t9 = 18 + b & (a | 10)
    t10 = a // 5 - (10 + a)
    a = (t9 ^ t10) % 65521
    t11 = b * a << 2
    b = t11 & 255
    b = (b - 20) * b & 131071
    b = ((2 * 14 << 4) - a) % 65521
    return (a ^ b) % 251

def fn1(j, g, a):
    tot = [26, 91, 48, 47]
    prv = 0
    while prv < 12:
        t0 = j * tot[g % 4]
        t1 = (t0 + g // 6 >> 3) + prv
        a = t1 % 9973
        prv = prv + 1
    t2 = tot[a % 4] - g
    g = t2 ^ j + 20
    a = g - a
    a = (g | 4) * 1
    t3 = tot[j % 4] - a + g
    t4 = (5 ^ a) // 2
    t5 = (t4 << 1) % 9973
    a = fn0(t3 % 9973, t5)
    t6 = a * j // 5 ^ j
    return t6 & 511

def f(x):
    tmp = [177, 245, 243, 20, 120, 144]
    buf = x & 11
    if x - buf != 17:
        buf = x ^ 16
    t0 = tmp[buf % 6] * x
    t1 = buf - 5 | 6 - buf
    tmp[buf % 6] = (t0 & buf) * t1 % 251
    t2 = (tmp[buf % 6] | buf) // 3
    v = t2 << 4
    j = buf + v - (7 | 11)
    if buf - 6 < 33:
        t3 = tmp[x % 6]
        t4 = x & 12 & j
        t5 = (t3 ^ buf) >> 4
        v = t4 ^ t5
    else:
        if x ^ buf != 25:
            tmp[x % 6] = (buf - v + 20) % 251
            x = v & buf
        else:
            t6 = tmp[buf % 6]
            t7 = tmp[j % 6]
            t8 = x << 1
            buf = t8 ^ (t6 | t7)
            buf = tmp[buf % 6] | x
        buf = tmp[j % 6] - j
    idx = x & j
    for prv in range(534):
        j = v * x - prv & 1023
        t9 = 7 + 18 ^ prv | prv
        j = (t9 ^ v) % 1009
    if buf - v >= 34:
        if j << 1 > 42:
            t10 = v - x
            t11 = t10 + (buf << 3)
            x = t11 % 1009
            t12 = j // 2 + 20 - idx
            tmp[x % 6] = t12 % 251
        for u in range(2):
            t13 = 3 - 14 ^ 8 - u
            tmp[buf % 6] = t13 * j % 251
    else:
        t14 = idx - tmp[idx % 6]
        t15 = (t14 ^ (8 ^ idx)) + 1
        t16 = tmp[x % 6]
        t17 = idx ^ v
        t18 = t17 ^ t16 - x
        t19 = tmp[j % 6]
        t20 = t18 + t19 & 32767
        v = fn0(t15 % 251, t20)
        x = (x ^ v) // 5
    return (5 - j - x * 13) % 251

if __name__ == "__main__":
    arg = 9
    expected = 160
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
