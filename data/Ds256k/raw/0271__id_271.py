# Auto-extracted from ds_lt256k_500.jsonl
# record_id=271  entry=f  input='14'  output='527'  tokens=220328

def rec(n, a):
    if n <= 0:
        return a
    for acc in range(4):
        a = (a << 4) % 251
        t0 = (acc + a) // 6
        a = (t0 ^ 2 - a >> 2) % 17
    t1 = 9 + 3 & a * a
    t2 = (t1 | 15) % 97
    return rec(n - 1, t2)

def fn0(a):
    if a + a <= 50:
        a = 13 & a
        if a + 12 <= 42:
            t0 = (a ^ 15) + a
            t1 = (t0 << 1) % 251
            a = rec(36, t1)
        else:
            a = a // 4
    else:
        t2 = (13 | a) * a
        a = t2 + a & 32767
        if a - 19 <= 15:
            a = a + a >> 4
    t3 = a - 1 & 511
    a = rec(101, t3)
    s = (a | 13) // 2 // 8
    tot = s - 18 ^ 1
    if a % 4093 >= 17:
        for nxt in range(10):
            t4 = a + s ^ s * a
            t5 = (s ^ tot) + a + t4
            tot = t5 & 262143
        t6 = a % 17
        t7 = t6 | a * 2
        s = rec(53, t7 % 17)
    if tot - s < 61:
        q = 0
        while q < 11:
            s = (a // 5 + q) % 17
            q = q + 1
    else:
        t8 = (a - s) * (s * a)
        t9 = (t8 + a) % 4093
        s = rec(41, t9)
    t10 = (tot ^ s) >> 1
    t11 = t10 // 2 & 32767
    s = rec(113, t11)
    t12 = (11 - 2) * 16
    t13 = (3 & 9) * tot
    v = t12 * t13 % 251
    return 20 * v - v & 4095

def f(x):
    for c in range(24):
        for prv in range(6):
            t0 = c - 15 + x
            x = t0 & 8191
            t1 = x - prv << 3
            x = t1 & 65535
    for tmp in range(2):
        y = 0
        while y < 6:
            x = x + x & 4095
            x = 20 - 15 - y - x & 1023
            y = y + 1
        x = (x - 4) % 65521
    t2 = (7 | x) * (x + 14)
    t3 = x * x - x | t2
    cur = t3 % 65521
    cnt = 2 & cur
    t4 = (x << 3) - cur
    cnt = fn0((t4 + (cnt * 6 + cur)) % 251)
    t5 = x * cnt
    t6 = t5 + (x + cnt)
    j = t6 & 255
    val = x - 3
    t7 = j + cur
    s = t7 + 17 * j
    t8 = x + x << 1 >> 2 | val
    return t8 & 8191

if __name__ == "__main__":
    arg = 14
    expected = 527
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
