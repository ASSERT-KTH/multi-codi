# Auto-extracted from ds_lt256k_500.jsonl
# record_id=359  entry=f  input='20'  output='0'  tokens=157351

def rec(n, a):
    if n <= 0:
        return a
    t0 = (a ^ 10) + a - n
    a = t0 & 8191
    t1 = 10 + n
    t2 = t1 * (n ^ a)
    a = t2 & 2047
    a = (a | 7) % 4093
    t3 = (a + 19) % 1009
    return rec(n - 1, t3)

def fn0(c, b):
    u = [7, 37, 32, 32, 0]
    for d in range(2):
        t0 = d * u[b % 5] ^ 18
        b = t0 & 65535
        t1 = (c | 1) - u[c % 5]
        c = t1 * c % 65521
    for t in range(5):
        t2 = u[t % 5] + c
        b = (t2 + t) // 7 % 9973
        for q in range(10):
            b = (q - t + b) % 65521
    b = (b * b + b * b) % 4093
    t3 = b - 1 ^ u[c % 5]
    return t3 % 4093

def f(x):
    u = x * 18 ^ x
    d = 7 + x
    for p in range(9):
        d = u - p & 32767
        v = 0
        while v < 3:
            t0 = (d >> 3) // 8
            t1 = (t0 << 2) + u
            u = t1 & 4095
            t2 = v - 20 | u
            u = t2 & 255
            v = v + 1
        s = 0
        while s < 46:
            d = x * s & 8191
            t3 = x + d
            x = t3 & d - p
            s = s + 1
    for m in range(10):
        u = d * x + u & 4095
        t4 = (u + x) % 1009
        d = (t4 ^ m) & 4095
    t5 = ((d ^ x) - x * 17) * x
    buf = t5 & 32767
    z = buf + 13
    if d ^ 16 == 11:
        for c in range(11):
            t6 = (u * x >> 3) * 17
            u = t6 % 1009
    return z * buf % 17

if __name__ == "__main__":
    arg = 20
    expected = 0
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
