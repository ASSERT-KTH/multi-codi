# Auto-extracted from ds_lt256k_500.jsonl
# record_id=241  entry=f  input='17'  output='12'  tokens=198640

def fn0(j):
    aux = j + j + (j + j)
    for idx in range(9):
        j = (j - 10) // 7 & 8191
    for g in range(10):
        tot = 0
        while tot < 4:
            aux = aux // 5 - tot & 32767
            t0 = (4 | 16) + aux + j
            j = t0 & 2047
            tot = tot + 1
        t1 = 3 + j - g
        aux = t1 & 262143
    v = 0
    while v < 3:
        q = 0
        while q < 6:
            t2 = 2 * aux ^ q + v
            j = t2 * 9 & 511
            j = (v - 18 | j) % 9973
            q = q + 1
        j = v * v & (aux & j)
        v = v + 1
    t3 = j + aux
    t4 = t3 * (5 * aux)
    t5 = (aux | 11) + j
    z = (t4 | t5) % 9973
    z = j ^ z
    for s in range(8):
        aux = (12 | s | aux) & 16383
        t6 = (s * 17 + (j | s)) * aux
        z = t6 & 255
        if 2 - z <= 18:
            t7 = (8 * z << 3 >> 1) + s
            aux = t7 & 2047
    for a in range(11):
        for d in range(10):
            t8 = a + d
            t9 = t8 + (z | a)
            z = t9 * j % 97
            j = (19 * aux + j) % 97
            t10 = (j >> 1) - (z ^ d)
            t11 = ((14 & aux) + d) * t10
            aux = t11 & 1023
        t12 = 8 * aux >> 2
        z = (t12 - z) % 97
        if aux - 11 == 32:
            aux = ((a ^ aux) + aux) % 97
    return ((aux - j) * j >> 2) % 97

def fn1(g, c):
    m = [23, 157, 218, 55, 16]
    t0 = m[g % 5]
    m[g % 5] = t0 * 3 >> 3
    t1 = m[g % 5]
    lo = (c ^ 10) & t1
    e = g - m[lo % 5]
    if lo - m[e % 5] < 27:
        for t in range(12):
            e = t * c & 1023
            m[g % 5] = (g | 8) % 251
    acc = e + c & 17 ^ e
    t2 = m[c % 5]
    return (t2 ^ acc) % 17

def f(x):
    j = [22, 15, 44, 92, 19]
    x = fn0((x - 11) % 9973)
    tmp = 0
    while tmp < 37:
        t0 = x + j[x % 5]
        t1 = j[tmp % 5] - 11
        t2 = t0 ^ tmp ^ t1 + 7
        x = t2 & 65535
        t3 = j[x % 5] + tmp
        t4 = t3 + j[tmp % 5]
        t5 = t4 ^ j[tmp % 5]
        x = t5 % 9973
        tmp = tmp + 1
    prv = 4 ^ 20 ^ x
    t6 = j[x % 5]
    a = (17 ^ x) - t6
    if j[a % 5] * x > 22:
        prv = x + x >> 3
        j[prv % 5] = (x + x) % 97
    else:
        for z in range(3):
            t7 = 19 - 12
            j[a % 5] = t7 - (z & prv)
            prv = (20 ^ x) - z & 1023
    t8 = j[prv % 5] + 9
    t9 = prv % 17 + prv * x
    t10 = t9 - (9 * x | t8)
    b = t10 & 511
    t11 = b * a
    t12 = t11 | 17 ^ a
    res = t12 & 511
    t13 = a + x ^ x
    return t13 & 2047

if __name__ == "__main__":
    arg = 17
    expected = 12
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
