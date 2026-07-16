# Auto-extracted from ds_lt256k_500.jsonl
# record_id=475  entry=f  input='14'  output='12'  tokens=165079

def fn0(c, j):
    t0 = c // 8 - (1 - c)
    res = t0 * c & 1023
    c = j * res % 251
    c = c | j
    j = 6 ^ j | 8
    if res * res < 14:
        c = (c ^ j) // 7
    else:
        for t in range(9):
            c = (20 * res ^ c) % 9973
            c = ((13 + j) // 4 - c) % 251
    j = res * res + (j >> 1) >> 1
    cnt = 0
    while cnt < 4:
        t1 = (c | res) - 7
        res = t1 & 16383
        cnt = cnt + 1
    for idx in range(4):
        t2 = j >> 4 ^ c
        c = t2 & 2047
        t3 = (8 + j) // 6
        j = t3 & 262143
    return ((j >> 2) // 7 - res) % 251

def fn1(j):
    idx = j + j
    idx = idx + j - (7 | j)
    y = 0
    while y < 3:
        t0 = j // 6 + (j ^ 17)
        idx = t0 * idx % 17
        t1 = (13 - j) % 17
        idx = (t1 - y) % 1009
        j = (j - idx) % 1009
        y = y + 1
    t2 = (j - 17) * idx // 6
    j = t2 % 1009
    j = (j - 4) * 4
    if 13 << 1 | j == 13:
        if 15 - 6 | idx == 16:
            idx = (idx << 2) * (j // 8) % 1009
    j = (j ^ idx) << 4 >> 4
    return idx + j & 131071

def f(x):
    d = [133, 9, 244, 30, 206, 248, 63, 0]
    for cur in range(18):
        acc = 0
        while acc < 11:
            x = (7 | x) & (x ^ 9)
            d[cur % 8] = 11 * acc + x
            t0 = (cur - 18) % 17 ^ x
            x = t0 % 17
            acc = acc + 1
        for buf in range(4):
            x = (17 | x) & 1023
            x = 9 & x
        for v in range(2):
            t1 = v | x
            t2 = t1 * (x ^ 11)
            t3 = (cur << 2) * cur
            x = t2 - t3 & 1023
            t4 = (13 ^ 9) & 9
            x = (t4 - x) % 17
    t5 = d[x % 8]
    t6 = 11 * x
    t7 = x & 6
    t8 = t6 ^ t5 + 17
    t9 = t7 & x >> 1
    d[x % 8] = (t8 - t9) % 251
    t10 = d[x % 8]
    t11 = 3 ^ x
    t12 = (x << 1) % 17
    t13 = t11 | t10 ^ x
    s = t12 * t13
    for idx in range(9):
        t14 = (s + s & s) + x
        x = t14 & 2047
    t15 = d[x % 8]
    t16 = (15 + s) * t15 + 15
    t17 = x >> 1 >> 4
    t18 = t17 * x & 65535
    s = fn0(t16 & 262143, t18)
    t19 = s - 8 + (s >> 1)
    t20 = t19 | s // 4 * (9 | x)
    lo = t20 & 8191
    for b in range(9):
        t21 = d[b % 8]
        t22 = t21 << 3 | s
        t23 = x * 5 << 1
        lo = (t22 - t23) % 251
        t24 = (b | x) >> 2
        lo = t24 * x & 131071
    t25 = (18 ^ x) >> 4 >> 2
    s = fn1(t25 % 17)
    t26 = x + d[lo % 8]
    return (x ^ s ^ t26) % 17

if __name__ == "__main__":
    arg = 14
    expected = 12
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
