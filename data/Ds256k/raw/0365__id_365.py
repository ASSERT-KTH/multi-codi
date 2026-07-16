# Auto-extracted from ds_lt256k_500.jsonl
# record_id=365  entry=f  input='16'  output='1'  tokens=86540

def fn0(b, g):
    for lo in range(9):
        b = lo * b % 17
        b = (8 ^ lo) - g + 2 & 4095
    t = 0
    while t < 11:
        t0 = (g | b) // 7 + g
        g = t0 % 17
        t1 = b & 12 | b
        b = t1 & 16383
        for prv in range(7):
            t2 = t - prv - g
            g = t2 % 17
            t3 = (t - prv) * b
            g = t3 // 8 % 17
        t = t + 1
    w = (12 & 10) - g
    c = (w | b) * g * g % 97
    t4 = b // 3 ^ w
    return t4 % 17

def f(x):
    prv = (x ^ 20) * x
    t0 = 3 * prv - prv
    j = t0 + x
    for e in range(16):
        for u in range(12):
            j = ((x - j) // 4 | prv) % 17
            t1 = x + u | 10 * x >> 4
            x = t1 % 17
    a = 16 + prv ^ prv
    t2 = (j - prv) % 17
    t3 = (x ^ prv) & 4
    t4 = t3 ^ j << 4 >> 3
    j = fn0(t2, t4 & 262143)
    for cnt in range(11):
        t5 = (j ^ 3) - prv
        t6 = t5 | prv | x
        x = t6 & 8191
        a = (a ^ 3) + prv & 262143
        if prv + prv != 24:
            t7 = (x ^ a) + prv
            prv = t7 % 97
            prv = (19 - a) % 97 + cnt & 255
    j = prv * j % 17
    t8 = prv - 1 - (12 ^ j)
    return t8 % 17

if __name__ == "__main__":
    arg = 16
    expected = 1
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
