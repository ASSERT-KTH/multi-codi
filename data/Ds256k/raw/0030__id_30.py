# Auto-extracted from ds_lt256k_500.jsonl
# record_id=30  entry=f  input='6'  output='9942'  tokens=172353

def f(x):
    g = x
    j = x + g
    g = 20 + 17 ^ x
    j = j & g
    t0 = 19 + x + j
    x = t0 + g
    b = 0
    while b < 7:
        for tot in range(145):
            t1 = ((b - j) * g << 1) - x
            x = t1 & 262143
        b = b + 1
    return ((8 * 9 >> 4) - g) % 9973

if __name__ == "__main__":
    arg = 6
    expected = 9942
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
