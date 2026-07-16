# Auto-extracted from ds_lt256k_500.jsonl
# record_id=338  entry=f  input='11'  output='16383'  tokens=97758

def f(x):
    w = (x | 9) - (x | 7)
    prv = w ^ x
    for tot in range(4):
        hi = 0
        while hi < 4:
            t0 = (prv // 4 ^ tot) + hi
            x = t0 % 97
            t1 = hi ^ 15 | prv
            prv = t1 & 16383
            prv = prv // 5 // 2 & 4095
            hi = hi + 1
        if prv | w > 40:
            x = (tot * x | tot) & 131071
        prv = ((tot << 4) - x) % 17
    z = 0
    while z < 226:
        x = (prv * 7 ^ x) % 97
        x = (x ^ z | prv) % 17
        t2 = x + prv + (x - 20)
        x = t2 & 511
        z = z + 1
    for p in range(9):
        w = w >> 2 & 4095
    cnt = x * w // 3 % 17
    t3 = prv % 17
    s = t3 - cnt * 1
    return (prv - 13) // 8 & 16383

if __name__ == "__main__":
    arg = 11
    expected = 16383
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
