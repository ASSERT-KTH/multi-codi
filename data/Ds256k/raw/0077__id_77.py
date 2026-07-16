# Auto-extracted from ds_lt256k_500.jsonl
# record_id=77  entry=f  input='16'  output='2'  tokens=217878

def fn0(b):
    if b * 11 >= 57:
        b = b * 10 - b + b
        b = (1 * 7 | b) % 251
    else:
        d = 0
        while d < 8:
            t0 = d - 12 - (d | b)
            b = t0 & 18 * (b & 18)
            d = d + 1
        t1 = 1 * b & b // 8
        b = t1 >> 1
    for val in range(8):
        for e in range(9):
            b = 8 + val & (b & e)
            t2 = 9 * e >> 3 | b
            b = t2 % 17
        if b * val <= 43:
            b = val - 20 - b & 2047
        else:
            t3 = val | 9 | b
            b = t3 & 2047
            b = val * b & 18
        b = (b + val) % 1009
    if b >> 3 <= 15:
        t4 = b + b | b
        b = t4 & 262143
        for m in range(3):
            b = 9 * b & 2047
            t5 = ((10 | m) ^ m) & m
            b = (t5 - b) % 4093
    else:
        b = b - 13 - b & 4095
        t6 = b ^ 3 ^ b + b
        b = t6 & b
    t7 = b % 17
    buf = t7 | b >> 4
    cur = (3 | buf) // 2
    cur = ((cur ^ b) << 1) % 1009
    t8 = buf // 8
    t9 = t8 * (cur - 7)
    return t9 % 1009

def f(x):
    x = fn0(x - (x ^ 12) & 8191)
    for lo in range(7):
        for e in range(114):
            t0 = 16 - 6 - lo
            x = (t0 + x) % 9973
            t1 = e - 5 - x // 3
            x = (e ^ lo - 19) * t1 & 16383
        if x - lo <= 33:
            x = ((x ^ 14) + lo - lo) % 17
    t = x * x - (7 - x) & 511
    x = fn0(t >> 1 & x)
    t2 = (19 + x) // 4
    t3 = t2 - (17 << 1) - t
    return t3 % 17

if __name__ == "__main__":
    arg = 16
    expected = 2
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
