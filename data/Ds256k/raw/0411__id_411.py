# Auto-extracted from ds_lt256k_500.jsonl
# record_id=411  entry=f  input='13'  output='1'  tokens=161226

def fn0(b, c):
    e = [478, 147, 583, 427, 170, 717]
    t0 = c * c >> 4
    lo = t0 % 1009
    t1 = b ^ 9 ^ 7
    c = t1 + e[b % 6]
    for buf in range(10):
        aux = 0
        while aux < 12:
            c = 18 + e[lo % 6] & c
            c = (buf | c) & 262143
            t2 = (aux & e[c % 6]) - buf
            c = t2 & 255
            aux = aux + 1
        if 17 + c <= 31:
            t3 = (18 + lo - 12) // 7
            e[c % 6] = t3 % 1009
            t4 = 6 * c >> 4
            b = (t4 | buf) & 4095
        else:
            e[c % 6] = lo * b % 65521 % 1009
    lo = lo // 7 ^ lo
    for j in range(3):
        b = ((j ^ 5) * j | c) & 32767
        e[j % 6] = (lo + 2) % 1009
        for cur in range(9):
            t5 = 1 - lo >> 3
            e[b % 6] = t5 & b
    e[lo % 6] = e[b % 6] // 4
    nxt = 0
    while nxt < 8:
        t6 = 13 - c
        t7 = t6 & lo * 7
        b = t7 + b & 1023
        t8 = nxt << 2 | lo
        c = t8 // 5 % 65521
        nxt = nxt + 1
    b = (c * lo * c ^ c) % 251
    t9 = 3 * 3 | lo
    return t9 & 255

def fn1(m, g):
    q = [3, 47, 209, 96]
    if g << 1 != 51:
        g = m ^ g
        g = m ^ 7
    p = (m ^ g) - g
    t0 = (g | 10) + m * p
    q[g % 4] = t0 % 9973 % 251
    prv = (g ^ m) % 9973 >> 3
    t1 = q[p % 4] - 9
    t = t1 * (prv ^ 4) >> 1
    t2 = g - prv + prv
    g = t2 ^ (6 * prv | m)
    m = t + 15 - m
    t3 = (p | 10) ^ q[m % 4]
    return t3 & 4095

def f(x):
    t = x * 2 - x
    for s in range(32):
        x = (x - s) % 251
        t = ((t ^ s) >> 3 << 4) % 4093
    if 12 * x <= 1:
        x = (x << 3) * 4 - x
        for e in range(9):
            x = t - 5 & e
            t0 = e * 20
            x = t0 & (x & e)
            t = (x - 6) * e & 8191
    t1 = (t - x) % 251
    t2 = t - 15 ^ x + x ^ t
    t = fn1(t1, t2 % 17)
    t3 = x // 3 * t
    res = t3 & t
    t4 = (res >> 3) % 17
    t5 = ((19 << 4) + res) % 251
    res = fn0(t4, t5)
    tmp = (x - 16) * (res - 4) & 1023
    t6 = 18 * res * (res << 2) * t
    t7 = tmp + res & 65535
    res = fn1(t6 & 65535, t7)
    for q in range(5):
        t8 = res - q ^ q
        res = t8 * tmp & 32767
        t = q * tmp % 251
    d = res * 15 >> 4 & x
    cur = 5 & d
    t9 = (x ^ 1) & (t | d)
    t10 = (t9 | t + d - tmp) % 4093
    t11 = (t - x ^ 4) & 511
    x = fn1(t10, t11)
    y = cur * tmp
    t12 = res // 6 ^ (res | d)
    d = fn0(t12 % 4093, 20 & tmp)
    return ((d >> 1 ^ 3) + 4) % 17

if __name__ == "__main__":
    arg = 13
    expected = 1
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
