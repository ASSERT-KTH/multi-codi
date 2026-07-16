# Auto-extracted from ds_lt256k_500.jsonl
# record_id=436  entry=f  input='16'  output='38'  tokens=217144

def rec(n, a):
    if n <= 0:
        return a
    a = (18 ^ n) + a & 1023
    t0 = a * a & (n ^ 5)
    a = ((n + a >> 2) - t0) % 9973
    a = (17 - n ^ a) % 65521
    t1 = (a + 8) % 9973
    return rec(n - 1, t1)

def fn0(a):
    t = ((a & 14) * a ^ a) % 65521
    j = t * a & 8191
    for w in range(12):
        t0 = (t & j) * j
        j = t0 % 65521
        if 18 + a <= 2:
            t = (t + t) % 251
        t1 = 9 | 13
        t2 = t1 * (t ^ 2)
        a = (t2 + w) % 65521
    t3 = a >> 2 & 511
    j = rec(91, t3)
    t4 = j >> 1 & 255
    a = rec(99, t4)
    return (t - a | t + t) % 17

def fn1(b):
    t0 = (7 | b) // 8
    c = t0 * b % 97
    t1 = (b & 5) + c
    p = t1 // 7
    for res in range(2):
        if p + res < 40:
            c = (11 ^ p) + (1 & res) & 131071
        t2 = p * b
        t3 = t2 - 5 * p
        b = t3 % 1009
    if c ^ b > 61:
        t4 = (p & c) >> 3
        p = t4 + p
        c = fn0(c & 4)
    else:
        p = p + b
    t5 = 10 - c
    t6 = t5 | c * c
    b = fn0(t6 % 97)
    return (p | c) & 511

def f(x):
    for hi in range(58):
        x = (15 & hi | x) % 4093
        for y in range(4):
            x = ((x >> 3) - x) % 9973
            t0 = y - 5 + hi + y - x
            x = t0 % 65521
            x = (hi ^ 11 ^ x) & 2047
        t1 = x * hi % 4093
        x = (t1 - x) % 4093
    t2 = (x ^ 3) * x & x
    x = rec(99, t2)
    x = fn1(((x ^ 11) - x) % 4093)
    b = (x ^ 19) * (x % 9973) & 511
    t3 = 18 * x * x
    a = t3 & 16383
    t4 = x ^ 10 | a * b
    t5 = b // 8 ^ (a ^ 17)
    tot = t4 - t5 & 16383
    t6 = tot & 15
    t7 = b // 3 - a
    t8 = t6 ^ a % 9973
    acc = t7 ^ t8
    return (x + 19 + a) % 9973

if __name__ == "__main__":
    arg = 16
    expected = 38
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
