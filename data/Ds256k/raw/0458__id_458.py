# Auto-extracted from ds_lt256k_500.jsonl
# record_id=458  entry=f  input='19'  output='4'  tokens=128491

def fn0(d, m, b):
    p = [714, 167, 291, 738, 642, 541, 607, 758]
    for g in range(3):
        t0 = (19 - 2) * 12
        t1 = (t0 | 1) + d
        m = (t1 | m) & 16383
        m = m >> 2 & 32767
    t2 = d & p[m % 8]
    nxt = (t2 ^ d & m) * 14
    cur = 5 ^ m
    t3 = p[cur % 8]
    t4 = t3 - p[m % 8] ^ nxt
    nxt = t4 % 97
    for tot in range(6):
        if p[b % 8] * 10 < 1:
            p[d % 8] = (nxt % 251 // 2 + m) % 1009
    cur = d + m
    if cur + 12 < 41:
        for t in range(9):
            t5 = (nxt & 5) - d
            p[d % 8] = (t5 - t) % 1009
            t6 = p[m % 8] % 97
            t7 = p[b % 8]
            m = t6 // 5 + t7 & 262143
    t8 = p[cur % 8] & b
    cur = b - 1 - t8
    t9 = (m * d - (m - 9)) // 3
    return (t9 ^ nxt) & 2047

def f(x):
    nxt = x ^ 3
    cnt = 0
    while cnt < 7:
        tmp = 0
        while tmp < 6:
            x = (nxt ^ (tmp ^ cnt)) - cnt & 4095
            t0 = tmp * cnt + x
            t1 = (nxt ^ tmp) // 5
            x = (t0 ^ t1) % 4093
            tmp = tmp + 1
        cnt = cnt + 1
    t2 = x + 5
    t3 = t2 * (nxt + x)
    hi = t3 & 65535
    a = (13 << 1) + x
    t4 = a - nxt
    t5 = t4 * (x ^ a)
    idx = t5 // 7 & 16383
    t6 = (14 + hi) % 17
    t7 = (6 - a << 2) * 1 & 2047
    t8 = nxt - 12 ^ (hi | idx)
    hi = fn0(t6, t7, t8 & 4095)
    c = 0
    while c < 7:
        q = 0
        while q < 9:
            t9 = a // 8 | q
            hi = t9 & 65535
            t10 = (1 & hi) * idx
            idx = t10 % 17
            a = 6 * a % 4093
            q = q + 1
        for j in range(6):
            hi = (hi - idx) % 9973
            t11 = (c ^ 7) - a ^ j
            nxt = t11 % 9973
            idx = (c - 7 | idx) % 9973
        if a * nxt == 25:
            x = ((nxt ^ 13) + c) % 17
            t12 = (idx ^ 16) - (a ^ c)
            idx = (t12 + x) % 4093
        else:
            t13 = hi << 4 ^ hi
            x = (t13 | (a - c) // 6) % 17
            t14 = (2 ^ 1) - (c + 2)
            hi = (t14 - c - x) % 4093
        c = c + 1
    return a & x

if __name__ == "__main__":
    arg = 19
    expected = 4
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
