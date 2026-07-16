# Auto-extracted from ds_lt256k_500.jsonl
# record_id=355  entry=f  input='4'  output='1'  tokens=104294

def fn0(m, b):
    tot = m | 2
    tot = m * 10 & 10
    tot = (m * m ^ 11) % 65521
    for c in range(2):
        m = (c - b) % 9973
        z = 0
        while z < 6:
            t0 = tot * tot // 3 | c
            m = (t0 ^ m) % 65521
            t1 = (b ^ 3) << 3
            m = t1 - z & 8191
            z = z + 1
    for aux in range(12):
        lo = 0
        while lo < 8:
            t2 = (aux - 20) * (lo * aux) | m
            tot = t2 % 9973
            t3 = b * 2 // 3
            t4 = (tot & 9) * b
            t5 = t3 ^ t4 | lo
            m = t5 % 9973
            lo = lo + 1
    t6 = m * b + b
    b = t6 & 131071
    b = b + tot
    return tot * m & 2047

def fn1(j, e):
    q = [164, 159, 207, 228, 176, 101, 142]
    aux = 0
    while aux < 9:
        e = (e + aux) % 4093
        z = 0
        while z < 3:
            q[aux % 7] = (15 ^ e) // 6 % 251
            t0 = (1 - j) // 3
            t1 = t0 >> 2 | z
            e = t1 & 511
            z = z + 1
        t2 = q[j % 7] - j
        e = t2 % 4093 - aux & 16383
        aux = aux + 1
    val = 11 + j - e
    e = ((10 | j) ^ j) >> 1
    t3 = j + 7 - val
    return t3 % 9973

def f(x):
    buf = x - 18
    u = (buf ^ 20) >> 4
    prv = 0
    while prv < 278:
        if buf ^ 2 < 28:
            buf = (buf + x) % 9973
        prv = prv + 1
    t0 = x - 8
    t1 = t0 + (u ^ buf)
    x = t1 & u
    t2 = buf * x * buf % 9973
    t3 = x - 7 + x
    t4 = t3 * (x * buf | buf)
    u = fn0(t2, t4 % 9973)
    return (9 - x ^ buf) % 17

if __name__ == "__main__":
    arg = 4
    expected = 1
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
