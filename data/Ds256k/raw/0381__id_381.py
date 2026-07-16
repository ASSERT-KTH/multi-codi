# Auto-extracted from ds_lt256k_500.jsonl
# record_id=381  entry=f  input='16'  output='216'  tokens=254419

def rec(n, a):
    if n <= 0:
        return a
    z = n + a & a
    t0 = (n - a) // 5
    t1 = n - 12 | a
    res = (t0 ^ t1) & 32767
    t2 = ((res | 5) + n - a) % 65521
    return rec(n - 1, t2)

def f(x):
    if x - 9 < 20:
        x = (x ^ 18) * x
        x = x * x
    t0 = x - 11 ^ x
    t1 = (t0 ^ x) % 9973
    x = rec(118, t1)
    res = 0
    while res < 7:
        t = 0
        while t < 2:
            t2 = x % 4093 // 8
            x = t2 & 255
            t3 = res ^ 7 | 20
            x = t3 + x & 4095
            t = t + 1
        w = 0
        while w < 75:
            t4 = (res << 1) * (res ^ 1)
            t5 = res + 17 - w ^ t4 ^ x
            x = t5 % 4093
            w = w + 1
        res = res + 1
    b = x % 4093
    lo = 3 * x & 16383
    for u in range(9):
        for acc in range(2):
            t6 = x + x - u + b
            b = t6 & 32767
            t7 = lo // 5 >> 4
            t8 = t7 * (b + acc ^ 1)
            x = t8 & 1023
            b = b // 4 & 4095
    return (b + 8) * (lo | 5) % 9973

if __name__ == "__main__":
    arg = 16
    expected = 216
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
