# Auto-extracted from ds_lt256k_500.jsonl
# record_id=326  entry=f  input='9'  output='51'  tokens=17298

def fn0(c, b):
    c = c ^ 10
    b = 15 & c
    for w in range(9):
        c = (b - 18 + w) % 17
        t0 = c - b ^ (b | 9)
        b = t0 % 4093
        b = (c + w - 4) // 2 % 97
    if b >> 1 != 61:
        c = (b - 15) % 17
        b = b + b
    for tot in range(2):
        c = (c + 20) % 17
    b = b - 4
    if 4 | c <= 57:
        c = ((b | 19) << 3) % 17
    else:
        c = b ^ 11
    return (b ^ 20) % 97

def f(x):
    if x * x >= 49:
        t0 = 10 + x
        t1 = t0 | (x | 8)
        t2 = (t1 >> 2) % 251
        x = fn0(t2, x & 20)
        t3 = x ^ 7
        t4 = t3 * (x // 3)
        x = t4 + x & 32767
    t5 = x | 19
    t6 = t5 + (x ^ 11)
    t7 = (x - 12) * x
    t8 = (t6 | t7) & 2047
    x = fn0(x & 6, t8)
    for y in range(20):
        x = x >> 4 & y
    hi = (x | 17) << 3
    q = (x - hi) * 8 // 5 & 511
    t9 = hi + hi
    t10 = t9 + q // 3
    t11 = (19 - hi) % 251
    hi = fn0(t10 % 97, t11)
    for lo in range(8):
        if 6 * 14 - x <= 32:
            q = ((3 ^ 13) + q) % 251
            t12 = (q - hi & q >> 3) + 5
            hi = t12 % 251
        else:
            t13 = lo ^ 16 | q
            hi = t13 & 1023
            hi = (7 - x + lo) % 251
    b = (hi + hi) % 251
    return (q ^ 8) % 251

if __name__ == "__main__":
    arg = 9
    expected = 51
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
