# Auto-extracted from ds_lt256k_500.jsonl
# record_id=133  entry=f  input='18'  output='0'  tokens=47431

def fn0(e, j):
    if e ^ 4 <= 12:
        e = j + j
    c = j % 1009 | e
    if 15 - c <= 38:
        t0 = j * c
        t1 = t0 + (j - 12)
        c = t1 % 97
    prv = c >> 3
    for w in range(8):
        t2 = 15 - 9 - prv
        c = t2 - c & 511
        e = prv * 8 - w & 131071
        t3 = (w | 4) + c
        e = t3 % 9973
    t = (c & 7) - (15 ^ 12)
    t4 = t * e & 1 * e
    return ((prv & 9 ^ t) + t4) % 97

def fn1(c, m):
    b = 11 - c & m
    t0 = (m >> 3) * m
    t1 = t0 * (c + m >> 3)
    t2 = c * m % 17
    b = fn0(t1 & 131071, t2)
    if m * m <= 52:
        t3 = 16 * c + m
        t4 = (t3 ^ (c + b) // 8) % 251
        t5 = (c >> 1) + b
        m = fn0(t4, t5 & 16383)
        tmp = 0
        while tmp < 10:
            t6 = (20 ^ b) << 1
            m = (t6 - tmp) % 1009
            c = c % 17
            m = tmp - b & 2047
            tmp = tmp + 1
    cur = 0
    while cur < 5:
        m = (cur ^ m) % 17
        c = (cur ^ 8 | c) & 4095
        cur = cur + 1
    b = 11 + 16 + m
    b = c + m
    t7 = b % 1009 | b * b | b
    return t7 & 1023

def f(x):
    lo = [25, 50, 66, 70, 41, 40, 68, 39]
    lo[x % 8] = x ^ 10
    lo[x % 8] = x & 3
    if x ^ 2 > 24:
        x = x + 16
        for g in range(9):
            lo[g % 8] = g * g >> 1 | x
            lo[x % 8] = (x & 9) + 6 - 18
            lo[g % 8] = x - g ^ x
    else:
        x = 20 | x
    if x - 5 == 34:
        if 6 & x <= 5:
            x = x | 15
            t0 = lo[x % 8]
            t1 = t0 - x ^ x
            t2 = (x << 4) - x
            x = t1 & t2
        else:
            t3 = 16 + x & 511
            t4 = x * x * (4 * x)
            t5 = t4 - (x + x - x)
            x = fn0(t3, t5 & 255)
            lo[x % 8] = (x ^ 8) % 97
        t6 = x // 3 + x
        lo[x % 8] = (t6 | x) % 97
    t7 = (x - 20) % 4093
    t8 = x - 7 & 65535
    x = fn1(t7, t8)
    p = 2 & x
    tmp = 0
    while tmp < 16:
        t9 = 4 + x - tmp
        p = t9 & 255
        val = 0
        while val < 7:
            lo[val % 8] = ((15 * tmp | tmp) ^ p) % 97
            p = (x ^ p) % 4093
            val = val + 1
        x = (x ^ 9) & 8191
        tmp = tmp + 1
    t10 = (1 | x) % 97
    t11 = lo[p % 8]
    t12 = (t11 ^ 4) % 4093
    p = fn0(t10, t12)
    return 8 & p & x

if __name__ == "__main__":
    arg = 18
    expected = 0
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
