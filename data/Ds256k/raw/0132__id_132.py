# Auto-extracted from ds_lt256k_500.jsonl
# record_id=132  entry=f  input='3'  output='3'  tokens=118501

def rec(n, a):
    if n <= 0:
        return a
    t0 = a % 65521 | n
    acc = t0 & 65535
    t1 = ((acc ^ 15) >> 3) + n
    a = t1 % 4093
    a = (n * a + a >> 3) % 65521
    t2 = (5 << 1) - a & 32767
    return rec(n - 1, t2)

def f(x):
    z = [25, 158, 634, 971, 99]
    t0 = (x ^ 5) & 8
    m = t0 ^ 9
    for t in range(10):
        t1 = t + t - (15 & x)
        m = t1 % 17
    if m * x < 32:
        t2 = z[x % 5]
        t3 = x - t2
        t4 = t3 + x * m
        x = t4 ^ 9
        for v in range(10):
            t5 = z[x % 5] & v
            t6 = z[m % 5]
            m = (t5 * v | t6) % 17
            t7 = (x ^ m) >> 3
            m = t7 % 4093
    if x // 8 >= 47:
        t8 = z[x % 5]
        m = x + m ^ t8 | x
    t9 = m * 17
    t10 = t9 & x // 6
    t11 = (t10 >> 1) % 4093
    m = rec(106, t11)
    t12 = z[m % 5]
    acc = t12 * z[m % 5] & 131071
    t13 = z[x % 5]
    t14 = x + x
    cur = t14 - (acc | t13)
    b = 0
    while b < 9:
        for tot in range(14):
            t15 = cur & 3 & tot
            z[acc % 5] = (t15 - cur) % 1009
            z[b % 5] = cur >> 4 >> 1 & tot
        if acc >> 4 != 34:
            t16 = b & acc ^ 16
            z[acc % 5] = (t16 - x) % 1009
        else:
            z[acc % 5] = ((20 + 12) * x + 20) % 1009
            t17 = z[x % 5]
            t18 = t17 & x
            t19 = t18 * (10 + m)
            z[m % 5] = t19 // 3 % 17
        b = b + 1
    nxt = 0
    while nxt < 6:
        t20 = (4 - x) * (nxt * acc)
        acc = t20 & 32767
        nxt = nxt + 1
    return (acc + x) % 4093

if __name__ == "__main__":
    arg = 3
    expected = 3
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
