# Auto-extracted from ds_lt256k_500.jsonl
# record_id=304  entry=f  input='9'  output='12688'  tokens=107954

def rec(n, a):
    if n <= 0:
        return a
    cur = n * n - n - a & 131071
    t0 = 9 + cur - (cur + a)
    cur = t0 % 251
    t1 = ((cur ^ 5) << 3) // 8
    t2 = t1 + a & 255
    return rec(n - 1, t2)

def fn0(a, j, d):
    q = 0
    while q < 10:
        t0 = a * d * (d * a)
        d = (t0 - (d >> 4 >> 3)) % 9973
        if j - 19 > 37:
            t1 = a // 2 - (a - 19) - d
            j = (t1 - q) % 9973
        buf = 0
        while buf < 6:
            t2 = q & 18 ^ d ^ buf
            a = t2 % 17
            t3 = a % 9973 * (j >> 1)
            j = t3 << 3 & 65535
            t4 = d * q
            t5 = t4 + (buf ^ d)
            a = t5 - d & 2047
            buf = buf + 1
        q = q + 1
    t6 = j // 3 * (a - 2)
    t7 = (a % 17 + 18) * t6
    a = rec(40, t7 & 4095)
    d = d // 5 + d
    for tmp in range(6):
        t8 = j >> 4
        t9 = t8 + (a - 2)
        d = (t9 | tmp) & 4095
        for u in range(2):
            t10 = (a + u) // 3
            j = t10 % 9973
            t11 = d * a - (d - tmp)
            t12 = t11 | u + u - u
            d = t12 % 251
            d = u + 10 - a & 4095
    t13 = (d + a | a + d) & d
    j = rec(98, t13)
    t14 = (16 | j) // 3
    return (t14 | 9) % 9973

def f(x):
    t0 = x + x + 11
    j = t0 + (x | x ^ 11)
    t1 = (x | 11) & 131071
    t2 = x * x | j ^ 15
    t3 = (j + x) * (x + 5)
    x = fn0(t1, t2 % 251, t3 % 1009)
    if x ^ 6 <= 6:
        j = 16 | x
    acc = 0
    while acc < 13:
        j = (7 - j | x) % 1009
        acc = acc + 1
    y = 7 * 16 ^ x
    tmp = y ^ 8
    if j * y > 10:
        tmp = j ^ x ^ j >> 2
    return 13 * j & 131071

if __name__ == "__main__":
    arg = 9
    expected = 12688
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
