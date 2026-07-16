# Auto-extracted from ds_lt256k_500.jsonl
# record_id=368  entry=f  input='12'  output='5'  tokens=259708

def rec(n, a):
    if n <= 0:
        return a
    q = a & n
    t0 = n + 20 + n
    t1 = t0 - (n + q - q)
    a = t1 % 251
    t = 0
    while t < 11:
        t2 = (a | t) - (t | 10)
        q = (a + t & a) * t2 % 251
        t = t + 1
    t3 = (a << 4) % 9973
    return rec(n - 1, t3)

def fn0(d):
    cnt = [85, 612, 209, 117, 151, 515]
    s = d >> 4
    t0 = (d >> 2) + s
    t1 = s * s ^ s
    z = (t0 + t1) % 1009
    y = 0
    while y < 4:
        if z * z < 34:
            t2 = s | cnt[s % 6]
            s = t2 * (z >> 1) & 16383
            cnt[d % 6] = (z + s) % 1009
        y = y + 1
    t3 = z * d - (z + s)
    a = t3 % 251
    if s >> 1 >= 59:
        t4 = (s + 8) * z
        d = t4 // 7 % 251
    else:
        t5 = a * a % 251
        a = rec(32, t5)
        tot = 0
        while tot < 7:
            t6 = d ^ 4 ^ s
            s = t6 & 16383
            tot = tot + 1
    p = 14 + s | s
    t7 = (9 ^ 19) + a
    return t7 & 511

def fn1(c):
    t = [93, 68, 24, 91, 25, 35, 14, 95]
    nxt = 0
    while nxt < 12:
        c = (c | nxt) % 251
        nxt = nxt + 1
    res = (c // 2 - c) // 4
    buf = (c >> 2) // 6
    for g in range(3):
        if 2 << 2 ^ buf == 12:
            t0 = 3 + res ^ t[g % 8]
            res = t0 & t[c % 8]
            c = (19 & c) * (res & 8) & buf
        else:
            t1 = 9 + 19 - g
            t[g % 8] = (t1 - res) % 97
        t2 = t[c % 8]
        t3 = res >> 2
        t4 = buf // 4
        t5 = t3 * (t2 ^ buf)
        t6 = t4 + (g ^ res)
        c = (t5 ^ t6) % 17
        if res % 251 == 62:
            t7 = (16 << 2) + buf
            c = (t7 | c) & 16383
            t8 = g - 14 - c
            t[c % 8] = t8 % 97
    return ((res << 1) - 17) % 4093

def f(x):
    b = 10 - x ^ x
    if 15 - b >= 9:
        if 18 * b <= 54:
            t0 = (b | x) - x & 262143
            x = rec(87, t0)
            x = b
        t1 = b + b & b
        x = t1 - (b & 6) * x
    x = 20 ^ x
    t2 = b - 8 + 9
    b = t2 + b
    for acc in range(6):
        b = acc + b & 1023
    for t in range(53):
        t3 = (x - 5) * (t - x)
        x = ((t ^ b) - b | t3) % 65521
        x = ((b | 20) + x) % 65521
    return b * x % 17

if __name__ == "__main__":
    arg = 12
    expected = 5
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
