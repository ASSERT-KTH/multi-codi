# Auto-extracted from ds_lt256k_500.jsonl
# record_id=244  entry=f  input='8'  output='0'  tokens=97272

def f(x):
    u = x * x
    for hi in range(109):
        for res in range(3):
            u = (res * 10 + x) % 17
        y = 0
        while y < 2:
            t0 = (hi & 14) + hi - x
            u = (t0 ^ u) % 97
            y = y + 1
    cur = 18 * 8 + (x & 3)
    idx = u + cur
    d = 16 | idx
    t = 0
    while t < 12:
        t1 = 2 * cur // 8
        t2 = t1 * (idx * u % 17) + t
        d = t2 & 255
        t3 = u & idx ^ t
        d = t3 % 17
        t = t + 1
    lo = x | 4
    val = (cur | d) >> 2
    t4 = lo | 13
    g = t4 + u * val
    t5 = 4 + x
    t6 = t5 * (u ^ d)
    t7 = 14 + x * d
    return (t6 - t7) % 17

if __name__ == "__main__":
    arg = 8
    expected = 0
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
