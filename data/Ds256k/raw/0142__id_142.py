# Auto-extracted from ds_lt256k_500.jsonl
# record_id=142  entry=f  input='13'  output='51'  tokens=44004

def rec(n, a):
    if n <= 0:
        return a
    t0 = (n << 4 & n * a) // 8
    prv = t0 % 1009
    t1 = a * a & 1023
    return rec(n - 1, t1)

def fn0(a, b):
    for y in range(5):
        if b - 2 < 14:
            t0 = y * y
            t1 = t0 * (b ^ 19)
            t2 = (a ^ 4) - y
            b = t1 * t2 & 131071
            a = y * b % 97
        else:
            b = (y | a) + b & 255
            b = (a // 7 | b) % 9973
    a = a ^ 7
    for tmp in range(2):
        a = (tmp | b) % 97
        b = (7 - b) % 97
    for buf in range(12):
        a = a + a & 262143
        t3 = buf - 4 - a
        b = t3 % 97
    t4 = 11 ^ b ^ b // 3
    t5 = t4 // 4 % 9973
    a = rec(68, t5)
    return (b + 4) % 9973

def f(x):
    b = [45, 78, 26, 27, 76, 55]
    if x & 16 != 9:
        t0 = b[x % 6]
        t1 = x ^ 20
        t2 = t1 * (t0 ^ x)
        x = t2 % 1009
        if x % 17 != 8:
            t3 = x * b[x % 6]
            t4 = (2 + x) * t3 & 16383
            b[x % 6] = t4 % 97
            t5 = b[x % 6]
            t6 = (t5 + x) * x
            t7 = t6 // 6 & 65535
            b[x % 6] = t7 % 97
        else:
            t8 = b[x % 6]
            t9 = (x << 1) // 2
            t10 = t9 & ((17 ^ 15) & t8)
            t11 = x - 20
            t12 = b[x % 6]
            t13 = t11 + (x - 19)
            t14 = (t12 << 2) // 4
            x = fn0(t10, t13 & t14)
            x = x | 3
    else:
        t15 = b[x % 6] // 8 | x
        x = t15 ^ 10
        for q in range(8):
            x = ((q & 12) - x) % 9973
            t16 = b[x % 6] - 17
            t17 = t16 ^ b[q % 6]
            x = t17 * x % 17
    if (17 & 7) - x <= 59:
        t18 = (x >> 2) * 10
        x = t18 + x
        for a in range(7):
            x = (x | b[a % 6]) % 17
            t19 = a * a + x
            b[x % 6] = t19 % 97
            x = (12 ^ x) // 5 % 251
    t20 = x ^ 5
    t21 = t20 + (x + x)
    tmp = t21 & 8191
    acc = 10 * tmp
    val = tmp & 10
    t22 = b[val % 6] | 2
    val = rec(22, t22 % 251)
    if tmp + 18 <= 5:
        t23 = acc // 5 << 2
        val = t23 ^ val
    for tot in range(55):
        t24 = (val & tmp) - 6
        t25 = (t24 | x) + tot
        acc = t25 % 1009
    return (acc + x) % 1009

if __name__ == "__main__":
    arg = 13
    expected = 51
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
