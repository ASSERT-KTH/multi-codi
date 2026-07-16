# Auto-extracted from ds_lt256k_500.jsonl
# record_id=46  entry=f  input='17'  output='111'  tokens=161813

def fn0(e, j):
    t0 = (4 + e) // 5
    prv = t0 & e
    t1 = 14 * e + j * j
    t2 = t1 | j * 13 & e
    val = t2 % 4093
    u = e ^ 18
    t3 = e ^ 19 | j
    t4 = (14 - j) // 4
    c = t3 - t4
    buf = 0
    while buf < 9:
        for lo in range(5):
            t5 = (11 | 2) ^ prv % 4093
            prv = t5 % 4093
        buf = buf + 1
    c = e >> 4
    return ((10 | 2) - val) % 4093

def fn1(j, d, c):
    t0 = d * 7 + 9
    c = t0 ^ (d - j ^ 20)
    t1 = (d | j) % 97
    t2 = j * c % 97
    c = fn0(t1, t2)
    t3 = (d * 16 << 1 >> 4) % 1009
    t4 = j << 3
    t5 = t4 | c & 19
    t6 = t5 >> 2 & 16383
    j = fn0(t3, t6)
    j = (c << 4) % 1009
    c = c - j + c - d & 255
    c = (20 ^ j ^ d - 10) % 97
    if c - j >= 24:
        c = j - d << 1
    return (4 + j << 2) % 97

def f(x):
    t0 = x * 13 & 2047
    t1 = x * x % 1009
    t2 = ((x | 19) << 4) - x
    x = fn1(t0, t1, t2 % 251)
    j = x + x
    if 4 + 17 ^ j > 53:
        t3 = x - 17 >> 1
        t4 = t3 | j * x - j
        x = t4 & 32767
        for cnt in range(7):
            x = (j + j) * (j ^ x) % 1009
    acc = x % 251
    res = 0
    while res < 8:
        t5 = res - x
        t6 = t5 + (res | 16)
        x = (t6 >> 3) % 251
        t7 = (j | 14) - acc
        acc = t7 % 251
        res = res + 1
    if acc * j > 28:
        t8 = 6 * x * j
        t9 = acc & 10 | x
        j = (t8 - t9) % 251
    else:
        t10 = x + 9 & 4 << 1
        t11 = (j | x) >> 2
        t12 = t11 * (x % 1009 >> 4)
        j = fn0(t10, t12 % 251)
    aux = 0
    while aux < 25:
        for q in range(9):
            t13 = j * 7 >> 1
            t14 = 18 * x << 3
            x = t13 * t14 % 251
        j = j // 4 & 131071
        x = ((aux | 10) - j) % 251
        aux = aux + 1
    e = j & 8
    nxt = e | j
    t15 = (19 * j + 14) * e
    t = t15 & 16383
    t16 = acc & 3 ^ e
    cur = t16 - j
    t17 = cur // 7
    hi = t17 - (16 & t)
    for s in range(6):
        if 5 * t < 58:
            t18 = hi + 6 ^ j
            t19 = t18 // 2 - acc
            acc = t19 % 251
        else:
            e = (t - j + s) % 251
            nxt = (s - acc) % 251
        t20 = (cur & nxt) * x
        t21 = t20 * (hi ^ j | hi) - s
        e = t21 % 251
        x = 2 + e & x
    t22 = (9 & 1) - 12 * cur
    v = (t22 + 16) % 1009
    t23 = 18 & x ^ t - cur
    idx = t23 - j % 251 * 11
    prv = 11 + acc
    t24 = 9 * 14 + v - 13
    return t24 % 251

if __name__ == "__main__":
    arg = 17
    expected = 111
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
