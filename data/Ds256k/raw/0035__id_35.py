# Auto-extracted from ds_lt256k_500.jsonl
# record_id=35  entry=f  input='9'  output='20'  tokens=159688

def f(x):
    a = [93, 42, 35, 82, 75, 96]
    t = x + 1
    z = t - x << 4
    t0 = (t | z) - z
    acc = t0 * 16
    if acc << 1 != 41:
        t1 = t ^ 7 ^ (17 ^ acc)
        t = t1 // 4
    tot = 8 + x
    t2 = z * acc * z - 1
    q = t2 & 32767
    if 5 - tot < 13:
        t3 = (x ^ z) - (2 & tot)
        q = t3 * x
    else:
        for d in range(7):
            x = (x + 20) % 251
            t4 = (17 ^ tot) - 20 | x
            acc = t4 + d & 32767
            tot = (z - tot ^ tot) % 251
    if 15 ^ q >= 21:
        a[q % 6] = (x - acc) % 97
        for res in range(2):
            a[res % 6] = (q + q) % 97
            acc = acc // 5 % 4093
            a[acc % 6] = 13 + res & t
    else:
        t = a[z % 6]
    prv = t & q
    p = z * t % 251
    t5 = (q >> 4) - a[x % 6]
    s = t5 ^ q
    for u in range(11):
        for aux in range(34):
            t6 = (z ^ p) + (s + 14)
            a[u % 6] = t6 % 4093 % 97
        t7 = q % 251 + x - u
        acc = t7 % 17
        t8 = a[z % 6] * s
        s = (t8 ^ 7 << 2) & 4095
    return 3 + tot & 32767

if __name__ == "__main__":
    arg = 9
    expected = 20
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
