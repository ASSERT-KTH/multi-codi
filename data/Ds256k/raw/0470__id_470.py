# Auto-extracted from ds_lt256k_500.jsonl
# record_id=470  entry=f  input='5'  output='33394'  tokens=252249

def fn0(d):
    hi = d * d - d & 511
    t0 = (7 | hi) - hi
    cnt = t0 - (hi * hi | hi)
    for tmp in range(10):
        for p in range(11):
            t1 = (d | tmp) - hi
            hi = t1 % 97
            d = (p | d) % 97
        t2 = d // 8 - tmp
        hi = t2 % 65521
        acc = 0
        while acc < 6:
            t3 = 17 + 12
            t4 = t3 - (hi >> 1)
            cnt = (t4 + cnt) % 9973
            hi = hi // 7 & 262143
            t5 = (acc & cnt) * d
            cnt = (t5 - acc) % 65521
            acc = acc + 1
    t6 = hi // 7 ^ 3
    u = t6 - ((13 ^ cnt) >> 4)
    val = 17 ^ u
    tot = val * hi - val & 131071
    cnt = (tot + 10 | 20) // 2
    t7 = (d ^ 16) >> 2 | tot
    return t7 & 32767

def f(x):
    t0 = x & 3
    t1 = t0 & (x | 12)
    t2 = x * x + x
    m = t1 * t2
    t3 = (15 + 18) * (11 << 4) // 3
    u = t3 | x
    t4 = m // 7 - (x + x)
    u = fn0(t4 << 2 & 16383)
    for val in range(6):
        t5 = 15 + val | x
        u = t5 % 65521
    g = u + m & u
    for idx in range(9):
        for prv in range(6):
            t6 = 15 - m - idx + u
            u = t6 % 65521
            t7 = ((x & 5) - 7) * prv
            g = t7 & 8191
    z = (g - x) * g & 131071
    tmp = 4 + 14 | z
    q = 3 + z << 2
    v = (x | tmp) + m
    m = fn0((x + z >> 2 | z) % 97)
    nxt = (q ^ 12) % 97
    for b in range(4):
        p = 0
        while p < 17:
            nxt = (tmp >> 2 | p) & 16383
            tmp = (u >> 2 ^ p) % 97
            p = p + 1
        t8 = (q | 1) - (1 + nxt) + g
        g = t8 % 97
    res = 0
    while res < 3:
        for w in range(9):
            v = (u << 1) + q - v & 65535
        x = (res & 5) + nxt & 65535
        t9 = u * 16 >> 2
        g = (t9 | res) % 97
        res = res + 1
    hi = 0
    while hi < 10:
        if g ^ v < 18:
            u = ((q | v) ^ u) & 511
            u = u * q & 511
        else:
            v = (((nxt | u) << 4) + v) % 65521
        if q - v == 34:
            t10 = ((3 | x) ^ tmp + hi) // 2
            v = t10 % 65521
            m = ((nxt // 7 | 5) + hi) % 65521
        hi = hi + 1
    t11 = q - 1 - (14 | x)
    return t11 % 65521

if __name__ == "__main__":
    arg = 5
    expected = 33394
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
