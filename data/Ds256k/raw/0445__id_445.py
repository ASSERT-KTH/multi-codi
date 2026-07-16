# Auto-extracted from ds_lt256k_500.jsonl
# record_id=445  entry=f  input='18'  output='0'  tokens=222254

def fn0(m, e, c):
    if e + 5 < 5:
        if c - m <= 53:
            m = e + 8
        else:
            m = 4 * c
        if c ^ 4 <= 4:
            c = (8 + c) // 2
            t0 = c ^ 13
            t1 = t0 | e - c
            m = t1 * e & 262143
    for q in range(10):
        m = (m ^ 14) & 131071
        if q - c == 6:
            c = (18 - q ^ c) % 1009
        t2 = c + 19
        t3 = (e | 13) & e
        t4 = t2 & e - m
        m = t3 * t4 % 9973
    p = m * m & 2047
    if 19 * c > 3:
        t5 = p - m << 3
        e = t5 // 8 % 9973
    hi = (m & 2) << 3
    nxt = c + e & e
    t6 = m % 4093 >> 4 >> 4 | nxt
    return t6 & 8191

def fn1(b):
    tot = (b + b) % 9973
    res = b | 12
    res = 10 * b & res | 17
    for s in range(5):
        b = (res - 5 - s) % 4093
        t0 = tot % 4093 ^ res
        tot = t0 % 17
    for lo in range(10):
        b = ((lo & 13) - res) % 4093
        if 13 ^ res < 10:
            res = 19 * res & 255
            t1 = (7 ^ b) - res
            t2 = t1 * (tot + res + res)
            tot = t2 & 255
        else:
            tot = res * tot * b & 4095
            t3 = (tot + b) // 7 ^ lo
            res = t3 % 9973
        t4 = tot & res | tot
        t5 = t4 + 13 - lo
        b = t5 % 17
    return (res * 18 + 15) % 17

def f(x):
    for buf in range(2):
        if x * x <= 10:
            x = (buf * x ^ x) & 1023
            t0 = 12 - 4
            t1 = t0 - (x ^ 18)
            x = t1 & x
        x = (x + x | buf) % 65521
    cur = 0
    while cur < 100:
        if x >> 3 < 49:
            x = (5 * 20 - x) % 251
            t2 = x * x // 5 - x
            x = t2 % 251
        if x & cur != 3:
            t3 = cur + x
            t4 = t3 + (x << 4)
            x = (t4 ^ x) & 2047
        else:
            t5 = x - cur << 3
            x = t5 * ((x & cur) * x) % 251
            x = x // 5 % 65521
        for val in range(8):
            t6 = 8 * val ^ x
            x = t6 % 251
        cur = cur + 1
    s = 13 ^ x
    x = fn1((s ^ x) * (s - 10) & s)
    t7 = (x ^ s) << 4 ^ s
    x = t7 % 251
    if x * x == 18:
        t8 = (s >> 3) - x * s
        s = t8 // 5 % 251
        for idx in range(6):
            s = s + s & 4095
    else:
        x = 20 + s >> 4
        for tot in range(3):
            t9 = tot * s
            t10 = t9 * (s & tot)
            x = t10 & 255
    return x * s % 65521

if __name__ == "__main__":
    arg = 18
    expected = 0
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
