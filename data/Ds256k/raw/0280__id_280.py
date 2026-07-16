# Auto-extracted from ds_lt256k_500.jsonl
# record_id=280  entry=f  input='9'  output='231'  tokens=88492

def rec(n, a):
    if n <= 0:
        return a
    t0 = (a & 20) * 7 ^ a
    q = (t0 ^ n) % 251
    t1 = a - n << 4
    q = t1 % 251
    t2 = 10 * q * q
    t3 = t2 // 2 ^ a
    return rec(n - 1, t3 & 4095)

def fn0(c):
    t0 = c // 8 * c ^ c
    t = t0 & 1023
    if c & 11 >= 1:
        for hi in range(3):
            t = t * 17 % 4093
            t = t // 8 // 3 & 262143
    for val in range(7):
        for aux in range(6):
            t1 = c ^ val ^ val * val
            c = (3 ^ 16) & t1
            t2 = (aux & t) - 18 * val
            c = t2 % 17
        t3 = (18 - c - t) * c
        c = t3 % 9973
        t4 = 9 * c * t
        t5 = t4 + (c - val) * t
        c = t5 & 255
    t6 = c // 4 // 7
    e = t6 + c
    res = 20 + e
    t7 = e // 7 // 4
    t = t7 ^ e + c - 10
    t8 = res >> 1 & 262143
    c = rec(75, t8)
    for buf in range(5):
        t9 = t % 4093 // 5 // 2
        c = (t9 - c) % 4093
        e = (t | e) // 3 % 251
        c = buf * e % 17
    t10 = e - res
    t11 = t10 ^ 9 - c
    t12 = 13 * c - t
    return t11 * t12 & 262143

def f(x):
    for cnt in range(6):
        t0 = (cnt ^ 4) * (x + cnt)
        t1 = t0 + (cnt - 13) * x
        x = t1 & 131071
    for val in range(12):
        a = 0
        while a < 22:
            x = x + x & 262143
            t2 = (a << 1) + (x >> 4)
            x = t2 % 97
            a = a + 1
        x = (val + (x - 5)) % 97
        x = x + val & 511
    for b in range(7):
        t3 = b * x - b
        x = t3 % 97
    for j in range(3):
        x = (x - 14) * 18 << 1 & 32767
        x = ((13 ^ 2) + x) % 97
        tmp = 0
        while tmp < 7:
            x = (x ^ 11 | 4) >> 3 & 131071
            x = (x ^ tmp) % 97
            tmp = tmp + 1
    buf = x * x % 9973
    m = 0
    while m < 6:
        t4 = (buf << 1) * buf
        t5 = t4 - buf ^ x
        x = t5 % 9973
        buf = buf + m & 4095
        m = m + 1
    t6 = x >> 4
    t7 = t6 | 5 ^ buf
    return t7 % 9973

if __name__ == "__main__":
    arg = 9
    expected = 231
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
