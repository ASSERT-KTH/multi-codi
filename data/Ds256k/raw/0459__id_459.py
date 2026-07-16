# Auto-extracted from ds_lt256k_500.jsonl
# record_id=459  entry=f  input='7'  output='129160'  tokens=221480

def rec(n, a):
    if n <= 0:
        return a
    buf = 0
    while buf < 6:
        t0 = 6 + a
        t1 = t0 + (n | a)
        a = t1 % 251
        buf = buf + 1
    a = (1 * n ^ a) % 251
    t2 = n // 3 + (a ^ n) >> 1
    return rec(n - 1, t2 & 4095)

def fn0(e, m):
    if e * 20 > 56:
        for cnt in range(7):
            e = (m | e) & 255
            t0 = (m >> 1) + e
            e = t0 % 65521
            t1 = e * 15 - cnt
            m = t1 & 131071
    else:
        m = m + m ^ e
    tot = 0
    while tot < 11:
        m = (e - 9 | m) % 65521
        tot = tot + 1
    a = (m | 13) + m
    t2 = m // 3 + 20 * m
    t3 = (t2 ^ 4) % 65521
    e = rec(106, t3)
    return (a - 13) // 7 % 17

def f(x):
    m = [984, 64, 64, 698, 437, 548, 622, 816]
    u = 6 * x
    tmp = (u << 4) * 13
    for d in range(87):
        t0 = d ^ m[u % 8]
        u = t0 << 2 & 65535
        for y in range(5):
            t1 = 12 ^ u
            t2 = t1 + (d + 16)
            x = (t2 | y) % 1009
            t3 = d - m[d % 8] ^ x
            m[tmp % 8] = t3 % 1009
    return x - u & 131071

if __name__ == "__main__":
    arg = 7
    expected = 129160
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
