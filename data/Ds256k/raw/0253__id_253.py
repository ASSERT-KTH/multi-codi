# Auto-extracted from ds_lt256k_500.jsonl
# record_id=253  entry=f  input='7'  output='201'  tokens=185049

def f(x):
    t0 = x * x
    t1 = t0 * (x + x)
    y = t1 + x
    s = x * x + (x - 18) ^ x
    if y >> 3 != 52:
        for val in range(7):
            t2 = (x | 13) + (x | s)
            x = t2 & 32767
        t3 = x - s
        t4 = t3 | s >> 4
        y = t4 + y
    t5 = (x & 2) * 7
    j = t5 + x
    t6 = 9 + s
    t7 = t6 & (10 | x)
    w = t7 - y
    t8 = 1 << 2 ^ x
    t9 = 16 + j & j
    t = t8 & t9
    prv = (w & s) << 3
    for tot in range(18):
        a = 0
        while a < 7:
            t10 = (prv & w) + prv
            t11 = t10 + tot ^ s
            s = t11 & 32767
            t12 = y * a ^ w
            prv = t12 % 65521
            w = (w ^ x) % 65521
            a = a + 1
        t13 = s // 8
        t14 = t13 - w * y
        s = t14 % 251
    return (s + prv) * (14 * s) % 251

if __name__ == "__main__":
    arg = 7
    expected = 201
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
