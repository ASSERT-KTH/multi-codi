# Auto-extracted from ds_lt256k_500.jsonl
# record_id=207  entry=f  input='17'  output='502'  tokens=167294

def rec(n, a):
    if n <= 0:
        return a
    if 10 - a == 53:
        if n << 1 | a != 34:
            t0 = 10 + n + n * 16
            a = (t0 | n * a >> 2) % 9973
        a = (n // 8 + a) % 1009
    t1 = (4 | a) & 255
    return rec(n - 1, t1)

def fn0(d, c):
    acc = (3 | 20) ^ c
    t0 = (acc >> 3 ^ (d | 6)) * acc
    d = rec(41, t0 % 9973)
    for tmp in range(3):
        t1 = 10 | tmp
        t2 = t1 | c * tmp
        t3 = (acc | 15) - 7
        c = (t2 - t3) % 65521
        if tmp - 13 | acc == 30:
            acc = d * d - acc & 65535
            d = (tmp | c) % 65521
        else:
            acc = tmp - acc & 255
            d = (d * tmp ^ tmp) & 131071
        d = (c | tmp) * acc % 65521
    z = (acc >> 2) // 4 - c
    val = z * 19 + acc >> 3
    return 16 + z & 8191

def f(x):
    t0 = x - 10
    a = t0 - x * x
    for w in range(4):
        x = x + x - a + x & 1023
        b = 0
        while b < 4:
            x = (15 * b ^ x) % 4093
            b = b + 1
        for cnt in range(12):
            t1 = (w - 1) * a
            a = t1 & 4095
    t2 = (x + a) % 9973
    x = fn0(t2, x % 9973)
    for lo in range(647):
        t3 = lo - x | lo
        x = t3 >> 4 & 131071
    idx = x >> 1
    c = 0
    while c < 9:
        a = (11 * 12 - idx - a) % 1009
        c = c + 1
    t4 = (15 - 2 ^ a) % 1009
    a = rec(37, t4)
    if a >> 4 == 51:
        t5 = (x ^ idx) >> 4
        t6 = idx // 4 & 7
        t7 = t6 + 10 & 262143
        x = fn0(t5 & 1023, t7)
    t8 = (x + x + (a + a)) // 3
    return t8 & 2047

if __name__ == "__main__":
    arg = 17
    expected = 502
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
