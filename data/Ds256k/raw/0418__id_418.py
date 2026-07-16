# Auto-extracted from ds_lt256k_500.jsonl
# record_id=418  entry=f  input='13'  output='79'  tokens=239882

def rec(n, a):
    if n <= 0:
        return a
    u = n * a % 1009
    t0 = n * n // 8
    t1 = t0 & n | a
    return rec(n - 1, t1 & 4095)

def fn0(b):
    t0 = 13 * b ^ 14 - b
    res = t0 // 6 % 4093
    z = ((b ^ 8) + 8) // 8
    t1 = res // 8 - res & 16383
    res = rec(109, t1)
    u = (16 - b ^ z) >> 4
    nxt = (13 ^ 11) - b
    for acc in range(7):
        if nxt % 17 != 13:
            t2 = ((5 << 2) - nxt ^ z) - acc
            res = t2 % 4093
            t3 = res % 97 - u
            u = t3 * ((12 & 9) * res) & 1023
        else:
            t4 = nxt >> 3
            t5 = t4 + res % 4093
            b = (t5 | acc) & 16383
            u = (((b | 20) >> 1) + acc) % 97
        z = (acc ^ b) & 8191
    t6 = (z >> 3) // 2
    t7 = t6 // 7 % 97
    u = rec(114, t7)
    return (u - z) * res & 8191

def f(x):
    t0 = x & 18 ^ x - 7
    cnt = t0 | x
    buf = (x - cnt & x) - cnt
    val = (x + buf | 4) // 4
    for u in range(85):
        x = x - val + cnt & u
        if 10 + u | buf < 19:
            val = u * 6 & val
        for b in range(6):
            t1 = buf * val << 3
            val = (t1 ^ val) & 2047
    s = cnt // 5 & buf
    t2 = buf + s & s
    prv = t2 // 3
    t3 = buf ^ x
    t4 = t3 - (cnt << 3)
    cur = t4 % 251
    for m in range(9):
        if (m ^ 5) + x >= 29:
            cur = (x - m) % 251
            x = x & val
        else:
            t5 = cnt >> 2 | x
            x = t5 & 2047
            cnt = ((val | buf) - m) % 17
    for c in range(8):
        if s + cnt == 61:
            t6 = (16 | x) * cur
            t7 = t6 - (buf | 4 | cur) + c
            cnt = t7 & 1023
            s = (cur + 2 ^ c) & 16383
    lo = 0
    while lo < 11:
        t8 = (cnt & cur) >> 2
        cnt = t8 & 8191
        p = 0
        while p < 6:
            t9 = (val >> 3) - s % 251
            cnt = ((t9 | 5) + cnt) % 17
            t10 = s * s | cur
            cur = t10 & 8191
            cnt = (buf | p) % 251
            p = p + 1
        lo = lo + 1
    t11 = val >> 1
    t12 = t11 + (cur - 3)
    g = t12 * buf
    a = 0
    while a < 5:
        res = 0
        while res < 6:
            x = ((val - 19) // 7 | res) & 32767
            res = res + 1
        a = a + 1
    t13 = (prv // 8 ^ x) % 17
    s = rec(101, t13)
    t14 = (buf >> 2) - prv
    t15 = s - 16 + prv
    z = t14 + t15
    for y in range(8):
        t16 = val - 1 >> 2
        t17 = (t16 ^ 6) - cnt
        cnt = t17 % 17
    hi = cur + cnt + 8
    v = (hi | cur) // 2 & cur
    t18 = (cnt | 13) * cur
    t19 = (val & s) >> 4
    tot = (t18 ^ t19) % 251
    t20 = (x >> 3) - v
    return (t20 | v) % 251

if __name__ == "__main__":
    arg = 13
    expected = 79
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
