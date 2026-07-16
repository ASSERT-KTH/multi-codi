# Auto-extracted from ds_lt256k_500.jsonl
# record_id=227  entry=f  input='19'  output='9'  tokens=221064

def rec(n, a):
    if n <= 0:
        return a
    for tmp in range(5):
        a = 11 + a & 4095
        if a - 6 < 57:
            t0 = (20 ^ 1) - (tmp ^ 20)
            t1 = t0 * (tmp + a >> 2)
            a = t1 % 97
    m = (n & 19) + a & 262143
    m = m * 3 % 4093
    t2 = (a + a) % 97
    return rec(n - 1, t2)

def fn0(m, j):
    m = j * j % 251
    for y in range(6):
        t0 = m >> 2 | 19
        t1 = t0 ^ (j | 12) >> 2
        m = t1 % 1009
    j = j // 3
    t2 = 20 * 20 + m * j
    m = t2 & 1023
    if j | m == 48:
        t3 = m // 2 | j
        t4 = (t3 + ((j ^ 16) + j)) % 1009
        j = rec(120, t4)
    return (j - m - 17) % 251

def f(x):
    hi = x * x
    for b in range(10):
        t0 = x - b
        t1 = t0 ^ hi + x
        x = t1 // 6 & 65535
        t2 = hi ^ 13 ^ x
        x = t2 & 262143
        p = 0
        while p < 69:
            t3 = hi & 6 & 19
            hi = t3 - ((9 ^ b) & x) & 32767
            p = p + 1
    res = hi + hi
    y = hi - 11
    if hi | res >= 47:
        if 3 + 18 + y != 0:
            res = x ^ res
    else:
        y = (3 << 4) - hi
        hi = y & res
    cnt = 0
    while cnt < 11:
        x = (hi - x >> 1) % 251
        cnt = cnt + 1
    q = 0
    while q < 12:
        hi = (hi | q) % 251
        q = q + 1
    aux = 0
    while aux < 4:
        res = (x - 11 - res) * x % 1009
        aux = aux + 1
    if y + y < 61:
        t4 = (hi ^ res) % 9973
        x = rec(29, t4)
        for j in range(9):
            x = x % 65521
    else:
        if 3 - hi <= 4:
            t5 = (res + y) * hi
            x = rec(29, t5 % 65521)
            res = 16 + 11 + res
    for m in range(11):
        if 17 * y != 52:
            t6 = x << 3
            t7 = t6 + hi * y
            x = t7 % 65521
        else:
            t8 = (m ^ y) * hi
            res = t8 % 251
    return (9 ^ y) & 11

if __name__ == "__main__":
    arg = 19
    expected = 9
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
