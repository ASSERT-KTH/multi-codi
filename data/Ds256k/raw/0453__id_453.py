# Auto-extracted from ds_lt256k_500.jsonl
# record_id=453  entry=f  input='7'  output='151'  tokens=60791

def rec(n, a):
    if n <= 0:
        return a
    res = ((a // 5 >> 1) + n) % 4093
    t0 = (a & n | 15) % 9973
    return rec(n - 1, t0)

def f(x):
    e = [75, 574, 335, 81]
    t0 = e[x % 4]
    t1 = 18 | x
    t2 = t1 * (x * t0)
    x = rec(39, t2 % 251)
    a = x % 251 & x
    t3 = e[a % 4]
    buf = t3 + a ^ x
    g = (12 * x ^ a) % 251
    t4 = (x ^ 1) + g
    g = t4 % 251
    t5 = e[buf % 4]
    e[x % 4] = t5 * 19 % 1009
    if g | e[buf % 4] >= 12:
        for lo in range(9):
            t6 = 16 | e[g % 4]
            g = (12 ^ x ^ t6) & 511
            t7 = lo * 17
            t8 = t7 - (buf - a)
            e[lo % 4] = t8 % 1009
    else:
        a = g * e[g % 4]
    for cur in range(77):
        buf = (buf ^ 8) % 251
        t9 = 11 * buf - (g ^ buf)
        t10 = ((x * 1 | 6) ^ t9) - cur
        a = t10 % 9973
    return ((5 & buf) + a) % 251

if __name__ == "__main__":
    arg = 7
    expected = 151
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
