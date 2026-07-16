# Auto-extracted from ds_lt256k_500.jsonl
# record_id=121  entry=f  input='4'  output='16362'  tokens=77971

def fn0(a, d, c):
    res = 0
    while res < 10:
        t0 = res + 6 + c
        d = t0 % 65521
        t1 = 16 * d + d ^ a
        d = t1 % 1009
        t2 = (1 - c) // 6
        c = t2 % 65521
        res = res + 1
    q = 0
    while q < 10:
        t3 = (a ^ 14) + d
        d = t3 % 1009
        t4 = 11 | c | a
        a = t4 % 1009
        w = 0
        while w < 7:
            t5 = c + d
            t6 = t5 ^ c + c
            t7 = (11 | a) - c
            c = (t6 - t7) % 65521
            w = w + 1
        q = q + 1
    cnt = a - c & a
    t8 = (a - d) // 8 * c
    c = t8 % 1009
    cnt = a + c
    j = 0
    while j < 6:
        a = c % 65521 - a & 255
        if (11 | j) - d <= 62:
            cnt = (d + d - j) % 1009
            a = (11 + j ^ cnt) & 511
        else:
            t9 = (c ^ 4) % 1009
            t10 = t9 - a ^ d
            d = t10 % 65521
        cnt = cnt * 11 % 1009
        j = j + 1
    t11 = d ^ 19 | cnt
    return t11 % 1009

def f(x):
    idx = [43, 198, 40, 8, 13]
    y = 2 - 10 ^ x
    d = y % 17
    res = 4 - 12 - x
    t0 = (res + res) * res
    z = d * d ^ t0
    t1 = idx[y % 5] * x
    aux = t1 ^ d & 11
    u = d - x + x
    b = d + d | u + aux
    s = 16 * aux
    m = 0
    while m < 7:
        t2 = d ^ idx[z % 5]
        t3 = (t2 + (d | y) | 19) - m
        res = t3 % 65521
        m = m + 1
    t4 = 4 * idx[b % 5]
    v = t4 & res // 6
    t5 = idx[b % 5]
    t6 = s % 65521
    prv = t6 & t5 // 6
    w = 0
    while w < 11:
        t7 = x * y % 17
        t8 = idx[y % 5]
        idx[aux % 5] = t7 * t8 % 251
        t9 = (z >> 2 & 1) + w
        x = t9 & 8191
        if 20 + v <= 10:
            t10 = v * 10 + u + 14 | x
            x = t10 % 65521
            t11 = (z ^ b ^ prv) - b
            b = t11 % 17
        w = w + 1
    c = s * x & 16383
    idx[c % 5] = (4 + x ^ z) % 251
    t12 = (z | c) << 4
    t13 = (idx[v % 5] + 13) * res
    t14 = idx[res % 5]
    t15 = c * t14 >> 3
    t16 = (t15 >> 1) % 17
    b = fn0(t12 % 4093, t13 & 32767, t16)
    idx[z % 5] = x // 5 % 251
    idx[y % 5] = d - prv >> 1
    t17 = idx[d % 5] - res
    t18 = (t17 ^ idx[z % 5]) - d
    return t18 & 16383

if __name__ == "__main__":
    arg = 4
    expected = 16362
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
