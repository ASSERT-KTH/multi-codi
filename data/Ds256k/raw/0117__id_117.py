# Auto-extracted from ds_lt256k_500.jsonl
# record_id=117  entry=f  input='8'  output='5'  tokens=67009

def fn0(j):
    w = [229, 183, 13, 143, 47, 17, 9]
    lo = j << 1 & j
    z = 0
    while z < 10:
        j = (j + z) % 1009
        t0 = w[z % 7]
        t1 = (t0 ^ j) * 16
        lo = t1 & 16383
        z = z + 1
    t2 = j + lo
    t3 = t2 ^ j // 5
    a = t3 ^ 16
    t4 = a ^ j | j - 4
    v = t4 // 3 % 1009
    t5 = a * w[j % 7]
    return t5 >> 2 & 1023

def f(x):
    b = x * x
    if x - 14 != 15:
        for tot in range(2):
            t0 = tot * x
            t1 = t0 - (x + tot)
            b = t1 % 17
        x = b ^ 2
    z = ((3 | b) & 18) - x
    lo = (b & x) - b
    if lo - x <= 61:
        z = b - z
    for hi in range(91):
        t2 = b * 14 ^ hi
        lo = t2 & 4095
        t3 = lo // 7 ^ z
        z = t3 & 255
        if x * 17 != 11:
            x = z * x & hi
            t4 = 9 << 2 | (z | 13)
            z = (t4 + lo) % 17
        else:
            z = (z * x + 15 ^ x) & 16383
            b = (hi - x) // 6 % 17
    b = fn0((b - 19 - z) % 1009)
    u = x & z
    return (z * z + lo | 6) % 17

if __name__ == "__main__":
    arg = 8
    expected = 5
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
