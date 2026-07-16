# Auto-extracted from ds_lt256k_500.jsonl
# record_id=354  entry=f  input='11'  output='3115'  tokens=170234

def rec(n, a):
    if n <= 0:
        return a
    t0 = ((a ^ 17) >> 2) + n
    u = t0 % 9973
    if u + u > 39:
        t1 = a * 11 - a
        u = t1 - u & 32767
    else:
        a = 9 * a & 255
    t2 = 12 | a
    t3 = t2 + 17 * 13
    t4 = n // 4 - 2
    t5 = (t3 | t4) % 251
    return rec(n - 1, t5)

def f(x):
    s = [810, 391, 977, 333]
    tmp = 0
    while tmp < 18:
        t0 = s[tmp % 4]
        t1 = tmp * t0 ^ x
        x = t1 & 511
        t2 = s[x % 4]
        t3 = s[x % 4]
        t4 = (t2 + x) * t3
        x = t4 // 2 % 65521
        x = (x ^ s[x % 4]) % 17
        tmp = tmp + 1
    p = x - 17
    t5 = s[x % 4]
    t6 = (4 & p) + t5
    b = t6 & 20
    t7 = b & 17
    t8 = t7 * (x | b)
    a = t8 & 255
    for w in range(11):
        t9 = s[w % 4] * b
        x = t9 % 65521
        cnt = 0
        while cnt < 9:
            s[p % 4] = (a - cnt + x << 3) % 1009
            t10 = x * 20 ^ p * b
            t11 = ((p >> 1) + b) * t10 + a
            a = t11 & 262143
            b = p + p + b & 4095
            cnt = cnt + 1
        t12 = (2 & 20) * p ^ b
        b = t12 % 9973
    t13 = x ^ 16
    t14 = t13 - (a >> 2)
    t15 = (8 - b) % 17
    t16 = t14 * t15 & 2047
    a = rec(88, t16)
    v = a + 16
    u = v & a
    return (x | v | u) % 9973

if __name__ == "__main__":
    arg = 11
    expected = 3115
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
