# Auto-extracted from ds_lt256k_500.jsonl
# record_id=4  entry=f  input='3'  output='50'  tokens=149071

def fn0(j, e, d):
    m = [89, 50, 82, 74, 95]
    for c in range(8):
        for z in range(8):
            t0 = (z + 5) * z - j
            d = t0 & 4095
    acc = 0
    while acc < 8:
        for val in range(12):
            t1 = (e << 2) + val
            j = t1 % 1009
        if j * acc >= 10:
            t2 = acc * acc % 17
            m[j % 5] = (t2 ^ j) % 97
        else:
            t3 = m[d % 5]
            t4 = t3 * acc
            t5 = t4 ^ acc * acc
            j = (t5 << 3) % 17
            t6 = m[e % 5]
            t7 = t6 ^ m[d % 5]
            m[e % 5] = (t7 + acc * 1) % 97
        t8 = 6 << 4 ^ acc
        d = t8 & e
        acc = acc + 1
    t9 = d - e ^ d
    a = t9 * (j - e >> 2) & 131071
    for t in range(5):
        t10 = (t + e | j) ^ d
        d = t10 % 1009
    if m[e % 5] | j > 64:
        a = 13 + 11 | d
        a = (j & 3) * (d >> 1)
    else:
        d = 13 ^ e
    t11 = e ^ 9 ^ d - 14
    return t11 - a & 255

def fn1(m, g, b):
    t = [992, 289, 223, 292, 565, 401, 67, 179]
    for y in range(11):
        for q in range(4):
            g = (q - b) % 1009
            t0 = y * q
            t1 = t0 + (q | g)
            g = t1 % 251
            t2 = g + t[y % 8] + g
            m = t2 - (4 * q ^ b) & 32767
        m = (g & 17 ^ y) % 1009
        if b // 2 == 15:
            t3 = (14 << 2) + g
            t[b % 8] = t3 % 1009
            b = (g + m) * b % 1009
    if t[m % 8] - b >= 44:
        t4 = t[b % 8]
        t5 = m + b
        t6 = t5 * (t4 + 4)
        b = t6 % 251
    t7 = t[b % 8] ^ 6
    t8 = t7 - (17 + 8)
    nxt = t8 + m // 3 // 8
    m = b | nxt
    t9 = t[b % 8]
    t10 = t9 | t[g % 8]
    g = t10 - g // 3
    if 9 * 11 | g > 12:
        b = 9 & nxt
        t[g % 8] = (b ^ g) % 1009
    else:
        g = 9 * g & (m | g)
        t11 = (b << 4) * nxt
        t12 = t11 * 18 & 1023
        t[m % 8] = t12 % 1009
    t13 = (13 ^ m) * g - b
    return (t13 + nxt) % 1009

def f(x):
    t0 = (x * x + x) % 97
    t1 = (x ^ 12) % 97
    t2 = 15 & x
    t3 = t2 | x - 8
    t4 = x - 18 + 15
    t5 = (t3 + t4) % 9973
    x = fn0(t0, t1, t5)
    t6 = (x | 11) & x * x
    nxt = t6 + (x - 10 | x // 5)
    t7 = nxt * x * 10
    t8 = (nxt + nxt) // 8
    prv = (t7 + t8) % 9973
    v = prv >> 4
    t9 = (x + 4) * prv % 9973
    t10 = x * x | nxt * nxt
    t11 = ((11 | prv) - nxt) * t10 & 511
    t12 = (x - 4) * 6
    t13 = (t12 ^ (v ^ x) & v) & 65535
    v = fn1(t9, t11, t13)
    c = x + prv
    t14 = 17 - nxt
    t15 = t14 | v & prv
    for tot in range(154):
        prv = 4 * prv % 9973
        nxt = 4 * (v + nxt) & 255
    return t15 & 255

if __name__ == "__main__":
    arg = 3
    expected = 50
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
