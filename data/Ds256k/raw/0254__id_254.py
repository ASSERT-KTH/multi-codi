# Auto-extracted from ds_lt256k_500.jsonl
# record_id=254  entry=f  input='14'  output='2838'  tokens=244603

def rec(n, a):
    if n <= 0:
        return a
    t0 = a + n + a
    tmp = t0 % 65521
    t1 = n + tmp & (a | n)
    return rec(n - 1, t1)

def fn0(m, a):
    t0 = 9 + a
    t1 = (a - 14) // 5
    t2 = t0 ^ m + m
    t3 = (t1 | t2) & 8191
    m = rec(100, t3)
    t4 = 3 * 17 * m
    lo = t4 % 97
    res = (m | a) + a * 7
    if a * res <= 4:
        a = (a % 97 | (res | 16)) & 16383
        t5 = (lo >> 1) + lo * 11
        res = t5 - lo
    else:
        m = (res ^ 1 | lo) & 8191
        for j in range(2):
            a = (lo - m ^ a) % 97
            t6 = (14 - j) * j
            res = t6 * lo & 511
    a = a % 97
    t7 = res + 1 << 3
    m = rec(90, t7 & res)
    if res + 15 <= 21:
        p = 0
        while p < 11:
            a = a * 5 % 17
            p = p + 1
        a = lo ^ 12 ^ a
    t8 = (a << 3 >> 1) % 1009 ^ lo
    return t8 % 17

def f(x):
    t0 = (x * x - x) % 4093
    t1 = x + 14 + 5 ^ x
    x = fn0(t0, t1 % 4093)
    t2 = (x + x) % 4093
    t3 = (x + x) % 65521 ^ 19
    x = fn0(t2, t3 % 251)
    cur = 0
    while cur < 10:
        for aux in range(4):
            x = (1 - x) % 65521
            t4 = aux * cur - (aux ^ 13)
            x = (t4 - x) % 1009
        for val in range(70):
            x = ((x >> 1) + x) % 1009
        prv = 0
        while prv < 8:
            t5 = prv + prv + (prv + 16) + x
            x = t5 % 65521
            prv = prv + 1
        cur = cur + 1
    s = x & 10
    z = (x & s) + x + s
    c = 0
    while c < 5:
        x = x - z & 65535
        if c * x != 6:
            t6 = (c & 14) + (x | c)
            x = t6 % 4093
            t7 = z + z
            t8 = t7 + (c - 18)
            s = t8 - c & 8191
        c = c + 1
    if (15 << 4) - s == 21:
        x = s * 9 - (x + s)
    t9 = 11 * 9 - s
    return t9 % 4093

if __name__ == "__main__":
    arg = 14
    expected = 2838
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
