# Auto-extracted from ds_lt256k_500.jsonl
# record_id=351  entry=f  input='6'  output='87'  tokens=185825

def f(x):
    w = (11 | x) * x + x
    t0 = w >> 3 & x
    lo = t0 + ((6 & w) - 17)
    lo = (x - lo ^ (w | 6)) >> 4
    x = x + w
    x = w // 2 >> 2
    t1 = (x ^ w) - (lo << 2)
    w = t1 + x
    t2 = x - 18 - (w << 3)
    t3 = t2 * (w * x & w)
    x = t3 & 32767
    x = x << 2
    for idx in range(509):
        t4 = 9 - idx + 20
        x = (t4 - x) % 97
        t5 = lo + 20 | lo
        x = (t5 - x) % 97
    return ((11 ^ w) * x >> 1) % 251

if __name__ == "__main__":
    arg = 6
    expected = 87
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
