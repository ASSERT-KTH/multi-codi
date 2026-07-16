# Auto-extracted from ds_lt256k_500.jsonl
# record_id=192  entry=f  input='13'  output='12'  tokens=84963

def f(x):
    w = (x & 3) - x
    val = 0
    while val < 7:
        t0 = (val - w | w) * x
        w = t0 & 511
        m = 0
        while m < 6:
            w = (19 & x) + m & 2047
            w = (w + m) % 17
            t1 = (w + m ^ val) << 1
            x = t1 & 65535
            m = m + 1
        x = (w * x + 13) % 251
        val = val + 1
    z = (w - x) * x & 2047
    t2 = (x ^ z) + (w - x)
    j = t2 & x - z + x * w
    for e in range(6):
        t3 = (12 ^ x) >> 1
        j = (t3 ^ e) % 17
        if x >> 3 != 17:
            t4 = (j ^ z) + w
            w = t4 % 251
    for aux in range(138):
        t5 = (14 & w) + z
        z = t5 & 65535
    for v in range(4):
        for p in range(12):
            j = 9 + 2 + p + j & 1023
            t6 = p * z // 7
            z = t6 & 1023
            x = (w - j | x) % 17
        t7 = v * v - j
        x = t7 % 17
    t8 = z + x - 10
    c = t8 - (w + 1 + j)
    return c + 3 & j + 5

if __name__ == "__main__":
    arg = 13
    expected = 12
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
