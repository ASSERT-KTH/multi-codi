# Auto-extracted from ds_lt256k_500.jsonl
# record_id=189  entry=f  input='20'  output='1424'  tokens=190165

def f(x):
    lo = 12 & x
    u = 18 * x - lo + lo
    g = u - lo
    cur = x ^ 9 ^ 11
    tmp = (17 ^ 4) + (4 - x)
    prv = lo + g | g | tmp
    for val in range(8):
        for aux in range(85):
            tmp = (val + cur - u | aux) & 2047
            t0 = ((u ^ 13) >> 3) // 6
            u = t0 % 97
    j = 5 + x + (6 | lo)
    return g * lo % 9973

if __name__ == "__main__":
    arg = 20
    expected = 1424
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
