# Auto-extracted from ds_lt256k_500.jsonl
# record_id=240  entry=f  input='1'  output='396'  tokens=216336

def fn0(m, d):
    w = [959, 651, 534, 203, 48, 980, 804]
    for aux in range(2):
        t0 = aux - d + w[aux % 7]
        d = t0 & 8 << 3
        t1 = d + 15 - (d | m)
        d = t1 & 65535
    p = d % 1009 >> 4
    if w[d % 7] ^ m < 57:
        p = p | 5
    else:
        d = d & 3 & p
    e = p ^ m
    w[d % 7] = (d + e) % 1009
    return (p >> 2) * e & 1023

def fn1(b, a):
    val = [32, 4, 54, 90]
    val[b % 4] = (9 + a) % 97
    v = b + val[b % 4] | 6
    t = a & 2 | a
    c = val[b % 4] + t
    t0 = val[a % 4]
    val[b % 4] = t0 // 3
    t1 = val[v % 4] * a << 2
    return (t1 >> 4) % 1009

def f(x):
    cnt = [692, 576, 373, 437, 522]
    idx = 0
    while idx < 9:
        if cnt[x % 5] == 22:
            t0 = idx * 6 * 16
            t1 = t0 + idx ^ x
            cnt[x % 5] = t1 % 1009
        else:
            t2 = (idx | 10) - (idx - 20)
            cnt[x % 5] = t2 + x
        t3 = cnt[x % 5]
        t4 = 9 - 19 ^ t3
        x = t4 & (idx ^ 9) - x
        x = x - 13 & 16383
        idx = idx + 1
    for q in range(4):
        t5 = 14 - q + (q | 15) - 17
        cnt[q % 5] = t5 ^ x
        t6 = (x + 14) * (20 & x)
        t7 = t6 - (x - 20) // 5
        x = t7 & 255
        x = (x ^ q) % 17
    prv = x
    cnt[prv % 5] = x | 4
    cnt[prv % 5] = (prv | 5) & prv
    z = 0
    while z < 8:
        t8 = 20 + x ^ (4 ^ x)
        x = t8 % 9973
        t9 = x & 1 ^ x ^ 4
        x = t9 % 1009
        prv = x * z & 20
        z = z + 1
    t10 = (10 - prv) % 65521
    t11 = 7 * cnt[x % 5] & 2047
    prv = fn0(t10, t11)
    t12 = prv + cnt[prv % 5]
    t13 = x * cnt[x % 5] // 3
    acc = t13 * (x % 17 | t12) & 2047
    buf = 0
    while buf < 8:
        t14 = (2 | x) + prv % 1009
        t15 = (x - acc) // 2 | t14
        acc = t15 & 8191
        t16 = (acc >> 3) * buf
        x = t16 * buf & 32767
        if 1 | x >= 35:
            x = (buf | acc) & (3 ^ 4)
            cnt[prv % 5] = (15 - prv) * x % 1009
        else:
            t17 = buf * x ^ acc
            cnt[buf % 5] = t17 % 1009
        buf = buf + 1
    t18 = x & cnt[x % 5]
    t19 = 7 ^ cnt[acc % 5]
    t20 = (16 ^ acc) + t19
    y = (t18 ^ x) - t20
    for s in range(270):
        t21 = (x ^ s) * (s ^ x)
        prv = (acc // 7 >> 1) * t21 % 1009
    if x - 3 > 63:
        t22 = cnt[x % 5] * y % 9973
        t23 = cnt[prv % 5]
        t24 = t23 * x | acc
        acc = fn1(t22, t24 & 4095)
    t25 = prv * 11 << 3
    t26 = t25 * prv & 1023
    cnt[y % 5] = t26 % 1009
    for tot in range(10):
        x = (x | tot) & 6
    t27 = cnt[acc % 5] ^ y
    t28 = (y << 4) * t27 % 1009
    x = fn1(prv & acc, t28)
    if prv >> 3 > 53:
        cnt[prv % 5] = (y - 14) % 1009
        for t in range(8):
            t29 = t - prv - (t - acc)
            t30 = t29 ^ x + t >> 2
            cnt[prv % 5] = t30 % 1009
            t31 = (y + y) * (t + y)
            prv = t31 & 4095
    else:
        t32 = 18 - 12 + acc
        prv = t32 * ((1 ^ y) + prv) % 65521
        if x * 14 > 15:
            t33 = 20 * prv - 12
            t34 = t33 - 1 & 2047
            cnt[y % 5] = t34 % 1009
            t35 = y - cnt[acc % 5]
            t36 = cnt[acc % 5]
            t37 = t36 * cnt[x % 5]
            t38 = (x ^ 2) - t35
            y = t38 * (t37 * (y - x)) & 255
    return acc * 20 & 511

if __name__ == "__main__":
    arg = 1
    expected = 396
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
