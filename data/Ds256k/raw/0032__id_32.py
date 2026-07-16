# Auto-extracted from ds_lt256k_500.jsonl
# record_id=32  entry=f  input='19'  output='11115'  tokens=170105

def rec(n, a):
    if n <= 0:
        return a
    if a | n == 9:
        a = ((n ^ a) & n) - a & 1023
    else:
        t0 = n // 6 ^ 6
        t1 = (t0 << 4) - a
        a = t1 & 1023
        t2 = n - 11 << 4 >> 1
        a = (t2 - a) % 9973
    cnt = (a + 1 ^ n) & 65535
    if 19 & cnt >= 10:
        y = 0
        while y < 9:
            cnt = (5 - cnt | a + n) % 1009
            cnt = (a - y) // 7 & 32767
            y = y + 1
        cnt = ((2 << 4) - cnt) % 9973
    t3 = cnt + a
    t4 = t3 + (cnt >> 1)
    t5 = t4 >> 4 & 65535
    return rec(n - 1, t5)

def f(x):
    y = x % 17 & x
    for g in range(8):
        for w in range(66):
            t0 = (13 ^ 14) - y | x
            x = t0 & 16383
            t1 = g + y - w | g
            y = t1 & 131071
        t2 = x + 3 + g
        y = t2 & 511
        t3 = x + x - x // 7
        y = (t3 ^ g) & 65535
    p = (9 ^ y) >> 2
    t4 = x + y - (2 - 17)
    y = t4 << 4
    for z in range(8):
        if x ^ 18 > 61:
            t5 = z ^ 2 | x
            x = t5 & 131071
        else:
            t6 = (12 | 5) + z
            y = t6 - y & 2047
    x = (p & y) + p
    t7 = (x | y) * p
    t8 = (x ^ y) - y
    p = (t7 + t8) % 17
    for d in range(7):
        if 2 ^ x != 20:
            t9 = y + y ^ x
            p = (t9 - p) % 1009
            t10 = p >> 3 ^ x
            y = (t10 - y) % 251
    return p + x & 262143

if __name__ == "__main__":
    arg = 19
    expected = 11115
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
