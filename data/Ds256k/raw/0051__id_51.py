# Auto-extracted from ds_lt256k_500.jsonl
# record_id=51  entry=f  input='19'  output='5244'  tokens=193491

def rec(n, a):
    if n <= 0:
        return a
    t0 = a // 3 + a ^ n
    res = t0 % 251
    t1 = a + n ^ 13
    val = t1 & 8191
    t2 = n >> 1
    t3 = t2 + a // 2
    return rec(n - 1, t3 & 262143)

def fn0(a):
    tmp = [11, 37, 50, 46, 32]
    for val in range(12):
        t0 = tmp[val % 5] - 16
        a = (t0 + a) % 4093
        t1 = val - 13 + 3
        tmp[val % 5] = (t1 + a) % 97
    w = a * 16 & 511
    y = 0
    while y < 12:
        t2 = tmp[a % 5] | y
        w = (t2 - a // 2) % 4093
        for j in range(6):
            t3 = a - y - (w ^ j)
            t4 = (t3 + w * w * j) % 1009
            tmp[w % 5] = t4 % 97
            t5 = tmp[j % 5]
            t6 = (j | 18) + t5
            tmp[a % 5] = (t6 - a) % 97
            w = w & y
        y = y + 1
    return w & 18

def f(x):
    if x % 17 < 0:
        v = 0
        while v < 5:
            x = x % 17 + (x - v) & x
            t0 = 19 & x
            t1 = t0 + (v + v)
            x = t1 & 65535
            t2 = (7 | x) - v
            t3 = t2 - (x ^ 14) * 17
            x = t3 % 1009
            v = v + 1
        q = 0
        while q < 4:
            t4 = q * x ^ q - x
            x = t4 * q & 4095
            q = q + 1
    else:
        t5 = x + 5 | 8 & x
        t6 = (x + x) * x + t5
        x = t6 % 4093
    x = fn0((x | 4) & 16383)
    tot = x - 3 + x
    res = tot + tot >> 2
    for d in range(7):
        for y in range(8):
            t7 = tot - 6 + y
            x = t7 % 9973
            t8 = (tot | y) * (d * y)
            t9 = tot - x >> 4 ^ t8
            x = t9 & 255
    for val in range(11):
        res = (val - x | val) * tot % 4093
    for u in range(4):
        prv = 0
        while prv < 3:
            t10 = (prv | u) ^ u ^ res
            x = t10 & 511
            res = (1 ^ u | res) % 9973
            prv = prv + 1
    c = 0
    while c < 8:
        t11 = (12 - tot) * res + tot
        res = t11 & 131071
        res = tot - c & 511
        c = c + 1
    b = 0
    while b < 3:
        tot = (x - 7 - tot) % 9973
        b = b + 1
    t12 = (res | x) * res
    j = t12 & (tot ^ 11) % 4093
    if 6 + res == 54:
        t13 = (x + tot) % 1009
        tot = rec(97, t13)
        j = j - x
    for z in range(11):
        t14 = (16 + x) * res
        tot = (t14 ^ tot) % 9973
        if 6 | tot >= 24:
            j = tot + res + z & 1023
    tot = fn0(j // 4 & j + j)
    cnt = 0
    while cnt < 8:
        t15 = (res ^ x) >> 4
        t16 = (t15 << 2) - cnt
        j = t16 % 9973
        cnt = cnt + 1
    if 6 - x > 18:
        tot = (j ^ tot) >> 1
    else:
        t17 = 9 - 4
        t18 = t17 * (j + res)
        tot = t18 % 17
    hi = 0
    while hi < 14:
        t19 = hi * j - (j >> 4)
        tot = t19 & 8191
        x = ((x ^ tot) // 6 - x) % 9973
        hi = hi + 1
    g = tot * j % 4093
    t20 = x - res
    return t20 & x * g

if __name__ == "__main__":
    arg = 19
    expected = 5244
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
