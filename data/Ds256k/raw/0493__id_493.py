# Auto-extracted from ds_lt256k_500.jsonl
# record_id=493  entry=f  input='11'  output='130874'  tokens=222462

def rec(n, a):
    if n <= 0:
        return a
    s = ((n | a) - a) * a % 17
    t0 = s + n
    t1 = t0 ^ s & n
    s = t1 & 131071
    if a // 8 < 45:
        t2 = a * a + (9 - a) ^ s
        a = t2 & 8191
        if s + a != 15:
            t3 = n // 7
            t4 = t3 - (a + n)
            a = (t4 >> 4) % 65521
    t5 = ((a ^ s) >> 4) % 17
    return rec(n - 1, t5)

def fn0(b):
    if 17 * b > 14:
        if b >> 3 <= 42:
            t0 = (b ^ 15) >> 1
            b = rec(94, t0 % 1009)
        for q in range(5):
            t1 = (q << 1 << 1) + b
            b = t1 & 32767
            t2 = q - b ^ b * q
            b = t2 % 251
    aux = ((b | 8) << 2) + b
    tot = 0
    while tot < 5:
        if tot - aux < 48:
            b = (tot ^ b) & 255
        else:
            t3 = b - 6 ^ aux
            aux = (t3 ^ 5) % 17
        if (tot ^ 11) + aux == 47:
            b = (tot ^ b) % 251
        s = 0
        while s < 8:
            aux = ((b << 2 >> 1) - s) % 1009
            t4 = tot * 18 // 5 - aux ^ s
            b = t4 & 2047
            s = s + 1
        tot = tot + 1
    t5 = (b ^ 11) * 16
    t6 = (t5 >> 3) % 1009
    b = rec(56, t6)
    for w in range(7):
        b = (aux * w + aux) % 251
        for g in range(4):
            t7 = w + 1 | b
            t8 = t7 + (w - aux - b)
            aux = t8 % 17
            t9 = g + 19 | b
            b = t9 & 131071
        m = 0
        while m < 5:
            b = (m - 19 ^ aux) & 511
            aux = b * aux & 255
            m = m + 1
    t10 = 16 * 7 & b
    aux = rec(79, t10)
    y = (18 ^ aux) >> 2
    t11 = aux * aux // 2
    return t11 & 65535

def fn1(a, b, m):
    t0 = a * b // 2 >> 1
    a = rec(75, t0 % 65521)
    hi = 15 ^ a
    t1 = (b & hi) * b
    prv = (t1 - a) % 65521
    t2 = (17 + a | 16) % 9973
    b = rec(21, t2)
    g = prv >> 3
    aux = 0
    while aux < 7:
        for v in range(12):
            t3 = (aux | 4) + m | g
            g = t3 & 32767
            t4 = (hi ^ aux) >> 1
            t5 = t4 + ((m ^ 16) << 3)
            a = (t5 - a) % 65521
        aux = aux + 1
    t6 = (b & a) // 3
    return (t6 | hi * 16 << 3) & 2047

def f(x):
    acc = x ^ 4
    if acc - 2 != 23:
        if x | 1 != 28:
            t0 = acc * 8 ^ acc - x
            t1 = (t0 ^ x) % 97
            t2 = (x ^ acc) % 17
            t3 = acc * 8 - (acc - 5) & 511
            acc = fn1(t1, t2, t3)
        for c in range(12):
            acc = (acc - 17) % 17
            t4 = 10 - acc | c
            x = t4 % 17
    nxt = (x | 13) - x * x
    tot = nxt | acc
    e = tot & nxt
    cnt = (tot + 1) * x % 97
    for idx in range(11):
        for aux in range(11):
            t5 = (aux ^ idx) << 3 << 1
            tot = (t5 + tot) % 17
            cnt = (e >> 2 ^ aux) & 511
            cnt = (tot << 3 << 2 ^ aux) & 32767
    lo = nxt + 18
    t6 = tot + 14 - acc
    a = t6 ^ lo
    res = 0
    while res < 12:
        t7 = 8 | x
        t8 = t7 ^ cnt * cnt
        acc = (t8 - res) % 97
        t9 = (a >> 2) - lo
        lo = t9 % 97
        res = res + 1
    for cur in range(33):
        t10 = acc ^ lo ^ cur
        cnt = t10 & 131071
        lo = (acc | x | cur) % 17
        x = (x - 14) % 97
    m = 4 + 9 ^ a | x
    t11 = tot % 97 & e
    t = t11 ^ 19 * nxt - tot
    return (x ^ e) & 131071

if __name__ == "__main__":
    arg = 11
    expected = 130874
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
