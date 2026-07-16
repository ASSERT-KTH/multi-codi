# Auto-extracted from ds_lt256k_500.jsonl
# record_id=170  entry=f  input='18'  output='9669'  tokens=81203

def rec(n, a):
    if n <= 0:
        return a
    nxt = (n & 11) - a & 511
    t0 = n * nxt - n | nxt
    t1 = (t0 | a) % 9973
    return rec(n - 1, t1)

def fn0(e):
    t0 = e * e | 3
    j = t0 % 65521
    if e // 2 <= 3:
        t1 = 8 - j - e
        e = t1 + (e >> 1 | j)
    else:
        e = 20 ^ e
    for hi in range(8):
        e = (hi ^ e ^ e) % 17
        t2 = (e & j) // 6
        j = (t2 >> 1) % 65521
    j = j << 2
    t3 = e - j - (17 - j)
    j = (e * e % 65521 | t3) & 2047
    e = e * j % 65521
    e = (3 - j ^ 3 + j) - e
    s = 0
    while s < 3:
        t4 = (13 + e ^ e + e) >> 3
        j = (t4 ^ j) & 511
        e = (j + e) % 65521
        t5 = (e & 17) * j
        j = t5 & 14 * e // 5
        s = s + 1
    return j % 17 * (e // 8) % 17

def fn1(b):
    hi = b | 16 | b
    q = b + 8 << 3
    t0 = b * 16 << 3
    b = t0 % 65521
    hi = 2 ^ b
    t1 = (q | b) % 97
    return t1 % 17

def f(x):
    m = [65, 31, 32, 39, 24]
    b = (x | 15) + (x | 20)
    m[x % 5] = x - b
    t0 = m[x % 5] ^ 16
    t1 = b * b % 251
    u = t1 | t0 * b
    t2 = (u ^ 11) * b
    t3 = t2 + m[u % 5]
    u = fn1(t3 % 251)
    m[b % 5] = (8 + u) // 8 % 97
    e = (16 ^ b) - b // 6
    u = b | 1 | x
    for y in range(13):
        p = 0
        while p < 8:
            x = 6 * x & 511
            t4 = (b ^ x) // 2 - y
            x = t4 % 1009
            t5 = (u ^ 7) + b
            b = t5 & 32767
            p = p + 1
        t6 = (x - 7) // 3
        t7 = t6 * m[b % 5] - y
        e = t7 % 1009
    t8 = m[e % 5]
    return (t8 - x) % 9973

if __name__ == "__main__":
    arg = 18
    expected = 9669
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
