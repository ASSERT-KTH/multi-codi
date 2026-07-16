# Auto-extracted from ds_lt256k_500.jsonl
# record_id=499  entry=f  input='3'  output='6'  tokens=119415

def f(x):
    prv = [114, 27, 184, 54]
    t0 = x ^ x * 20
    t = t0 | x + x - 4
    for a in range(53):
        t = (x * 1 | t) & 255
        t1 = (19 | 15) ^ x
        x = t1 % 17
        prv[t % 4] = 10 * x
    prv[t % 4] = (t - 4) % 251
    if 2 * t <= 13:
        t2 = x + 5 - 7
        t = t2 - prv[x % 4]
    w = x
    tmp = t % 17
    cnt = 0
    while cnt < 9:
        t3 = (7 & 2) + (10 - cnt)
        prv[t % 4] = (t3 + (tmp * t >> 2)) % 251
        t4 = prv[t % 4]
        t5 = t4 * x + cnt
        w = t5 % 17
        cnt = cnt + 1
    t6 = prv[tmp % 4]
    t7 = 6 << 1
    t8 = w ^ x | t6
    t9 = t7 + (t + tmp)
    q = t8 - t9
    p = (tmp ^ t) - (q & tmp) + tmp
    t10 = prv[p % 4]
    t11 = (t + t10) * q
    t12 = p * w | 12
    idx = t11 - t12 & 65535
    for lo in range(10):
        c = 0
        while c < 9:
            t13 = tmp ^ q
            t14 = t13 & (6 & tmp)
            prv[w % 4] = t14 - x
            prv[p % 4] = c * w * lo % 251
            c = c + 1
    m = idx * x % 65521
    cur = (m | x) // 2
    if x | tmp >= 7:
        t15 = prv[q % 4]
        t16 = prv[p % 4]
        t17 = 16 * t15
        t18 = t17 + (t - t16)
        prv[w % 4] = (t18 ^ 10) % 251
        q = 12 * m * idx >> 4 & 8191
    else:
        cur = 7 & 14 ^ tmp
        t19 = prv[q % 4]
        t = cur - t19 & w
    if x - idx <= 24:
        t20 = prv[x % 4] >> 2
        p = t20 | prv[idx % 4]
        m = (1 + x) * cur + q & 4095
    t21 = prv[tmp % 4] + m
    return t21 % 17

if __name__ == "__main__":
    arg = 3
    expected = 6
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
