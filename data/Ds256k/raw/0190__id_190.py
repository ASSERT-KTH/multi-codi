# Auto-extracted from ds_lt256k_500.jsonl
# record_id=190  entry=f  input='4'  output='219'  tokens=182406

def rec(n, a):
    if n <= 0:
        return a
    if a ^ n != 45:
        t0 = a - n - 19
        a = t0 + a & 1023
    t1 = n * 3
    t2 = t1 - (n + a)
    idx = (t2 + a) % 4093
    t3 = (a & n) // 4 % 4093
    return rec(n - 1, t3)

def f(x):
    p = x * 20
    for val in range(2):
        t0 = x * p << 3
        t1 = val - 16 + t0
        x = t1 & 511
        t2 = p & x
        t3 = t2 ^ val * x
        t4 = x + p + val
        x = t3 - t4 & 8191
        for buf in range(7):
            t5 = buf * 13
            t6 = t5 ^ (18 ^ buf)
            p = (t6 | p) & 65535
            t7 = buf + (x << 4)
            p = t7 % 97
            x = (val + p ^ buf) % 1009
    cnt = 6 + 17 << 2 ^ x
    d = (cnt - 7) % 97
    u = 0
    while u < 12:
        t8 = (p ^ x) >> 1
        t9 = t8 * cnt ^ d
        d = t9 & 8191
        for lo in range(3):
            cnt = (6 * x | lo) & 32767
        u = u + 1
    e = (p * d ^ x) * x & 255
    a = x - p
    s = a & x
    t10 = (s + d << 3) % 97
    d = rec(105, t10)
    tot = 0
    while tot < 9:
        t11 = (p ^ e) - (e + d)
        s = (cnt | tot) + a - t11 & 1023
        tot = tot + 1
    for cur in range(21):
        t12 = cur * s + cur | 20
        cnt = t12 & 2047
        y = 0
        while y < 5:
            t13 = p >> 2 ^ s
            s = t13 & 8191
            d = (d << 4) % 1009
            y = y + 1
    t14 = e * p | d
    t15 = p - 10 - s
    g = t14 ^ t15
    t16 = (cnt + g) * 12 - x
    z = t16 % 97
    t17 = 4 - s ^ 11
    return t17 & 255

if __name__ == "__main__":
    arg = 4
    expected = 219
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
