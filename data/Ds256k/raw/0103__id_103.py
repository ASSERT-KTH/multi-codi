# Auto-extracted from ds_lt256k_500.jsonl
# record_id=103  entry=f  input='6'  output='0'  tokens=221210

def fn0(m, e, a):
    a = a + 18 << 3
    t0 = a * e
    t1 = t0 ^ (m | e)
    a = t1 << 1 & 262143
    for z in range(10):
        a = a - z + z & e
        t2 = e + e + z
        a = t2 & 131071
    t3 = (m & 15) - 9
    return t3 + 19 & 131071

def fn1(a):
    t0 = 6 & 4
    t1 = t0 | a & 4
    t2 = (t1 + a) % 17
    t3 = (a ^ 5) & 255
    t4 = a // 5 >> 1
    a = fn0(t2, t3, t4 & 2047)
    t5 = (a >> 3 ^ 20) & 32767
    t6 = a // 8 % 97
    t7 = a % 17 + a
    a = fn0(t5, t6, t7 % 251)
    m = 0
    while m < 6:
        a = (a | m) & 4095
        if a ^ m > 21:
            t8 = (m + a) * 10
            a = (t8 + (a + 19 >> 1)) % 97
        else:
            t9 = (m - 15 ^ 10) - m
            a = (t9 ^ a) & 8191
            t10 = m + m + m
            t11 = m * m | m
            t12 = t10 ^ t11 ^ a
            a = t12 & 4095
        m = m + 1
    p = a + 18 + (4 << 3)
    for g in range(2):
        t13 = (p & 7) - (g - p) ^ p
        p = t13 & 1023
    t14 = (p >> 2) + (p >> 2) - p
    return t14 & 32767

def f(x):
    p = [56, 32, 92, 64]
    s = 0
    while s < 33:
        cur = 0
        while cur < 9:
            t0 = (x & 13) * (s ^ cur)
            x = t0 & 32767
            t1 = s ^ 9 ^ x
            x = t1 % 97
            cur = cur + 1
        t2 = 16 * x - p[s % 4]
        x = (x + s - s) * t2 % 1009
        s = s + 1
    t3 = p[x % 4] * 20
    x = fn1((x // 2 - t3) % 97)
    if x * 19 >= 25:
        z = 0
        while z < 3:
            t4 = p[x % 4] | z
            x = t4 & 16383
            x = z & x
            z = z + 1
        t5 = p[x % 4] >> 4
        x = t5 - 9
    tmp = 0
    while tmp < 7:
        y = 0
        while y < 8:
            t6 = x - 8 - (5 + x)
            x = t6 % 1009
            t7 = x * tmp
            t8 = t7 - (y & 8)
            t9 = tmp * 7 << 4
            x = t8 * t9 & 16383
            y = y + 1
        for prv in range(7):
            p[prv % 4] = (x * x + 11 | prv) % 97
        if x >> 2 >= 41:
            t10 = p[tmp % 4] | tmp
            t11 = (t10 ^ 4) & tmp << 4
            x = (t11 ^ x) % 1009
            x = x & tmp
        else:
            x = (tmp * tmp ^ x) & 255
        tmp = tmp + 1
    for b in range(3):
        if b & 5 ^ x != 26:
            t12 = p[b % 4] + 18
            x = (x ^ b) + t12 & 1023
        else:
            x = (x >> 4) % 97
        t13 = p[x % 4]
        t14 = b - t13 - 1
        x = t14 & 65535
    t15 = p[x % 4]
    t16 = t15 + p[x % 4]
    t17 = p[x % 4] << 3
    t18 = 5 << 4 & x
    t19 = (t17 * 19 ^ t18) % 97
    t20 = p[x % 4] - x
    t21 = (x ^ 10) - t20
    t22 = t21 + p[x % 4]
    x = fn0(t16 % 97, t19, t22 % 97)
    p[x % 4] = (8 | x) % 97
    if x - p[x % 4] > 5:
        t23 = p[x % 4]
        x = (x & 5) - t23
        for val in range(12):
            t24 = (val + p[val % 4]) * val
            p[val % 4] = (t24 << 1 | x) % 97
    j = x // 6
    res = x - 10 | 6 - 20
    idx = x + j
    if j * p[x % 4] == 43:
        j = j - p[idx % 4] - x
        idx = idx + 6 - (17 ^ res)
    else:
        for t in range(12):
            t25 = (idx // 5 ^ 17) + j
            p[res % 4] = t25 % 97
            p[idx % 4] = ((7 ^ 8) + x) % 97
            x = (t * j + (idx ^ res)) % 1009
    t26 = (res << 2 & 18) * j
    return t26 % 97

if __name__ == "__main__":
    arg = 6
    expected = 0
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
