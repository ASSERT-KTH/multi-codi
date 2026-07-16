# Auto-extracted from ds_lt256k_500.jsonl
# record_id=426  entry=f  input='9'  output='16'  tokens=72725

def rec(n, a):
    if n <= 0:
        return a
    e = 0
    while e < 7:
        t0 = (n & a) - a
        a = (t0 - a) % 65521
        if 19 * n | a > 56:
            a = (n + 12 - n | a) % 251
            a = (6 - a) % 251
        t1 = e * e + a
        a = t1 % 65521
        e = e + 1
    res = 0
    while res < 9:
        for hi in range(2):
            a = ((a + 6) // 3 | hi) % 9973
            a = (res * n ^ a) & 2047
            a = (n - res - a) % 251
        res = res + 1
    t2 = 5 - n + 7
    t3 = (t2 ^ a) % 65521
    return rec(n - 1, t3)

def fn0(m, j):
    t0 = m + m - m
    t1 = j % 17 << 1
    prv = t0 * t1 % 9973
    y = 8 ^ j
    m = rec(75, m & j)
    cnt = (j | y) % 9973
    t2 = j * m - j
    j = t2 % 9973
    if m * prv != 55:
        prv = cnt // 4
    if j ^ y >= 47:
        t3 = m & cnt
        t4 = t3 - prv * j
        prv = t4 - cnt & 16383
        for val in range(4):
            j = (m + prv ^ val) % 9973
            cnt = (m + m | val) % 4093
    return prv >> 3 & 16383

def fn1(g):
    y = [292, 879, 872, 792, 882, 692]
    w = g - 12 + 12 >> 2
    buf = w * 16 - 6
    t0 = (8 ^ g) + buf
    t1 = (19 + w) // 8
    cur = t0 | t1
    for j in range(4):
        w = (w - buf + g) % 4093
    t2 = g % 9973 - (cur | g)
    aux = t2 % 97
    lo = 0
    while lo < 3:
        g = (14 | 6) - buf + g & 16383
        aux = (cur ^ 3) + aux & 4095
        lo = lo + 1
    t3 = g + 3
    t4 = t3 ^ (cur | aux)
    b = (t4 + w) % 4093
    return aux & 13

def f(x):
    c = [950, 178, 411, 931, 680]
    y = x % 17 * (x ^ 4)
    s = x ^ c[y % 5]
    acc = 0
    while acc < 304:
        y = (acc & x) * y * 12 % 97
        s = (acc - 6 - x) % 17
        c[y % 5] = (y | acc) * s % 97
        acc = acc + 1
    if x & c[y % 5] <= 19:
        t0 = c[x % 5]
        t1 = (x ^ t0) - x
        x = t1 & s
    else:
        c[y % 5] = x - 16 & y
    s = y - x ^ s
    t2 = s - 6 & y * s
    s = (y * s | s) * t2 & 255
    return (y // 4 ^ x) % 17

if __name__ == "__main__":
    arg = 9
    expected = 16
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
