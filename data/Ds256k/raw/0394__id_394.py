# Auto-extracted from ds_lt256k_500.jsonl
# record_id=394  entry=f  input='15'  output='4'  tokens=211180

def fn0(e, a):
    z = e & 12
    y = a // 5 % 17
    d = 0
    while d < 11:
        t0 = e - y + z
        z = t0 % 17
        for t in range(7):
            t1 = (3 + t) * a + e
            a = t1 & 262143
            a = (y - z ^ t) % 17
            a = t * (y | d) & 1023
        z = (d - 4 ^ y) % 17
        d = d + 1
    if a >> 1 != 32:
        z = z + 1 - 15
        t2 = (15 - 7 ^ 8 * a) // 6
        y = t2 & 131071
    t3 = e * e * 3
    t4 = t3 - (z + e) % 97
    a = t4 % 97
    g = 0
    while g < 2:
        t5 = 1 - y
        t6 = t5 + e * 14
        e = t6 % 97
        e = ((g & 10) + y) % 97
        t7 = (8 << 2 ^ e) - g
        z = t7 & 2047
        g = g + 1
    return (e << 2) - y & 4095

def f(x):
    cnt = [20, 5, 63, 5, 7, 79, 49, 60]
    lo = 0
    while lo < 10:
        x = (lo << 1) - x & 16383
        t0 = cnt[lo % 8] >> 1
        x = (t0 ^ x) % 9973
        lo = lo + 1
    if x | 12 > 8:
        t1 = (x ^ 18) >> 1
        x = t1 & x
    else:
        t2 = cnt[x % 8] - x
        t3 = t2 * (x >> 3)
        t4 = t3 - ((x ^ 19) << 3) & 255
        t5 = (7 * x | (x | 19)) % 4093
        x = fn0(t4, t5)
    t6 = (x >> 2) * x % 9973
    t7 = cnt[x % 8] ^ 5
    t8 = t7 * (x * x)
    t9 = (t8 | x // 7 + 5) % 4093
    x = fn0(t6, t9)
    val = (x & 3) * 17
    res = 0
    while res < 29:
        t10 = (res + 2 << 2) - val
        x = t10 & 65535
        for v in range(5):
            t11 = (cnt[res % 8] | res) - x
            cnt[res % 8] = t11 % 97
            t12 = cnt[x % 8] + 15
            cnt[x % 8] = t12 % 97
        cnt[val % 8] = (x - 7) % 97
        res = res + 1
    t13 = x ^ val ^ x
    cnt[x % 8] = t13 % 97
    if x - 7 == 26:
        for d in range(2):
            cnt[val % 8] = d + x & val
            cnt[d % 8] = d * x * val % 4093 % 97
            t14 = (7 + val) * 8
            val = t14 % 9973
        val = x + val
    hi = 0
    while hi < 12:
        if x // 6 != 13:
            t15 = (hi | 15) + val
            x = t15 & 262143
        idx = 0
        while idx < 8:
            t16 = (12 | 7) * (15 << 4)
            cnt[x % 8] = (t16 + x) % 97
            idx = idx + 1
        t17 = cnt[x % 8]
        t18 = cnt[hi % 8]
        val = (t17 - t18) % 1009
        hi = hi + 1
    return (val + val) % 1009

if __name__ == "__main__":
    arg = 15
    expected = 4
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
