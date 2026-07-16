# Auto-extracted from ds_lt256k_500.jsonl
# record_id=237  entry=f  input='7'  output='16'  tokens=34972

def rec(n, a):
    if n <= 0:
        return a
    t0 = (n * n - 3) * n | a
    s = t0 % 9973
    t1 = (a + n) * (8 - n)
    return rec(n - 1, t1 & 16383)

def f(x):
    acc = x - 4
    z = 18 ^ x
    tmp = (z | 18) << 4
    acc = rec(51, z & 12)
    cnt = tmp % 251 - (17 | z) | z
    if x & tmp >= 15:
        t0 = (9 ^ 7) + 5
        z = t0 - tmp
        if z & acc <= 14:
            acc = (z >> 2) // 6 & acc
        else:
            t1 = (5 - cnt) % 251
            acc = rec(46, t1)
            t2 = 15 + z & 4095
            acc = rec(69, t2)
    else:
        x = (tmp | 8) & acc * x
        x = 11 + tmp
    for val in range(14):
        for e in range(8):
            t3 = acc - 5 - e
            z = t3 & 131071
        if tmp >> 2 <= 39:
            acc = ((val * x >> 4) + z) % 1009
            x = (acc ^ x) * 9 % 251
    for q in range(2):
        t4 = tmp - x - q * q
        t5 = q - 12 + cnt - t4
        acc = t5 & 1023
        acc = (q ^ 6) - x & 8191
    t6 = (tmp ^ cnt) % 1009 >> 4
    return t6 % 1009

if __name__ == "__main__":
    arg = 7
    expected = 16
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
