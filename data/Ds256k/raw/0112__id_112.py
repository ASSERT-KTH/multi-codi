# Auto-extracted from ds_lt256k_500.jsonl
# record_id=112  entry=f  input='4'  output='0'  tokens=67856

def fn0(c, b, d):
    t0 = d - c - 17
    d = t0 | b
    t1 = (b | c) >> 2
    b = t1 & d >> 3 >> 2
    b = b % 65521
    c = 17 - d
    return (c >> 4) * d % 9973

def fn1(b):
    for q in range(4):
        for v in range(2):
            t0 = (v ^ q) - b
            t1 = t0 - ((v ^ q) - q)
            b = t1 & 1023
            b = (19 & 17 ^ b) % 65521
            t2 = v & 10
            t3 = t2 + (v - b)
            b = t3 % 65521
    for u in range(10):
        if 13 | 4 | b != 48:
            t4 = b + 20
            b = t4 & b // 8
    t5 = 20 | 4 | b
    t6 = 6 * b
    t7 = t6 * (b - 6)
    t8 = 11 + 14 - t7
    t9 = (b >> 4) % 17
    b = fn0(t5 % 4093, t8 & 131071, t9)
    if b * 3 > 3:
        t10 = (b + 15) % 65521
        t11 = (3 ^ b) % 65521
        t12 = (b >> 2) * (b - 19)
        b = fn0(t10, t11, t12 & 4095)
        t13 = b - 14 & b
        b = t13 + ((11 ^ b) & b)
    else:
        b = (b ^ 1) * b & 8191
    t14 = (b * 20 - (b >> 2)) % 17
    t15 = b + b
    t16 = t15 ^ b - 12
    t17 = (t16 | b) % 17
    b = fn0(t14, t17, b & 12)
    t18 = b // 5 * b
    s = t18 << 3 & 131071
    t19 = b * s * (7 + s)
    return t19 & 262143

def f(x):
    m = x + x & x
    t0 = x - m + (x | 1)
    t1 = m | 20 | x
    t2 = 15 - m & 2047
    m = fn0(t0 & 1023, t1 % 9973, t2)
    nxt = (18 ^ m) // 3
    nxt = fn1((11 * m >> 3 << 2) % 9973)
    z = 16 * x
    t3 = 6 * x + (16 | 9)
    t4 = (nxt - z) // 6 & 65535
    t5 = 16 * m % 9973
    x = fn0(t3 & 255, t4, t5)
    g = nxt * 10
    for c in range(330):
        nxt = nxt << 4 & 32767
    return g & 12

if __name__ == "__main__":
    arg = 4
    expected = 0
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
