# Auto-extracted from ds_lt256k_500.jsonl
# record_id=424  entry=f  input='19'  output='281'  tokens=55465

def rec(n, a):
    if n <= 0:
        return a
    t0 = (a - 17) * n
    aux = t0 & n
    t1 = (12 - a) * (aux | n)
    hi = t1 & 2047
    hi = (n ^ hi) + aux & a
    t2 = (hi // 5 << 3) - hi - a
    return rec(n - 1, t2 & 65535)

def fn0(g):
    for z in range(11):
        g = (g | 9) % 97
        for hi in range(7):
            g = (g - 11) % 1009
            t0 = 10 + 20 - g
            g = t0 // 7 % 97
        if 3 * 16 - g < 37:
            g = (10 - z | g) & 65535
        else:
            g = (g + z) % 97
            t1 = (g & 4) + 8
            g = t1 & 32767
    t2 = (8 ^ 7) + g // 7
    t3 = t2 * g % 97
    g = rec(50, t3)
    t4 = (g + g) % 97
    g = rec(85, t4)
    for nxt in range(9):
        t5 = 12 + nxt
        t6 = t5 + (g | nxt)
        g = t6 % 4093
        t7 = 19 * (g >> 2)
        g = t7 & 1023
        if g - nxt <= 25:
            g = (g ^ nxt) & 8191
            g = nxt + nxt - g & 1023
        else:
            g = (nxt ^ g) % 4093
    for v in range(2):
        g = (g + v) % 97
        if 6 - 20 + g != 35:
            t8 = 6 * v + (v + g)
            g = (t8 | g) & 32767
    lo = g % 1009
    for y in range(2):
        g = lo * y & 2047
    t9 = lo + g | g
    t10 = g + lo + 17
    return (t9 + t10) % 1009

def f(x):
    v = (x ^ 18 | x) & x
    for cur in range(4):
        t0 = 1 - cur - v * v
        x = t0 & 1023
    q = 0
    while q < 9:
        for m in range(18):
            x = (q * v | m) % 17
            x = v * x % 4093
        q = q + 1
    if v ^ 5 >= 26:
        v = (v ^ 7) << 4
        if x | 17 < 35:
            v = fn0(((x & v) - v // 6) % 17)
        else:
            x = rec(57, v & 9)
    t1 = (v - 17) % 4093
    t2 = v // 2 - v
    t3 = (t1 - t2) % 17
    v = rec(56, t3)
    g = 18 + v
    y = 0
    while y < 11:
        t4 = (3 ^ x) // 4
        t5 = t4 & (x ^ g ^ 11)
        v = (t5 | y) % 4093
        t6 = (11 + 15 ^ x) - v
        v = t6 & 8191
        y = y + 1
    b = g * v & v
    hi = (18 | v) * g // 5 % 4093
    return (hi >> 3) % 4093

if __name__ == "__main__":
    arg = 19
    expected = 281
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
