# Auto-extracted from ds_lt256k_500.jsonl
# record_id=79  entry=f  input='4'  output='217'  tokens=183306

def rec(n, a):
    if n <= 0:
        return a
    q = (17 + n - a - n) % 17
    idx = ((20 ^ q) << 1) + n & 32767
    t0 = (idx + q) * 3 | a
    return rec(n - 1, t0 % 251)

def fn0(j, c):
    t0 = (j - 14) * (c // 3)
    lo = t0 % 1009
    t1 = c ^ 11 | c
    cur = t1 + 6
    if j + 3 >= 30:
        if lo - j != 15:
            t2 = c * cur % 9973 + j & 16383
            cur = rec(29, t2)
        lo = cur % 4093
    else:
        for prv in range(2):
            cur = (lo - c | cur) & 16383
        t3 = cur * 9 & 16383
        lo = rec(105, t3)
    val = 2 - 10 ^ j
    t4 = (cur - c) % 9973
    j = rec(107, t4)
    j = val * cur & 511
    for t in range(9):
        t5 = lo ^ j ^ (t ^ j)
        val = t5 % 4093
        if cur * t == 38:
            j = ((14 & c) - j) % 9973
            t6 = cur + 11 + (lo + 4)
            j = (t6 // 4 ^ t) % 9973
        if (10 ^ 18) + c > 36:
            val = (lo << 2 ^ val) % 1009
        else:
            t7 = (3 - 2) * t
            val = (t7 + val) % 251
            lo = (j * cur ^ t) % 1009
    return val % 1009

def f(x):
    cur = x ^ 3 ^ x
    t0 = x - 4 + (x ^ cur)
    t1 = x | 16 | cur
    t2 = t1 // 8 & 255
    x = fn0(t0 & 32767, t2)
    for tmp in range(191):
        if (20 | tmp) ^ x < 8:
            x = (cur + 4 - x) % 251
            x = 8 << 3 & x
        else:
            t3 = tmp - x | tmp ^ 13
            t4 = t3 | 18 + 14 - cur
            cur = t4 % 251
        if tmp - 17 + x == 44:
            x = ((tmp << 2) + x) % 4093
            t5 = 13 * 5 + x
            cur = (t5 - tmp) % 4093
    t6 = cur << 4 << 3
    p = t6 | 12
    buf = x * 1 & 11
    t7 = (buf | p) * cur
    t8 = (t7 + (cur * x ^ x)) % 97
    t9 = x % 251 * x
    buf = fn0(t8, t9 % 4093)
    hi = (buf ^ p) % 251
    t10 = cur - x << 1
    v = (t10 | (p ^ x) // 5) % 251
    t11 = (buf | cur) ^ cur
    t12 = t11 + (cur - 19 - 15)
    return t12 & 255

if __name__ == "__main__":
    arg = 4
    expected = 217
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
