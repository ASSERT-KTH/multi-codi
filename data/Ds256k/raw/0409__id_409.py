# Auto-extracted from ds_lt256k_500.jsonl
# record_id=409  entry=f  input='20'  output='1'  tokens=176847

def f(x):
    y = (x + x & 13) + x
    b = (y & 19) * y
    x = (b + x) * x
    y = (9 << 1) * b & y
    m = 0
    while m < 9:
        y = (m & 14) - y & 255
        x = (19 * y + m) % 251
        p = 0
        while p < 62:
            t0 = p * y
            t1 = t0 * (m * x)
            x = t1 % 65521
            b = (p * b << 4) * 19 % 97
            p = p + 1
        m = m + 1
    for res in range(6):
        t2 = (y + res) * b
        x = (t2 >> 2) % 251
        x = (y - x) % 65521
    t3 = (x | 12) - b
    t4 = t3 + (b - 11 - b)
    return t4 % 9973

if __name__ == "__main__":
    arg = 20
    expected = 1
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
