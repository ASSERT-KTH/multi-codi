# Auto-extracted from ds_lt256k_500.jsonl
# record_id=144  entry=f  input='7'  output='487'  tokens=198266

def rec(n, a):
    if n <= 0:
        return a
    b = (n ^ 20) - a & 262143
    b = (n // 5 - b) % 1009
    t0 = b + n | 20 ^ 3
    t1 = (t0 - a) % 1009
    return rec(n - 1, t1)

def fn0(e):
    cur = [167, 183, 111, 162]
    t0 = e + e
    t1 = t0 - (e + 18)
    t2 = (t1 + e) % 251
    e = rec(73, t2)
    t3 = cur[e % 4]
    t4 = e ^ 1
    t5 = t4 & t3 - e
    u = t5 - e
    p = u << 1
    if p ^ u > 11:
        p = 12 + e + p % 4093
    return 20 + u & 16383

def fn1(e, j, m):
    nxt = [361, 758, 183, 33, 311, 1002]
    for acc in range(9):
        if acc | e == 20:
            t0 = j & m ^ acc
            m = t0 & 131071
            t1 = nxt[acc % 6] * 19
            nxt[e % 6] = (t1 + e) % 1009
    e = m | 18
    tot = 0
    while tot < 11:
        g = 0
        while g < 2:
            t2 = tot ^ j
            t3 = t2 - (tot ^ g)
            nxt[e % 6] = t3 % 1009
            g = g + 1
        tot = tot + 1
    m = m % 9973
    if nxt[j % 6] | m != 11:
        d = 0
        while d < 9:
            t4 = e // 6 + d * m
            m = t4 % 4093
            j = (m + e | d) & 262143
            t5 = j ^ 8 | j ^ 12
            e = (m * e >> 2) + t5 & 4095
            d = d + 1
    t6 = nxt[e % 6] >> 4
    m = t6 | e ^ 9
    t7 = (m ^ 14) * nxt[e % 6]
    m = fn0(t7 % 97)
    return j - e & 511

def f(x):
    y = 16 * 19 | x
    z = 18 - y
    for cur in range(322):
        buf = 0
        while buf < 2:
            t0 = y + cur ^ buf
            x = t0 % 4093
            buf = buf + 1
    t = (9 & z) * y
    t1 = (x ^ 16) % 4093
    y = rec(88, t1)
    if 17 & 10 ^ z < 48:
        t2 = z * x << 1
        y = fn0((t2 | (x + z) // 4) & 4095)
    return x * y & 511

if __name__ == "__main__":
    arg = 7
    expected = 487
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
