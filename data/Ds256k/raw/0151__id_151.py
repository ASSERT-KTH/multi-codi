# Auto-extracted from ds_lt256k_500.jsonl
# record_id=151  entry=f  input='16'  output='1002'  tokens=192766

def rec(n, a):
    if n <= 0:
        return a
    if 10 - a == 50:
        a = a - n & 4095
    else:
        a = (n - 20 + a) % 1009
        a = a + 19 & 511
    a = (10 | 15) * a & 16383
    a = ((n | 3) ^ a) % 1009
    t0 = a | 12
    t1 = t0 * (5 & a)
    return rec(n - 1, t1 % 97)

def fn0(e, a, b):
    for tmp in range(8):
        a = ((e ^ b) - a) % 17
    t0 = (a & 14) - (b - e)
    v = t0 << 2
    res = (v + v) % 251
    for prv in range(8):
        cur = 0
        while cur < 6:
            t1 = b + a & 2 ^ v
            v = t1 & 511
            res = (v - a << 1) * res & 131071
            cur = cur + 1
        res = (res + b) % 251
        if a << 2 <= 3:
            v = (v ^ res) % 17
            e = e * a * e % 251
        else:
            t2 = ((e ^ 12) >> 4) + a | b
            b = t2 % 251
    s = 0
    while s < 9:
        b = ((s << 2) - res) % 251
        acc = 0
        while acc < 3:
            t3 = 14 + res | v
            v = t3 % 9973
            t4 = (a >> 3) - res - v
            v = t4 & 511
            res = v - res & 1023
            acc = acc + 1
        e = (s ^ 5) - (res + 4) & 65535
        s = s + 1
    t5 = v * res - (19 | v)
    e = t5 & 2047
    if e + a <= 34:
        t6 = (e - a) * (17 + res)
        a = (t6 | (a ^ res) // 5) & 32767
    else:
        t7 = (a ^ e) * 1
        t8 = (b & e) % 65521
        res = t7 + t8
    for p in range(4):
        if res + res == 35:
            a = (b | e) + p & 1023
        for g in range(11):
            t9 = (e & b) + (11 + g)
            t10 = (e - a - g) * t9
            a = t10 & 8191
            t11 = e * a + g
            res = t11 & 131071
            res = (a * e + g) % 65521
    t12 = b & 1
    t13 = t12 * (a * res)
    return t13 % 17

def f(x):
    j = 0
    while j < 10:
        x = j & x
        j = j + 1
    t0 = (x ^ 17) + x
    t1 = t0 - (x * x & 1)
    x = rec(96, t1 & 16383)
    p = 14 + x + x
    tmp = 3 * 14 - x
    if tmp // 2 == 35:
        p = (tmp << 3 ^ 9) >> 4
        tmp = tmp | x
    cnt = tmp % 251
    for v in range(845):
        t2 = p * 3 ^ cnt
        cnt = t2 % 251
    t3 = (x | 2) + cnt
    m = t3 & cnt
    return (m - 7 | 9) % 1009

if __name__ == "__main__":
    arg = 16
    expected = 1002
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
