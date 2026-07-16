# Auto-extracted from ds_lt256k_500.jsonl
# record_id=323  entry=f  input='2'  output='1137'  tokens=151583

def fn0(c):
    u = [801, 786, 887, 532, 633, 301, 816, 616]
    tot = c // 4 + u[c % 8]
    buf = 0
    while buf < 11:
        t0 = (tot | 11) + 11
        tot = t0 & 511
        buf = buf + 1
    t1 = u[c % 8]
    t2 = c >> 1
    t3 = t2 * (c & t1)
    tot = t3 % 251
    for nxt in range(5):
        for d in range(11):
            t4 = c - u[c % 8]
            c = (d & nxt ^ t4) & 1023
            t5 = u[tot % 8] % 251
            t6 = c ^ tot ^ nxt & d
            tot = (t6 | t5 * tot) & 255
    t7 = u[c % 8]
    c = t7 + 17 & tot
    c = tot + tot + tot << 2
    t8 = c - 13
    c = t8 + (19 & tot)
    y = 0
    while y < 3:
        e = 0
        while e < 9:
            u[e % 8] = (10 - c & c) % 1009
            e = e + 1
        p = 0
        while p < 10:
            t9 = (u[c % 8] << 2) + tot
            tot = t9 & 255
            u[tot % 8] = (p - 7 - tot) % 1009
            t10 = u[p % 8]
            tot = (tot | t10) % 9973
            p = p + 1
        y = y + 1
    return (20 * 1 ^ tot) & 2047

def f(x):
    z = x + x + (x & 13)
    z = fn0((x ^ z) * z & 511)
    t0 = (x ^ 15) % 17
    x = t0 + (z % 17 << 1)
    for m in range(11):
        for tmp in range(6):
            x = (x - m) % 65521
            t1 = (10 - z) * x
            x = t1 * ((x >> 4) * m) % 65521
            z = (z - 9) % 65521
        if 5 | z == 29:
            z = (x ^ 6 ^ m) % 251
        else:
            x = (z + x >> 3 ^ m) % 65521
        t2 = 11 & 13 | z
        x = (t2 - x) % 251
    t3 = (x + 13) * (10 * x)
    x = t3 & 65535
    for c in range(2):
        for u in range(3):
            t4 = c + 1 + c - z
            z = t4 & 1023
    nxt = 0
    while nxt < 10:
        s = 0
        while s < 10:
            t5 = ((nxt | nxt + 6) << 3) - z
            z = t5 % 17
            x = x * z - nxt & 511
            s = s + 1
        nxt = nxt + 1
    t6 = z ^ 13
    z = t6 ^ z & 15
    return 5 * x * z & 2047

if __name__ == "__main__":
    arg = 2
    expected = 1137
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
