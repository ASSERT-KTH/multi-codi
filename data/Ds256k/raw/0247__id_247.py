# Auto-extracted from ds_lt256k_500.jsonl
# record_id=247  entry=f  input='20'  output='27'  tokens=215453

def rec(n, a):
    if n <= 0:
        return a
    for buf in range(10):
        res = 0
        while res < 9:
            t0 = 7 + a
            t1 = t0 ^ n - buf
            a = t1 & 511
            a = n * a & 131071
            t2 = n + a + res
            a = t2 * (18 & (6 & buf)) % 251
            res = res + 1
        t3 = buf - 20
        t4 = t3 - 7 * 3
        t5 = (t4 | 10) - a
        a = t5 & 262143
    t6 = (a - 1) // 8 * n
    return rec(n - 1, t6 & 8191)

def f(x):
    for cur in range(4):
        if 9 * cur + x > 16:
            t0 = cur * x + 4
            x = t0 & 16383
            t1 = x ^ 2 ^ x
            x = t1 % 17
        else:
            x = (18 | cur | x) % 17
        u = 0
        while u < 7:
            t2 = ((u | 18) << 2) - x
            x = t2 % 17
            x = (cur * cur + x) % 17
            t3 = cur * 16 | u + u
            t4 = 9 * u - x // 4
            x = (t3 | t4) % 251
            u = u + 1
        t5 = x * x
        t6 = t5 - x * 4
        x = t6 & 4095
    if x - 10 >= 55:
        if x * x != 19:
            t7 = x - 8 & x + x
            x = t7 | (x ^ 9) - (x >> 1)
        for y in range(7):
            x = (y - x) % 251
            t8 = y + 7 | y
            x = (t8 | x) % 251
    for g in range(8):
        x = g + x & 511
    for idx in range(841):
        if 18 ^ x >= 39:
            t9 = x * idx & idx + idx
            t10 = x * idx >> 1 | t9
            x = t10 & 8191
    for aux in range(4):
        x = (x << 1) + 16 - 11 & 262143
    t11 = 20 + x & x
    cnt = t11 ^ 5
    t12 = x - cnt + cnt
    tot = t12 - cnt * x % 65521
    if tot + 8 == 51:
        t13 = (tot ^ 20) + cnt
        tot = t13 * (x ^ 20 ^ x) % 97
        t14 = (11 & 8) * tot | tot
        x = t14 & 8191
    t15 = 10 + x ^ cnt
    return t15 & 255

if __name__ == "__main__":
    arg = 20
    expected = 27
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
