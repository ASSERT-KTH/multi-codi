# Auto-extracted from ds_lt256k_500.jsonl
# record_id=329  entry=f  input='8'  output='175'  tokens=14080

def fn0(a):
    w = 2 + a
    cnt = (a & w) >> 1
    nxt = 12 + cnt
    lo = 0
    while lo < 2:
        a = (cnt + w ^ lo) & 65535
        lo = lo + 1
    p = 5 ^ cnt
    if a - w <= 5:
        c = 0
        while c < 5:
            p = (p ^ c) & 255
            t0 = (c ^ 16) & p << 1
            t1 = t0 - (w + nxt ^ 20)
            a = t1 % 1009
            c = c + 1
        nxt = (a ^ p) + a >> 2
    return (cnt - 15) % 4093

def fn1(a, e, j):
    for lo in range(6):
        for idx in range(2):
            t0 = j + e ^ 13
            a = (t0 - a) % 65521
            t1 = (idx & 11) + lo
            t2 = t1 ^ 5 | e
            j = t2 % 17
            e = ((lo + 15 | j) ^ idx) % 17
    v = 0
    while v < 3:
        g = 0
        while g < 8:
            t3 = g * 4 + e
            j = t3 & 8191
            a = (j | g) % 65521
            a = v - e + g & 255
            g = g + 1
        t4 = 9 + v + 9 | e
        a = t4 & 8191
        t5 = (v << 4) - a
        e = t5 << 2 & 1023
        v = v + 1
    t6 = j + j & e
    e = t6 & 11
    s = 0
    while s < 4:
        a = (e - 18 + e | s) & 2047
        for m in range(9):
            j = (m + e) * e & 4095
            t7 = (j & a) - (e ^ m)
            a = t7 & 32767
        t8 = s * a - j
        t9 = t8 ^ a * e & e
        j = t9 & 8191
        s = s + 1
    e = j | 15
    t10 = j + e ^ j - 7
    j = fn0(t10 // 6 % 65521)
    t11 = (2 + e) % 65521 - j
    return t11 % 65521

def f(x):
    z = [85, 1, 27, 65, 8, 52, 85]
    t0 = z[x % 7] * x
    a = t0 ^ x
    t1 = z[a % 7] * x
    x = t1 | x
    for c in range(2):
        for buf in range(15):
            a = ((a - x) // 6 - buf) % 17
            t2 = (12 * 14 | 8 + c) - a
            a = t2 % 65521
            t3 = x >> 4 >> 4 ^ x
            z[buf % 7] = t3 % 97
    t4 = z[a % 7]
    z[a % 7] = (13 + t4) % 97
    t5 = (12 | x) & 8 & x ^ a
    return t5 % 65521

if __name__ == "__main__":
    arg = 8
    expected = 175
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
