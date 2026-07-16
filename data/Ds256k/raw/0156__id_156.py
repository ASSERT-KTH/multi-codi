# Auto-extracted from ds_lt256k_500.jsonl
# record_id=156  entry=f  input='2'  output='7772'  tokens=66056

def fn0(c):
    w = 1 * c
    tot = w & 11
    t0 = 6 ^ tot
    c = t0 + (w << 2)
    if tot * c != 7:
        for q in range(11):
            tot = (w - c - tot) % 65521
            tot = (c + 13 - tot) % 1009
            tot = ((w ^ 16) << 1) * q & 8191
        c = 10 + c
    else:
        t1 = (c | w) - w
        c = t1 + ((tot | c) ^ tot)
    c = 15 + w + (5 + 16)
    w = tot + c - 15
    if c * tot <= 14:
        if 20 * w == 7:
            t2 = (5 | c) + (w & c) ^ c
            w = t2 % 1009
            c = (w + tot) * tot % 251
    else:
        if 7 - c < 36:
            w = c + c & c
            w = tot + 19 - tot
        else:
            tot = tot - 9 >> 3
            c = (w | 12) % 65521
    w = (c - tot) * w & 1023
    return (w * 3 + c - w) % 9973

def fn1(c, g):
    c = fn0(12 - c & g)
    c = fn0((g - c) // 8 & 131071)
    for buf in range(10):
        g = (buf - 13 ^ g) % 4093
    c = g - 14 ^ c
    t0 = g ^ c
    t1 = t0 * (9 & c)
    c = (t1 + g) % 1009
    val = 0
    while val < 4:
        t2 = (13 ^ g) - c
        c = t2 // 2 % 1009
        g = g & 10
        t3 = c - 15 + 10
        g = (t3 + val) % 4093
        val = val + 1
    g = 4 + g
    t4 = (g * g ^ g - 19) * c
    g = t4 & 65535
    t5 = g - c - (3 | g)
    return t5 & 32767

def f(x):
    acc = (x | 5) << 2
    hi = 13 * x + 2
    if 16 ^ hi == 21:
        e = 0
        while e < 4:
            hi = (e | x) % 97
            hi = (7 * 20 ^ x ^ e) % 97
            t0 = e | x
            x = t0 & acc // 7
            e = e + 1
        if acc | 2 < 62:
            hi = ((x ^ acc) & acc) // 7
            acc = acc // 5
        else:
            t1 = x + hi ^ acc % 97
            hi = t1 << 4
            acc = acc
    else:
        for idx in range(11):
            hi = (idx - acc) % 97
            t2 = (acc << 1) * 9
            t3 = (hi & x) - hi
            x = t2 + t3 & 1023
            x = ((hi << 3) * x - acc) % 9973
    if hi // 7 >= 55:
        hi = hi | 11
    else:
        w = 0
        while w < 2:
            x = (9 - x) % 97
            hi = hi * hi % 9973
            w = w + 1
    t4 = (x | acc) - x
    hi = t4 - (acc & 3) * hi
    hi = x - hi << 1
    x = 2 - 18 - x
    t5 = (18 + x) * (hi | acc) - acc
    for m in range(11):
        nxt = 0
        while nxt < 8:
            t6 = (3 ^ nxt) - hi
            acc = t6 % 9973
            t7 = (x & hi) + nxt
            t8 = t7 - (m + 8) * m
            acc = t8 & 16383
            nxt = nxt + 1
    return t5 & 8191

if __name__ == "__main__":
    arg = 2
    expected = 7772
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
