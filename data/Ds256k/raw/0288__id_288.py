# Auto-extracted from ds_lt256k_500.jsonl
# record_id=288  entry=f  input='8'  output='65319'  tokens=92428

def f(x):
    a = 19 * 3 - x
    if x * 6 == 9:
        x = x + 11
        x = x - a
    for aux in range(2):
        t0 = 3 * 20
        t1 = t0 - a // 4
        t2 = 10 * a * a
        a = (t1 - t2) % 251
        if x >= 33:
            t3 = 12 * x // 6
            a = (t3 | a) & 255
        else:
            x = x - aux - a & 4095
        a = aux - x - x & 1023
    if x - 18 == 1:
        for t in range(2):
            t4 = a * t // 2
            t5 = x + x | a
            a = t4 - t5 & 4095
        for d in range(7):
            t6 = (11 | d) << 4
            a = (t6 - a) % 65521
            t7 = (a ^ d) - d
            a = t7 // 8 % 97
    c = x & 6
    for m in range(12):
        t8 = m * x ^ c
        t9 = a + c - 19
        x = (t8 + t9) % 251
        if c * c <= 20:
            t10 = 5 * x - a
            x = (t10 ^ 5) & 4095
            c = (a - 10 ^ m) & 8191
        x = (m - x << 4) % 97
    for acc in range(8):
        j = 0
        while j < 3:
            t11 = 12 * acc
            t12 = t11 | j * 2
            x = (t12 | c) % 251
            j = j + 1
        z = 0
        while z < 3:
            a = (z + c) % 97
            z = z + 1
    t13 = 17 * a
    t14 = t13 & a - c
    buf = t14 - 20
    t15 = (c | x) - (19 & buf)
    nxt = (buf | 3) ^ 2 ^ t15
    res = buf & 3 ^ c
    tot = c >> 3 & x
    for v in range(4):
        for p in range(35):
            tot = (19 + nxt - tot) % 1009
        t16 = (v + res + c) // 7
        tot = t16 % 65521
        t17 = (res * res >> 2) // 8
        buf = t17 - v & 4095
    y = (8 ^ a ^ x) >> 3
    b = buf * tot & 255
    tmp = y - tot >> 3
    t18 = buf // 6 // 5 << 4
    val = t18 % 97
    for hi in range(2):
        res = ((res >> 1) - (17 ^ y)) % 97
        t19 = (a + val) * (a ^ nxt) + hi
        buf = t19 & 255
    t20 = x | 1
    t21 = t20 - a * val
    return (t21 ^ c) % 65521

if __name__ == "__main__":
    arg = 8
    expected = 65319
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
