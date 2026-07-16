# Auto-extracted from ds_lt256k_500.jsonl
# record_id=412  entry=f  input='3'  output='63599'  tokens=138048

def rec(n, a):
    if n <= 0:
        return a
    a = (n + a) * n % 9973
    t0 = n * a // 7 // 4
    return rec(n - 1, t0 % 9973)

def fn0(e):
    t0 = e // 7 + e * 9
    t1 = t0 + ((2 | e) ^ e)
    e = rec(114, t1 % 9973)
    p = e + 5
    t2 = (p + 5) % 97
    p = rec(66, t2)
    for prv in range(2):
        t3 = (15 ^ e) - (prv - 3)
        e = t3 & 32767
        e = (e - 5) % 9973
        p = (prv & p) + p & 4095
    e = e - 10 ^ e | p
    for lo in range(12):
        t4 = 9 | 3
        t5 = t4 * (lo * e)
        p = (t5 | p) % 9973
    t6 = (e - p) % 97
    return t6 << 4 & 255

def fn1(c):
    c = fn0(15 + c & 4095)
    for buf in range(2):
        t0 = buf * buf + c
        c = t0 % 17
        for res in range(12):
            c = ((res ^ buf) - c) % 17
            t1 = c * res ^ buf * 17
            c = buf - 3 & t1
    nxt = c | 1
    for q in range(3):
        t2 = (q ^ 1) + 1
        c = (t2 ^ c) % 17
    t3 = (c + nxt | 18) % 1009
    nxt = rec(97, t3)
    t4 = c // 6 - c % 17
    g = t4 ^ (c ^ nxt) & c // 3
    t5 = 18 ^ c | g
    return t5 % 17

def f(x):
    g = [43, 45, 70, 77]
    g[x % 4] = ((x + x) * x >> 2) % 97
    u = 0
    while u < 16:
        x = (u + x ^ 16) % 97
        t0 = 1 * 9 ^ u - x
        t1 = t0 * g[u % 4]
        x = t1 & 32767
        q = 0
        while q < 9:
            t2 = u * u | u | x
            g[q % 4] = t2 % 97
            t3 = g[x % 4] * x
            t4 = t3 + 17 * 18
            t5 = (t4 - (4 ^ x) * q) % 4093
            g[u % 4] = t5 % 97
            q = q + 1
        u = u + 1
    d = x >> 2 ^ 11
    t6 = g[x % 4]
    t7 = d - x - t6
    e = t7 & x
    t8 = (7 - x) * e
    acc = t8 % 65521
    p = e + acc
    t9 = g[e % 4]
    g[d % 4] = (t9 - 8) % 97
    for m in range(5):
        d = (m * 16 ^ p) % 4093
        t10 = (acc - d) // 8 * acc + x
        x = t10 % 97
    t11 = (17 | x) + p // 4
    s = t11 | (d | e) + (x - e)
    t12 = g[p % 4]
    cur = s - t12 - s
    t13 = g[p % 4]
    t14 = acc * t13
    t15 = t14 | 16 + x
    buf = t15 % 97
    t16 = s * cur ^ e - acc
    p = fn0(t16 & 32767)
    t17 = g[buf % 4]
    t18 = x % 97
    t19 = t18 - (d + t17)
    t20 = g[cur % 4]
    return (t19 - t20) % 65521

if __name__ == "__main__":
    arg = 3
    expected = 63599
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
