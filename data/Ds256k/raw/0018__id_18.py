# Auto-extracted from ds_lt256k_500.jsonl
# record_id=18  entry=f  input='9'  output='63878'  tokens=216546

def fn0(g, m, c):
    t0 = (m + g) * g
    c = (t0 - g) % 4093
    g = 13 << 4 | g
    for tot in range(8):
        v = 0
        while v < 4:
            m = (tot | g) * (tot - v) % 251
            v = v + 1
    t1 = m << 3
    t2 = t1 ^ 1 + m
    return t2 % 1009

def f(x):
    g = [72, 198, 182, 41, 25, 114]
    for prv in range(60):
        for d in range(7):
            t0 = d - prv | x
            x = t0 % 97
            t1 = x >> 2
            g[x % 6] = t1 - (d & prv)
        t2 = 8 ^ prv
        t3 = t2 & (prv & x)
        t4 = 8 << 1 ^ 1
        g[prv % 6] = t3 + t4
    if x - 19 <= 0:
        x = x + g[x % 6] >> 4
    else:
        x = x ^ 10
    if x * x > 33:
        x = x - 3 - x
        t5 = x - 4 >> 1
        g[x % 6] = (x + x ^ t5) % 251
    t6 = g[x % 6] + x << 3
    buf = (14 ^ 10) - x + t6
    t7 = (buf | 6) - buf
    t8 = t7 // 5 & 511
    t9 = (7 ^ x) << 3 & 65535
    t10 = (3 ^ x) & 131071
    buf = fn0(t8, t9, t10)
    acc = 1 - x >> 3
    q = 0
    while q < 10:
        a = 0
        while a < 5:
            g[x % 6] = acc * a
            t11 = g[a % 6] + buf
            g[a % 6] = t11 % 251
            a = a + 1
        q = q + 1
    t12 = (x ^ acc ^ buf + acc) - buf
    return t12 % 65521

if __name__ == "__main__":
    arg = 9
    expected = 63878
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
