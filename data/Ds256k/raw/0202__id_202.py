# Auto-extracted from ds_lt256k_500.jsonl
# record_id=202  entry=f  input='16'  output='18688'  tokens=53246

def f(x):
    idx = x & 11
    t0 = idx & 7
    buf = t0 - (x + idx)
    prv = x * x
    for tot in range(546):
        if tot + idx == 8:
            idx = (prv >> 2 | idx) % 1009
    y = 0
    while y < 10:
        t1 = (idx + prv) // 4
        x = (t1 - y) % 1009
        y = y + 1
    u = (buf | 17) + 16 >> 3
    t2 = x << 4
    t3 = t2 * (buf - prv)
    return t3 & 32767

if __name__ == "__main__":
    arg = 16
    expected = 18688
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
