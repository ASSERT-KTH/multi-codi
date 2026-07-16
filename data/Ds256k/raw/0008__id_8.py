# Auto-extracted from ds_lt256k_500.jsonl
# record_id=8  entry=f  input='13'  output='734'  tokens=195597

def fn0(e, a, b):
    val = (5 - e ^ b) - 16
    t0 = 12 + a - a
    u = t0 * (a ^ 12 | val) % 251
    cnt = 0
    while cnt < 11:
        v = 0
        while v < 10:
            t1 = 14 ^ u
            t2 = t1 - (9 - val)
            val = t2 + a & 2047
            val = (val ^ 4) & e + cnt
            t3 = e // 5
            t4 = t3 + b // 8
            t5 = t4 // 3 ^ v
            val = t5 & 2047
            v = v + 1
        cnt = cnt + 1
    tot = (u ^ val) - b >> 1
    t6 = 9 - a ^ u & a
    t7 = b >> 3 ^ val // 7
    val = t6 | t7
    tot = val + a ^ 1 + val
    return (a - b + u % 17) % 251

def fn1(d, g):
    t0 = (g ^ 9 | d | d) & 262143
    t1 = (d >> 1) % 4093
    d = fn0(d % 17, t0, t1)
    q = 0
    while q < 5:
        g = (d - g) % 4093
        if d + g != 54:
            d = (d ^ q) & 1023
        q = q + 1
    t = d - g
    tot = 0
    while tot < 8:
        t2 = (t >> 3) * (d // 5)
        g = t2 & (t - g ^ 15)
        tot = tot + 1
    t3 = d * d * (t ^ 15)
    t4 = (g ^ d) + d ^ t3
    t5 = d // 6 ^ d ^ d
    g = fn0(d & 2, t4 % 17, t5 % 4093)
    m = t | g
    return d * g // 8 & m

def f(x):
    acc = (x ^ 9) + 14 - x
    cnt = acc + acc
    cnt = (11 << 1) + cnt
    for t in range(7):
        cur = 0
        while cur < 7:
            t0 = (cnt * 9 | t) - x
            x = t0 % 4093
            t1 = 9 + x >> 4
            x = t1 & 4095
            x = x - cnt & 65535
            cur = cur + 1
        for res in range(32):
            t2 = (cnt // 3 & 8) - 11
            x = (t2 - res) % 4093
        t3 = x >> 2
        t4 = t3 - (cnt + cnt)
        t5 = t4 * cnt - acc
        acc = t5 & 1023
    t6 = cnt * cnt * (acc * 14)
    t7 = (acc ^ x) // 7 % 9973
    t8 = x * 5 * (acc - cnt)
    t9 = (cnt + cnt) * cnt * t8 & 2047
    cnt = fn0(t6 & 4095, t7, t9)
    for lo in range(12):
        t10 = (lo - cnt) * (x * 4)
        acc = t10 & 511
        acc = (cnt << 3) * lo * lo % 9973
    prv = 0
    while prv < 6:
        if x - 9 == 62:
            x = (acc - x) // 2 % 9973
            acc = cnt & acc
        cnt = (acc >> 1 | prv) & 16383
        prv = prv + 1
    t11 = cnt + 11 >> 2 | 20
    return t11 % 65521

if __name__ == "__main__":
    arg = 13
    expected = 734
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
