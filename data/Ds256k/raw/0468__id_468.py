# Auto-extracted from ds_lt256k_500.jsonl
# record_id=468  entry=f  input='4'  output='45'  tokens=210183

def rec(n, a):
    if n <= 0:
        return a
    t0 = (8 << 4 | (a | 1)) + n
    val = t0 % 4093
    hi = ((n & val) + (a + 10)) % 4093
    a = hi - a & 8191
    return rec(n - 1, n & a)

def f(x):
    cur = [785, 520, 155, 1001, 120, 376, 269, 581]
    t0 = cur[x % 8]
    nxt = t0 >> 3
    t1 = cur[x % 8]
    t2 = cur[nxt % 8]
    t3 = nxt ^ t1
    t4 = t3 * (t2 * x)
    tot = t4 & 262143
    t5 = nxt - x & 1
    tot = rec(114, t5)
    lo = 0
    while lo < 258:
        if x - lo <= 15:
            t6 = cur[tot % 8]
            t7 = nxt >> 2
            t8 = 7 ^ x ^ t6
            t9 = t7 * (x ^ lo)
            x = t8 * t9 % 9973
        else:
            cur[x % 8] = (tot + lo) // 4 % 1009
        t10 = (10 | 15) * x
        x = t10 % 9973
        lo = lo + 1
    e = (tot | nxt) + tot
    t11 = ((tot ^ x) >> 4) * 16
    return t11 % 97

if __name__ == "__main__":
    arg = 4
    expected = 45
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
