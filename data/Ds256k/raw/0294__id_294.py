# Auto-extracted from ds_lt256k_500.jsonl
# record_id=294  entry=f  input='5'  output='15'  tokens=222767

def rec(n, a):
    if n <= 0:
        return a
    for z in range(2):
        a = ((z | 16) * 6 + a) % 251
    if 5 - a >= 50:
        a = (n * n * 1 | a) & 16383
    t0 = a * a
    t1 = t0 + (a ^ n)
    return rec(n - 1, t1 % 1009)

def fn0(b, d):
    res = (1 - d - d // 7) // 4
    if d - res != 57:
        d = (d - b) * d & d
    else:
        d = res - b
    aux = res - d | res
    j = b + 3 + 8 + res
    lo = (aux | j) * j & 2047
    aux = (lo - d) * 11 % 9973
    t0 = aux // 4 | aux
    t1 = b - lo & j
    return (t0 + t1) % 251

def fn1(e, d):
    res = [949, 183, 101, 719, 646, 158]
    w = (e ^ 3) * e % 9973
    if res[w % 6] * d != 39:
        t0 = res[d % 6]
        t1 = 11 & t0
        t2 = t1 ^ (w ^ e)
        res[w % 6] = t2 % 1009
    else:
        if 5 * e < 18:
            t3 = e - res[d % 6]
            t4 = (t3 * e ^ d) % 9973
            res[e % 6] = t4 % 1009
        else:
            t5 = (8 << 2) * e * d & 32767
            res[e % 6] = t5 % 1009
    t6 = res[w % 6]
    lo = t6 | res[d % 6]
    if lo ^ e >= 50:
        s = 0
        while s < 3:
            t7 = (s << 2) - s + e
            res[e % 6] = t7 % 1009
            s = s + 1
    for m in range(6):
        for u in range(11):
            t8 = lo << 2
            t9 = t8 | u ^ 10
            d = t9 & 65535
            t10 = d + lo + w * w
            res[d % 6] = t10 % 65521 % 1009
            lo = (lo >> 1) % 9973
        w = (e + w) % 97
    t11 = 17 * e * 15
    idx = (t11 + 2) % 97
    t12 = (w ^ d) + w
    t13 = (e ^ 2) - idx
    return (t12 | t13) & 16383

def f(x):
    t0 = x ^ 18
    lo = t0 ^ x & 12
    lo = 18 | x
    t1 = lo ^ x | x * lo
    t2 = (x * lo % 97 + t1) % 97
    t3 = x & lo ^ 18
    x = fn0(t2, t3 & 16383)
    t4 = (lo & 10) * (3 + 19)
    lo = rec(119, t4 & 16383)
    t5 = lo + 1 - lo
    t6 = (x ^ 14) // 6
    x = t5 | t6
    for z in range(1171):
        lo = (11 & z | x) & 511
    return ((1 - x) % 17 | lo) % 17

if __name__ == "__main__":
    arg = 5
    expected = 15
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
