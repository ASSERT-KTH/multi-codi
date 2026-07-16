# Auto-extracted from ds_lt256k_500.jsonl
# record_id=102  entry=f  input='13'  output='95'  tokens=33399

def fn0(c):
    res = 8 << 4 & c % 9973
    if 7 - res <= 14:
        t0 = res * res
        t1 = t0 ^ 1 + c
        t2 = (res + c) // 8
        res = t1 ^ t2
        v = 0
        while v < 6:
            c = (13 - v | res) & 131071
            t3 = (c & v) - v
            c = t3 & 511
            v = v + 1
    else:
        c = c // 7
    t4 = res + res - c
    idx = t4 | c
    idx = (idx * 6 & c) // 8
    t5 = 16 + c ^ 18 * c
    c = (t5 + idx) % 251
    t6 = idx & res ^ (15 | c)
    return t6 // 4 % 251

def f(x):
    for u in range(8):
        for b in range(16):
            x = (b - u ^ x) % 97
            t0 = b * b - u
            t1 = u ^ b | x
            x = t0 & t1
        if u - 5 - x > 43:
            t2 = 19 + x >> 4
            x = t2 % 97
        else:
            x = (u - 15 ^ x) % 4093
            t3 = ((x << 3) + x) // 2
            x = t3 % 97
    val = (17 & x) - x % 97
    prv = val | 20
    v = prv ^ 14
    t = x + x - prv | prv
    m = (prv & 14) * x
    t4 = 9 * m // 8
    tmp = t4 * v & 2047
    tmp = 6 * prv
    t5 = (1 - x) // 6 | val
    return t5 % 97

if __name__ == "__main__":
    arg = 13
    expected = 95
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
