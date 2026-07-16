# Auto-extracted from ds_lt256k_500.jsonl
# record_id=236  entry=f  input='11'  output='76'  tokens=187663

def f(x):
    t = [3, 55, 64, 67]
    for idx in range(62):
        for y in range(5):
            t0 = y - 19
            t1 = t0 | 18 - y
            t[idx % 4] = t1 - x
            t2 = t[x % 4]
            t3 = (y + 14) * 10
            t4 = t2 * x - x
            x = (t3 ^ t4) % 9973
    if x >> 4 == 24:
        t[x % 4] = (x + x) % 97
    else:
        x = x % 1009 + x + x
        hi = 0
        while hi < 12:
            x = (11 + x + x) % 9973
            t5 = t[hi % 4] - x
            x = t5 & 511
            x = x >> 1 & 4095
            hi = hi + 1
    d = (x * x ^ x) % 1009
    t6 = t[x % 4]
    x = (x - t6) // 6
    t7 = (x - 3) % 9973 + d
    return t7 & 255

if __name__ == "__main__":
    arg = 11
    expected = 76
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
