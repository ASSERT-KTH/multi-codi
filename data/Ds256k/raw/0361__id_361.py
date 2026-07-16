# Auto-extracted from ds_lt256k_500.jsonl
# record_id=361  entry=f  input='17'  output='865'  tokens=65285

def fn0(j, d, c):
    for acc in range(5):
        c = (3 + c) % 17
        d = (j - d) % 17
    lo = 12 - j
    t0 = c & 5 | lo
    t1 = (lo ^ c) * j
    d = t0 * t1 & 511
    c = (c - 17) * lo - lo & 65535
    t2 = (j // 5 & (j | lo)) - lo
    return t2 % 4093

def f(x):
    for s in range(11):
        x = (x * s >> 1 ^ s) % 17
    t0 = (x ^ 20) % 9973
    t1 = x | 14
    t2 = t1 ^ x % 17
    x = fn0(t0, t2 % 9973, x % 17)
    m = 0
    while m < 6:
        for idx in range(15):
            x = ((x ^ m) + idx) % 9973
        t3 = x // 3 + x
        x = t3 % 9973
        t4 = m + m | x
        x = t4 & 131071
        m = m + 1
    e = x | 16
    if 8 ^ e > 50:
        t5 = (x ^ 13) % 9973
        t6 = (x + e) % 9973
        t7 = (e ^ 17) & 65535
        e = fn0(t5, t6, t7)
        if 16 ^ e < 9:
            e = x % 17
        else:
            t8 = (5 - x) // 5
            t9 = (e - x) % 17
            t10 = (4 & x) + (e ^ 4) ^ x
            x = fn0(t8 & 131071, t9, t10 % 17)
    else:
        for val in range(7):
            x = (x - 6 - (x ^ 1)) % 9973
            t11 = e * e * (6 + e) + x
            e = t11 & 4095
            e = ((x ^ val) // 2 | 2) & 262143
        if x // 3 <= 41:
            t12 = e + x - (e | 11)
            t13 = e + x & 131071
            e = fn0(x % 17, t12 % 17, t13)
        else:
            t14 = x * 16
            t15 = t14 * (e >> 2)
            t16 = (e ^ 19) % 17
            t17 = ((18 | 17) ^ e) % 9973
            x = fn0(t15 & 255, t16, t17)
            t18 = e // 5 - x
            t19 = x * e * x
            t20 = t19 | (e >> 1) - x
            t21 = (x >> 3) * (e - x)
            t22 = t21 + (x * 9 - x) & 511
            e = fn0(t18 % 9973, t20 % 9973, t22)
    t23 = (e & 19) + x & 8191
    t24 = x // 8 % 17
    t25 = x // 8 - e
    x = fn0(t23, t24, t25 % 17)
    t26 = (x + e) * x
    t27 = t26 + x & 262143
    t28 = x * x
    t29 = t28 - (e + x)
    t30 = e // 3 - 2 & 262143
    e = fn0(t27, t29 & 255, t30)
    t31 = (9 & 7) * e | e
    lo = t31 & 2047
    t32 = e ^ x
    t33 = t32 | e * lo
    nxt = t33 % 9973
    t34 = lo * lo >> 4
    t35 = t34 & nxt * 17 + x
    t36 = (x | nxt) % 17
    t37 = nxt * nxt & 19 - 16
    t38 = t37 + (lo + nxt - lo)
    x = fn0(t35, t36, t38 % 9973)
    t39 = e << 4
    t40 = t39 * (nxt + e)
    d = t40 >> 3 & 4095
    for q in range(4):
        d = (d >> 1) % 9973
        for cur in range(2):
            t41 = (q - e) * (x - q)
            lo = t41 * 20 + lo & 8191
            d = (19 ^ e) + d & 2047
            t42 = cur * 9 & q * e
            t43 = t42 - ((cur ^ e) - (9 - d))
            lo = t43 & 255
        t44 = (lo | 9) ^ 20 - lo ^ q
        d = t44 % 17
    tmp = 0
    while tmp < 9:
        nxt = 20 & e & (nxt | 15)
        t45 = lo - nxt + 12
        nxt = t45 % 9973
        tmp = tmp + 1
    v = nxt * lo & nxt
    p = v + d
    return (v | e) % 9973

if __name__ == "__main__":
    arg = 17
    expected = 865
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
