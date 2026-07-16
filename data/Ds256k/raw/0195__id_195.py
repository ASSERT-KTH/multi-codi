# Auto-extracted from ds_lt256k_500.jsonl
# record_id=195  entry=f  input='9'  output='470'  tokens=167260

def rec(n, a):
    if n <= 0:
        return a
    t = 0
    while t < 4:
        a = a + n & 65535
        t0 = a + a >> 2 | t
        a = t0 & 131071
        t = t + 1
    t1 = ((n | 9) - a) % 17
    return rec(n - 1, t1)

def fn0(d, a):
    d = 8 + d
    for acc in range(4):
        t0 = 9 * a + acc
        d = t0 % 9973
        t1 = 3 - acc | a
        a = t1 % 9973
    a = d * a & 65535
    t2 = ((d | a) - d) * 4
    return t2 % 17

def f(x):
    d = [223, 156, 42, 241, 13, 135, 46, 53]
    lo = d[x % 8] & 19
    if 3 ^ lo > 30:
        t0 = d[lo % 8]
        t1 = x - lo
        lo = t1 - (t0 & x)
    else:
        lo = (lo ^ x) * 14 + lo
    t2 = d[x % 8]
    u = lo & t2
    t3 = (lo ^ 5) % 4093
    t4 = (u & x) + 6
    t5 = t4 << 2 & 32767
    u = fn0(t3, t5)
    t6 = u // 8
    t7 = d[u % 8]
    t8 = d[lo % 8]
    t9 = t7 + t8
    t10 = t6 - (lo - 8)
    t11 = t9 - x * u
    t12 = t10 * t11 % 4093
    d[u % 8] = t12 % 251
    cur = (x << 2) + 16
    t13 = d[cur % 8] & x
    prv = t13 * (lo - d[cur % 8])
    res = (d[lo % 8] & 11) - cur
    for idx in range(109):
        res = res * u & 1023
        t14 = d[prv % 8]
        t15 = t14 >> 2
        t16 = t15 - u * u
        x = (t16 + x) % 9973
    t17 = d[prv % 8] ^ 4
    t18 = t17 + d[u % 8]
    w = (7 + prv << 1) - t18
    z = prv * prv - 12 & 16383
    for s in range(7):
        t19 = d[w % 8]
        t20 = s << 2
        t21 = t20 - t19 * 1
        u = t21 % 251
    t22 = d[w % 8] | res
    t23 = t22 & d[z % 8] * cur
    val = t23 << 4
    t24 = 18 - val ^ u
    cur = rec(59, t24 & 131071)
    hi = d[x % 8] ^ u
    v = val % 251
    y = d[hi % 8] - 9
    return (u + d[y % 8]) % 4093

if __name__ == "__main__":
    arg = 9
    expected = 470
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
