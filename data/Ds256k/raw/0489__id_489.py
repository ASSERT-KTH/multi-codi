# Auto-extracted from ds_lt256k_500.jsonl
# record_id=489  entry=f  input='3'  output='56'  tokens=53067

def rec(n, a):
    if n <= 0:
        return a
    a = (14 - n | a) & 16383
    a = (n + a | 6) & 2047
    t0 = n // 5 ^ a
    return rec(n - 1, t0 & 32767)

def fn0(e, a, b):
    j = (b // 2 >> 4) + e
    z = j * 15 % 1009
    for val in range(10):
        t0 = z * e * (j & z)
        a = (t0 * z | a) & 511
        z = (e << 1 & z) * z % 1009
        for res in range(6):
            t1 = b - 19 & j
            t2 = t1 + ((val & 10) - z) ^ res
            e = t2 & 4095
            t3 = (e | 8) * (2 | 4)
            a = (t3 << 4 ^ res) % 1009
            a = res * val * e % 1009
    if a % 65521 >= 41:
        z = (b + 11 ^ j & a) // 5
    else:
        t4 = (14 - e) * b
        t5 = t4 * (a + 14 >> 4) % 1009
        j = rec(36, t5)
    t6 = (j | e) ^ (a | z)
    t7 = (t6 ^ j) & 32767
    a = rec(96, t7)
    b = e + b
    t8 = j + j + (e + 7)
    return t8 & 13

def fn1(j, c):
    aux = [770, 855, 635, 711, 378, 137, 475]
    t0 = aux[j % 7]
    t1 = c - t0 & 8191
    t2 = c * c % 65521
    t3 = 4 * c - 4
    t4 = t3 * c & 2047
    c = fn0(t1, t2, t4)
    for e in range(9):
        j = (j | c) & 262143
        q = 0
        while q < 11:
            aux[c % 7] = ((1 ^ q) + j) % 1009
            t5 = aux[c % 7]
            t6 = q - (t5 - 4)
            aux[q % 7] = (t6 + j) % 1009
            q = q + 1
    t7 = c // 2
    acc = t7 ^ (20 ^ j)
    a = aux[acc % 7] - j
    t8 = aux[acc % 7] - 12
    tot = t8 - acc + 19
    t9 = ((7 ^ a) >> 1) % 65521
    a = rec(80, t9)
    d = (aux[c % 7] | j) % 65521
    t10 = 11 + a ^ 6
    a = t10 ^ d
    return (d * acc ^ 15 & d) % 17

def f(x):
    tot = x * x
    t0 = x ^ tot
    x = t0 + (x | 4)
    t1 = x - 1 + (tot >> 3) & 1023
    tot = rec(112, t1)
    t2 = (tot ^ x) + (tot - 15)
    tot = t2 ^ 19
    x = tot // 8
    t3 = (tot | 15) ^ (tot ^ 1)
    tot = t3 & 32767
    for d in range(10):
        for idx in range(8):
            tot = ((d * x ^ tot) >> 3) % 251
            x = (x ^ d) % 17
            t4 = tot // 7 - (6 - 5)
            x = (t4 ^ tot ^ x) % 17
        x = x + tot >> 1 & 262143
    return (tot * tot - x) % 251

if __name__ == "__main__":
    arg = 3
    expected = 56
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
