# Auto-extracted from ds_lt256k_500.jsonl
# record_id=230  entry=f  input='17'  output='8'  tokens=230465

def rec(n, a):
    if n <= 0:
        return a
    if 11 * 16 + a <= 41:
        for buf in range(4):
            t0 = a + n + a
            a = (t0 ^ buf + a + n) % 9973
    else:
        t1 = (n - 3) // 8 | a
        a = t1 % 97
    a = a % 97 // 3 & 1023
    a = n + a + n & 511
    t2 = (a + a) % 9973
    return rec(n - 1, t2)

def fn0(c):
    b = [27, 60, 16, 66, 32, 81, 59]
    for buf in range(11):
        c = (c - buf + buf) % 97
        t0 = (b[buf % 7] | buf) ^ c
        c = t0 % 17
    for t in range(9):
        if c % 1009 > 64:
            t1 = c - 14 & c
            c = (t1 - (t + c ^ c)) % 17
        t2 = b[t % 7] * c
        t3 = t - b[c % 7]
        t4 = 19 & b[t % 7]
        t5 = t2 | 8 & c
        c = (t5 | t3 ^ t4) % 97
        m = 0
        while m < 8:
            t6 = t * (m ^ 14)
            t7 = t6 ^ (c ^ m) + m
            c = t7 % 1009
            c = c * c // 4 & 255
            m = m + 1
    t8 = b[c % 7]
    t9 = t8 // 7
    t10 = t9 ^ (c ^ 8)
    a = t10 - 6
    z = 0
    while z < 4:
        t11 = z ^ b[a % 7]
        a = t11 * z % 1009
        for d in range(12):
            t12 = b[a % 7]
            t13 = c * t12 - c
            a = t13 % 1009
        z = z + 1
    t14 = 6 - b[a % 7]
    return (t14 + a) % 1009

def f(x):
    m = 0
    while m < 759:
        if 20 - x == 10:
            x = (x & 20) - (x - 2) & 8191
            t0 = 9 - m | x
            x = t0 % 97
        if m | x < 12:
            x = (m + x) % 4093
        else:
            x = x // 3 * x & 65535
        x = ((m ^ 12) * m | x) % 17
        m = m + 1
    if x ^ 6 == 51:
        for w in range(5):
            t1 = ((w | 15) << 2) // 3 ^ x
            x = t1 & 1023
    else:
        t2 = x * x ^ 15
        x = (t2 | x) % 4093
        x = (2 - x) * x >> 4 & 4095
    x = fn0(x * x & 10)
    return (x + x) % 17

if __name__ == "__main__":
    arg = 17
    expected = 8
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
