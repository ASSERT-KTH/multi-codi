# Auto-extracted from ds_lt256k_500.jsonl
# record_id=339  entry=f  input='7'  output='0'  tokens=193168

def f(x):
    tot = x - 14
    x = tot * tot
    x = 13 * x ^ 6
    x = (tot + tot) * tot
    x = x + x + 9
    tot = x * tot % 17
    for val in range(77):
        x = (x * val ^ tot) & 2047
        for q in range(7):
            t0 = 11 * q >> 2
            t1 = t0 * ((13 - tot) * 8)
            x = t1 & 32767
            t2 = val + 16 + (tot + val)
            tot = t2 % 97
    if x ^ tot > 45:
        if x << 3 > 35:
            tot = tot + 3
            t3 = (x ^ 6) * (x | tot)
            t4 = (x | tot) & x >> 2
            x = t3 & t4
        tot = tot << 2
    t5 = x | 3
    t6 = t5 + (tot | 17)
    return t6 * x & 1023

if __name__ == "__main__":
    arg = 7
    expected = 0
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
