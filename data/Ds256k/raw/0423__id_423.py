# Auto-extracted from ds_lt256k_500.jsonl
# record_id=423  entry=f  input='7'  output='15'  tokens=57582

def fn0(j):
    v = j * j & 32767
    for w in range(2):
        t0 = j * j + v
        v = t0 & 65535
        idx = 0
        while idx < 7:
            t1 = 14 << 4
            t2 = t1 + (12 - w)
            t3 = t2 // 4 - v
            v = t3 % 251
            idx = idx + 1
    prv = 0
    while prv < 4:
        v = prv - 19 & v
        prv = prv + 1
    t4 = j * j * j
    t5 = (v >> 3) * 14
    b = (t4 ^ t5) % 1009
    return b - 12 & (b & 13)

def f(x):
    t0 = (19 & x) + (x ^ 17)
    x = fn0(t0 & 255)
    t = 0
    while t < 499:
        x = x // 3 % 251
        t = t + 1
    t1 = 9 * x ^ x
    x = fn0(t1 << 2 & 262143)
    t2 = (x | 15) ^ x - 8
    return (t2 | 20 ^ 15 ^ 18) % 65521

if __name__ == "__main__":
    arg = 7
    expected = 15
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
