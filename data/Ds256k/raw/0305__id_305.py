# Auto-extracted from ds_lt256k_500.jsonl
# record_id=305  entry=f  input='13'  output='1'  tokens=49226

def rec(n, a):
    if n <= 0:
        return a
    t0 = (n // 4 >> 2) - a
    j = t0 % 4093
    acc = (n * a - a) % 65521
    t1 = (acc - 1 | a) & 262143
    return rec(n - 1, t1)

def fn0(d, a):
    a = a + a ^ a << 1
    t0 = 16 * 15
    t1 = t0 - d * a
    d = t1 % 9973
    d = a + 6
    t2 = (1 & 18) * 12
    t3 = (t2 ^ d) % 17
    d = rec(73, t3)
    t4 = (a | d) // 8
    return t4 % 9973

def f(x):
    aux = [175, 226, 228, 11]
    u = (x ^ 14) - x
    u = x & 10 & u
    for val in range(5):
        d = 0
        while d < 28:
            t0 = aux[val % 4]
            aux[u % 4] = x & t0
            aux[u % 4] = (val ^ x) + x
            d = d + 1
        if u - 11 != 37:
            t1 = (11 & u) * (4 ^ x) << 1
            aux[u % 4] = t1 % 251
            t2 = aux[x % 4]
            aux[x % 4] = t2 % 17
        t3 = 20 - val ^ u
        x = t3 & 511
    t4 = u ^ aux[u % 4]
    x = t4 * 11
    return ((x | 1) - u) % 97

if __name__ == "__main__":
    arg = 13
    expected = 1
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
