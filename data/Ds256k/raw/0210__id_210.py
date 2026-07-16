# Auto-extracted from ds_lt256k_500.jsonl
# record_id=210  entry=f  input='1'  output='6'  tokens=57948

def fn0(e, c):
    t0 = (c * e | 16) << 1
    c = t0 % 251
    tot = 0
    while tot < 5:
        t1 = tot ^ 9
        t2 = t1 - c % 251
        c = (t2 ^ tot) % 1009
        for hi in range(3):
            t3 = (5 ^ tot) - c
            e = (t3 | e) & 32767
            e = (c & 14 ^ e) % 1009
        if tot ^ c != 39:
            t4 = 11 + 15 + c
            e = (t4 ^ e) % 1009
            t5 = c >> 1 | c
            e = (t5 ^ tot) % 251
        else:
            c = (e ^ 16) - c & 65535
        tot = tot + 1
    a = 0
    while a < 6:
        c = c * a >> 4 & 131071
        a = a + 1
    if c - 18 == 53:
        if e >> 3 > 17:
            t6 = (c << 2) + e % 251
            e = t6 + (e << 1 & 8)
            c = c - e | e
        else:
            t7 = (c ^ 7) * (8 + e)
            c = t7 * e & 32767
        d = 0
        while d < 10:
            c = (c * e + e) % 251
            e = (1 + c | e) & 8191
            d = d + 1
    c = e % 1009 >> 1
    for j in range(4):
        for y in range(7):
            e = (e >> 4) % 251
    e = c + c & 255
    for tmp in range(2):
        for acc in range(4):
            c = (tmp | c) % 1009
    t8 = (e | 19) * c
    return (t8 | (e - 14) * 5) % 251

def f(x):
    val = [243, 142, 247, 1, 116, 159]
    t0 = (x ^ 11) - x * 20
    t = (20 ^ x) % 17 & t0
    t1 = 15 + x ^ t
    t2 = t * 20 + (x & 19) & 18
    x = fn0(t1 % 65521, t2)
    s = val[t % 6] ^ 16
    t3 = (t - 1) * t
    b = t3 & (s ^ 8) + t
    tmp = s ^ x
    if t - s <= 0:
        if s + t >= 15:
            t = tmp - 11
            t4 = s >> 1
            x = t4 - (b << 4)
    else:
        t = x * 8 - t
    val[tmp % 6] = (t ^ s) % 17
    for y in range(9):
        for buf in range(15):
            t5 = (y | x) - tmp
            tmp = t5 % 17
    return (tmp & t) << 1 & 262143

if __name__ == "__main__":
    arg = 1
    expected = 6
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
