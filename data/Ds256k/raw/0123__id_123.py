# Auto-extracted from ds_lt256k_500.jsonl
# record_id=123  entry=f  input='8'  output='33'  tokens=229342

def fn0(e):
    prv = [60, 82, 79, 78, 0]
    v = 0
    while v < 9:
        for u in range(11):
            t0 = prv[u % 5]
            t1 = t0 // 3 | e
            prv[e % 5] = t1 % 97
            e = (v - u << 4 ^ e) % 4093
            t2 = 12 * prv[v % 5] << 3
            t3 = (t2 ^ e // 7 * v) % 4093
            prv[e % 5] = t3 % 97
        e = (e >> 3) % 9973
        v = v + 1
    t4 = (e - 5) * e
    t5 = prv[e % 5]
    lo = (t4 - t5) % 65521
    idx = 0
    while idx < 12:
        for m in range(5):
            prv[m % 5] = (prv[lo % 5] - lo) % 97
            t6 = (idx << 3) - idx
            prv[m % 5] = (t6 + e) % 97
            prv[lo % 5] = (m + 16 - idx + lo) % 97
        e = e - lo & 511
        idx = idx + 1
    tot = lo + lo - lo
    t7 = prv[e % 5]
    t8 = lo * t7
    t9 = t8 - (2 & lo)
    z = t9 % 9973
    z = tot - z
    t10 = z * z ^ 19
    e = t10 * 5 & 16383
    tot = z // 7 * (tot >> 3) & 16383
    t11 = e - prv[tot % 5]
    return ((z & e) + t11) // 4 % 4093

def f(x):
    a = x - 5 - x * x
    t0 = 18 + x | x
    a = t0 - x
    for hi in range(403):
        x = (x ^ a) // 3 & 8191
        a = hi * a % 251
        q = 0
        while q < 3:
            x = (5 * 12 ^ x) & 4095
            q = q + 1
    t1 = x << 2 >> 2
    a = t1 + 6
    return x * x & (a ^ 8)

if __name__ == "__main__":
    arg = 8
    expected = 33
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
