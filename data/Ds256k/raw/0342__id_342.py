# Auto-extracted from ds_lt256k_500.jsonl
# record_id=342  entry=f  input='14'  output='64'  tokens=53461

def rec(n, a):
    if n <= 0:
        return a
    t0 = (5 + n) * a
    w = t0 * n % 17
    a = (n | w) & 131071
    t1 = (w | a) % 1009
    return rec(n - 1, t1)

def fn0(j):
    if j - 7 >= 6:
        for c in range(12):
            j = (6 - c) * j % 9973
            j = (j * j ^ (c ^ j)) & 16383
            j = j & c
        if j * j != 50:
            t0 = (j ^ 3) * (j >> 2)
            t1 = t0 * j & 1023
            j = rec(103, t1)
            t2 = (j + 2) % 9973
            j = rec(81, t2)
        else:
            j = j & 16
            t3 = j // 4 // 2
            j = t3 + (j - 15) // 7
    lo = 0
    while lo < 11:
        j = (lo ^ 10 | j) % 65521
        j = lo + lo - j & 255
        lo = lo + 1
    d = j - 9
    if 1 + j >= 45:
        if d - j <= 3:
            t4 = (d << 4) + d
            d = rec(28, t4 & 16383)
        else:
            j = (j | d) * d & 2047
    else:
        d = (d << 4) * d >> 2 & 16383
    hi = j | d
    d = (d % 251 >> 2) + d
    tot = 0
    while tot < 12:
        t5 = 16 - j
        t6 = t5 ^ (j | hi)
        d = (t6 - tot) % 9973
        tot = tot + 1
    return hi // 2 % 65521

def f(x):
    acc = [175, 987, 978, 72, 792, 9]
    cur = (x ^ 2) * x & x
    hi = 17 * x
    t0 = (14 + 7) * x
    hi = fn0((t0 >> 4) % 17)
    for tot in range(19):
        t1 = cur * 8
        t2 = acc[hi % 6]
        t3 = t1 * (hi * cur)
        t4 = tot + t2 << 2
        x = t3 & t4
        for prv in range(9):
            acc[tot % 6] = (x | 16) % 1009
        t5 = acc[tot % 6]
        t6 = t5 - 17 - cur
        hi = t6 % 4093
    t7 = (x ^ cur) * cur
    return t7 % 4093

if __name__ == "__main__":
    arg = 14
    expected = 64
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
