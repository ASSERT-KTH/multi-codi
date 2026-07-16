# Auto-extracted from ds_lt256k_500.jsonl
# record_id=215  entry=f  input='17'  output='3'  tokens=255984

def rec(n, a):
    if n <= 0:
        return a
    cur = a * 18 * (n + 11) % 9973
    cur = (n // 4 - cur) % 251
    t0 = 8 - a + cur * 16
    t1 = (18 & 17) - (cur + cur)
    t2 = t0 - t1 & 2047
    return rec(n - 1, t2)

def fn0(m, g, a):
    prv = [25, 111, 1, 186, 49, 4, 250]
    s = a & g
    buf = 14 * m
    d = 10 * m - 16
    buf = (m * d << 2) % 9973
    t0 = prv[g % 7]
    s = t0 & prv[m % 7]
    t1 = (m + s) * 5
    a = (t1 ^ (3 - g) // 6) % 4093
    if m // 5 > 47:
        cnt = 0
        while cnt < 3:
            t2 = m - s - prv[g % 7]
            t3 = cnt * 19 + prv[g % 7]
            m = (t2 + t3) % 9973
            cnt = cnt + 1
    else:
        if 12 * d <= 9:
            s = 13 - a
            t4 = buf // 6 // 5
            buf = rec(117, t4 & 262143)
    t5 = prv[s % 7] ^ g
    return t5 % 9973

def fn1(m, a, b):
    for p in range(11):
        t0 = (p ^ b) + p >> 4
        m = t0 & 16383
        b = p + p + a & 1023
    for e in range(5):
        for buf in range(8):
            b = ((2 | buf) ^ a) & 262143
            a = buf & a
        b = (e & 16 | m) % 97
        t1 = a - 14 - e
        b = t1 & 511
    if 4 + b >= 0:
        a = b & 1
        t = 0
        while t < 11:
            t2 = m * 19 << 1
            b = t2 + t & 8191
            t3 = m >> 3 | b
            b = t3 % 97
            t4 = 5 * m >> 1
            t5 = (m >> 2) // 4
            m = (t4 ^ t5) % 97
            t = t + 1
    else:
        b = b ^ a
        a = 17 ^ a ^ m
    t6 = (a + b ^ b << 3) % 97
    b = rec(49, t6)
    d = m ^ 11
    t7 = 12 * b * a * d
    return t7 % 97

def f(x):
    t0 = 11 ^ x ^ 9 & x
    p = t0 ^ 13 - x - x
    t1 = (p - 3) * (p >> 1)
    t2 = (t1 ^ x) & 16383
    t3 = p * p << 2
    t4 = t3 & (20 & 2)
    t5 = p * x % 4093
    p = fn0(t2, t4, t5)
    s = x * 16
    if 16 | s > 14:
        p = x * 20
        x = (p ^ x) + 20
    d = s ^ p
    t6 = p ^ 4 | p * p
    aux = t6 & s
    for t in range(8):
        t7 = x * s >> 4
        t8 = t7 % 9973 - t
        d = t8 % 17
    for g in range(6):
        t9 = s - aux + (aux ^ 9)
        t10 = (aux // 4 & t9) - d
        d = t10 & 2047
        for m in range(12):
            p = ((s | aux) ^ p - d) & 65535
            t11 = m * aux
            t12 = t11 & (x & p)
            p = (t12 >> 1) % 4093
    t13 = (aux >> 2) - p & 131071
    t14 = 13 - x & 16383
    t15 = (s ^ 1 | x) & 131071
    p = fn0(t13, t14, t15)
    for y in range(147):
        t16 = (d ^ y ^ x & d) + y
        p = t16 % 4093
    res = s * x % 4093
    t17 = ((s + aux) // 6 + p) % 9973
    t18 = x - res + res & 255
    t19 = (res // 2 // 5 - 4) % 4093
    s = fn0(t17, t18, t19)
    t20 = d + d & aux
    t21 = d // 6
    t22 = t21 * (s - res)
    t23 = (res >> 3) - aux + x
    aux = fn1(t20, t22 % 9973, t23 & 1023)
    for a in range(3):
        p = (d >> 4) + p & 262143
        t24 = res * s + aux | x
        aux = t24 % 17
    for q in range(2):
        if d - 2 != 3:
            t25 = 3 * d * 7
            t26 = q * aux * s
            x = (t25 - t26) % 17
            t27 = p // 5 ^ p
            t28 = t27 << 4 | s
            s = t28 % 4093
        t29 = s + 17 - (d ^ 10) | res
        p = (t29 | p) & 8191
        x = (d + q) % 4093
    w = 17 + aux ^ res
    nxt = 0
    while nxt < 4:
        res = (nxt ^ 17 ^ p) % 9973
        for val in range(7):
            t30 = nxt - 18 & (x ^ p)
            aux = t30 - aux & 1023
            t31 = aux ^ d ^ val
            w = t31 & 4095
            t32 = 1 - nxt & s
            d = (t32 | d) & 8191
        nxt = nxt + 1
    t33 = 12 + 10 | s >> 4
    t34 = (14 - res) * (d | 19)
    c = t33 - t34 & 1023
    if p * d < 48:
        t35 = (p * s - w ^ s) & 1023
        t36 = 12 + 17
        t37 = t36 & w >> 1
        t38 = w * aux & 17 * 13
        w = fn1(t35, t37, t38)
    return (p << 4) % 17

if __name__ == "__main__":
    arg = 17
    expected = 3
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
