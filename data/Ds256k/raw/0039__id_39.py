# Auto-extracted from ds_lt256k_500.jsonl
# record_id=39  entry=f  input='5'  output='460'  tokens=223699

def fn0(a, m):
    s = 11 - m
    e = 9 & m
    for idx in range(4):
        a = e + m + idx & 32767
        for q in range(3):
            t0 = (5 | idx) ^ (q | a)
            m = t0 * ((idx ^ a) % 1009) & 65535
            a = (m - a) % 1009
            t1 = idx ^ 16
            t2 = t1 - (3 | m)
            m = t2 % 65521
    for cur in range(12):
        for hi in range(3):
            t3 = (a - 5) // 6
            t4 = t3 ^ cur | hi
            m = t4 & 511
            t5 = 2 + 13
            t6 = t5 | m + 5
            a = (t6 + a) % 1009
        e = (18 - 2 ^ cur) + e & 255
        for z in range(10):
            m = (z + cur ^ e) & 511
            t7 = a + s >> 4
            a = t7 & 32767
    t8 = m * m ^ a ^ e
    return t8 % 65521

def fn1(j, m):
    c = 0
    while c < 9:
        t0 = m + c ^ 20
        m = t0 * (10 + c | m) & 131071
        c = c + 1
    cur = j * j % 1009
    t1 = m * j & 16383
    t2 = (m << 4) + j & 32767
    m = fn0(t1, t2)
    cur = m - 16
    j = m ^ 6
    t3 = cur * j + j * cur
    cur = (t3 >> 1) % 1009
    t4 = (1 - cur) % 251
    m = t4 | cur
    j = m % 251
    return (m // 4 ^ cur) % 1009

def f(x):
    cnt = [209, 39, 130, 51, 89, 174]
    res = x + x
    t0 = (x ^ 18) & 1023
    t1 = (14 << 1) + res & 16383
    res = fn1(t0, t1)
    t2 = cnt[res % 6] >> 1
    t3 = t2 * res & 8191
    t4 = (res - 19) * 5 * res
    x = fn0(t3, t4 % 17)
    for g in range(8):
        hi = 0
        while hi < 11:
            t5 = x - res - (g | res)
            res = t5 % 17
            x = (x << 3) % 17
            hi = hi + 1
        if res // 2 != 40:
            res = (x + 15 ^ g) & 65535
            x = 14 * x // 6 & 8191
    t6 = 9 - cnt[x % 6]
    t7 = (res ^ x) - t6
    t8 = t7 * ((4 & res) - x)
    return t8 & 2047

if __name__ == "__main__":
    arg = 5
    expected = 460
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
