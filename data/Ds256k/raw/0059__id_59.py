# Auto-extracted from ds_lt256k_500.jsonl
# record_id=59  entry=f  input='13'  output='229'  tokens=165061

def fn0(j, a):
    cur = 0
    while cur < 11:
        t0 = j * cur // 3
        a = t0 % 4093
        t1 = j + 18 + cur
        a = t1 % 17
        cur = cur + 1
    res = 15 * a
    if j >> 2 != 23:
        t2 = 7 - j
        t3 = (15 & j) - 15
        t4 = t2 - (a + 1)
        j = t3 & t4
        for g in range(6):
            t5 = a % 4093 + g
            j = t5 & 8191
    else:
        t6 = j * a ^ 4 - j
        j = (t6 - j) % 4093
    if 1 ^ j > 8:
        j = a - 18 >> 4
        t7 = j - res
        t8 = t7 + j // 4
        j = t8 - res & 262143
    else:
        p = 0
        while p < 12:
            t9 = ((res >> 3) - p) * res
            res = t9 & 2047
            p = p + 1
    t10 = j * 14
    t11 = res | 12
    t12 = t10 | j ^ 5
    t13 = t11 * (16 | j)
    hi = t12 + t13 & 255
    t = hi | a
    return ((t & j) >> 1) * j % 251

def f(x):
    cur = [14, 186, 24, 211, 62, 119, 141]
    t0 = (x - 15 ^ x) % 1009
    t1 = cur[x % 7]
    t2 = x * x * t1 % 9973
    x = fn0(t0, t2)
    t3 = (x * x | x) >> 3
    val = t3 % 9973
    lo = x * val * 19 & x
    t4 = cur[val % 7]
    t5 = lo // 7
    v = t5 - (val - t4)
    for nxt in range(2):
        z = 0
        while z < 7:
            t6 = cur[v % 7] + 20
            val = (t6 >> 2 ^ val) % 9973
            z = z + 1
        for buf in range(229):
            t7 = (x - 1 ^ buf) - 2
            lo = t7 & 262143
    a = x & cur[lo % 7]
    m = 5 + a
    return (a + lo) % 9973

if __name__ == "__main__":
    arg = 13
    expected = 229
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
