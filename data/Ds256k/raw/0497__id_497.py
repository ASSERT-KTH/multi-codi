# Auto-extracted from ds_lt256k_500.jsonl
# record_id=497  entry=f  input='9'  output='65520'  tokens=10177

def fn0(m, a):
    t0 = (m + a) * (a // 3)
    g = (t0 >> 3) % 1009
    acc = (18 & a) + 17
    a = m * m >> 3 & 8191
    t1 = (m | 7) - m
    a = t1 % 1009
    acc = (g ^ acc) - g
    acc = m | g
    for tot in range(9):
        s = 0
        while s < 10:
            acc = (s + 7 + acc) % 1009
            s = s + 1
        g = tot * g & 2047
    return (acc * g ^ 11) & 131071

def f(x):
    for z in range(10):
        x = z - x & 2047
        x = (x + z ^ z) % 65521
    for cnt in range(123):
        x = 18 * x * x & 32767
    t0 = (x - 19) // 4
    m = t0 + 9
    p = ((m | 12) >> 4) * x & 262143
    val = (x - 15 >> 1) // 6
    t1 = val & 12 & x
    t2 = x << 2 >> 3
    x = t1 * t2
    t3 = x // 7 >> 2
    val = t3 >> 3
    t4 = val | x | x
    val = t4 + x & 131071
    t5 = (p & 7) - m >> 4
    return t5 % 65521

if __name__ == "__main__":
    arg = 9
    expected = 65520
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
