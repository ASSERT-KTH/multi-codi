# Auto-extracted from ds_lt256k_500.jsonl
# record_id=50  entry=f  input='15'  output='2990'  tokens=85036

def fn0(e, d, m):
    nxt = [115, 203, 17, 53, 66, 207, 46]
    t0 = nxt[d % 7] * 18
    m = t0 & e
    t1 = (d + d) * d
    e = t1 << 4 & 131071
    t2 = nxt[m % 7] + d
    m = t2 % 251
    nxt[d % 7] = (e >> 3) % 251
    d = d >> 2
    t = 0
    while t < 10:
        for cur in range(2):
            t3 = e * m
            t4 = t3 + (t - 20)
            nxt[d % 7] = t4 % 251
            t5 = m // 2 - 12
            t6 = nxt[d % 7]
            nxt[d % 7] = (t5 + t6) % 251
        t = t + 1
    t7 = (e & 5) * d
    m = t7 // 2
    t8 = nxt[d % 7] + e
    return (t8 ^ m) // 5 & 8191

def f(x):
    for q in range(944):
        x = q * x & 255
    for a in range(2):
        for d in range(2):
            x = a * x & 255
            t0 = d ^ a ^ x
            x = t0 & 131071
    hi = 0
    while hi < 3:
        t1 = hi + hi ^ hi ^ x
        x = t1 & 8191
        x = (hi ^ 5) & (hi & x)
        hi = hi + 1
    t2 = (x | 17) & 255
    t3 = x | 1
    t4 = t3 ^ (x | 12)
    t5 = (t4 | x) % 251
    t6 = 11 - x + x + x
    x = fn0(t2, t5, t6 & 511)
    t7 = (x ^ 1) - x
    idx = t7 ^ x
    t8 = (x ^ 20) % 97
    t9 = (idx ^ 20) & (idx | 19)
    t10 = (idx + idx ^ x) % 97
    x = fn0(t8, t9, t10)
    j = idx & x | x - idx
    return j - x - idx & 8191

if __name__ == "__main__":
    arg = 15
    expected = 2990
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
