# Auto-extracted from ds_lt256k_500.jsonl
# record_id=225  entry=f  input='19'  output='994'  tokens=131881

def rec(n, a):
    if n <= 0:
        return a
    p = (n // 4 - a) % 17
    if n * n | p <= 36:
        p = (p & 17) + (a ^ n) & 4095
    t0 = (p + p | a) & 32767
    return rec(n - 1, t0)

def fn0(b, g):
    aux = [80, 26, 6, 45, 15, 71, 23, 9]
    acc = 0
    while acc < 6:
        g = (acc ^ b) & 4095
        g = ((b + acc & b) + b) % 65521
        acc = acc + 1
    for lo in range(9):
        t0 = (b - 13) // 4
        b = t0 & 255
        g = (7 - g) % 251
    t1 = 16 * b % 251
    g = rec(44, t1)
    aux[g % 8] = (b * g & 65535) % 97
    s = 18 * 13 - g
    t2 = aux[b % 8]
    g = (t2 << 3) - b
    t3 = b | aux[b % 8]
    aux[b % 8] = ((1 << 1) - t3 | b) % 97
    aux[b % 8] = g // 5 % 97
    t4 = b | 9
    t5 = 8 - s + s
    t6 = t4 ^ 9 * s
    return t5 * t6 % 251

def fn1(b):
    t0 = b | 8 | b
    prv = t0 + b
    t1 = 1 - prv & prv
    idx = t1 + prv
    c = 0
    while c < 4:
        b = b >> 1 & 262143
        for lo in range(9):
            t2 = idx * 4 & prv << 4
            b = t2 - idx - lo & 8191
            t3 = prv // 6 | lo ^ c
            prv = t3 & 65535
            t4 = (c * 11 - (idx ^ lo)) // 3
            prv = t4 % 4093
        c = c + 1
    val = b << 3
    for buf in range(9):
        for acc in range(6):
            t5 = (prv ^ 5) * (15 + b)
            prv = (t5 | val) % 9973
            t6 = acc + buf + idx
            idx = t6 % 9973
            t7 = acc - buf
            t8 = t7 * (val + b)
            b = t8 % 4093
    t = 0
    while t < 12:
        t9 = (prv - b) % 9973 ^ idx
        idx = t9 % 9973
        t = t + 1
    t10 = (idx >> 1) % 9973
    b = rec(35, t10)
    t11 = (val + val) // 4
    a = (t11 << 2) % 4093
    return b * b + val & 262143

def f(x):
    t0 = x - 16 ^ x * x
    x = fn1(t0 % 17)
    acc = 0
    while acc < 3:
        for z in range(12):
            x = (15 - x) % 1009
            x = x + acc & 262143
        acc = acc + 1
    cnt = 0
    while cnt < 13:
        t1 = (x // 2 & x) * 20
        x = t1 % 1009
        nxt = 0
        while nxt < 2:
            t2 = 3 * cnt * (x - 8)
            x = t2 & 16383
            t3 = cnt << 4
            t4 = t3 ^ 15 - 16
            t5 = t4 - 17 | x
            x = t5 % 1009
            t6 = 1 * nxt ^ nxt ^ nxt
            x = (t6 | x) % 17
            nxt = nxt + 1
        cnt = cnt + 1
    prv = x ^ 8 | 15
    tmp = (prv + prv) * prv - 13 & 2047
    t7 = ((8 << 1) * 17 + prv) % 4093
    t8 = (tmp | 15) - 11
    x = fn0(t7, t8 % 1009)
    tmp = prv << 3 >> 3 ^ tmp
    t9 = 12 ^ prv
    t10 = t9 & x * tmp
    return (t10 - prv) % 1009

if __name__ == "__main__":
    arg = 19
    expected = 994
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
