# Auto-extracted from ds_lt256k_500.jsonl
# record_id=175  entry=f  input='20'  output='24'  tokens=46485

def fn0(g):
    prv = g - 10
    for hi in range(9):
        if prv ^ 6 <= 54:
            t0 = prv * 20 ^ hi
            t1 = g % 97 + g
            g = t0 & t1
        g = prv // 6 + hi & 262143
    t2 = g * prv ^ g
    t3 = t2 * (prv >> 1 << 3)
    q = t3 % 251
    d = 0
    while d < 12:
        t4 = q - 5 >> 4
        q = t4 % 97
        d = d + 1
    t5 = (q ^ g) + (q + prv)
    return t5 >> 2 & 8191

def f(x):
    buf = x + x - (12 - x)
    t0 = (buf + 9) * (x | 4)
    hi = t0 + 2 * 16
    aux = (buf ^ 16) + x
    hi = fn0((10 + x - (8 ^ hi)) % 4093)
    j = 0
    while j < 219:
        hi = (aux - 3 + hi) % 97
        j = j + 1
    t1 = buf - aux
    t2 = t1 ^ 11 * x
    aux = fn0(t2 % 1009)
    for y in range(9):
        buf = (y + hi) % 4093
        t3 = x ^ hi
        t4 = t3 + (buf + hi)
        t5 = t4 // 8 - aux
        aux = t5 & 8191
        hi = x * hi % 97
    for z in range(2):
        t6 = 5 * aux
        hi = t6 & z + 12
        t7 = (z ^ 9) * hi
        aux = t7 & 511
        t8 = (x ^ buf) + z
        t9 = t8 * (aux - buf | buf)
        aux = t9 % 9973
    d = aux * 2
    t10 = x - 9 + hi
    return (t10 ^ 12) % 9973

if __name__ == "__main__":
    arg = 20
    expected = 24
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
