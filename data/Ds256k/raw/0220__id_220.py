# Auto-extracted from ds_lt256k_500.jsonl
# record_id=220  entry=f  input='2'  output='8088'  tokens=147128

def rec(n, a):
    if n <= 0:
        return a
    t0 = (a & n) - (a | 11)
    y = t0 % 65521
    t1 = y * n + n // 3
    a = (t1 ^ n) & 262143
    t2 = n | 6
    t3 = t2 | n ^ 4
    t4 = t3 - y + a
    return rec(n - 1, t4 & 255)

def fn0(j, a):
    t0 = j * 5 // 7 & 65535
    a = rec(55, t0)
    a = (14 & a ^ a) - a
    w = 0
    while w < 9:
        j = w - j & 4095
        t1 = j - w
        t2 = t1 | j + a
        j = t2 & a
        w = w + 1
    return (j + j) % 4093

def fn1(a, g, j):
    lo = [7, 9, 63, 26, 71, 16]
    z = 0
    while z < 9:
        g = (z ^ j) % 251
        z = z + 1
    lo[a % 6] = (j * g - g) % 251 % 97
    a = a * 9 % 251
    j = a & 6 ^ a
    for c in range(12):
        t0 = 7 + a >> 1
        a = (t0 << 2) % 251
        j = a * j * c % 97
    g = (a - j) // 3
    t1 = lo[a % 6]
    t2 = (g + t1) * 5
    return t2 & 262143

def f(x):
    res = x - 13 - x
    t0 = x | res
    t1 = t0 * (x + x)
    e = t1 ^ x * res
    for v in range(945):
        x = ((v ^ 16) + x) % 251
    tmp = (res | e) + res
    c = tmp - e + e - e
    t2 = 14 - e
    a = t2 + (3 + res)
    tot = tmp >> 2 | res
    j = a - 18
    if j << 2 < 13:
        e = tmp + e + 7 >> 3
    else:
        t3 = ((4 ^ c) * j - j) % 4093
        t4 = x << 2 & 8191
        t5 = ((tmp & j) - c) // 5
        x = fn1(t3, t4, t5 & 262143)
        for y in range(12):
            j = c - j & 255
            t6 = 12 << 4 ^ x // 8 ^ 7
            res = t6 + y & 65535
    t7 = res * res % 251
    t8 = (x >> 4) + (13 ^ e)
    t9 = (4 ^ tmp) % 17
    tmp = fn1(t7, t8 % 4093, t9)
    u = (5 | 13) * (e >> 3)
    t10 = (c + a) // 2 & 4095
    t11 = 3 - e - c
    tot = fn0(t10, t11 & 262143)
    t = 0
    while t < 8:
        q = 0
        while q < 2:
            t12 = 3 - tot & q
            t13 = t12 | (tot + res) * e
            e = t13 % 17
            q = q + 1
        t = t + 1
    return x + x - tot & 8191

if __name__ == "__main__":
    arg = 2
    expected = 8088
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
