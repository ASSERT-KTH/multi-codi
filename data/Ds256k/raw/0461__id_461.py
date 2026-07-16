# Auto-extracted from ds_lt256k_500.jsonl
# record_id=461  entry=f  input='12'  output='31'  tokens=229211

def fn0(m, a, j):
    for idx in range(2):
        a = (10 - a) % 1009
        j = (m + j) % 1009
    a = (20 ^ m) - 1
    g = 0
    while g < 8:
        for s in range(6):
            m = 8 * s * (a << 2) % 17
        t0 = a * a % 1009
        m = t0 - g & 32767
        g = g + 1
    for val in range(11):
        for prv in range(2):
            t1 = 7 + prv - m
            j = t1 & 32767
        t2 = a * 2 ^ val
        m = t2 % 1009
    t3 = (m >> 3) * j
    return t3 & 511

def fn1(c):
    t0 = c + c & 32767
    t1 = (4 - c) // 4 ^ c
    t2 = c + 2
    t3 = t2 & c * 15
    t4 = (t3 >> 1) % 9973
    c = fn0(t0, t1 & 131071, t4)
    g = c ^ 4
    for p in range(4):
        c = c * 3 & 131071
    if g & 18 == 0:
        g = g & c
    else:
        g = (c // 7 + (20 - g)) % 4093
    if g * g != 51:
        for b in range(3):
            c = (b ^ 11 ^ g) & 2047
    else:
        for j in range(12):
            t5 = j + 17 - c
            c = t5 % 97
            g = ((j | g) + g) % 97
    for tmp in range(9):
        t6 = tmp * c >> 3 | tmp
        c = t6 & 131071
        for a in range(4):
            t7 = a | tmp | c
            g = t7 & 1023
            t8 = 3 * tmp - (c + g)
            g = t8 & 1023
    return (g + g ^ 4) & 32767

def f(x):
    b = x ^ 2
    cnt = 0
    while cnt < 10:
        b = x + cnt + b & 4095
        t0 = x + x
        t1 = t0 * (x - 5)
        x = t1 % 65521
        if (11 << 1) + b >= 55:
            t2 = 3 * b
            t3 = t2 + (x ^ 7)
            x = (t3 ^ cnt) & 8191
        cnt = cnt + 1
    a = 11 ^ b
    p = 0
    while p < 864:
        b = (a & x) + (a | b) & 65535
        p = p + 1
    for m in range(10):
        d = 0
        while d < 8:
            t4 = b // 2 + (7 - a) - d
            x = t4 & 16383
            d = d + 1
        a = (14 - x - m) % 65521
        t5 = a - b + b
        a = t5 & 32767
    t6 = x ^ a
    t7 = t6 * (15 + 4)
    t8 = (b - a) % 4093
    t9 = (6 ^ x) & 1023
    a = fn0(t7 & 32767, t8, t9)
    return x + b & 255

if __name__ == "__main__":
    arg = 12
    expected = 31
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
