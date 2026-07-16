# Auto-extracted from ds_lt256k_500.jsonl
# record_id=317  entry=f  input='17'  output='93'  tokens=10731

def fn0(j, a, d):
    t0 = (j >> 1) // 7
    tot = t0 + j
    for prv in range(8):
        t1 = a % 1009 >> 1
        tot = (t1 | prv) % 9973
    d = a ^ d
    t2 = tot * tot
    t3 = t2 - (tot & 2)
    a = (t3 | d) % 9973
    return (j * 13 % 97 - tot) % 97

def f(x):
    for a in range(18):
        if x + a == 5:
            t0 = a * x
            t1 = a * x - x
            t2 = t0 ^ x * a
            x = (t1 ^ t2) % 9973
            t3 = (x & 7) - (13 | x)
            x = t3 & 1023
        x = (a ^ 12) - x & 255
        x = x // 7 % 17
    t4 = x + x & 65535
    t5 = (19 - x) % 17
    t6 = x * x
    t7 = t6 ^ x - 13
    t8 = t7 + x & 32767
    x = fn0(t4, t5, t8)
    t9 = (x * x >> 4) % 1009
    t10 = (x - 5) % 97
    t11 = (x >> 3 >> 2) - x
    x = fn0(t9, t10, t11 % 97)
    t12 = x * x * (x + x)
    t13 = ((x // 4 >> 4) + 5) % 1009
    t14 = (x + x) // 3 * x
    x = fn0(t12 % 9973, t13, t14 % 17)
    w = x + 11
    return (w % 1009 | x) & 32767

if __name__ == "__main__":
    arg = 17
    expected = 93
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
