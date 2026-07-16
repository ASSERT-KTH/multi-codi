# Auto-extracted from ds_lt256k_500.jsonl
# record_id=67  entry=f  input='5'  output='4067'  tokens=142631

def fn0(g, e, a):
    c = (e & a) // 3 // 6
    for cur in range(7):
        t0 = a << 4
        t1 = e * 2 ^ cur
        t2 = t0 & (14 & e)
        e = (t1 ^ t2) % 9973
    prv = (c << 4 & a) - a
    if (5 << 1) + c >= 58:
        if 7 + e <= 36:
            g = (g ^ e) // 2 + c
    else:
        g = e // 6
    for s in range(2):
        prv = (10 + prv) * a % 17
        t3 = 20 * a ^ a ^ e
        e = t3 & 262143
        t4 = c + 6 + a | 18
        e = (t4 + e) % 97
    t5 = ((prv ^ g) - g) * prv
    return t5 % 9973

def fn1(d, c, b):
    for idx in range(8):
        for w in range(10):
            t0 = w * c // 3 << 2
            c = t0 % 97
            b = ((idx << 2) - c - b) % 251
            t1 = (d + 3) // 4
            d = t1 & 32767
        d = (c | idx) * c & 1023
        for hi in range(7):
            t2 = 7 + 15 ^ 5 + 19 ^ d
            d = t2 % 97
    val = (c * b | 11) % 251
    t3 = c - d - (d << 4)
    aux = t3 * c % 251
    aux = b ^ 14
    t4 = (d >> 3) // 2
    t5 = (10 - b) % 97
    val = t4 & t5
    return d - b + aux & 131071

def f(x):
    t0 = x * x % 9973
    t1 = x - 17 & 1023
    t2 = (x ^ 16) & 8191
    x = fn0(t0, t1, t2)
    t3 = x - 17 - x
    aux = t3 * (18 - x ^ x) & 511
    if aux + aux != 16:
        t4 = x & aux
        t5 = t4 | aux // 5
        t6 = (t5 ^ x) % 251
        t7 = ((aux // 4 ^ aux) >> 4) % 9973
        t8 = 3 * aux % 1009
        x = fn0(t6, t7, t8)
        if aux - 3 == 2:
            t9 = 7 * aux & 511
            t10 = aux + aux >> 2 & 511
            t11 = aux >> 3
            t12 = t11 + (x >> 1)
            t13 = (t12 - x) % 4093
            x = fn1(t9, t10, t13)
        else:
            t14 = aux - 15 & 16383
            t15 = (4 * 9 - aux) % 4093
            x = fn0(aux & x, t14, t15)
            t16 = 6 + x & aux
            t17 = aux | 8
            t18 = t17 * (3 & x)
            t19 = t18 * aux & 65535
            x = fn0(t16, x % 4093, t19)
    else:
        aux = aux * x & 4095
    t20 = aux >> 3 | x
    t21 = (x | aux) >> 3
    t22 = (t21 ^ 6) % 1009
    t23 = x * x ^ x & 20
    t24 = (x ^ 18 | 7) & t23
    x = fn1(t20 & 16383, t22, t24)
    t25 = aux * aux | 2 * 14
    t26 = (x ^ 8) % 1009
    t27 = (x ^ 6) + aux
    x = fn0(t25 % 251, t26, t27 & 131071)
    hi = 18 ^ x
    c = hi // 7
    for cur in range(3):
        tmp = 0
        while tmp < 3:
            t28 = c + c + (aux ^ 14)
            c = t28 + aux & 65535
            tmp = tmp + 1
        nxt = 0
        while nxt < 16:
            t29 = x & aux
            t30 = t29 - (nxt << 2)
            aux = t30 % 1009
            aux = (aux - hi) * (4 * x) % 4093
            nxt = nxt + 1
    return ((x ^ 8) - hi) % 4093

if __name__ == "__main__":
    arg = 5
    expected = 4067
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
