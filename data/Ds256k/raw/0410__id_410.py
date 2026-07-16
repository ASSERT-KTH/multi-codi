# Auto-extracted from ds_lt256k_500.jsonl
# record_id=410  entry=f  input='5'  output='16345'  tokens=180537

def fn0(e):
    hi = 17 & e
    for a in range(10):
        if e * 16 <= 10:
            t0 = (e & 6) + hi
            e = (t0 << 2) % 1009
            t1 = 20 * a | 3 | a | hi
            hi = t1 % 1009
        nxt = 0
        while nxt < 12:
            e = (hi - (nxt - a)) % 97
            t2 = nxt + e
            t3 = t2 | 1 & e
            hi = t3 // 4 & 8191
            hi = (15 + 18 ^ e) + nxt & 511
            nxt = nxt + 1
    for lo in range(6):
        hi = (lo - hi) % 97
        m = 0
        while m < 12:
            t4 = 2 + 1 | m
            t5 = (t4 ^ 12) - hi
            e = t5 % 97
            t6 = 14 * hi | m
            e = t6 & 65535
            m = m + 1
        if e + hi <= 28:
            t7 = 16 | 10 | hi >> 3
            e = (t7 | e) & 1023
        else:
            t8 = 3 + (5 + e) - lo
            hi = t8 % 1009
    g = 0
    while g < 8:
        acc = 0
        while acc < 6:
            hi = 10 + hi & 4095
            hi = ((4 ^ e) & acc) + acc & 32767
            acc = acc + 1
        e = hi * g % 4093
        g = g + 1
    idx = e + hi >> 4
    t9 = idx - 16 - hi
    t10 = t9 * (20 * hi | 6)
    return t10 % 4093

def f(x):
    for d in range(3):
        x = (x | 8) - x - d & 8191
        for val in range(10):
            x = d - x & 1023
    if x - 17 == 3:
        x = (13 ^ x) - x
    else:
        x = x * x + x
        x = x + x & x
    t0 = (x >> 2) - (x - 8)
    x = fn0(t0 + (x + x) // 5 & 131071)
    hi = x * 19 % 17
    nxt = ((x << 4) + hi) * 5 % 251
    g = 0
    while g < 8:
        t1 = x // 5 * (g * g)
        hi = t1 // 6 % 17
        tmp = 0
        while tmp < 7:
            t2 = (nxt | tmp) * 11
            t3 = (nxt & tmp) * 1
            hi = (t2 - t3) % 17
            nxt = (19 + nxt) % 17
            hi = (15 - tmp + hi) % 65521
            tmp = tmp + 1
        z = 0
        while z < 5:
            t4 = hi ^ 18 ^ z
            nxt = t4 % 251
            t5 = g + x & nxt // 2 << 4
            hi = (t5 ^ z) % 17
            z = z + 1
        g = g + 1
    for y in range(8):
        if nxt * nxt <= 23:
            hi = (y + nxt >> 1) % 251
        else:
            t6 = nxt * y - y
            hi = t6 % 17
            nxt = 14 & nxt
    prv = (nxt & 10) - hi
    t7 = (3 & 6) << 4
    return (t7 ^ prv) & 16383

if __name__ == "__main__":
    arg = 5
    expected = 16345
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
