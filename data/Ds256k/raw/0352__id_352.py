# Auto-extracted from ds_lt256k_500.jsonl
# record_id=352  entry=f  input='13'  output='5981'  tokens=169687

def fn0(m, d):
    res = 2 + d
    if 1 - d != 5:
        aux = 0
        while aux < 5:
            res = aux - res & 511
            t0 = 4 + aux ^ m
            res = t0 % 251
            m = (aux ^ 12) * (res + aux) % 65521
            aux = aux + 1
        if 12 ^ res > 10:
            t1 = d % 1009 & m
            m = t1 >> 3
    else:
        for buf in range(7):
            t2 = m * buf + 18
            m = (t2 + (m - res >> 1)) % 251
    for t in range(6):
        res = (res - t | 16) & 32767
        m = (t * res - d) % 65521
    if d & res > 33:
        m = res % 17
        if 7 + 14 + res >= 44:
            d = m | d
        else:
            d = (15 | 8) ^ m
            res = m & res
    m = m % 65521
    if m + d > 22:
        if m + res > 6:
            d = (m ^ d) - 9
        for v in range(11):
            m = (17 + 20) * v - res & 1023
            t3 = res & 11 ^ res
            t4 = t3 + m + v
            d = t4 & 255
            t5 = 2 * d
            t6 = v * d % 17
            t7 = t5 ^ 19 + v
            m = t6 & t7
    return (d - 4 ^ res) & 1023

def f(x):
    if x ^ 14 < 0:
        for val in range(6):
            t0 = (x | val) - 2 + val
            x = t0 & 1023
            x = (7 * 8 * x << 4) % 9973
            x = ((val ^ 17) * val ^ x) % 9973
    else:
        for w in range(5):
            x = (w ^ x) & 255
            t1 = x ^ 11 ^ w + x
            x = (t1 << 3) % 17
        x = 2 - x
    acc = (x * x | x) & 8191
    for a in range(3):
        idx = 0
        while idx < 66:
            t2 = idx * x - (2 & idx)
            acc = t2 % 9973
            t3 = (acc - a) * (16 * acc) << 2
            x = (t3 | idx) & 255
            t4 = 16 + x
            t5 = t4 - (idx & 18)
            t6 = 20 % 17 * acc
            x = (t5 + t6) % 1009
            idx = idx + 1
        x = acc * x & 4095
        t7 = x * a + a * x
        x = t7 % 1009
    cur = (7 | acc) >> 1
    p = x & 3
    t8 = (5 << 2) * (p - acc)
    g = acc + acc << 2 & t8
    t = g * acc * cur % 9973
    d = acc + cur
    t9 = p * cur >> 2
    return (t9 + (6 + t) % 9973) % 9973

if __name__ == "__main__":
    arg = 13
    expected = 5981
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
