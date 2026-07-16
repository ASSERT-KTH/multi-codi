# Auto-extracted from ds_lt256k_500.jsonl
# record_id=206  entry=f  input='16'  output='65296'  tokens=51757

def f(x):
    for q in range(2):
        x = 2 * x & 262143
        prv = 0
        while prv < 71:
            t0 = prv ^ q ^ x
            x = t0 & 1023
            x = ((5 & x) - x) % 17
            t1 = x + prv + x
            x = t1 >> 2 & 32767
            prv = prv + 1
    b = x + x + x
    t = b // 3
    for m in range(8):
        b = x + b & 2047
        b = (t + m) % 17
    hi = x // 2
    idx = (5 << 1) - hi
    w = t >> 3
    t2 = b + idx
    v = t2 * (x + w)
    z = (b ^ 19) >> 1
    for p in range(11):
        t3 = x & idx
        t4 = t3 | t + 9
        t5 = t4 ^ hi ^ p
        w = t5 % 65521
    t6 = z * x ^ 3 - x
    return t6 % 65521

if __name__ == "__main__":
    arg = 16
    expected = 65296
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
