# Auto-extracted from ds_lt256k_500.jsonl
# record_id=10  entry=f  input='16'  output='8'  tokens=246656

def f(x):
    m = [247, 761, 325, 933]
    res = (x & 10) + (x << 3)
    m[res % 4] = x - 2
    e = (12 & 3) + 10 + x
    for hi in range(11):
        t0 = (res ^ 3) - e
        e = t0 & 8191
    if e - x > 27:
        q = 0
        while q < 9:
            t1 = (9 - res) * 4
            t2 = m[e % 4]
            m[res % 4] = (t1 ^ t2) % 1009
            m[q % 4] = e * x % 1009
            q = q + 1
        if x & 4 >= 0:
            m[e % 4] = (e * x - (res << 4)) % 1009
            m[e % 4] = (e ^ 1) - e
        else:
            t3 = m[x % 4] * x
            t4 = (x - e) * t3 << 2
            x = t4 & 2047
    for z in range(6):
        for b in range(6):
            t5 = (z << 2) * x
            t6 = m[e % 4]
            m[x % 4] = t5 * t6 % 97
            t7 = (res // 4 ^ 5) * 5
            m[x % 4] = t7 % 1009
            m[res % 4] = (15 + 20 + x) % 1009
        res = (z * z | x) % 17
        p = 0
        while p < 12:
            m[res % 4] = (z + 2 - (x >> 1)) % 1009
            p = p + 1
    if res * e > 22:
        res = x // 7
    j = 4 * res + (x ^ 6)
    prv = 0
    while prv < 8:
        t8 = m[prv % 4] & prv
        x = (t8 | res) % 97
        d = 0
        while d < 10:
            t9 = (3 << 3) - j ^ d
            m[prv % 4] = t9 % 1009
            j = (prv | 2) + j & 16383
            m[prv % 4] = (prv - x) % 1009
            d = d + 1
        if res & 6 >= 4:
            t10 = m[j % 4]
            t11 = t10 >> 4
            t12 = m[j % 4]
            t13 = t11 * (e - 6)
            t14 = (t12 + j) % 1009
            e = t13 * t14 % 1009
        prv = prv + 1
    buf = res // 3 // 3
    c = buf + 16 >> 2
    g = j << 3
    if c * 7 <= 44:
        t15 = m[g % 4]
        t16 = (e + buf) * t15
        t17 = m[g % 4]
        e = (t16 ^ t17) & 511
    else:
        buf = (g + j | j) & 1
        if e >> 2 == 12:
            t18 = 4 & g
            res = t18 | 7 * 7
        else:
            buf = g - buf
    w = buf * x & 16
    for cnt in range(217):
        t19 = buf // 4 ^ e * x
        buf = t19 // 7 % 1009
    t20 = (w | c) + (c + c)
    y = t20 // 2
    t21 = m[c % 4] + y
    return t21 % 97 // 5 % 1009

if __name__ == "__main__":
    arg = 16
    expected = 8
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
