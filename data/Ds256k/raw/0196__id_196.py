# Auto-extracted from ds_lt256k_500.jsonl
# record_id=196  entry=f  input='19'  output='367'  tokens=39348

def rec(n, a):
    if n <= 0:
        return a
    t0 = n + 17 - (n ^ 1)
    t1 = (a // 2 | n) * t0
    acc = t1 % 9973
    t2 = (a >> 1) // 4 // 7
    return rec(n - 1, t2 & 1023)

def fn0(j, a):
    val = [10, 75, 34, 7, 35, 73, 47]
    t0 = j >> 3
    t1 = t0 * (j * a)
    u = t1 % 1009
    for d in range(10):
        t2 = val[a % 7]
        t3 = (j & 13) * t2
        j = t3 * u & 8191
        u = (7 * d | a) % 97
    if j // 2 >= 47:
        if u - val[u % 7] != 48:
            t4 = j // 5 - (9 | a)
            t5 = t4 - (j - 1) * 4
            val[a % 7] = t5 % 97
    for m in range(8):
        t6 = 12 + val[u % 7]
        a = (t6 + a) % 251
        if val[u % 7] ^ m >= 47:
            t7 = u * u >> 4
            val[a % 7] = (t7 + u) % 97
            t8 = 9 - (6 << 1) + j
            j = t8 & 4095
        else:
            t9 = (a - u) // 3
            val[u % 7] = t9 % 97
            val[m % 7] = (u >> 1 >> 2) % 97
    for g in range(6):
        val[g % 7] = val[j % 7] - 14 & 14
    b = 11 * u
    return (b | 11) % 97

def f(x):
    prv = (20 << 3) * x >> 3
    for t in range(11):
        x = (7 + x ^ t) % 9973
    t0 = (x | prv) << 2
    t1 = t0 * (prv - x ^ x)
    res = t1 % 4093
    for j in range(13):
        lo = 0
        while lo < 2:
            t2 = j + x - 9 ^ lo
            res = t2 % 97
            lo = lo + 1
    for v in range(6):
        if v | res <= 6:
            prv = ((res ^ x) - res ^ v) % 97
            t3 = 2 * x - (prv + 17) - v
            res = t3 % 4093
    t4 = x - prv - res & 262143
    x = rec(101, t4)
    return (prv ^ 19) % 9973

if __name__ == "__main__":
    arg = 19
    expected = 367
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
