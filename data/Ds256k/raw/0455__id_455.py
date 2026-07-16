# Auto-extracted from ds_lt256k_500.jsonl
# record_id=455  entry=f  input='8'  output='956'  tokens=85971

def rec(n, a):
    if n <= 0:
        return a
    t0 = 8 - n & n
    t1 = n + n + a
    tot = (t0 ^ t1) % 65521
    if tot - n <= 5:
        t2 = 10 * 12 - a
        a = t2 & 511
    for p in range(12):
        for g in range(9):
            a = p * a % 65521
            t3 = 9 ^ 18
            t4 = t3 * (n // 3)
            t5 = t4 ^ p | tot
            tot = t5 % 97
        t6 = a + tot + tot
        a = (t6 + (tot + a) // 4) % 97
        t7 = (p ^ 2) - (a & 14)
        t8 = (tot >> 3 >> 3) * t7
        tot = t8 & 262143
    t9 = tot * tot - 11 + a
    return rec(n - 1, t9 % 97)

def fn0(d, c):
    t0 = (d - 7 | 2) % 17
    c = rec(20, t0)
    t1 = c & 8 & (d ^ 12) & c
    d = rec(55, t1)
    for hi in range(6):
        c = 7 & c
        t2 = d * hi - (c | d)
        d = t2 & 1023
        t3 = (hi + c) * 3
        c = (t3 + hi) % 97
    p = c * 1 * d & 255
    cnt = c ^ 7
    return (p | c) & 262143

def fn1(b, a, g):
    t0 = b * g | b % 97
    u = t0 * b % 97
    c = g ^ 11
    if b * u == 13:
        for s in range(12):
            t1 = (c ^ a | c) * b
            a = t1 & 1023
            t2 = c // 2 * 6
            b = (t2 ^ s) & 65535
        t3 = u * c + b
        c = rec(107, t3 % 17)
    else:
        if 16 - g > 50:
            t4 = (c * a + b) % 17
            t5 = (b - u) % 17
            g = fn0(t4, t5)
            t6 = (11 << 1) + 8 | a
            t7 = c * a & 4095
            c = fn0(t6 % 97, t7)
        for cur in range(3):
            t8 = (1 - u) * c
            t9 = (a | b) ^ cur
            b = (t8 - t9) % 97
            u = cur - 11 + u & 4095
            t10 = u + b ^ c
            c = t10 % 17
    t11 = a | 2
    t12 = t11 * (g // 5)
    t13 = (u ^ a) % 17
    a = fn0(t12 & 1023, t13)
    aux = (c | b) + g
    c = ((b | 18) << 3) % 17
    for tmp in range(4):
        t14 = tmp << 4 ^ u
        u = t14 % 97
        t15 = 17 * b - c >> 2
        b = t15 & 131071
    for res in range(4):
        c = ((g ^ 12) * g ^ res) % 97
        if res - aux != 1:
            t16 = b - 11
            t17 = t16 - (aux ^ b)
            aux = t17 + a & 511
            b = (res - 8 ^ b ^ g) & 8191
    t18 = b * b // 2 * b
    return (t18 ^ aux) & 2047

def f(x):
    nxt = [40, 71, 12, 39, 16, 32, 44, 73]
    nxt[x % 8] = nxt[x % 8] // 6
    p = 15 * x + 2 << 1
    for cur in range(11):
        j = 0
        while j < 36:
            x = (14 | p | x) % 9973
            nxt[j % 8] = (17 | p) % 97
            j = j + 1
    a = x >> 1
    t0 = nxt[p % 8]
    t1 = a - t0 >> 1
    nxt[a % 8] = t1 % 97
    t2 = nxt[a % 8]
    e = (t2 ^ a) % 1009
    val = x % 1009
    buf = e - x
    t3 = (nxt[a % 8] << 4) - 8
    idx = t3 - a
    aux = e + e & (p & idx)
    lo = 0
    while lo < 12:
        for z in range(3):
            x = (buf >> 2 ^ x) % 1009
            p = 19 * p & 1023
        lo = lo + 1
    return ((buf | aux) ^ 16) % 1009

if __name__ == "__main__":
    arg = 8
    expected = 956
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
