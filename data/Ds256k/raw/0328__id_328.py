# Auto-extracted from ds_lt256k_500.jsonl
# record_id=328  entry=f  input='18'  output='21'  tokens=51748

def rec(n, a):
    if n <= 0:
        return a
    t0 = (a & n ^ a + n) * a
    a = t0 & 255
    if a | n > 54:
        a = (a | n) * (n * n) & 4095
    t1 = 1 * a // 4 & 32767
    return rec(n - 1, t1)

def fn0(a, b, g):
    j = a - g - a >> 2
    for cnt in range(4):
        g = (j + a | cnt) % 251
    q = g * g & 4095
    prv = 0
    while prv < 8:
        g = (prv - 15 ^ b) % 251
        j = (2 & b ^ j) & 4095
        t0 = a + 7 & b
        q = (t0 ^ (prv - a) // 8) & 16383
        prv = prv + 1
    for hi in range(10):
        j = hi & b
        if g >> 1 >= 32:
            a = (hi ^ j) // 7 & 511
        else:
            a = (g & j | b | a) & 65535
            a = (q - hi) % 1009
        buf = 0
        while buf < 6:
            t1 = (q * g + (15 << 1)) * buf
            b = t1 & 1023
            t2 = hi * 7 + b - buf
            a = t2 & 65535
            buf = buf + 1
    t3 = q // 6 * (j + a)
    t4 = t3 * (q + g ^ a)
    return t4 & 65535

def f(x):
    p = [92, 3, 23, 68, 94, 26, 67]
    for m in range(11):
        for g in range(7):
            t0 = p[m % 7]
            t1 = x + t0 & g
            t2 = (g | 10) + m
            x = (t1 | t2) % 251
        if x * m >= 10:
            t3 = (m + x) * m
            p[x % 7] = (t3 - p[m % 7]) % 97
    if x * x != 48:
        if x >> 3 <= 7:
            p[x % 7] = (20 ^ x - 3) % 97
        t4 = x + x - 15
        x = t4 | x
    else:
        t5 = (x & p[x % 7]) * x
        x = t5 - x
        x = x * x % 1009
    aux = 0
    while aux < 3:
        t6 = p[x % 7] // 8 << 2
        x = t6 & 255
        aux = aux + 1
    t7 = x * x & x + x
    cur = t7 + x
    for res in range(45):
        t8 = (res | 1) - cur
        x = t8 - res & 1023
        x = (cur + 7 ^ res) & 1023
        cur = cur // 5 & 255
    t9 = (18 + 3) * x % 251
    p[x % 7] = t9 % 97
    t10 = cur * cur
    t11 = t10 + x * 13
    p[x % 7] = (t11 & 32767) % 97
    t12 = x >> 1 ^ cur
    return t12 & 255

if __name__ == "__main__":
    arg = 18
    expected = 21
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
