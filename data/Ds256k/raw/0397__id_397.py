# Auto-extracted from ds_lt256k_500.jsonl
# record_id=397  entry=f  input='5'  output='2'  tokens=107164

def fn0(d):
    for j in range(6):
        d = d & 13
        if d + d != 27:
            d = (12 | d) % 4093
            t0 = (j - 12) * d // 8
            d = t0 % 17
        else:
            t1 = d // 7 - d
            d = (t1 + (14 + j - 10)) % 4093
            t2 = j ^ 11 ^ j
            d = (t2 - d) % 4093
        t3 = (19 ^ j) + d
        d = t3 % 1009
    w = (d ^ 20) >> 1
    c = d * w & 255
    t4 = c * w
    hi = t4 & (w & 15)
    if d & 20 >= 12:
        aux = 0
        while aux < 11:
            t5 = c // 6 * (w % 4093)
            t6 = t5 ^ (11 + aux) * (hi - d)
            d = t6 % 4093
            t7 = d % 4093 ^ d
            t8 = t7 - d ^ aux
            hi = t8 % 1009
            t9 = w * d | 15
            w = t9 % 1009
            aux = aux + 1
    else:
        u = 0
        while u < 5:
            t10 = (w | c) + d
            d = t10 & 262143
            t11 = w & c ^ c | hi
            hi = t11 % 4093
            c = (w // 6 >> 4 ^ c) % 4093
            u = u + 1
        hi = (d ^ c) & c
    hi = 9 - d + w
    w = (hi % 4093 | c) >> 2
    w = hi - w
    t12 = 14 - hi
    t13 = t12 + (hi << 3)
    return (t13 ^ hi) & 8191

def f(x):
    x = fn0(((x | 4) ^ x) % 17)
    t0 = (8 ^ 16) + x
    t1 = t0 | (x >> 1) // 4
    x = fn0(t1 & 262143)
    cnt = 4 * 4 + x + 5
    for v in range(43):
        for g in range(5):
            t2 = (13 & 19) - x
            cnt = (t2 + g) % 4093
            t3 = x - v ^ x
            x = t3 % 65521
        if 12 & cnt == 12:
            t4 = (cnt * cnt & (x & cnt)) << 2
            cnt = t4 & 8191
    return ((x & cnt) >> 2) % 4093

if __name__ == "__main__":
    arg = 5
    expected = 2
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
