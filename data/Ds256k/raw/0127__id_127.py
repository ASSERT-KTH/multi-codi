# Auto-extracted from ds_lt256k_500.jsonl
# record_id=127  entry=f  input='3'  output='98'  tokens=200212

def rec(n, a):
    if n <= 0:
        return a
    a = n & a
    a = a - 5 & 32767
    t0 = (5 * n >> 1 | a) & 4095
    return rec(n - 1, t0)

def f(x):
    d = [10, 58, 26, 8, 6, 43]
    t0 = x & d[x % 6]
    q = t0 - x * 1 * 6
    if 6 + 1 | x <= 24:
        for a in range(9):
            d[q % 6] = x + a & 6
            x = (q - x) % 65521
    else:
        x = x // 8
        if x - q > 55:
            x = x + x >> 1
    x = 3 & x
    x = x & 9 | x
    q = 1 * q + 19
    q = x ^ 19 ^ q // 7
    t1 = 11 + x & x
    x = rec(34, t1)
    t2 = d[x % 6] * q // 5
    for p in range(12):
        for lo in range(3):
            d[p % 6] = (lo & 12 | q) % 97
            d[p % 6] = (6 + x) % 97
            d[q % 6] = ((x | 19) & (x | q)) % 97
        for m in range(30):
            t3 = q ^ d[m % 6]
            t4 = d[p % 6] | p
            t5 = t3 + d[x % 6] // 4
            x = t5 * ((q - m) * t4) % 251
        t6 = x - p + p
        x = t6 // 2 & 1023
    return t2 & 65535

if __name__ == "__main__":
    arg = 3
    expected = 98
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
