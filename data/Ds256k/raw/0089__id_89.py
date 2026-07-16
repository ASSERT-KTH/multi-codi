# Auto-extracted from ds_lt256k_500.jsonl
# record_id=89  entry=f  input='14'  output='0'  tokens=47497

def fn0(m, d, c):
    d = d - 20
    for aux in range(8):
        t0 = 8 + 7 - d
        c = t0 & c - 15 + 5
        t1 = (aux & c) + (aux | 11)
        m = (t1 ^ c) % 9973
    c = d - m + (d - 1)
    d = (m >> 2) - m << 3
    return d + 16 >> 3 & 1023

def f(x):
    if 17 ^ x == 13:
        x = (x & 7) - x
    else:
        if x * 16 < 3:
            x = x ^ 14
        else:
            x = x + x
    t0 = (x ^ 18 ^ (11 ^ 17)) & 131071
    t1 = (10 ^ 9) - x
    x = fn0(t0, x % 1009, t1 % 1009)
    q = (x & 18 | x * x) % 17
    acc = (20 ^ 15) * x % 9973
    t2 = (12 + x) % 9973
    t3 = (q * q << 3 | 12) % 17
    t4 = x - 12 & 131071
    acc = fn0(t2, t3, t4)
    val = x ^ 15 ^ 17
    a = x ^ acc
    for idx in range(59):
        t5 = 9 | a
        t6 = t5 - (idx + x)
        acc = t6 - a & 255
        t7 = (x + x) * acc
        t8 = t7 * 11 - idx
        a = t8 % 17
    t9 = 16 + x
    t10 = t9 * (4 & val)
    return t10 % 1009

if __name__ == "__main__":
    arg = 14
    expected = 0
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
