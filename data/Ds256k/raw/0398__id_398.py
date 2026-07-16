# Auto-extracted from ds_lt256k_500.jsonl
# record_id=398  entry=f  input='7'  output='43'  tokens=85373

def f(x):
    t0 = x + x
    q = t0 & 2 * x
    for v in range(10):
        x = (q + v) % 9973
        for idx in range(12):
            q = (q * q + 5 + x) % 1009
    for prv in range(2):
        if x + prv != 24:
            q = ((q & 7) * prv | prv) % 9973
        x = q * x % 9973
        t1 = x // 4 // 5
        q = (t1 | q) & 511
    t2 = 16 + 11
    t3 = x - 17
    t4 = t2 | x + x
    t5 = t3 - (x + 2)
    x = t4 - t5
    for t in range(13):
        q = (1 * q + x) % 9973
        for lo in range(7):
            t6 = (lo | x) - (t ^ 10) >> 1
            x = t6 % 4093
        for buf in range(6):
            t7 = buf - x | 17
            t8 = t7 + ((buf & 12) + buf)
            q = t8 % 1009
    t9 = q - x
    x = t9 ^ q // 4
    q = (x % 9973 ^ q) >> 4
    t10 = x % 1009
    t11 = t10 ^ x & 20
    t12 = (t11 >> 4) - q
    return t12 % 1009

if __name__ == "__main__":
    arg = 7
    expected = 43
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
