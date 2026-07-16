# Auto-extracted from ds_lt256k_500.jsonl
# record_id=309  entry=f  input='20'  output='0'  tokens=215290

def rec(n, a):
    if n <= 0:
        return a
    t0 = 18 * n
    t1 = t0 | (19 | a)
    e = t1 & 2047
    t = 0
    while t < 2:
        t2 = e - 17
        a = t2 & t - 1
        t3 = 18 * 5 - 17
        a = t3 + a & 1023
        a = 5 - e & t
        t = t + 1
    t4 = 5 - 16 - a - n
    u = t4 & 32767
    t5 = 1 + (e << 1)
    t6 = t5 + a & 511
    return rec(n - 1, t6)

def fn0(d, m):
    cnt = [1, 45, 45, 90]
    t0 = cnt[m % 4] >> 3 << 1
    val = t0 + d
    val = val * m % 17
    nxt = 0
    while nxt < 5:
        z = 0
        while z < 11:
            t1 = nxt ^ 17 ^ nxt
            cnt[val % 4] = (t1 - val) % 97
            t2 = cnt[z % 4]
            cnt[z % 4] = (m + t2) % 97
            z = z + 1
        nxt = nxt + 1
    d = m & val
    t3 = cnt[d % 4]
    t4 = t3 * m % 1009
    val = rec(65, t4)
    t5 = m // 7 + 13
    cnt[d % 4] = t5 % 97
    cnt[m % 4] = (d >> 3) % 97
    val = (m | 16) + 13 | d
    return val * m + 19 * 2 & 8191

def f(x):
    t0 = 20 ^ x
    t1 = t0 ^ (x ^ 10)
    tot = t1 // 7
    t2 = (tot - 13) % 9973
    t3 = 8 - x - 6 & 2047
    tot = fn0(t2, t3)
    if 5 + x < 4:
        x = x * tot % 97
    tmp = tot // 4 * 9
    p = (tot ^ 6) * tmp % 251
    acc = 20 & tot
    b = acc + 18 - (acc << 2)
    for g in range(7):
        t4 = x * tot // 2 ^ g
        tmp = t4 % 1009
        if g & 3 | b > 19:
            t5 = x * 8 + g
            tot = t5 & 2047
            t6 = tmp // 5 * tot ^ b
            tmp = t6 % 9973
    aux = (b | p) - b + b
    prv = 0
    while prv < 101:
        t7 = aux >> 1
        t8 = t7 ^ (prv ^ 3)
        p = (t8 - p) % 1009
        prv = prv + 1
    t9 = (1 * 7 | x) % 97
    b = rec(22, t9)
    cur = 7 + b
    t = (tmp - tot & p) + aux
    if aux ^ b < 39:
        buf = 0
        while buf < 12:
            aux = (17 * tmp + aux) % 251
            t10 = (b | tot) * tmp
            b = (t10 ^ tot) & 32767
            buf = buf + 1
        idx = 0
        while idx < 12:
            t11 = (cur | 9) + idx
            b = t11 % 1009
            tmp = (9 + t - idx) % 251
            idx = idx + 1
    if x ^ 11 < 55:
        t12 = b + tot
        t13 = t12 - (b + tmp)
        t14 = t13 ^ 6 - tot
        x = t14 & 16383
        for hi in range(11):
            t15 = t | hi
            t16 = t15 ^ (tmp ^ acc)
            x = t16 % 251
            t17 = (tmp | t) + t ^ acc
            acc = t17 % 251
    else:
        d = 0
        while d < 2:
            t18 = (tot + acc) // 8
            aux = (t18 - aux) % 1009
            tmp = (x - tmp ^ 10) % 97
            t19 = b // 2 | d
            t = t19 & 8191
            d = d + 1
        if x + t <= 1:
            t20 = cur * aux - t & 255
            cur = rec(20, t20)
            tot = acc - tot
    return tot & 11

if __name__ == "__main__":
    arg = 20
    expected = 0
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
