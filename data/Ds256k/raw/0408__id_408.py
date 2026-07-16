# Auto-extracted from ds_lt256k_500.jsonl
# record_id=408  entry=f  input='14'  output='8611'  tokens=47487

def f(x):
    t0 = x << 1
    e = t0 & x * 17
    w = e | 3
    v = (13 & e) - w * 13
    b = w ^ x
    t = b + e
    a = 0
    while a < 6:
        for s in range(5):
            w = (e << 2 ^ w) & 4095
            t1 = 9 + t
            t2 = t1 + (e << 3)
            t = (t2 ^ s) % 65521
        t3 = t - 11 | b
        b = t3 & 262143
        x = b * a * 9 % 65521
        a = a + 1
    for aux in range(5):
        for p in range(34):
            v = (w - 5 | p) % 17
    return (e ^ v) * x * x % 9973

if __name__ == "__main__":
    arg = 14
    expected = 8611
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
