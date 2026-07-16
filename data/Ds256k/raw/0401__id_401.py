# Auto-extracted from ds_lt256k_500.jsonl
# record_id=401  entry=f  input='14'  output='8'  tokens=216598

def f(x):
    t0 = 13 | 1 | 3
    t1 = (11 & x) << 2
    nxt = t0 | t1
    tmp = (nxt ^ 15) * x >> 4
    if tmp | 13 < 63:
        if x | nxt == 33:
            tmp = x + 17
        t2 = (nxt | 10) * (17 * x)
        t3 = ((13 ^ x) << 4) * t2
        tmp = t3 % 4093
    tmp = tmp * x
    tmp = (tmp + x ^ 13 - nxt) >> 4
    for y in range(847):
        nxt = x * nxt % 65521
        nxt = (nxt | x) % 9973
        x = (6 ^ x) % 97
    return (x ^ tmp) & x

if __name__ == "__main__":
    arg = 14
    expected = 8
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
