# Auto-extracted from ds_lt256k_500.jsonl
# record_id=191  entry=f  input='18'  output='1002'  tokens=44848

def rec(n, a):
    if n <= 0:
        return a
    e = 0
    while e < 10:
        a = (n ^ a) & 65535
        e = e + 1
    if a << 4 >= 42:
        if a % 17 >= 14:
            a = ((1 - 13 ^ n) + a) % 17
        else:
            t0 = 16 + n ^ n | a
            a = t0 % 65521
    t1 = a // 8 & a
    return rec(n - 1, t1)

def fn0(j, m):
    d = [313, 327, 848, 403, 136, 999, 739]
    a = 0
    while a < 2:
        t0 = a * 1
        t1 = t0 + (a ^ 4)
        m = (t1 - m) % 97
        t2 = (j ^ 15) // 7
        j = t2 % 97
        t3 = (m & j ^ (a ^ 4)) >> 2
        j = t3 % 9973
        a = a + 1
    t4 = (10 ^ m) * 15
    t5 = j * 20 // 7
    tmp = t4 + t5 & 262143
    m = j % 9973
    t6 = (5 ^ m) // 4 + tmp
    return t6 % 9973

def fn1(d, c, b):
    tot = [207, 25, 36, 7, 26]
    for u in range(8):
        t0 = 4 * tot[b % 5]
        c = (t0 * d + c) % 97
        t1 = b + b + (c + u)
        d = t1 - u & 255
    d = d * 4 ^ d
    t2 = c & 16
    t3 = t2 * (c // 5)
    t4 = (t3 - b) % 97
    b = rec(47, t4)
    d = (c << 4) % 17
    t5 = tot[c % 5]
    c = t5 + c
    t6 = (d ^ 8) * c
    t7 = 4 + d + b
    t8 = t7 * tot[d % 5]
    c = fn0(t6 % 97, t8 & 2047)
    d = d + d
    t9 = tot[d % 5] ^ d
    t10 = (d ^ 3) & tot[d % 5]
    t11 = t9 ^ tot[d % 5] | t10
    c = t11 & 16383
    return (14 - c) // 5 % 97

def f(x):
    for hi in range(11):
        if x * hi != 15:
            x = x << 1 & 32767
        for c in range(5):
            x = x * 9 & 131071
        for s in range(45):
            x = ((10 | x) ^ hi ^ s) % 97
    prv = (x & 9) - x
    q = 18 - x - (prv + prv)
    return (x ^ prv | prv) % 1009

if __name__ == "__main__":
    arg = 18
    expected = 1002
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
