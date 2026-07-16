# Auto-extracted from ds_lt256k_500.jsonl
# record_id=153  entry=f  input='8'  output='3879'  tokens=190679

def f(x):
    w = [43, 15, 240, 122, 130, 188, 244]
    p = 13 & x
    nxt = 0
    while nxt < 10:
        z = 0
        while z < 2:
            t0 = w[p % 7]
            t1 = t0 & p
            t2 = w[z % 7]
            t3 = t1 + (z ^ nxt)
            t4 = nxt - p ^ t2
            x = (t3 ^ t4) & 262143
            t5 = w[x % 7]
            t6 = ((z | 11) & t5) - nxt
            x = t6 & 1023
            w[z % 7] = 6 ^ nxt ^ p
            z = z + 1
        t7 = w[x % 7] // 7 + p
        p = t7 & 2047
        nxt = nxt + 1
    for q in range(10):
        for lo in range(9):
            x = 16 * p + lo & 4095
            t8 = w[x % 7]
            t9 = lo + q + t8
            x = t9 & 16 * lo - x
            t10 = 4 * 13 ^ p
            p = t10 % 65521
        t11 = q * q - x
        x = t11 & 511
    x = x * x % 251
    x = 8 + p | p
    for idx in range(7):
        t12 = w[idx % 7]
        t13 = idx | t12
        t14 = t13 ^ p * idx
        p = t14 & 4095
        for b in range(11):
            w[p % 7] = (idx << 2 | idx | p) % 251
            t15 = w[b % 7]
            t16 = b + t15 ^ x
            p = (t16 ^ p) & 255
        p = (2 + p ^ p) & 4095
    t17 = p - x + p + 19
    return t17 & 4095

if __name__ == "__main__":
    arg = 8
    expected = 3879
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
