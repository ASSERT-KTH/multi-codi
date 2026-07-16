# Auto-extracted from ds_lt256k_500.jsonl
# record_id=118  entry=f  input='20'  output='4'  tokens=135603

def rec(n, a):
    if n <= 0:
        return a
    j = 0
    while j < 11:
        a = ((j * j | a) ^ n) & 8191
        t0 = 10 + 2 - j << 4 ^ a
        a = t0 % 65521
        t1 = n >> 2 << 4
        t2 = (t1 >> 4) - a
        a = t2 & 255
        j = j + 1
    if a | 19 == 43:
        for cur in range(9):
            a = (cur & 1 ^ a + cur) % 17
    else:
        y = 0
        while y < 7:
            t3 = a % 17
            t4 = t3 + (1 + n)
            a = t4 * a & 511
            t5 = (8 | y) << 1
            a = (t5 - a) % 17
            t6 = y * a - (1 & a)
            a = t6 * n % 17
            y = y + 1
        t7 = 15 + n
        t8 = t7 ^ n + n
        t9 = (12 + n) // 7
        t10 = t8 * t9 - a
        a = t10 % 9973
    t11 = n | 10 | n | a
    return rec(n - 1, t11 % 65521)

def fn0(b, d, a):
    t0 = b * b & (b ^ 9)
    b = (d ^ b ^ b) + t0
    b = a * d & a << 2
    aux = 0
    while aux < 9:
        t1 = d % 65521 | a
        a = t1 & 32767
        aux = aux + 1
    if 11 ^ d < 5:
        t2 = (b - a) // 2
        t3 = b & 7 & b
        d = t2 + t3
    if a >> 4 <= 10:
        d = d // 8
    else:
        for cnt in range(10):
            t4 = (a << 4) + d << 3
            d = t4 % 1009
            a = a * b & 255
    for tmp in range(5):
        t5 = (7 - tmp & 12 - tmp) + 3
        a = t5 + b & 16383
        b = (12 & a ^ b) & 8191
        acc = 0
        while acc < 7:
            b = (tmp ^ 4 ^ b) % 251
            acc = acc + 1
    return a * b % 251

def f(x):
    t = 0
    while t < 3:
        t0 = 8 * (t | 15) ^ x
        x = t0 & 16383
        t = t + 1
    a = 0
    while a < 6:
        for m in range(10):
            x = a + a & x
        x = (a & 9) + (x - a) & 65535
        a = a + 1
    for hi in range(2):
        t1 = (hi & 2) + x
        x = t1 % 4093
        for cur in range(7):
            x = (1 ^ x) % 17
            x = (x ^ x + hi) % 1009
        t2 = hi ^ x
        t3 = t2 - 13 * 1
        x = t3 % 4093
    tot = x * x % 4093
    lo = x - 2
    for j in range(12):
        for prv in range(13):
            t4 = j - lo | 3
            x = t4 & (tot & j) - x
            t5 = lo + 4 - prv
            x = t5 % 1009
            t6 = prv * j ^ prv | tot
            lo = t6 & 65535
    for idx in range(10):
        lo = (lo + tot ^ 17) % 65521
    nxt = (tot | 15) // 5 & 4
    t7 = lo * x - 10
    return (t7 >> 4) % 17

if __name__ == "__main__":
    arg = 20
    expected = 4
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
