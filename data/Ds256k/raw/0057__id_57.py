# Auto-extracted from ds_lt256k_500.jsonl
# record_id=57  entry=f  input='4'  output='326'  tokens=90295

def f(x):
    if x ^ 10 <= 11:
        x = x * x
        x = x * x
    for hi in range(154):
        t0 = (hi ^ x) * (hi * x)
        x = t0 % 9973
        for res in range(3):
            t1 = 19 * hi + x
            x = t1 % 1009
    buf = x // 2 - x % 1009
    tot = x // 8 >> 4
    for d in range(10):
        x = x - 8 >> 2 & 8191
        t2 = x // 5 % 9973
        x = (t2 << 1) % 9973
        tot = (tot // 3 - tot) % 1009
    t3 = (x // 3 * 17 >> 3) - buf
    return t3 & 4095

if __name__ == "__main__":
    arg = 4
    expected = 326
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
