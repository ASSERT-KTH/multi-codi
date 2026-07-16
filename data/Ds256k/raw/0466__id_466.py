# Auto-extracted from ds_lt256k_500.jsonl
# record_id=466  entry=f  input='14'  output='0'  tokens=32267

def fn0(j, a, b):
    hi = 8 << 4 ^ a
    if b - 10 <= 63:
        hi = hi & 3
        t0 = (j % 9973 - a) * 19
        b = t0 % 4093
    d = (a ^ 9) >> 3
    d = (a | 17) - (j - 3) & 20
    d = j - hi + d
    hi = b ^ hi
    return (20 - b + d) % 65521

def f(x):
    t0 = 6 - x
    p = t0 ^ x + 9
    g = 16 + x - p
    t1 = (11 + g) * (g // 7)
    c = t1 - (p << 1 ^ x)
    t2 = c - 15 | c
    t3 = (p - 19 - 10) % 251
    t4 = (g + 9) % 1009
    x = fn0(t2 & 4095, t3, t4)
    for s in range(8):
        v = 0
        while v < 10:
            x = 1 + x & 255
            x = g * (c - v) & 131071
            v = v + 1
        t5 = 9 + p - x
        x = t5 & 511
    buf = g * x % 1009
    t6 = buf + buf
    t7 = t6 - (x & 16)
    aux = t7 & x
    t8 = 8 * x & aux
    t9 = (t8 - 5) % 251
    t10 = (c - g) * x + aux
    t11 = (aux ^ buf) & 65535
    buf = fn0(t9, t10 & 255, t11)
    return (c & aux) >> 2 & 131071

if __name__ == "__main__":
    arg = 14
    expected = 0
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
