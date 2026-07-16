# Auto-extracted from ds_lt256k_500.jsonl
# record_id=407  entry=f  input='6'  output='230'  tokens=75299

def fn0(b, j):
    hi = [636, 470, 767, 832]
    t0 = j + hi[b % 4] << 3
    t1 = (j | b) + b * j ^ t0
    b = t1 % 17
    if j & b == 52:
        t2 = hi[j % 4]
        t3 = j & t2
        t4 = t3 ^ j - b
        hi[b % 4] = 9 * 13 & t4
    j = j - 14 << 3
    if b & hi[j % 4] < 19:
        if j & 9 != 8:
            b = b | 4
            j = j ^ 7
    j = 15 - b & b * 6
    acc = 0
    while acc < 9:
        t5 = j // 2 - acc
        j = (t5 | acc) & 8191
        acc = acc + 1
    return (j << 2) % 4093

def fn1(j, g, m):
    c = 0
    while c < 3:
        e = 0
        while e < 3:
            m = (11 & g) - e & 1023
            t0 = (j * 12 - m * g) // 6
            m = t0 % 17
            e = e + 1
        c = c + 1
    m = 7 * m - m
    if g + m == 41:
        g = (j << 4 ^ g >> 3) % 17
        m = 7 - j << 2
    else:
        j = j - m
    for w in range(11):
        t1 = 9 ^ 4 ^ w & j
        j = (t1 + (w - m) % 251) % 17
        m = m + g & 1023
        j = (j // 3 >> 4) % 251
    for p in range(11):
        t2 = p - j
        t3 = t2 & 14 - m
        j = (t3 | m) & 511
        g = (5 * m | g) % 17
    return (j * 20 + m) % 17

def f(x):
    hi = x * x
    buf = 18 + hi
    prv = (hi - buf) // 5
    t0 = prv * hi % 9973
    t1 = (x + prv) % 251
    t2 = (x | prv) >> 2
    buf = fn1(t0, t1, t2 % 1009)
    t3 = (x | 3) * prv
    t = t3 + buf
    t4 = (hi & buf) * (t - buf)
    t5 = 13 ^ t | prv + 20
    t6 = (t ^ x) % 1009
    t7 = t6 * x % 1009
    hi = fn0(t4 & t5, t7)
    if buf * buf <= 31:
        hi = buf + 17
        t8 = prv << 1 & 2047
        t9 = (hi - 6) % 251
        x = fn0(t8, t9)
    t10 = (hi << 1) * (prv >> 3)
    res = t10 - (buf ^ x ^ buf) & 4095
    for g in range(10):
        t = (res ^ t) % 9973 * t % 9973
        b = 0
        while b < 5:
            res = (prv | g | b) % 9973
            t11 = t * prv & res
            t12 = t11 >> 3 | x
            x = t12 & 8191
            t13 = (b - 19 + 2 | 9) ^ t
            buf = t13 % 9973
            b = b + 1
        res = ((res ^ prv) << 1) % 9973
    return (12 - x ^ prv) % 251

if __name__ == "__main__":
    arg = 6
    expected = 230
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
