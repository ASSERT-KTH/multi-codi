# Auto-extracted from ds_lt256k_500.jsonl
# record_id=197  entry=f  input='14'  output='13'  tokens=181590

def rec(n, a):
    if n <= 0:
        return a
    v = a % 1009 - n & 65535
    t0 = (18 | n | v) - a
    return rec(n - 1, t0 & 262143)

def fn0(m):
    a = [51, 127, 41, 39, 132, 183, 89, 66]
    t0 = (m ^ 8) & m
    a[m % 8] = (t0 - m) % 251
    if m * m <= 25:
        for e in range(2):
            a[m % 8] = (m | 7) % 251
            m = (((m | e) >> 1) - e) % 1009
            a[m % 8] = ((12 ^ m) >> 3) % 1009 % 251
    t1 = a[m % 8] // 4
    b = (t1 << 3) + m
    t2 = a[m % 8]
    t3 = t2 & 20
    acc = t3 & 13 + m
    hi = 0
    while hi < 2:
        t4 = acc & hi ^ acc
        m = t4 % 97
        m = acc * hi & 511
        hi = hi + 1
    t5 = (b ^ m) * (acc * acc)
    m = rec(112, t5 % 4093)
    return (acc ^ b) % 1009

def fn1(m, e):
    if m ^ 3 >= 0:
        m = 18 - e
        t0 = 7 - 6 ^ e
        m = fn0(t0 & 131071)
    t1 = m - 15
    t2 = m * e
    t3 = t1 - 16 * e
    t4 = t2 + m * m
    m = t3 * t4 % 9973
    for g in range(10):
        m = ((19 << 1) + m) % 65521
        for lo in range(11):
            t5 = 13 * 1 + e
            e = t5 % 65521
            m = (3 * g | m) % 65521
            t6 = 2 - g
            t7 = t6 - (8 - 3)
            t8 = t7 << 2 | e
            m = t8 - lo & 16383
        e = (m | g) // 7 & 8191
    return e * e % 9973

def f(x):
    if x - 1 < 8:
        for a in range(4):
            x = (x - 7) * (x + x) & 8191
            x = (x - 1) % 17
            t0 = x & 14 ^ a
            x = t0 & 6
    else:
        x = x + x
    x = fn0(x * x % 17)
    m = (x & 10) - x
    acc = x + m
    t1 = acc << 2 & 32767
    t2 = acc // 2 * x
    t3 = t2 * x & 8191
    acc = fn1(t1, t3)
    t4 = 10 * acc
    t5 = t4 + (acc | x)
    cur = t5 % 97
    t6 = (x | 9) + cur - m
    for tot in range(193):
        t7 = (2 * 15 & cur) + 8 ^ tot
        x = t7 % 17
    return t6 % 17

if __name__ == "__main__":
    arg = 14
    expected = 13
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
