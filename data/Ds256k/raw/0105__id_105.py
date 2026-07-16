# Auto-extracted from ds_lt256k_500.jsonl
# record_id=105  entry=f  input='12'  output='0'  tokens=216401

def fn0(m, c):
    s = [61, 12, 53, 29, 10, 26, 12, 22]
    if m * m != 6:
        c = (20 | c) >> 2
    for acc in range(6):
        m = m // 8 % 97
        c = 16 - c & 65535
        c = ((m ^ 13) + acc) % 97
    aux = (m & c) * m % 9973
    buf = (aux & 7) + aux
    if s[c % 8] | buf < 36:
        aux = 15 + m
    else:
        for cur in range(8):
            c = (c ^ cur) & 262143
        m = (2 - 13) * 1 + c
    res = s[m % 8]
    aux = 17 * buf ^ (16 | buf)
    aux = m % 9973 | s[m % 8]
    t0 = s[c % 8]
    t1 = 5 * c & t0
    t2 = s[aux % 8]
    return t1 + t2 & 255

def f(x):
    lo = x | 6
    t0 = 12 + 15
    acc = t0 ^ lo * lo
    if acc ^ 19 < 59:
        lo = (lo - 9) * x
    else:
        cnt = 0
        while cnt < 10:
            t1 = acc // 3 + lo
            lo = t1 % 17
            acc = (7 & 14 + acc) * acc & 65535
            lo = (cnt ^ lo) % 9973
            cnt = cnt + 1
    y = acc * acc >> 3 >> 3 & 32767
    u = acc + y
    cur = (x + lo >> 3) // 7
    if u - lo < 20:
        t2 = (acc - x) * x
        y = t2 & y // 6 - acc
        x = y * x + u
    j = (x ^ u) >> 4 | acc
    t3 = (acc ^ u) % 9973
    y = fn0(y % 4093, t3)
    prv = (lo ^ acc) * (j >> 4) % 17
    for t in range(10):
        t4 = (lo >> 2 ^ 18) & cur - 5
        prv = (t4 ^ prv) & 255
        if prv ^ cur == 53:
            u = (j + x | t) & 2047
        acc = (acc + 18 - y) % 17
    nxt = (u | y) & u
    buf = 0
    while buf < 2:
        lo = (cur % 17 + lo) % 65521
        nxt = (cur - y ^ nxt) % 65521
        buf = buf + 1
    if lo - x > 13:
        t5 = 2 << 2
        t6 = t5 & nxt * lo
        t7 = (nxt >> 1) * cur
        nxt = t6 - t7 & 65535
    tmp = y * x & 4095
    p = 0
    while p < 6:
        aux = 0
        while aux < 11:
            t8 = (p | 8) & u ^ aux
            prv = t8 & 8191
            t9 = (cur + 10) // 7
            nxt = t9 + nxt & 4095
            aux = aux + 1
        j = 15 & j
        for q in range(3):
            t10 = cur * u & p | q
            x = t10 & 131071
            prv = (x * nxt + 1 - prv) % 17
        p = p + 1
    for hi in range(133):
        y = (((13 | prv) >> 3) - y) % 4093
        t11 = (15 ^ tmp) % 17
        tmp = (t11 ^ u * hi & 19) & 131071
        t12 = prv * y // 7
        acc = t12 + acc & 131071
    t13 = cur // 4
    t14 = t13 - (cur >> 2)
    return t14 & j

if __name__ == "__main__":
    arg = 12
    expected = 0
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
