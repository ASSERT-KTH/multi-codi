# Auto-extracted from ds_lt256k_500.jsonl
# record_id=84  entry=f  input='3'  output='11'  tokens=246809

def f(x):
    cnt = x + x
    t0 = (x << 2) - x
    v = t0 & x
    b = cnt * x & 1
    for idx in range(25):
        buf = 0
        while buf < 2:
            t1 = v * cnt * (b & v)
            t2 = v + 16 + cnt - t1
            cnt = t2 % 9973
            buf = buf + 1
        for d in range(6):
            b = (b - d) % 9973
    acc = v - 8 & v
    for j in range(8):
        tot = 0
        while tot < 2:
            cnt = x * cnt % 9973 & acc
            tot = tot + 1
        if v + b < 23:
            t3 = 9 - j | cnt
            v = t3 % 17
        else:
            t4 = (x ^ b) & v * j | acc
            v = t4 & 32767
        for lo in range(10):
            b = ((b >> 1) * lo + b) % 9973
    t5 = (v << 1) - 2 * cnt
    g = t5 + 5
    for hi in range(2):
        g = (g << 4) - cnt & 65535
        x = (9 | v) - cnt - hi & 8191
    for u in range(10):
        for c in range(9):
            t6 = 16 * b
            t7 = t6 + (c | x)
            cnt = t7 & 1023
            t8 = 1 - acc | 1
            t9 = b * 1 >> 1
            t10 = (t8 | t9) - v
            v = t10 % 17
            t11 = (u & 7) - 5
            t12 = (t11 << 1) + x
            x = t12 & 1023
    s = acc + x >> 3
    prv = s >> 3
    if x - 19 >= 43:
        if 4 + cnt != 17:
            g = v | 4
            t13 = s * s
            t14 = (b + prv) // 4
            t15 = t13 ^ s + 18
            s = t14 & t15
        else:
            b = acc - v
            b = b % 17 * prv
        if 4 ^ 10 | x <= 56:
            t16 = (9 | b) * b + 12
            b = t16 % 9973
    if 5 + s >= 46:
        t17 = acc + acc << 3
        v = t17 & 2
    else:
        cur = 0
        while cur < 11:
            t18 = s * b - (v + v)
            t19 = (b + 2 << 4 | t18) ^ cnt
            cnt = t19 % 9973
            cur = cur + 1
        z = 0
        while z < 3:
            prv = acc + acc - prv & 4095
            z = z + 1
    m = 0
    while m < 3:
        if acc + 13 >= 19:
            t20 = s ^ prv ^ acc
            acc = t20 & 4095
            t21 = s // 3 - acc
            acc = t21 % 17
        else:
            t22 = (15 ^ x) * 12 >> 4
            v = (t22 ^ v) & 2047
        t23 = (acc ^ x) + cnt
        cnt = t23 & 2047
        m = m + 1
    return (v - cnt) % 17

if __name__ == "__main__":
    arg = 3
    expected = 11
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
