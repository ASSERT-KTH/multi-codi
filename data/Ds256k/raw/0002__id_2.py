# Auto-extracted from ds_lt256k_500.jsonl
# record_id=2  entry=f  input='16'  output='32753'  tokens=86802

def fn0(d, b, g):
    for acc in range(5):
        t0 = b - g ^ g + d
        g = (t0 + d) % 1009
        for j in range(5):
            t1 = (g & d) * (acc | 6) + b
            b = t1 & 262143
            g = b // 8 - g & 1023
    t2 = d * g * (b * g)
    g = (t2 >> 1) % 251
    b = d & b
    for lo in range(10):
        t3 = (g >> 1) * lo
        t4 = t3 + ((9 ^ g) >> 2)
        d = t4 & 65535
        b = (g % 65521 ^ b) & 1023
    t5 = (19 & 12) - (b | d) ^ d
    return t5 & 32767

def f(x):
    buf = (19 * x | x) * x
    if x | 9 <= 26:
        t0 = x * (buf >> 3) * buf
        x = t0 % 65521
    else:
        q = 0
        while q < 8:
            t1 = (2 ^ q ^ buf >> 2) + x
            buf = t1 % 65521
            t2 = (1 - 9) * (buf ^ 16)
            x = t2 + x & 262143
            q = q + 1
        buf = 3 * buf * 17 >> 2
    b = x | 7
    t3 = (buf ^ 5) * b * buf
    tot = t3 & 131071
    if b >> 1 <= 40:
        prv = 0
        while prv < 4:
            buf = (x & 20) - prv & 511
            prv = prv + 1
    else:
        t4 = tot * 7 >> 1
        b = t4 * (buf * 11 * 16) % 65521
        b = x % 65521
    if x + 2 < 48:
        for m in range(10):
            buf = buf >> 3 & 32767
            x = (b * buf | m) % 65521
            t5 = (1 ^ buf) + x
            x = t5 & 65535
        for cur in range(3):
            t6 = 1 * buf >> 3
            buf = (t6 ^ tot) & 8191
            tot = (buf // 3 | cur) & 511
            t7 = (cur | 11) & (cur & x) | 14
            b = t7 & 32767
    else:
        if b << 1 > 44:
            t8 = x - b - tot
            tot = (t8 + buf) % 65521
    s = 0
    while s < 91:
        t9 = (x << 2) - (s + 20)
        x = t9 & x
        b = (s | b) % 17
        t10 = tot >> 1 & (s ^ 4)
        tot = (t10 ^ s) & 511
        s = s + 1
    t11 = (x << 1) + (b + b) | buf
    hi = t11 & 511
    a = buf // 6
    t = a * tot % 17
    for w in range(8):
        t12 = (w + w) * (tot ^ 5)
        tot = t12 % 65521
    t13 = (tot - t + a + t) % 17
    t14 = (tot ^ x) & b - hi
    t15 = (t14 >> 1) % 17
    t16 = tot // 3 % 65521
    t = fn0(t13, t15, t16)
    if buf % 65521 >= 45:
        e = 0
        while e < 7:
            t17 = (t << 3) // 5
            tot = (t17 ^ tot) % 17
            t18 = t >> 4 ^ 19
            b = (t18 - e) % 17
            a = a * 14 & 131071
            e = e + 1
        t19 = buf + buf & 255
        t20 = buf + 7 + 17 & 16383
        t21 = (buf - x) % 17
        x = fn0(t19, t20, t21)
    t22 = (b | x) - (x & tot) - tot
    return t22 % 65521

if __name__ == "__main__":
    arg = 16
    expected = 32753
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
