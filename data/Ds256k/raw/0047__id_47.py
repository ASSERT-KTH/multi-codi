# Auto-extracted from ds_lt256k_500.jsonl
# record_id=47  entry=f  input='1'  output='62'  tokens=108677

def rec(n, a):
    if n <= 0:
        return a
    if n * 9 + a > 26:
        t0 = (n & 8) - 9 ^ a
        a = t0 & 511
        t1 = 8 * 13 // 4
        a = (t1 | a) % 251
    t2 = (n ^ a) * (a ^ n)
    u = t2 % 17
    return rec(n - 1, a & 14)

def fn0(b, c, g):
    p = 13 & c
    d = ((b | 11) << 1) // 3
    for nxt in range(11):
        if c >> 3 < 64:
            d = ((c | nxt) ^ nxt) % 1009
        else:
            t0 = (g ^ c) * d
            g = (t0 | p) & 65535
    for s in range(6):
        d = ((d ^ p) - s) * p & 2047
    buf = b | d
    b = 15 | g
    t1 = g % 97 + g | d
    return t1 % 1009

def f(x):
    tmp = [74, 58, 40, 15, 33]
    if x ^ 20 <= 6:
        for lo in range(11):
            t0 = lo - lo * lo ^ x
            x = t0 % 1009
            t1 = tmp[lo % 5]
            t2 = tmp[lo % 5]
            t3 = tmp[x % 5]
            t4 = t1 * 9
            t5 = t4 & t2 * t3
            tmp[lo % 5] = (t5 >> 2) % 97
    else:
        x = (x | 7) & 19 ^ x
        t6 = tmp[x % 5]
        t7 = (6 | x) ^ 4
        t8 = 15 - t6 >> 4
        x = t7 + t8
    t9 = x >> 2
    t10 = t9 + (2 - x)
    t11 = (x | 14) >> 4
    q = t10 ^ t11
    if 14 ^ tmp[x % 5] == 21:
        x = 17 * q
    else:
        tmp[x % 5] = (3 | q) % 9973 % 97
        if 5 * x < 4:
            x = q & x
    t12 = 15 + tmp[x % 5] - q
    d = (q >> 3 ^ q - x) & t12
    nxt = tmp[q % 5] ^ x
    for acc in range(11):
        d = (2 - d) % 9973
        tot = 0
        while tot < 9:
            t13 = (q | 17) * q - d
            x = (t13 ^ tot) % 1009
            t14 = (7 & nxt) << 3
            nxt = t14 % 1009
            t15 = 15 * q // 3 // 4
            q = t15 % 1009
            tot = tot + 1
        t16 = (x - tmp[acc % 5]) // 6
        nxt = t16 & 131071
    a = x ^ d
    return 16 + a & 4095

if __name__ == "__main__":
    arg = 1
    expected = 62
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
