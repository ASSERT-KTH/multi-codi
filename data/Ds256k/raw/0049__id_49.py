# Auto-extracted from ds_lt256k_500.jsonl
# record_id=49  entry=f  input='2'  output='9'  tokens=187974

def fn0(d, e, b):
    if e << 1 != 5:
        for tot in range(12):
            t0 = (11 | tot) ^ tot
            e = (t0 | b) & 2047
            t1 = 16 & 14 | b
            e = (t1 + e) % 65521
            d = d - tot & 262143
        d = e + e
    j = b + e >> 2
    hi = b // 5 - 17
    acc = 0
    while acc < 12:
        for idx in range(5):
            t2 = (acc - 6) * (9 | 11) - j
            e = (t2 ^ e) & 2047
        t3 = hi >> 2
        t4 = t3 * (acc ^ hi)
        e = t4 % 65521
        acc = acc + 1
    j = hi * 20 % 9973
    return e * 17 * (b - hi) & 255

def f(x):
    e = [14, 110, 206, 104, 142, 6, 247, 6]
    if e[x % 8] ^ 15 == 46:
        for d in range(2):
            e[d % 8] = x % 17 & x
    t0 = x - 5
    t1 = t0 + (x + x)
    j = t1 - x
    for u in range(5):
        for nxt in range(75):
            e[x % 8] = (5 | 1 + j) // 3
            x = ((5 ^ u) - j - x) % 4093
            t2 = e[u % 8] - u | x
            e[x % 8] = t2 % 251
        x = ((j ^ u) - u) % 17
    acc = 0
    while acc < 7:
        for y in range(5):
            t3 = e[y % 8] - x
            t4 = (acc - y) * (x | 15)
            t5 = (t3 - 8) * t4 & 32767
            e[y % 8] = t5 % 251
            t6 = j & e[x % 8]
            e[j % 8] = t6 * (y + j) % 251
            t7 = x + acc - (12 - j) + 8
            x = t7 % 17
        j = (x + j) % 17
        j = 7 * x * (j // 4) % 4093
        acc = acc + 1
    g = 0
    while g < 3:
        x = (x << 1) % 97
        if j - 18 > 42:
            t8 = 10 * x - (x ^ 17)
            e[j % 8] = (t8 >> 1) % 251
            t9 = (7 - e[g % 8]) // 5
            e[j % 8] = (t9 >> 2 | j) % 251
        x = x & j
        g = g + 1
    for m in range(12):
        x = (j - x) % 17
    if j & x <= 7:
        j = (j << 3) % 97 // 2
    else:
        for s in range(10):
            x = (11 ^ 6) - j - x & 32767
            t10 = 17 * e[x % 8]
            e[x % 8] = (t10 << 2) % 251
        t11 = x * e[x % 8]
        j = t11 % 4093
    x = x // 6 ^ x & 16
    return (13 - 4 | j) % 4093

if __name__ == "__main__":
    arg = 2
    expected = 9
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
