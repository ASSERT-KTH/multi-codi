# Auto-extracted from ds_lt256k_500.jsonl
# record_id=129  entry=f  input='13'  output='64930'  tokens=105529

def rec(n, a):
    if n <= 0:
        return a
    u = (10 * a ^ n) % 4093
    a = u - n + a & 65535
    if a ^ 14 > 33:
        if a * n >= 23:
            t0 = (n << 2) + u * a
            a = t0 % 97
            t1 = a - u
            t2 = t1 - 13 * 18
            a = (t2 | n) % 1009
        else:
            u = ((n & 18) << 2) - a & 16383
            t3 = a - n & 4
            u = (t3 ^ a - u - n) % 1009
        a = a - 1 >> 3 & 131071
    else:
        for lo in range(3):
            t4 = (5 + lo - lo) * n
            a = (t4 - a) % 1009
            t5 = (a ^ 8) - (n + 3)
            u = (t5 - lo) % 97
            t6 = a - 2 >> 3
            a = (t6 | (u << 4 | 4)) % 1009
        val = 0
        while val < 9:
            a = (u + 12 + val) % 4093
            t7 = n * a << 2
            u = (t7 ^ val) % 4093
            t8 = a - 17
            a = t8 & 18 + a
            val = val + 1
    t9 = ((u << 2) + a) % 97
    return rec(n - 1, t9)

def f(x):
    hi = x * x
    c = 6 * 14 - hi
    p = 0
    while p < 12:
        for z in range(10):
            hi = (z + c) % 4093
            x = z + hi & 255
        hi = c // 4 + hi & 8191
        c = (p ^ hi | hi) % 1009
        p = p + 1
    t0 = 1 & c & c
    c = rec(42, t0)
    idx = (hi >> 1) // 8
    for tmp in range(11):
        t1 = (c ^ tmp) >> 3
        t2 = t1 | hi & 3 ^ c
        idx = t2 % 4093
        for cnt in range(4):
            t3 = (tmp ^ hi) + (1 ^ x)
            c = t3 + cnt & 65535
            idx = (cnt - x) // 4 << 4 & 131071
            idx = ((cnt | 4) + c) % 1009
    aux = c // 6
    for m in range(5):
        if idx & m <= 5:
            t4 = (14 ^ x ^ idx // 3) + hi
            hi = t4 % 1009
            t5 = aux - 9 - idx + aux - m
            x = t5 & 2047
        t6 = c // 7 | aux
        aux = t6 % 4093
        u = 0
        while u < 4:
            t7 = aux * 19 ^ c
            c = t7 & 262143
            t8 = x * aux ^ u
            hi = t8 % 4093
            t9 = ((17 ^ m) + m | idx) + u
            c = t9 % 4093
            u = u + 1
    if (11 ^ 13) - idx > 34:
        for w in range(6):
            c = (aux | c) & 32767
        x = x * x % 4093
    val = (hi * idx << 2) % 1009
    for g in range(7):
        aux = (val // 7 | aux) & 8191
        t10 = (g + val) // 4
        t11 = aux + g ^ g
        x = (t10 ^ t11) & 131071
    d = aux + idx - 11
    if x * c < 47:
        t12 = 17 - 9
        d = t12 + (hi ^ c)
        d = d % 4093 - (val & 14) << 1
    else:
        aux = (aux - 6) // 5
        t13 = d + c | 16 * idx
        x = (val + val - idx | t13) & 2047
    t14 = hi - 12 + (idx - x)
    return t14 & 65535

if __name__ == "__main__":
    arg = 13
    expected = 64930
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
