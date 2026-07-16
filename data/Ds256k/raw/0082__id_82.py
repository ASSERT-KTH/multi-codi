# Auto-extracted from ds_lt256k_500.jsonl
# record_id=82  entry=f  input='2'  output='66'  tokens=20920

def fn0(b):
    z = [105, 79, 4, 151, 33]
    t0 = b ^ z[b % 5]
    w = t0 ^ b
    d = b & 2 & b
    res = d & z[d % 5] & b
    w = 17 * d
    t1 = d - 3
    t2 = t1 + (16 & w)
    return t2 + b & 2047

def fn1(m, c):
    lo = m - 14
    for hi in range(9):
        t0 = (8 + m) // 2
        t1 = t0 | hi + c - lo
        c = t1 % 9973
        t2 = c + c - hi
        lo = t2 & lo
    if c // 5 <= 27:
        for z in range(11):
            t3 = (m + 14) * (lo + 19)
            c = (t3 - m ^ z) % 9973
            t4 = 1 ^ lo ^ c
            c = t4 % 97
            t5 = c | lo
            t6 = t5 & 10 * z
            t7 = 9 * 1 << 3
            c = t6 + t7 & 255
        m = fn0(lo * lo % 4093)
    t8 = (20 ^ 1) - (m >> 3)
    aux = t8 // 4
    c = fn0(m + aux + c - m & 65535)
    idx = (m ^ aux) // 2 | c
    return (idx + c | aux) % 9973

def f(x):
    y = x - 12 ^ x * x
    t0 = (y & x) - (x + x)
    y = t0 + (19 ^ y)
    x = y - 7 ^ x + y
    x = (2 << 2) * y
    for m in range(45):
        x = (m << 1) + y & 2047
        if m - x < 30:
            t1 = x | 5
            t2 = t1 | m * 14
            t3 = (y - x) // 8
            x = (t2 - t3) % 97
        y = (x | m) & 20 - y
    y = x // 4 * y % 4093
    return (x ^ y) % 65521

if __name__ == "__main__":
    arg = 2
    expected = 66
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
