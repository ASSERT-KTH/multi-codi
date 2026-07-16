# Auto-extracted from ds_lt256k_500.jsonl
# record_id=107  entry=f  input='20'  output='15'  tokens=13319

def fn0(j, g, e):
    if 12 | j == 4:
        e = (4 | e) + (e >> 2)
        j = (j ^ 14) - j
    else:
        g = j + 13 | e
    for val in range(5):
        t0 = (13 + e >> 3) * j
        j = t0 % 65521
    idx = 0
    while idx < 9:
        t1 = e % 97 ^ j * e
        e = t1 & 4095
        j = (j - 7 >> 2) % 97
        idx = idx + 1
    t2 = (j ^ 2) // 2
    u = t2 + j
    return 7 - e + u & 511

def fn1(c, a, e):
    y = [42, 711, 387, 888]
    cnt = 0
    while cnt < 5:
        t0 = (c | cnt) * c
        y[e % 4] = t0 * ((3 & cnt) * e) % 1009
        if c // 5 != 62:
            t1 = 8 * cnt
            t2 = t1 + (1 + e)
            e = t2 % 1009
            c = (a ^ cnt) & (cnt ^ 5)
        else:
            t3 = a << 2 >> 4
            y[e % 4] = t3 % 1009
        for g in range(9):
            y[g % 4] = (a + e | 17) % 1009
        cnt = cnt + 1
    t4 = y[c % 4]
    idx = t4 >> 2
    if e * idx < 7:
        t5 = ((a & 19) - a) % 1009
        t6 = (a >> 3) % 97
        t7 = y[c % 4] + 7
        t8 = t7 * (idx - 12) % 97
        a = fn0(t5, t6, t8)
    t = (c * 9 ^ a) & 2047
    y[t % 4] = (idx // 7 << 4) % 1009
    y[c % 4] = (2 - c) % 1009
    t9 = idx * 7 ^ t + 14
    c = t9 << 3
    t10 = (idx + a) // 7
    t11 = (t10 | c) % 1009
    t12 = (e & t) // 8
    t13 = t12 - 19 & 32767
    t14 = y[e % 4] + idx
    t15 = 18 + t + t14 & 255
    e = fn0(t11, t13, t15)
    t16 = y[e % 4] ^ 5
    t17 = t16 // 7 + c | idx
    return t17 % 97

def f(x):
    for a in range(142):
        x = ((a | 3) + x) % 17
    if x + x >= 2:
        t0 = (x + x) * x
        x = t0 ^ x
        t1 = (x | 7) ^ x - 9
        t2 = t1 << 4 & 65535
        t3 = (x ^ 16) & 4095
        t4 = 18 + 3 | x
        x = fn0(t2, t3, t4 & 262143)
    else:
        for t in range(11):
            x = (t ^ x) & 8191
            t5 = x >> 3 ^ t
            x = (t5 - (13 + 6 ^ t)) % 17
    t6 = x % 65521
    t7 = t6 ^ x // 7
    t8 = (12 & 9) - x
    j = t7 + t8
    j = 2 + j | x
    t9 = (x ^ 4) // 5 * x - j
    return t9 % 17

if __name__ == "__main__":
    arg = 20
    expected = 15
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
