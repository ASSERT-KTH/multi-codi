# Auto-extracted from ds_lt256k_500.jsonl
# record_id=219  entry=f  input='10'  output='132'  tokens=55610

def rec(n, a):
    if n <= 0:
        return a
    for s in range(10):
        t0 = 7 * n + s - a
        a = t0 % 17
        t1 = (n ^ 20) >> 2
        t2 = t1 * s | a
        a = t2 % 251
    t3 = a - 3 ^ a
    g = t3 + n & 32767
    t4 = 16 ^ n | a
    return rec(n - 1, t4 % 17)

def f(x):
    w = (x + x ^ (x | 7)) & x
    t0 = x * 1 + 3
    p = t0 ^ w
    for lo in range(10):
        for z in range(10):
            p = 14 * w - z & 131071
            p = (x + p) % 1009
        if w ^ lo >= 7:
            t1 = x - 11 ^ (13 ^ 9)
            x = t1 % 1009
        t2 = p + 3 ^ 18 | w
        w = t2 & 1023
    for m in range(8):
        for res in range(12):
            w = (res | 3 | p) & 4095
            w = (x ^ 17 | w) & 262143
        for v in range(2):
            p = ((m ^ w) + p) % 97
            x = (v - x) * p % 97
            t3 = (v ^ p) << 2
            p = t3 % 97
    if p - x < 26:
        t4 = (x + 19 + x) % 1009
        p = rec(106, t4)
    x = (p * x & w) % 97
    w = (w & x) * w % 97
    t5 = p * p + p * p >> 1
    return t5 & 511

if __name__ == "__main__":
    arg = 10
    expected = 132
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
