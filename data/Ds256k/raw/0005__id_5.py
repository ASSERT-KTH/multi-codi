# Auto-extracted from ds_lt256k_500.jsonl
# record_id=5  entry=f  input='18'  output='6533'  tokens=106161

def fn0(a, j):
    tmp = (j >> 3) * j - j & 255
    cur = j * j % 9973
    j = j // 2 - j
    prv = 0
    while prv < 6:
        cur = ((cur ^ tmp) - (a ^ 7)) % 9973
        for acc in range(2):
            t0 = 1 * 12 * acc
            t1 = (t0 ^ prv) + tmp
            tmp = t1 % 9973
            t2 = (j >> 4) - j
            j = (t2 ^ tmp) & 2047
        if cur % 4093 > 16:
            t3 = cur * cur - prv
            tmp = t3 % 17
        prv = prv + 1
    a = (a | tmp) - cur * tmp & 16383
    cur = j << 2
    for b in range(4):
        if cur * 11 <= 63:
            t4 = a | 4
            t5 = t4 + tmp // 8
            t6 = t5 + j - cur
            cur = t6 % 97
        a = a * j % 4093
    t7 = ((cur | a) - cur) // 6
    return t7 % 17

def fn1(c, g, d):
    tot = [30, 78, 70, 40, 84]
    t0 = (16 & 10) + 9
    y = t0 - 10 | c
    for res in range(10):
        y = d - res & 16
        for acc in range(10):
            c = (d | g) - acc & 262143
        t1 = c ^ tot[c % 5]
        t2 = t1 * tot[d % 5]
        d = t2 & 4095
    if d % 97 >= 42:
        y = (1 - d) * 5
        t3 = 7 + g
        t4 = t3 ^ y >> 4
        t5 = t4 >> 1 & 255
        t6 = tot[c % 5] // 6 + d
        t7 = t6 + ((g | d) + 7) & 1023
        d = fn0(t5, t7)
    else:
        p = 0
        while p < 7:
            t8 = tot[d % 5] * y
            t9 = (t8 ^ y - d) % 251
            tot[p % 5] = t9 % 97
            t10 = tot[c % 5]
            t11 = (g & y) // 7
            t12 = 15 - t10 + p
            c = (t11 + t12) % 97
            t13 = (10 & 6) + y
            g = t13 - p & 8191
            p = p + 1
        d = c + g + d ^ c
    y = 16 + d
    t14 = 6 | 4
    d = t14 - (d & y)
    c = 14 + c
    t15 = c << 2 << 1 | y
    return t15 % 251

def f(x):
    s = [9, 185, 3, 214, 164]
    tot = s[x % 5] ^ 1 | x
    nxt = 0
    while nxt < 5:
        x = (tot - nxt) % 65521
        t0 = s[nxt % 5] >> 1
        x = t0 * x % 65521
        t1 = x - tot << 1
        tot = t1 & 16
        nxt = nxt + 1
    x = (x ^ tot) // 7
    t2 = s[tot % 5]
    t3 = x ^ t2
    t4 = t3 + (x ^ tot)
    t5 = t4 + tot & 255
    t6 = x * 16 % 251
    x = fn0(t5, t6)
    if tot - 4 == 32:
        t7 = s[tot % 5]
        t8 = s[tot % 5]
        tot = t7 & tot & t8
    else:
        if 10 + x < 61:
            t9 = (4 | 12) * (tot << 3)
            s[tot % 5] = t9 % 251
        else:
            t10 = (x << 4) - tot & 255
            s[x % 5] = t10 % 251
    t11 = x - 18 | x * x
    tot = t11 >> 2 & 255
    for m in range(17):
        x = (m | tot) % 17
        res = 0
        while res < 12:
            s[res % 5] = (11 - x) % 251
            s[m % 5] = 9 - tot % 17
            res = res + 1
    t12 = x * tot << 1
    return (t12 ^ tot) % 65521

if __name__ == "__main__":
    arg = 18
    expected = 6533
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
