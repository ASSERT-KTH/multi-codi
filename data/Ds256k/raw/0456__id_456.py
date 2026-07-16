# Auto-extracted from ds_lt256k_500.jsonl
# record_id=456  entry=f  input='5'  output='31'  tokens=225790

def rec(n, a):
    if n <= 0:
        return a
    t0 = a - n
    t1 = t0 ^ a & 9
    a = t1 % 17
    t2 = 1 * 4 * 15
    t3 = t2 ^ n ^ a
    return rec(n - 1, t3 & 65535)

def fn0(b, m):
    tmp = [460, 644, 735, 883]
    if m << 2 < 41:
        t0 = tmp[m % 4]
        t1 = m % 65521
        t2 = tmp[b % 4]
        t3 = t1 + (b ^ t0)
        t4 = m * t2 // 8
        b = t3 * t4 % 97
        q = 0
        while q < 4:
            t5 = tmp[b % 4]
            t6 = tmp[b % 4]
            t7 = b ^ t5
            t8 = t7 & t6 - 9
            m = t8 - m & 4095
            q = q + 1
    val = b * tmp[b % 4] & m
    t9 = tmp[m % 4]
    tmp[b % 4] = val * m + t9 & 255
    t10 = b + val
    t11 = t10 * (val * 12)
    b = t11 % 65521
    for lo in range(3):
        t12 = m ^ val
        t13 = t12 | 3 - m
        b = (t13 + b) % 97
    return (m // 3 | val) % 97

def fn1(g, b, e):
    t0 = e * 2 % 4093
    idx = t0 & e
    t1 = e >> 2 & g
    e = rec(61, t1)
    t2 = (5 + b) % 17
    t3 = (e << 3) - (b | idx)
    b = fn0(t2, t3 & 65535)
    if 11 + g < 43:
        if g >> 4 == 64:
            t4 = ((idx ^ 18) * idx >> 1) % 4093
            t5 = (6 * e << 3) % 4093
            g = fn0(t4, t5)
        else:
            t6 = (b + idx >> 2 | 19) % 4093
            g = rec(115, t6)
            t7 = (e - 15) % 4093
            t8 = (20 - b) * (b & idx)
            g = fn0(t7, t8 % 17)
    idx = 14 | idx
    if 13 - e != 37:
        a = 0
        while a < 8:
            idx = (idx + g) * e % 17
            t9 = (e ^ g) % 4093 + a
            b = t9 % 4093
            t10 = idx * 10 | e // 2
            e = (t10 << 2) % 4093
            a = a + 1
    else:
        if b - 20 == 20:
            b = (idx ^ b) // 8
        else:
            t11 = b >> 1
            t12 = t11 ^ e + b
            t13 = (g | 10) ^ 8
            t14 = (t12 | t13) % 4093
            t15 = (g ^ 2) // 3
            b = fn0(t14, t15 & 511)
        for p in range(2):
            t16 = g + b ^ g - 10 | b
            idx = t16 - idx & 131071
    return (19 + g | idx) % 17

def f(x):
    t0 = x + x + (x ^ 16)
    t1 = (x + x) * t0 % 65521
    t2 = x & 7 & x
    t3 = (x + x) % 97
    x = fn1(t1, t2, t3)
    cnt = x - 18
    for v in range(19):
        tot = 0
        while tot < 10:
            x = tot & x
            t4 = cnt + x ^ 7
            cnt = t4 % 65521
            tot = tot + 1
        for prv in range(6):
            t5 = x & 10
            t6 = t5 - (x & cnt)
            x = t6 & 4095
            cnt = ((cnt - v >> 2) - v) % 97
            t7 = prv - v - 11 - x
            x = t7 & 2047
        if cnt * cnt >= 15:
            cnt = (v - 8 | cnt) % 97
        else:
            t8 = (x ^ 5) // 7
            cnt = (t8 ^ v) % 65521
    t9 = x - 7
    t10 = t9 - (x ^ 5)
    t11 = (cnt ^ 17) * (cnt >> 4)
    t12 = (t11 - x) % 97
    x = fn1(t10 & 4095, t12, x & 11)
    t13 = (cnt >> 1) + 10 - 16
    return t13 & 32767

if __name__ == "__main__":
    arg = 5
    expected = 31
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
