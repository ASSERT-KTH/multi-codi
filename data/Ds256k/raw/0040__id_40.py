# Auto-extracted from ds_lt256k_500.jsonl
# record_id=40  entry=f  input='17'  output='127851'  tokens=77304

def fn0(m, c):
    for e in range(11):
        c = c & m
        t0 = 18 + c >> 2
        c = (t0 ^ c) & 511
        t1 = 20 ^ 10 | m
        m = t1 % 65521
    b = m + c ^ 4
    q = 6 ^ c
    for j in range(7):
        if m & j == 5:
            c = 17 * c % 65521
            t2 = (b >> 2) * (c // 2)
            q = (t2 ^ j) % 65521
        c = ((16 ^ q) + c) % 65521
        t3 = q - c - (j - q)
        b = t3 % 1009
    buf = 9 & b
    t4 = b + q
    t5 = t4 ^ q % 65521
    return (t5 | c) & 1023

def fn1(m):
    cur = [56, 84, 36, 21]
    t0 = m + 4
    t1 = t0 - m * m
    prv = (t1 + m) % 4093
    lo = cur[prv % 4] * prv ^ 15
    lo = (m | 8) * lo & 1023
    return cur[lo % 4] & lo

def f(x):
    y = [156, 70, 17, 35, 157]
    for cnt in range(6):
        x = (cnt ^ 17 | x) % 9973
        y[cnt % 5] = (cnt + x) % 251
        hi = 0
        while hi < 11:
            t0 = (17 ^ 11) - 2
            y[x % 5] = (t0 ^ x) % 251
            hi = hi + 1
    if 19 ^ x >= 14:
        x = (x ^ 4 | 17) // 8
    for v in range(118):
        x = v * x % 9973
        t1 = y[x % 5]
        t2 = x * v
        t3 = t2 - (7 - t1)
        x = t3 % 9973
        y[v % 5] = (15 | x) % 251
    t4 = y[x % 5] + x
    m = t4 ^ x // 5
    t5 = y[x % 5]
    m = (x & m) - t5
    t6 = (m ^ 1) - (m >> 2) & 511
    t7 = (x ^ m) - x
    t8 = t7 >> 2 & 131071
    x = fn0(t6, t8)
    return 12 - m & 131071

if __name__ == "__main__":
    arg = 17
    expected = 127851
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
