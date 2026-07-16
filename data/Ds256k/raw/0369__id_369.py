# Auto-extracted from ds_lt256k_500.jsonl
# record_id=369  entry=f  input='11'  output='76'  tokens=85588

def rec(n, a):
    if n <= 0:
        return a
    t0 = (n ^ 7) + a
    cnt = (t0 + n) % 65521
    cnt = a - n & 255
    t1 = a * n + n
    t2 = (t1 >> 2) % 4093
    return rec(n - 1, t2)

def fn0(d):
    tmp = [124, 84, 204, 138, 143, 48, 84]
    a = d // 8
    t = d // 5
    t0 = tmp[a % 7]
    d = t0 ^ tmp[t % 7]
    t1 = (a & 16) + t & 255
    d = rec(52, t1)
    return t * d & 255

def fn1(g, a):
    buf = [49, 223, 193, 155, 47, 98, 35]
    t0 = buf[a % 7]
    a = fn0(t0 * g % 4093)
    if a - g != 24:
        q = 0
        while q < 5:
            t1 = 19 << 3
            t2 = t1 - (16 - 20)
            buf[q % 7] = (t2 | a) % 251
            t3 = a - buf[g % 7]
            buf[a % 7] = (t3 ^ q * q) % 251
            g = (g ^ a) & a + q
            q = q + 1
        for v in range(6):
            buf[g % 7] = (16 * g & 32767) % 251
            t4 = buf[a % 7]
            t5 = g + t4 - v
            a = t5 & 4095
    else:
        a = g + a - a
        a = a >> 4
    for prv in range(3):
        m = 0
        while m < 8:
            g = (a + g ^ a) % 4093
            m = m + 1
    acc = 0
    while acc < 7:
        w = 0
        while w < 12:
            buf[g % 7] = (g - a) % 251
            t6 = a * a * 5
            t7 = (t6 | a) + w
            g = t7 & 511
            w = w + 1
        g = g * acc % 251
        acc = acc + 1
    tmp = 20 ^ a
    t8 = (8 & 15) * (g + tmp)
    s = (t8 - tmp) % 4093
    for c in range(7):
        if a - 4 != 63:
            t9 = (1 ^ tmp) + c
            s = t9 % 4093
        else:
            t10 = (c ^ 10) * buf[a % 7]
            buf[c % 7] = t10 & buf[g % 7]
        t11 = c * g // 4 * g & 2047
        buf[s % 7] = t11 % 251
        t12 = g - 4 - (g << 2)
        buf[a % 7] = t12 % 251
    for hi in range(2):
        t13 = (5 - tmp ^ 15) // 5
        buf[s % 7] = t13 % 251
        tmp = tmp & 20
        a = (tmp ^ 16 | a) % 251
    return (s | 15) & 2047

def f(x):
    for v in range(5):
        for cur in range(39):
            x = (cur ^ 3) - x & 32767
            t0 = cur - 15 - x - v
            x = t0 % 9973
        for g in range(7):
            t1 = x - g + (g - 19)
            x = (t1 + g) % 251
            t2 = x // 8 ^ 13 - g
            x = t2 % 9973
            x = (v - 3 | x) & 16383
    t3 = (x - 6) % 9973
    x = rec(41, t3)
    lo = 7 * x * x - x & 1023
    lo = fn0((x << 2) % 9973)
    if x | lo <= 14:
        for aux in range(11):
            t4 = 19 ^ x
            t5 = lo + 13
            t6 = t4 * (lo + 6)
            t7 = t5 + (lo << 3)
            lo = (t6 + t7) % 251
            lo = ((19 + x) % 251 | aux) % 251
        lo = (10 & lo) + lo & lo
    nxt = (x >> 2) - (lo + x)
    t8 = x + 19 | x
    return (t8 - lo) % 251

if __name__ == "__main__":
    arg = 11
    expected = 76
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
