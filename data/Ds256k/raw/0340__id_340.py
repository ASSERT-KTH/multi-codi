# Auto-extracted from ds_lt256k_500.jsonl
# record_id=340  entry=f  input='1'  output='25'  tokens=55530

def rec(n, a):
    if n <= 0:
        return a
    if a ^ 9 == 6:
        t0 = (n | a) * a
        a = t0 % 1009
    t1 = n & a & n + n
    t2 = (n & 7) * (a ^ 7)
    a = (t1 ^ t2) & 255
    t3 = (a - 14 | n) % 1009
    return rec(n - 1, t3)

def fn0(c):
    acc = [91, 41, 3, 47, 0, 79, 63, 20]
    t0 = c * c ^ c
    t1 = (t0 >> 1) % 4093
    acc[c % 8] = t1 % 97
    for q in range(10):
        cur = 0
        while cur < 3:
            t2 = q - acc[q % 8] + c
            c = t2 % 4093
            t3 = (c ^ 13) << 4
            t4 = acc[c % 8]
            t5 = (t3 | t4) & 2047
            acc[c % 8] = t5 % 97
            t6 = 3 & acc[c % 8]
            c = t6 * (c & q) & 16383
            cur = cur + 1
        t7 = c // 7
        t8 = t7 ^ 1 - c
        c = t8 & 1023
        if c + q <= 28:
            t9 = c >> 3 ^ c // 8
            acc[c % 8] = t9 % 97
            t10 = 1 + c | 4
            acc[q % 8] = (t10 + 6) % 97
        else:
            t11 = q | acc[c % 8]
            t12 = (9 * 17 ^ t11) // 3
            c = t12 & 511
    t13 = acc[c % 8] << 3
    acc[c % 8] = ((c * c & t13) << 4) % 97
    lo = 0
    while lo < 8:
        prv = 0
        while prv < 3:
            t14 = c - prv ^ c
            t15 = acc[c % 8]
            t16 = t14 * t15 & 511
            acc[c % 8] = t16 % 97
            prv = prv + 1
        lo = lo + 1
    val = 0
    while val < 4:
        c = ((12 & 9) + c) % 65521
        t17 = acc[c % 8]
        c = (t17 >> 3) % 9973
        if acc[val % 8] ^ val | c > 30:
            t18 = c | acc[val % 8]
            c = t18 % 9973
        else:
            t19 = val + acc[val % 8]
            t20 = val + val - 2 ^ t19 | c
            acc[c % 8] = t20 % 97
        val = val + 1
    for w in range(9):
        t21 = (c + c) // 6
        c = (t21 >> 2) % 65521
    tot = (c | 5) + c
    m = tot - 6
    return tot * tot % 4093

def f(x):
    lo = [89, 93, 30, 66, 46, 92, 68]
    prv = 0
    while prv < 7:
        t0 = x + lo[prv % 7]
        t1 = (prv & x) - t0 | 7
        x = t1 & 1023
        prv = prv + 1
    if 9 ^ x != 11:
        if x // 5 >= 0:
            t2 = x * 20 + 20
            lo[x % 7] = t2 % 97
            t3 = lo[x % 7]
            x = t3 - x - x
        else:
            x = fn0((x | 7) & 32767)
            x = x // 2
        v = 0
        while v < 7:
            t4 = 2 + 4 + v
            lo[v % 7] = (t4 - x) % 97
            t5 = lo[v % 7] << 4 ^ x
            lo[x % 7] = t5 % 97
            v = v + 1
    d = x ^ 3
    z = x // 7 + x ^ d
    for p in range(79):
        t6 = (z ^ lo[x % 7]) // 5
        d = (t6 >> 2) + d & 255
        x = (z + p) % 97
        t7 = x * lo[x % 7]
        z = t7 * p % 251
    return z // 6 & 255

if __name__ == "__main__":
    arg = 1
    expected = 25
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
