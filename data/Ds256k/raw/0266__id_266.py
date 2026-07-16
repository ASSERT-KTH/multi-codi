# Auto-extracted from ds_lt256k_500.jsonl
# record_id=266  entry=f  input='18'  output='5503'  tokens=103032

def rec(n, a):
    if n <= 0:
        return a
    a = (5 - a) % 251
    t0 = n * n - a & 32767
    return rec(n - 1, t0)

def f(x):
    if x - 9 != 19:
        if x * x <= 31:
            t0 = (x | 2) ^ x
            x = t0 - x
        else:
            t1 = x // 3 * x & 65535
            x = rec(41, t1)
    else:
        p = 0
        while p < 3:
            t2 = (x >> 4) * (x & 9)
            x = t2 % 9973
            t3 = (p & 5) + (p | 10) ^ x
            x = t3 % 251
            p = p + 1
    t4 = x + x + (x | 12)
    t5 = (t4 - x) % 9973
    x = rec(69, t5)
    for tmp in range(7):
        t6 = x | 3 | 19
        x = t6 % 9973
    for hi in range(239):
        t7 = ((hi << 3) - hi ^ hi) + x
        x = t7 % 9973
        t8 = hi + 17 ^ x
        x = t8 & 32767
    if x ^ 7 >= 31:
        x = x | 10
    else:
        x = (x & 12) << 3
        x = x + x
    return (x + x) * (x ^ 1) % 9973

if __name__ == "__main__":
    arg = 18
    expected = 5503
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
