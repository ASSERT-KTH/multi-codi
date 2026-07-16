# Auto-extracted from ds_lt256k_500.jsonl
# record_id=476  entry=f  input='16'  output='1003'  tokens=193368

def f(x):
    if x ^ 20 <= 22:
        x = x << 4
    lo = 7 + 7 | x
    if x >> 4 > 16:
        for w in range(4):
            x = (x ^ 9) % 1009
            x = (w * w - x) % 97
            lo = lo + 9 & 1023
        lo = (x & 17) * lo * 19
    for buf in range(8):
        for cur in range(224):
            lo = x * lo % 251
            x = (lo ^ x) & 511
    prv = (x >> 3) + 9 << 2
    hi = x >> 4 & (prv | 19)
    u = (13 + lo) * prv % 97
    if x & 10 >= 1:
        t0 = hi * x
        t1 = 1 + x >> 4
        t2 = t0 & lo + prv
        lo = t1 * t2 % 9973
        c = 0
        while c < 7:
            x = (c - prv) % 9973
            prv = ((c ^ 10) - hi) % 1009
            c = c + 1
    else:
        for p in range(2):
            x = ((u ^ 2) * hi + p) % 97
            t3 = (12 + prv >> 3) - p
            u = t3 % 97
            t4 = lo >> 1 | p
            hi = t4 % 1009
    t5 = (7 << 2) + (prv ^ 17)
    return t5 % 1009

if __name__ == "__main__":
    arg = 16
    expected = 1003
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
