# Auto-extracted from ds_lt256k_500.jsonl
# record_id=38  entry=f  input='18'  output='2731'  tokens=107787

def f(x):
    e = 0
    while e < 418:
        t0 = e + e - (19 & x)
        x = (t0 + (x + 4) * x) % 65521
        x = 17 & x
        e = e + 1
    for tmp in range(12):
        x = (19 + 1 & tmp) - x & 32767
        if tmp | x == 47:
            t1 = tmp - 7 - x
            x = t1 % 97
        else:
            t2 = 17 - tmp ^ tmp - x
            t3 = t2 * (tmp * tmp - (tmp | 18))
            x = t3 & 131071
    aux = 0
    while aux < 12:
        t4 = aux - x & x
        x = t4 & x
        x = (x >> 1) % 251
        t5 = 13 * aux << 1
        t6 = (aux ^ x) & 12
        x = t5 & t6
        aux = aux + 1
    hi = x * x & x - 8
    for lo in range(4):
        if x * hi < 2:
            x = (x | lo) % 251
        z = 0
        while z < 12:
            t7 = (4 | 8 * lo) // 8 ^ x
            x = t7 % 65521
            z = z + 1
        t8 = 13 - x
        t9 = t8 - (lo ^ hi)
        hi = t9 & 131071
    for s in range(7):
        t10 = s + x + s
        x = t10 * s % 97
        hi = (s * hi * 14 ^ x) & 65535
        hi = ((hi | 13) >> 1) % 65521
    t11 = hi ^ x ^ 19
    prv = t11 - hi
    return (x * x + prv) % 9973

if __name__ == "__main__":
    arg = 18
    expected = 2731
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
