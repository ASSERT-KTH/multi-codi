# Auto-extracted from ds_lt256k_500.jsonl
# record_id=425  entry=f  input='14'  output='74018'  tokens=166888

def fn0(e, m):
    for g in range(9):
        t0 = (e | g) * (5 ^ e)
        m = t0 % 1009
    for z in range(5):
        for j in range(7):
            t1 = (m | j) >> 4
            m = t1 % 65521
            t2 = j & 12 ^ m
            e = t2 % 65521
        e = (e ^ 16) - 4 & 1023
        if z << 4 | m == 56:
            t3 = (z | 10) - e
            m = t3 >> 3 & 32767
            m = (m * z >> 3) % 1009
    t4 = (m ^ e) + 6 * 5
    v = t4 - e
    t5 = 13 - e
    t6 = t5 ^ e << 4
    t = t6 & 8191
    t7 = e * m
    t = t7 & t % 251
    for cnt in range(12):
        t8 = 18 * cnt ^ 5 - 17 ^ v
        v = t8 % 65521
        t9 = m // 2
        t10 = t9 - m // 4
        m = (t10 + v) % 65521
        if t + t <= 12:
            t = (v & t) - cnt & 16383
            t = (14 + v - cnt) % 251
    e = m & 15 ^ 8 & 3
    return (t | 16) % 65521

def f(x):
    a = x | 17
    for u in range(5):
        for p in range(12):
            t0 = a + 6 | u
            x = (p + x) * t0 % 4093
            x = (x + 1) // 4 & 255
            t1 = u & 10 | x * p
            x = t1 & 32767
        t2 = u & 19
        t3 = u - 12 + u
        t4 = t2 & (12 ^ x)
        a = (t3 ^ t4) % 1009
    t5 = x | a | x
    t6 = t5 - x & 1023
    t7 = a * a * (x & 13)
    t8 = t7 * (a + x ^ x)
    x = fn0(t6, t8 % 1009)
    aux = 0
    while aux < 126:
        t9 = 10 ^ 20
        t10 = t9 & a - x
        x = (t10 + x) % 4093
        aux = aux + 1
    for s in range(9):
        x = x & a
        for idx in range(8):
            a = (x - idx - 6 + s) % 4093
            a = (10 ^ idx ^ a) & 65535
            t11 = idx + a - idx * x
            x = t11 % 1009
    t12 = a * a * a + a
    return t12 & 131071

if __name__ == "__main__":
    arg = 14
    expected = 74018
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
