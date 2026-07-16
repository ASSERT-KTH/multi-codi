# Auto-extracted from ds_lt256k_500.jsonl
# record_id=239  entry=f  input='4'  output='20'  tokens=141085

def fn0(c, b, g):
    for res in range(12):
        b = (b ^ g) % 1009
        for u in range(12):
            g = b * u & 1023
            t0 = b + g + 18 >> 1 ^ u
            c = t0 & 511
            t1 = 16 ^ b | g >> 3
            b = (res + res + b - t1) % 4093
    q = 0
    while q < 5:
        for aux in range(3):
            t2 = (q | b) // 3
            b = t2 * 7 % 1009
            g = (aux | b) % 65521
        if q ^ 16 ^ c < 51:
            b = (c << 1) - b & 4095
        c = (6 + 4 - b | q) % 1009
        q = q + 1
    t3 = c * b + 7
    m = t3 & ((g | 16) & c)
    val = (c - g ^ g) * b & 255
    if g ^ c == 13:
        val = (1 + g) * 11 - 11
    else:
        t4 = val + c + val << 2
        val = t4 & 65535
    m = ((b | val) + b) % 4093
    return ((b - 6) * 17 - val) % 1009

def f(x):
    q = x * x - 1
    a = q // 5 - (q | 5)
    p = x * q - x
    g = p >> 2 ^ a // 7
    if g ^ x >= 40:
        p = (x << 2) * x ^ g
        a = g - 15
    else:
        for v in range(10):
            q = v - 15 + q & 2047
        for t in range(9):
            t0 = (x - g & x * x) + t
            q = t0 % 251
    t1 = x + q & 1023
    t2 = (q | x) * x
    t3 = 2 * g % 251
    x = fn0(t1, t2 & 4, t3)
    for acc in range(16):
        for b in range(8):
            t4 = 9 - p | q
            q = t4 & 255
            t5 = 4 + p
            t6 = t5 + (q - 5)
            a = (t6 ^ b) & 255
    return (3 ^ a) & 1023

if __name__ == "__main__":
    arg = 4
    expected = 20
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
