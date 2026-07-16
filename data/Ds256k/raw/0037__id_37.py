# Auto-extracted from ds_lt256k_500.jsonl
# record_id=37  entry=f  input='1'  output='534'  tokens=147270

def fn0(a):
    if a | 17 > 29:
        t0 = a * a
        t1 = t0 ^ (a | 10)
        t2 = a * a ^ a
        a = (t1 ^ t2) % 97
        if a * a <= 60:
            t3 = a + 20 & a
            t4 = 3 * a ^ a
            a = t3 - t4
        else:
            a = 13 * a & 16383
    else:
        t5 = (a + a | a) ^ a
        a = t5 & 65535
        a = a + 14 + 14 - a
    if a - 6 == 35:
        for aux in range(9):
            t6 = (aux + aux) * aux ^ a
            a = t6 & 4095
            t7 = aux ^ 16
            t8 = t7 - (13 - a)
            a = t8 % 1009
        t9 = a * a >> 4
        a = t9 & 32767
    else:
        for buf in range(11):
            a = (a ^ 5) & buf - 6
    t10 = (a // 7 | 13 ^ a) + a
    g = t10 % 9973
    for u in range(5):
        t11 = g ^ u ^ a * u
        t12 = (g << 1) - 7 ^ t11
        a = t12 & 65535
    return (a * g * g ^ a) & 4095

def f(x):
    val = [922, 634, 1001, 719, 169, 412]
    for a in range(2):
        x = (a - 17 - x ^ x) % 1009
    prv = 0
    while prv < 9:
        t0 = val[x % 6]
        t1 = (10 & prv) << 3
        t2 = t0 + x - 20
        x = t1 * t2 % 1009
        x = val[x % 6] & x
        prv = prv + 1
    for s in range(258):
        x = (s * 5 ^ x) % 17
        x = s + x & 1023
        t3 = 18 * x
        t4 = (6 + x) // 3
        t5 = t3 + (x + s)
        x = t4 & t5
    v = x & 18
    t = 14 - v
    if x >> 4 <= 29:
        t = v ^ t ^ v
    else:
        for idx in range(2):
            t6 = v + val[x % 6]
            t7 = t6 * (idx << 1)
            t8 = t7 & (v + 7) * x
            val[idx % 6] = t8 % 1009
            t9 = (8 ^ 11) + (x >> 2)
            v = t9 * ((13 + t) * idx) % 9973
        x = t + x + x
    t10 = t + x
    t11 = t10 ^ x << 3
    t12 = (t ^ 15) * v
    return (t11 | t12) & 2047

if __name__ == "__main__":
    arg = 1
    expected = 534
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
