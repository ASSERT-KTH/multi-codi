# Auto-extracted from ds_lt256k_500.jsonl
# record_id=450  entry=f  input='10'  output='41'  tokens=226439

def rec(n, a):
    if n <= 0:
        return a
    a = (a - n) % 17
    a = (n ^ a) + (n ^ 8) & 131071
    t0 = ((1 ^ n) - a) % 17
    return rec(n - 1, t0)

def fn0(j, a, b):
    if a // 3 <= 2:
        t0 = j - b
        t1 = (a ^ 7) * j
        t2 = t0 * (j * a)
        b = t1 * t2 & 65535
    else:
        t3 = j - b ^ j * a
        t4 = t3 ^ (a // 5 | 4)
        a = t4 % 17
        if j // 5 < 8:
            t5 = (b | 1) & 131071
            j = rec(46, t5)
            b = (3 ^ 11) + a
    a = j % 9973
    if 4 * b >= 51:
        for w in range(7):
            t6 = a * 19 ^ j
            j = t6 % 65521
            a = b * w - 7 - 4 & 65535
            t7 = b << 2 | w << 4
            j = t7 & 32767
        t8 = j + j ^ b
        a = t8 & 14
    else:
        b = j - 3 - 5
    t9 = (9 + b) // 6
    t10 = b - 16 + a
    b = t9 + t10
    p = 0
    while p < 5:
        t11 = 12 * p * 19
        t12 = t11 // 4 + j
        a = t12 & 131071
        t13 = 11 * b ^ p
        a = t13 % 97
        p = p + 1
    t14 = a + b - j
    b = t14 - (2 + b << 1)
    j = 3 & b
    return j // 2 % 65521

def f(x):
    if x + x < 40:
        for j in range(9):
            x = (j ^ 4 | x) % 4093
            x = j + j + 7 - x & 1023
            x = (14 ^ j | x) % 65521
        t0 = x * 2 - x
        t1 = t0 * 18 % 97
        t2 = (x - 12) // 4 ^ x
        t3 = x * x % 4093
        x = fn0(t1, t2 % 4093, t3)
    else:
        t4 = (x // 2 | 16) % 65521
        t5 = x + x & 255
        x = fn0(t4, t5, x & 3)
    t6 = x * x
    t7 = t6 * (x ^ 18)
    hi = (t7 - x) % 4093
    prv = hi - x >> 4 ^ x
    if 17 - prv == 23:
        if prv ^ 17 <= 9:
            prv = x & hi | x
            t8 = prv % 97
            t9 = t8 | prv ^ 7
            prv = t9 ^ hi
        else:
            x = hi // 7
            t10 = (hi & x) >> 4
            t11 = (t10 + 15) % 65521
            t12 = x // 2 * hi % 97
            t13 = hi ^ 20 | 19
            t14 = t13 // 4 % 97
            x = fn0(t11, t12, t14)
        t15 = hi << 3 | 17
        prv = t15 + hi
    s = 1 * x + 7 - hi
    for val in range(10):
        for nxt in range(3):
            t16 = (nxt - x) // 8
            hi = t16 & 255
        for g in range(46):
            prv = (prv ^ hi) % 1009
        for cur in range(9):
            t17 = 10 * hi - hi | s
            s = t17 % 1009
            x = (prv - x) % 97
            t18 = (x | cur) + cur ^ cur
            prv = t18 % 65521
    if prv >> 3 > 60:
        tot = 0
        while tot < 5:
            s = (hi >> 2) + tot & 1023
            hi = ((17 | 9) + s ^ tot) & 65535
            tot = tot + 1
        t19 = x * s % 1009
        s = rec(119, t19)
    else:
        if 7 * s == 50:
            x = (prv ^ hi) // 3 & 1023
    t20 = (prv ^ hi) & 65535
    hi = rec(119, t20)
    for p in range(4):
        t21 = s >> 4 ^ p
        x = t21 & 65535
        hi = ((9 ^ hi) + prv) % 1009
    aux = 10 + hi & s
    cnt = prv // 8 * aux % 65521
    v = (prv // 7 ^ s + 2) % 65521
    return ((17 + s) * cnt << 2) % 97

if __name__ == "__main__":
    arg = 10
    expected = 41
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
