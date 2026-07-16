# Auto-extracted from ds_lt256k_500.jsonl
# record_id=376  entry=f  input='6'  output='2356'  tokens=86832

def f(x):
    cur = x & 9
    for val in range(8):
        for prv in range(40):
            cur = (x | cur) % 97
            x = 9 - cur + x & 511
            t0 = (cur ^ val) + x
            x = t0 % 1009
    for z in range(2):
        u = 0
        while u < 10:
            x = 9 * x % 1009
            cur = ((20 ^ x) + u) % 9973
            t1 = z + 14 - (u ^ cur)
            x = t1 % 97
            u = u + 1
        t2 = cur + z
        t3 = t2 + (7 + cur)
        cur = t3 % 9973
        for hi in range(9):
            cur = (hi ^ 19 ^ x) % 9973
            x = 13 + x & 32767
    if x >> 2 < 43:
        t4 = x // 8 + cur * 8
        t5 = t4 * ((cur ^ 16) // 8)
        x = t5 & 262143
    for tot in range(4):
        t6 = x ^ cur | x
        cur = t6 * 13 & 1023
        x = (14 - tot | x) % 9973
    t7 = cur + cur + (cur - 18)
    return (t7 ^ cur) % 9973

if __name__ == "__main__":
    arg = 6
    expected = 2356
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
