# Auto-extracted from ds_lt256k_500.jsonl
# record_id=301  entry=f  input='11'  output='1'  tokens=22025

def fn0(g, m):
    t0 = (g * g ^ m) + g
    m = t0 % 9973
    g = g & 2 ^ m
    m = g >> 2
    tot = 0
    while tot < 3:
        if tot + m < 61:
            m = m * 1 & 511
            m = g * tot & 16383
        else:
            t1 = g >> 3 & (15 ^ 12)
            m = t1 - 3 - m & 32767
            t2 = (9 ^ g | g) + m
            m = t2 % 9973
        if tot + g >= 50:
            m = (g ^ tot) & 4095
            g = (g * m + (g | m)) % 4093
        tot = tot + 1
    g = 4 & m
    if 19 - 10 | m != 37:
        g = (g & m) + (g >> 3)
    else:
        g = g * m & 131071
    g = (m ^ g) - (m ^ 2)
    return (9 ^ g << 2) & 131071

def f(x):
    idx = [184, 338, 508, 584, 68, 265, 900, 1006]
    q = idx[x % 8] ^ x
    if q + q <= 46:
        t0 = q * x // 7
        q = t0 >> 4
    else:
        idx[q % 8] = x - 10
        q = 10 + q
    hi = x ^ 20
    b = 0
    while b < 8:
        x = (q << 1 | b) & 32767
        nxt = 0
        while nxt < 3:
            hi = ((x << 1) + hi) % 17
            q = (b * nxt - (x - 17)) % 17
            nxt = nxt + 1
        b = b + 1
    d = idx[x % 8] >> 1
    for aux in range(16):
        if x - 20 != 37:
            t1 = 13 & 5 | 15
            t2 = t1 & 7 | q
            x = (t2 + aux) % 65521
            t3 = x * d % 1009
            hi = (t3 + hi) % 65521
        else:
            t4 = aux + aux + (hi & d)
            idx[d % 8] = 9 + t4
            t5 = aux + 6 | hi
            hi = t5 & 262143
    buf = 0
    while buf < 10:
        t6 = (d | hi) ^ (d ^ 4)
        x = (t6 | 12 | x) & 131071
        t7 = (d | 13) - (d | buf)
        d = t7 & 1023
        buf = buf + 1
    t8 = ((x | d) ^ hi) >> 2
    return t8 & 4095

if __name__ == "__main__":
    arg = 11
    expected = 1
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
