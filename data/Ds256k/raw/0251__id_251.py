# Auto-extracted from ds_lt256k_500.jsonl
# record_id=251  entry=f  input='2'  output='1014'  tokens=168538

def rec(n, a):
    if n <= 0:
        return a
    for lo in range(12):
        for s in range(7):
            a = ((a ^ lo) - s) % 97
            t0 = (s + 15 | s) - n
            a = (t0 | a) & 262143
            t1 = n << 2
            t2 = t1 ^ a * lo
            a = t2 & 262143
    t3 = a & 1 | a ^ n
    t4 = t3 + (a + a) * n
    idx = t4 & 16383
    t5 = ((20 | 5) - (3 + a)) % 4093
    return rec(n - 1, t5)

def fn0(j, m, c):
    aux = [141, 67, 215, 28, 78, 119, 157]
    d = j // 3 >> 2
    c = 4 | d
    d = c + d
    if j ^ 13 > 11:
        t0 = 17 | aux[d % 7]
        t1 = 18 * aux[j % 7]
        m = (t0 + t1) // 4
    d = 13 << 2 | j
    if aux[c % 7] & m == 45:
        if aux[c % 7] - d != 7:
            t2 = (d | c) - m
            d = rec(31, t2 & 2047)
        else:
            c = (c // 2 * j ^ 1) % 251
    else:
        t3 = d * m
        t4 = t3 * (9 & m)
        d = rec(89, t4 & 131071)
        t5 = (d >> 3) * 12
        t6 = t5 // 6 % 17
        j = rec(102, t6)
    t7 = aux[m % 7]
    t8 = j - 18 | t7
    return (t8 + d) % 97

def fn1(e, d, b):
    t = [970, 418, 495, 167, 466, 731]
    if t[e % 6] * d > 54:
        for idx in range(8):
            t[b % 6] = (e - b + d) % 1009
        t[e % 6] = e * d % 17
    else:
        prv = 0
        while prv < 2:
            e = (b + prv) % 251
            t0 = 2 ^ prv | d
            t[prv % 6] = t0 % 1009
            prv = prv + 1
        t1 = t[d % 6] % 251
        t2 = (t1 & e) // 4 & 262143
        b = rec(51, t2)
    t3 = b * e - 15
    t4 = e + e - 18 & 511
    t5 = b + t[e % 6]
    t6 = (t5 + b // 8) % 251
    e = fn0(t3 % 251, t4, t6)
    d = d - e
    e = e - 6 >> 3
    t7 = t[d % 6] << 4
    t8 = t[b % 6] * d
    t9 = t[b % 6] >> 1
    t10 = t7 // 3 + (t8 + t9)
    e = rec(43, t10 % 251)
    return (e - d & b) // 2 % 251

def f(x):
    m = x + x
    s = 12 + 9 ^ (19 ^ m)
    cur = x * 17
    y = ((m ^ x) & x - 17) + 13
    for prv in range(8):
        t0 = y - 20 | prv
        s = t0 % 4093
        m = ((x | 2) ^ m) % 1009
        if 19 + 6 | s > 49:
            y = (cur + y) % 1009
            t1 = 6 * s ^ 12
            cur = t1 & (cur ^ m) - y
        else:
            t2 = ((4 & y) << 1) + y
            m = (t2 - m) % 4093
    for t in range(11):
        t3 = s * 12 ^ t
        m = t3 % 1009
    aux = x | cur
    a = 0
    while a < 23:
        t4 = (9 - aux >> 2) + a
        cur = t4 % 4093
        nxt = 0
        while nxt < 10:
            t5 = (cur >> 1) - nxt
            cur = t5 % 1009
            s = aux * s & 131071
            s = (nxt & cur) * a & 32767
            nxt = nxt + 1
        s = (s | aux) % 1009
        a = a + 1
    return cur + 6 & 8191

if __name__ == "__main__":
    arg = 2
    expected = 1014
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
