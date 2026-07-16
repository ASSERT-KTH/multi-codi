# Auto-extracted from ds_lt256k_500.jsonl
# record_id=152  entry=f  input='4'  output='14'  tokens=178371

def f(x):
    t0 = x + x ^ x
    cur = t0 - 17
    hi = 0
    while hi < 319:
        x = ((cur >> 1) - hi) * cur & 2047
        hi = hi + 1
    p = x & 13
    t1 = 17 * x | x & p
    t2 = (p + p) * x * t1
    tot = t2 & 511
    v = 0
    while v < 12:
        if (16 << 4) + p != 21:
            t3 = (tot >> 1) + x
            x = t3 % 17
        else:
            cur = ((x | tot) - p | v) & 8191
            t4 = 3 + x << 3 << 4 ^ v
            tot = t4 & 2047
        v = v + 1
    y = cur & tot
    t5 = (cur - 17) // 5
    lo = t5 + y
    for m in range(2):
        tot = (p ^ cur ^ tot) & 1023
    for e in range(3):
        t6 = (x << 4) // 4
        x = t6 & 16383
        t7 = (x | p) * (e << 4)
        lo = t7 & 32767
        t8 = 7 * y
        t9 = 10 * cur + p
        t10 = t8 * (p & cur)
        t11 = (t9 | t10) ^ x
        x = t11 & 262143
    c = tot >> 1
    s = 15 * cur
    for nxt in range(11):
        if p & y != 1:
            t12 = (lo << 3) * 18
            t13 = t12 ^ (y ^ 18) % 17
            cur = (t13 ^ nxt) & 4095
        else:
            cur = ((s + tot) // 2 - cur) % 1009
    g = (x * x | s >> 3) % 1009
    aux = c - 17
    for idx in range(12):
        y = (aux ^ 7) + cur + y & 16383
        t14 = idx * lo
        t15 = t14 * (tot - s)
        s = t15 & 1023
    j = 0
    while j < 9:
        t16 = (18 << 4) * g
        t17 = t16 - (y >> 3 >> 3) - j
        cur = t17 & 511
        for res in range(10):
            t18 = aux - 17 ^ lo
            lo = t18 % 251
            tot = c + 5 + tot & 511
        t19 = y - 8
        t20 = t19 - y * x
        t21 = (t20 >> 4) + p
        p = t21 & 131071
        j = j + 1
    return ((3 | s) ^ c) & 2047

if __name__ == "__main__":
    arg = 4
    expected = 14
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
