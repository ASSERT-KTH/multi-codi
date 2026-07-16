# Auto-extracted from ds_lt256k_500.jsonl
# record_id=106  entry=f  input='9'  output='0'  tokens=105188

def f(x):
    g = x * x // 3 - x
    t0 = x - 9
    t1 = t0 * (9 ^ x)
    d = t1 + x
    t2 = x - 3 - g
    tot = t2 - ((g | 20) - g)
    j = 13 * g + tot
    t3 = 12 - g
    hi = t3 - (tot & 2)
    v = hi * hi & 20
    e = g + d ^ v
    if hi << 2 >= 64:
        for cnt in range(8):
            hi = (13 - hi - g) % 4093
            t4 = e * v | v ^ d
            t5 = t4 + (d + g) // 8
            e = t5 % 9973
        for m in range(2):
            t6 = (v ^ j) - e ^ m
            g = t6 & 4095
    else:
        tot = 18 - v + hi
        for q in range(3):
            hi = (g + j - q) % 9973
            hi = (hi - q - e) % 9973
            t7 = q - 5 + d
            d = t7 % 9973
    y = tot ^ x
    t8 = (20 - 4) * (j + g)
    res = t8 * hi % 4093
    for w in range(12):
        d = (res | w) % 4093
    for b in range(9):
        s = 0
        while s < 2:
            res = (b << 2) + x + s & 32767
            d = (3 | b) - y + s & 262143
            s = s + 1
        t9 = 7 + x | tot
        d = (t9 - b) % 9973
        a = 0
        while a < 10:
            t10 = (b << 4) + e
            e = t10 % 65521
            hi = hi >> 1 & 16383
            a = a + 1
    t11 = (tot | hi) - y * g
    t12 = t11 ^ (g - tot ^ res & g)
    val = t12 & 8191
    for aux in range(5):
        if y * g <= 28:
            d = (res + j | aux) % 4093
        else:
            t13 = (y & 13) * aux
            v = t13 % 65521
        t14 = x + aux ^ val
        e = t14 % 4093
        v = (res * y ^ aux) & 255
    t15 = res // 5 ^ g - val
    p = t15 + (res + hi - val)
    nxt = 0
    while nxt < 6:
        t16 = val // 6 // 2 >> 3
        v = t16 - nxt & 131071
        nxt = nxt + 1
    tmp = 0
    while tmp < 5:
        t17 = 2 * j << 3
        y = (t17 ^ y) & 32767
        if e ^ d == 18:
            t18 = 8 << 4
            t19 = t18 ^ (y | tmp)
            res = t19 & 32767
            t20 = (1 | d) * y ^ tmp
            res = t20 & 16383
        tmp = tmp + 1
    t21 = hi // 2 * d
    u = t21 % 65521
    t22 = 9 + v
    return t22 & (4 & 8)

if __name__ == "__main__":
    arg = 9
    expected = 0
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
