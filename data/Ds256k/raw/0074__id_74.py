# Auto-extracted from ds_lt256k_500.jsonl
# record_id=74  entry=f  input='17'  output='0'  tokens=151252

def rec(n, a):
    if n <= 0:
        return a
    a = (n + 19 + a) % 9973
    for j in range(11):
        t0 = a - 6 + a
        a = t0 % 17
    t1 = n * n
    t2 = t1 | n * 20
    t3 = (t2 ^ a) % 9973
    return rec(n - 1, t3)

def fn0(m, b):
    m = m + 5
    if m - 3 < 44:
        b = m % 65521
        if b & 1 > 2:
            m = b & m
    m = b & m
    p = 0
    while p < 11:
        t0 = (m >> 4) // 7 >> 1
        b = (t0 ^ p) & 16383
        t1 = (p << 3) + (b & 15)
        b = (p + m) % 251 - t1 & 131071
        p = p + 1
    t2 = (b - 9 >> 3) - 10
    return t2 % 17

def f(x):
    for y in range(9):
        x = (13 ^ x - y) % 17
        for res in range(47):
            t0 = x ^ 19
            t1 = t0 * (y * 6)
            x = t1 % 17
            x = (x + res) % 9973
            t2 = (((y | res) ^ 3) & 11) - x
            x = t2 & 511
    hi = 7 & x
    t3 = 3 - 10 + (x | hi)
    d = t3 & (hi & 4) + x
    prv = hi * hi + (d + d)
    return hi + prv & hi & d

if __name__ == "__main__":
    arg = 17
    expected = 0
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
