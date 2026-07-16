# Auto-extracted from ds_lt256k_500.jsonl
# record_id=221  entry=f  input='8'  output='12'  tokens=105582

def fn0(c):
    for j in range(12):
        res = 0
        while res < 8:
            t0 = 6 << 4 >> 1
            t1 = t0 & res | c
            c = t1 % 65521
            t2 = 19 * res // 8 << 2 | c
            c = t2 & 16383
            c = c // 4 & 2047
            res = res + 1
    for z in range(5):
        for buf in range(7):
            t3 = (buf | z) - z
            c = (t3 ^ c) % 4093
            c = (z + buf - c) % 9973
            c = c // 5 % 9973
    e = c + c + c
    if e - 20 <= 14:
        u = 0
        while u < 5:
            c = (c // 3 | u) % 65521
            u = u + 1
    else:
        t4 = c - 4 + 18 * c
        t5 = t4 - (e - c | 9)
        e = t5 % 4093
    t6 = (c + 20) * (e >> 3)
    return (t6 - e * c % 9973) % 9973

def fn1(j, g):
    if g - j == 24:
        j = j >> 4
    else:
        buf = 0
        while buf < 5:
            t0 = buf << 3
            t1 = t0 ^ 19 * g
            g = t1 % 65521
            t2 = j >> 2 ^ 16 ^ g
            g = t2 % 4093
            buf = buf + 1
        g = fn0(g // 7 + 16 & 65535)
    j = fn0((j >> 3) % 65521)
    for m in range(10):
        if j * 18 <= 22:
            g = (g - 16 ^ m) & 262143
        else:
            g = (5 * 15 + j + g) % 9973
    for q in range(10):
        g = q - (q + q) - j & 255
        j = (q ^ g) % 4093
    g = fn0((j | 2) & 5)
    return g * j % 4093

def f(x):
    x = fn0((4 ^ x ^ x) & 1023)
    for acc in range(9):
        x = x >> 2 & x
        t0 = x | acc
        t1 = t0 & x >> 4
        x = (t1 >> 3) % 17
    u = (14 | x) - 10
    x = fn0((x + 19) % 9973)
    return (x // 2 | u) % 17

if __name__ == "__main__":
    arg = 8
    expected = 12
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
