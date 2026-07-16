# Auto-extracted from ds_lt256k_500.jsonl
# record_id=346  entry=f  input='15'  output='6'  tokens=59342

def fn0(g):
    for tot in range(9):
        t0 = g + 17
        t1 = t0 * (g - tot)
        g = t1 & 8191
    acc = g % 4093
    for j in range(8):
        g = ((g & j) - g) % 9973
        t2 = j - g + 16 * g
        g = (t2 | g) & 4095
        t3 = (13 - g + j) * j
        acc = t3 & 1023
    buf = acc // 4 ^ g
    b = 17 * 20 >> 1 ^ buf
    t4 = 1 | buf - acc
    return t4 & 131071

def f(x):
    g = x + x
    x = fn0((x - 13 | x) % 97)
    if g >= 27:
        g = g + x
        x = g - x & g >> 1
    t0 = (g + x >> 4) // 4
    g = fn0(t0 & 1023)
    t1 = x - 17 + g
    g = fn0(t1 & 1023)
    for v in range(2):
        nxt = 0
        while nxt < 8:
            t2 = (v & 14) + (nxt - x)
            t3 = (6 & 15) + nxt - t2
            x = t3 % 97
            t4 = (nxt - 18) * v
            t5 = (v - 17) * g
            g = t4 * t5 % 1009
            x = (x | nxt) % 97
            nxt = nxt + 1
    if x & 19 != 10:
        if g >> 1 > 51:
            g = g ^ x
        else:
            x = 18 ^ g
    if g - 3 != 52:
        t6 = (g + g) * 10
        g = t6 % 1009
    g = fn0((g | x) & 65535)
    x = fn0(x // 6 & 255)
    aux = (x >> 1) // 2
    z = 0
    while z < 47:
        aux = x - 6 - z & 511
        t7 = x + aux << 4
        g = (t7 | z) & 255
        z = z + 1
    buf = (aux ^ 2) // 5
    t8 = aux - 16 ^ 12
    return t8 % 97

if __name__ == "__main__":
    arg = 15
    expected = 6
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
