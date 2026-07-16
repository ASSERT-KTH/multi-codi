# Auto-extracted from ds_lt256k_500.jsonl
# record_id=333  entry=f  input='8'  output='910'  tokens=18965

def fn0(g, m):
    t0 = g * 1
    t1 = t0 | m >> 3
    b = (t1 << 4) % 1009
    t2 = 15 * 2
    t3 = t2 + (b + 10)
    aux = t3 - g
    for hi in range(5):
        g = m % 17 - (m - hi) & 1023
    b = (g >> 3) * m // 2 & 131071
    for z in range(5):
        g = aux + aux - g & 65535
        t4 = 14 - m >> 3 ^ m | g
        g = t4 % 1009
    t5 = (m ^ 19) * m * b
    g = t5 & 65535
    g = 9 * aux
    return (m << 2) * aux % 1009

def f(x):
    t0 = (x | 11) & x
    t1 = ((2 - 6) * 5 - x) % 4093
    x = fn0(t0, t1)
    t2 = 7 * x + x
    t3 = (x - 20) % 97
    x = fn0(t2 & 131071, t3)
    t4 = x // 4 * x >> 2
    t5 = (x + x) * x % 4093
    x = fn0(t4 % 4093, t5)
    t6 = (x + 2) * x
    res = t6 & 2047
    t7 = (res + x) * (x * res)
    t8 = (res | x) + x - t7
    for t in range(49):
        x = (res - x) % 4093
    return t8 % 4093

if __name__ == "__main__":
    arg = 8
    expected = 910
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
