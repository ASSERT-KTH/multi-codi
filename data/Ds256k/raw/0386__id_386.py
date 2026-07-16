# Auto-extracted from ds_lt256k_500.jsonl
# record_id=386  entry=f  input='4'  output='184'  tokens=70063

def rec(n, a):
    if n <= 0:
        return a
    t0 = a + a
    t1 = t0 + n * n
    a = t1 % 9973
    t2 = n // 4 + 18 - a
    a = t2 % 97
    j = 0
    while j < 5:
        a = (n - 20 | a) % 9973
        a = (8 - n | a) % 65521
        j = j + 1
    t3 = (a + n) % 97
    return rec(n - 1, t3)

def fn0(e):
    val = [36, 45, 29, 37, 8]
    for u in range(7):
        if e ^ u > 50:
            val[e % 5] = (u + u ^ e) % 97
            t0 = 1 ^ u
            t1 = t0 * (e * u)
            val[e % 5] = t1 % 9973 % 97
        else:
            t2 = (u | 8) + 11
            t3 = (t2 | 13) + e
            val[e % 5] = t3 % 97
            t4 = u * val[u % 5] + e
            val[u % 5] = t4 % 97
        for v in range(4):
            e = e * 9 // 2 % 9973
            t5 = 9 - v | e
            val[u % 5] = t5 % 97
            t6 = v & e
            t7 = t6 | e + u
            t8 = v * v * u
            val[v % 5] = (t7 - t8) % 97
    t9 = 5 - 20
    t10 = t9 | e & 2
    tmp = t10 * e & 1023
    res = (val[tmp % 5] | 13) // 5
    tmp = 18 * tmp + e + res
    for w in range(11):
        val[e % 5] = (res + res) % 97
    for tot in range(2):
        t11 = res - tot & tot
        e = t11 & tot * tmp // 3
        t12 = tot - 3 ^ res
        e = t12 & 131071
    e = 2 ^ res
    return ((10 + res) // 5 ^ 20) % 251

def fn1(m):
    t0 = m - 6 & m
    tot = t0 - 9
    if tot + 5 != 10:
        t1 = tot << 2 | tot
        t2 = t1 + m & 511
        tot = rec(78, t2)
    else:
        for lo in range(5):
            m = (m - lo) % 4093
    for s in range(7):
        for p in range(8):
            t3 = 3 * p + s - m
            m = t3 & 255
            m = ((8 & s) + m) % 17
    val = 0
    while val < 8:
        tot = (val ^ tot) % 4093
        if m & val < 2:
            tot = (19 ^ val) * tot & 2047
        else:
            m = (val - m) % 97
        val = val + 1
    res = m - 2 >> 4 << 3
    return (res - m) % 17

def f(x):
    w = [114, 223, 243, 129, 25, 51]
    b = x - 17
    t0 = w[b % 6]
    t1 = (t0 ^ 15) * b
    x = t1 + b
    for q in range(12):
        t2 = q + q | x
        x = t2 & 32767
        t3 = q - 17 + 8 ^ x
        x = t3 % 9973
        x = (x ^ q ^ 14) & 1023
    t4 = 15 * 4 * (x << 1) % 9973
    w[x % 6] = t4 % 251
    for tmp in range(2):
        for z in range(177):
            w[z % 6] = (b ^ z) + b
    t5 = (b & 7 | b * b) - b
    return t5 % 251

if __name__ == "__main__":
    arg = 4
    expected = 184
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
