# Auto-extracted from ds_lt256k_500.jsonl
# record_id=86  entry=f  input='18'  output='694'  tokens=91949

def rec(n, a):
    if n <= 0:
        return a
    v = 0
    while v < 11:
        a = ((a << 1) + 18) % 17
        nxt = 0
        while nxt < 5:
            t0 = n + 4 - (a & nxt)
            a = (nxt - v ^ v) * t0 & 2047
            a = ((n ^ 20) - nxt | a) & 32767
            nxt = nxt + 1
        t1 = n * n
        t2 = t1 * (v * v)
        a = t2 - a & 2047
        v = v + 1
    a = ((19 + a & a) + a) % 251
    t3 = ((n ^ a) // 2 + a) % 251
    return rec(n - 1, t3)

def f(x):
    j = [255, 133, 297, 745, 876, 41]
    for cnt in range(5):
        for nxt in range(76):
            x = (12 + 1 + x - 20) % 4093
            t0 = cnt * nxt | x
            x = t0 & 131071
        t1 = x * cnt - (x - cnt)
        x = (t1 ^ (cnt & 2) * x) % 4093
    t2 = x + j[x % 6] << 1
    m = t2 - x
    for aux in range(7):
        t3 = m + m
        t4 = t3 * (m * m)
        x = (t4 + x) % 4093
        t5 = aux - x + 6
        t6 = j[aux % 6]
        m = (t5 - t6) % 251
    p = 12 ^ m
    for cur in range(8):
        t7 = (p + cur) * (p ^ cur)
        x = (t7 >> 3) % 4093
        m = (p + 2) % 4093 + m & 2047
    for acc in range(11):
        t8 = p * 20 >> 4
        p = t8 % 4093
    t9 = j[m % 6]
    t10 = 15 << 4
    t11 = (x | m) ^ p
    t12 = t10 + (p ^ t9)
    return (t11 + t12) % 4093

if __name__ == "__main__":
    arg = 18
    expected = 694
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
