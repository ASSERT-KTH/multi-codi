# Auto-extracted from ds_lt256k_500.jsonl
# record_id=261  entry=f  input='20'  output='46487'  tokens=13421

def fn0(b):
    y = 0
    while y < 5:
        b = y & b
        b = (b % 4093 >> 4) % 4093
        y = y + 1
    t0 = (b ^ 1) * (b * b)
    v = t0 & (b & 3) - (b + b)
    d = 0
    while d < 8:
        if d - 5 - v > 44:
            b = (d - v) % 65521
        else:
            t1 = (b * 11 & b // 4) + v
            v = t1 % 65521
            b = 17 - d + b & 511
        b = (b - v) % 65521
        d = d + 1
    idx = (v ^ 3) * b % 65521
    w = 0
    while w < 6:
        b = (w & 10 | w) + b & 262143
        if idx // 5 >= 64:
            b = b << 3 & 511
            v = (w - v) % 65521
        else:
            idx = ((17 | 12) ^ idx) & 511
            idx = (v ^ 11 ^ v + w) % 9973
        w = w + 1
    v = v + idx
    return (v >> 3) % 65521

def fn1(b):
    u = [439, 226, 408, 801]
    prv = 0
    while prv < 4:
        for a in range(10):
            t0 = (b & 14) + b * 19
            t1 = 11 * prv - (prv << 4)
            u[b % 4] = (t0 - t1 & 8191) % 1009
        cur = 0
        while cur < 8:
            t2 = (prv ^ 5) * 4 - b
            u[cur % 4] = t2 % 1009
            cur = cur + 1
        t3 = u[prv % 4] * b
        b = t3 * 1 & 65535
        prv = prv + 1
    t = (b * b >> 2) % 4093
    t4 = (t * b + (b ^ t)) * t
    t = fn0(t4 % 9973)
    for m in range(10):
        if b << 3 == 58:
            t = (m - 20 | b) % 17
        aux = 0
        while aux < 12:
            t5 = (u[aux % 4] >> 2) // 8
            t = (t5 | t) % 4093
            aux = aux + 1
    if b * u[t % 4] < 60:
        if t & b == 24:
            t6 = t // 5 ^ 12
            t = t6 * t % 4093
            u[t % 4] = (t + u[t % 4]) % 1009
        t = b << 3 ^ 1
    else:
        t7 = u[t % 4]
        b = t7 + u[t % 4]
    acc = t + b - (7 << 2) + b
    t8 = b * u[b % 4]
    j = (t8 - (9 - 6)) % 4093
    tot = (2 ^ 6) - b
    return acc % 17

def f(x):
    j = [892, 350, 245, 162, 516, 338]
    if x ^ 10 <= 23:
        t0 = j[x % 6]
        t1 = x | t0
        t2 = t1 + (x + x)
        x = fn0(t2 // 3 % 4093)
        for w in range(12):
            t3 = (x & j[w % 6]) + 10
            x = t3 - (w * x - w) & 262143
            t4 = (12 - w) * x
            x = t4 & 65535
            t5 = (w - 13) * (w - x)
            x = t5 % 4093
    j[x % 6] = (x ^ 7) % 1009
    for prv in range(2):
        t6 = prv - x ^ prv
        j[prv % 6] = t6 % 1009
    j[x % 6] = j[x % 6] >> 2
    nxt = x ^ 5
    b = j[nxt % 6] // 2 + x
    acc = (18 - b) * 7 % 17
    q = (acc ^ x) + 5
    m = 13 | q
    e = 0
    while e < 3:
        if 8 & m <= 5:
            t7 = (20 ^ j[e % 6]) >> 4
            q = ((x + b) * x - t7) % 65521
        e = e + 1
    for res in range(2):
        for p in range(26):
            q = q & b
        if b - res >= 50:
            j[x % 6] = (x + 1) % 1009
        else:
            t8 = j[x % 6]
            t9 = j[x % 6]
            j[b % 6] = t8 * t9 % 17
            t10 = b - j[res % 6]
            m = acc - 1 & t10
        t11 = m * j[res % 6]
        nxt = t11 % 65521
    if acc * x > 37:
        if j[nxt % 6] * j[m % 6] == 12:
            t12 = (18 + acc) * (q - acc)
            m = t12 % 17
        v = 0
        while v < 2:
            j[m % 6] = (19 ^ m) % 4093 % 1009
            v = v + 1
    else:
        idx = 0
        while idx < 6:
            j[nxt % 6] = (nxt ^ 2 ^ acc) % 97
            j[idx % 6] = (11 * 8 ^ b) % 1009
            idx = idx + 1
    return (2 + 5 | nxt) % 65521

if __name__ == "__main__":
    arg = 20
    expected = 46487
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
