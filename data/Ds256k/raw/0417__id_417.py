# Auto-extracted from ds_lt256k_500.jsonl
# record_id=417  entry=f  input='11'  output='1'  tokens=13629

def f(x):
    if 7 + 15 - x > 31:
        x = 18 ^ x ^ x + x
        x = x * x
    lo = x & 19
    for j in range(17):
        t0 = x - 6 + (x ^ lo)
        lo = t0 & j
        for aux in range(5):
            x = (13 | x) & 17
            x = aux & lo
    a = (lo ^ 13) * x
    t1 = (lo | 10) * (lo << 3) * a
    prv = t1 & 511
    if x - lo > 26:
        t2 = (x ^ prv) + a
        lo = t2 & lo * a - a
    else:
        a = a + lo - 4
        t3 = 19 + a
        t4 = (x | prv) << 1
        t5 = t3 * (lo + a)
        a = (t4 ^ t5) % 17
    return (a & x | a) & 2047

if __name__ == "__main__":
    arg = 11
    expected = 1
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
