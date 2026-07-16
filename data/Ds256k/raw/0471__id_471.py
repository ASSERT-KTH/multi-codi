# Auto-extracted from ds_lt256k_500.jsonl
# record_id=471  entry=f  input='6'  output='0'  tokens=100437

def fn0(d, c, j):
    cnt = [262, 92, 121, 946]
    d = 3 - c ^ (1 ^ c)
    t0 = c ^ cnt[c % 4]
    cnt[j % 4] = t0 % 1009
    lo = 0
    while lo < 2:
        for z in range(4):
            t1 = (j << 1) // 5 // 6
            cnt[j % 4] = t1 % 1009
            t2 = 16 - cnt[z % 4]
            c = (t2 ^ d) % 9973
            t3 = cnt[d % 4]
            t4 = lo | j
            t5 = cnt[lo % 4]
            t6 = cnt[c % 4]
            t7 = 9 | d
            t8 = t4 + 12 * t3
            t9 = t7 * (t5 + t6)
            t10 = (t8 - t9) % 9973
            cnt[lo % 4] = t10 % 1009
        lo = lo + 1
    b = 0
    while b < 7:
        for v in range(5):
            t11 = cnt[c % 4]
            t12 = cnt[b % 4]
            t13 = d - t12
            t14 = t11 + b << 2
            t15 = t13 + 2 * 3
            c = (t14 ^ t15) % 1009
            j = d - cnt[v % 4] & 16383
            t16 = cnt[j % 4]
            t17 = cnt[d % 4]
            t18 = t16 * t17 | 8
            cnt[j % 4] = (t18 + j) % 1009
        if d + b < 1:
            t19 = d % 1009 * c
            j = (t19 ^ b) & 16383
        d = ((b << 4 >> 2) + d) % 1009
        b = b + 1
    t20 = cnt[d % 4]
    t21 = j & c
    t22 = c - j - c
    t23 = t21 * (t20 << 3)
    return t22 - t23 & 4095

def f(x):
    tmp = [47, 81, 5, 78, 48, 27, 19]
    e = tmp[x % 7] * x
    t0 = tmp[e % 7]
    aux = (x - e) * t0 >> 1
    s = x - 17 - aux
    p = aux - 19
    y = 7 ^ p
    g = s ^ y
    idx = 0
    while idx < 95:
        t1 = (20 | s) ^ p
        y = (t1 ^ y) % 4093
        if e - 15 <= 40:
            tmp[x % 7] = p // 7 % 97
        else:
            tmp[p % 7] = (g | 19) % 97
        x = idx * tmp[aux % 7] & 262143
        idx = idx + 1
    tot = aux >> 2
    b = (e + 8 | s) * x & 511
    t2 = y // 5
    cnt = t2 | s ^ aux
    t3 = (x * x ^ b) * b
    t = t3 % 17
    c = (x >> 3) % 17
    a = cnt // 7 * x % 4093
    if p - x >= 16:
        tmp[cnt % 7] = (cnt - tmp[b % 7]) % 97
    nxt = 14 & p & 4
    t4 = p ^ tmp[e % 7]
    w = t4 * tot % 4093
    j = 0
    while j < 10:
        for m in range(9):
            t5 = (m << 1) * aux >> 1
            tmp[t % 7] = t5 % 97
        j = j + 1
    t6 = tmp[w % 7]
    t7 = x & t6
    t8 = t7 | t & x
    t9 = e * 18 % 17
    hi = t8 & t9
    return (tot ^ nxt ^ t) * p % 17

if __name__ == "__main__":
    arg = 6
    expected = 0
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
