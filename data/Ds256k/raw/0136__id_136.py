# Auto-extracted from ds_lt256k_500.jsonl
# record_id=136  entry=f  input='18'  output='966'  tokens=17691

def rec(n, a):
    if n <= 0:
        return a
    t0 = a & 11 ^ (a ^ 18)
    t1 = n - 6 & (a ^ 7)
    val = (t0 | t1) % 251
    q = 0
    while q < 11:
        t2 = n ^ 12
        t3 = t2 ^ a + q
        val = t3 - q & 8191
        t4 = (n + q) // 2
        val = (t4 | a) % 251
        val = (18 & 19 ^ val) & 16383
        q = q + 1
    if n + n - val != 33:
        a = (val ^ n) + (n + val) & 255
    else:
        val = ((val ^ 7) >> 2) % 97
        val = ((18 & val) - 14) % 9973
    t5 = n | 1 | a
    return rec(n - 1, t5 % 4093)

def fn0(d):
    prv = 0
    while prv < 9:
        d = (prv + prv - d) % 17
        prv = prv + 1
    res = d * d & 8191
    idx = 7 * d
    if idx | 1 >= 63:
        t0 = ((res ^ 6) - 13) % 9973
        res = rec(55, t0)
        for e in range(10):
            d = (15 - e - idx) % 65521
            t1 = (res << 2) + e | idx
            idx = t1 % 65521
            t2 = (res & 2) << 3 | e
            idx = t2 % 17
    t3 = res * idx * d
    t4 = idx * idx + idx
    t5 = (t3 | t4) & 8191
    res = rec(48, t5)
    j = idx * d % 65521
    g = 0
    while g < 4:
        if 7 - res != 12:
            idx = (res + idx) * j % 17
            res = ((11 ^ 19) - j | g) & 4095
        d = idx + g & 131071
        g = g + 1
    m = (idx // 5 | 4) // 4
    return (j >> 4) * d % 65521

def fn1(c):
    if c + c != 47:
        for nxt in range(9):
            c = c * nxt * c % 251
    if c | 18 == 60:
        t0 = (c | 14) % 97
        c = rec(25, t0)
    else:
        t1 = (c ^ 11) & 511
        c = rec(97, t1)
        t2 = c - 15 ^ c
        c = fn0(t2 % 251)
    b = (c - 15) * c % 97
    m = c + b << 2
    t3 = c - b | b
    b = fn0(t3 % 251)
    t4 = 11 ^ 7 ^ 12
    t5 = (m & b) << 4
    b = (t4 ^ t5) % 251
    t6 = b // 2 & 8191
    m = rec(62, t6)
    return (b >> 3) % 97

def f(x):
    t = [899, 615, 318, 428, 855, 45, 837]
    res = (x + 15 + 4) * 6
    t0 = t[res % 7]
    t1 = (res ^ 11) - res
    t2 = res + x ^ t0
    w = t1 ^ t2
    for j in range(24):
        t3 = w >> 1
        t4 = t3 - (15 + res)
        res = t4 & 255
        t5 = j * res - res
        x = t5 & w // 4 * w
    prv = res // 8 + (18 ^ res)
    buf = 0
    while buf < 4:
        t6 = t[w % 7] - w
        prv = (t6 ^ res ^ buf) % 65521
        t7 = t[buf % 7] - 7
        x = (t7 >> 3 | x) % 1009
        t8 = t[w % 7]
        t9 = x - t8 ^ buf
        prv = t9 & 2047
        buf = buf + 1
    p = w // 6
    t[prv % 7] = (9 - 15 ^ w) % 1009
    aux = prv ^ 20
    t[res % 7] = x & t[p % 7]
    t10 = 9 ^ p | aux
    return t10 % 1009

if __name__ == "__main__":
    arg = 18
    expected = 966
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
