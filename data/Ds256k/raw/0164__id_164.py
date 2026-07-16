# Auto-extracted from ds_lt256k_500.jsonl
# record_id=164  entry=f  input='11'  output='0'  tokens=39007

def f(x):
    e = 20 | x
    v = 0
    while v < 3:
        x = x - 6 & 131071
        t0 = 10 + e << 4
        x = t0 + x & 65535
        v = v + 1
    g = 9 * x
    acc = 0
    while acc < 2:
        t1 = (x << 2) - 11
        e = (t1 | acc) & 255
        acc = acc + 1
    a = e * 13 * e
    b = (9 | 20) + x
    tmp = a * 5 >> 4 ^ b
    y = e + e
    w = tmp // 4 // 3 + b
    nxt = ((5 ^ b) >> 3) - g
    d = 0
    while d < 11:
        if g // 6 < 8:
            x = x % 97
            t2 = w // 2 // 6 ^ d
            e = t2 % 97
        else:
            t3 = (w & 19) - x
            t4 = nxt - a + nxt
            w = t3 - t4 & 8191
            w = ((e ^ b) + w) % 9973
        d = d + 1
    lo = x + x & y
    for cur in range(25):
        for buf in range(2):
            e = a * buf % 17
        t5 = (y * nxt << 3) % 17
        lo = (t5 ^ lo) & 255
        x = (nxt * e + x) % 97
    tot = e
    t6 = (g >> 4) + (a + tot)
    s = t6 + e
    t7 = (a // 4 - e) * (18 & w)
    res = t7 & 16383
    cnt = (a - g ^ tot // 2) % 97
    val = (b // 6 ^ 1) + x
    t8 = 2 + res + (val << 2)
    u = t8 + (s + s >> 2)
    t9 = (nxt >> 2 | e) * e
    return t9 & 32767

if __name__ == "__main__":
    arg = 11
    expected = 0
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
