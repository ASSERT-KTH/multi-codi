# Auto-extracted from ds_lt256k_500.jsonl
# record_id=370  entry=f  input='8'  output='282'  tokens=13518

def f(x):
    j = (x - 4) * x - x
    t0 = (j >> 4) - (j | 10)
    z = 1 + j + j + t0
    for t in range(66):
        z = (x - 18) * z % 65521
        x = (x * 4 * x - z) % 1009
        if x - z < 7:
            j = ((x & j | j) ^ x) & 511
            z = (t * 6 + j) % 17
    t1 = j % 17 * z
    hi = t1 * 16 % 1009
    buf = hi * 18 + 8
    y = z + buf
    t2 = (y & buf) * (15 ^ y)
    m = t2 & 8191
    t3 = j * hi
    t4 = (8 | x) - 4
    t5 = t3 * (10 | m)
    a = (t4 | t5) % 17
    p = (m ^ a) + z
    return j & 16383

if __name__ == "__main__":
    arg = 8
    expected = 282
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
