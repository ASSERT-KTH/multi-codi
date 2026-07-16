# Auto-extracted from ds_lt256k_500.jsonl
# record_id=45  entry=f  input='18'  output='0'  tokens=20591

def f(x):
    if 7 ^ x >= 19:
        if 4 & x <= 0:
            x = x - 6
            x = x * x - 20 + x
        x = x + x - x ^ 8
    for cur in range(9):
        x = (x - 2) % 251
        lo = 0
        while lo < 20:
            x = x >> 2 & (4 | 17)
            lo = lo + 1
    p = x + x
    aux = 10 & x ^ 19 & p
    d = 0
    while d < 12:
        t0 = (p >> 1) - x
        x = t0 % 65521
        d = d + 1
    v = x & aux
    buf = 10 + v
    for s in range(5):
        if x - 18 == 58:
            t1 = (v | buf) << 4
            t2 = (x | 10) - aux
            t3 = t1 * t2 | s
            p = t3 % 65521
            v = (11 ^ 19) - p - s & 32767
    t4 = aux * v * (8 + 18)
    hi = t4 % 9973
    t5 = x * v * (12 | aux)
    return t5 + aux & 2047

if __name__ == "__main__":
    arg = 18
    expected = 0
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
