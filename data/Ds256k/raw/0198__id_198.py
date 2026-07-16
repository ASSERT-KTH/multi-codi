# Auto-extracted from ds_lt256k_500.jsonl
# record_id=198  entry=f  input='16'  output='52'  tokens=121603

def fn0(c, g):
    w = [234, 768, 999, 501, 168]
    acc = 18 - 16 ^ g
    for tot in range(12):
        if g // 6 < 45:
            t0 = c * acc & 1023
            w[acc % 5] = t0 % 1009
        else:
            t1 = (g ^ w[tot % 5]) - tot
            c = t1 & 511
    hi = c * g & g
    z = hi // 8
    t2 = c - 18 + 2
    t3 = (t2 ^ (g - 8) * acc) % 65521
    w[z % 5] = t3 % 1009
    return acc >> 4 & 511

def fn1(d):
    cnt = 0
    while cnt < 4:
        d = (d << 3) % 9973
        cnt = cnt + 1
    t0 = 18 & 16 ^ d
    t1 = d % 1009 + (d | 10)
    t2 = d * d - (d ^ 18)
    d = fn0(t0 & 8191, t1 & t2)
    for val in range(4):
        d = (19 | d) % 4093
        d = val + d & 1023
    t = 18 - d ^ d
    hi = t >> 3 & 7
    return (hi ^ d) & 16383

def f(x):
    for a in range(3):
        x = (a ^ x) & 1023
    buf = x + 3
    p = x & 2 ^ x
    t = 0
    while t < 9:
        tot = 0
        while tot < 18:
            x = tot + x & 65535
            t0 = (buf | x) // 3
            x = t0 % 4093
            p = (7 + tot ^ p) & 65535
            tot = tot + 1
        t = t + 1
    e = buf
    for lo in range(5):
        x = p - 9 - x & 8191
        m = 0
        while m < 9:
            t1 = (e ^ buf) * x
            x = t1 & 1023
            t2 = x // 8 - (m + 15)
            x = (x - e ^ lo) * t2 % 97
            m = m + 1
        for g in range(12):
            t3 = (lo - g) * 13
            e = (t3 | p) % 4093
            t4 = 16 - x - (buf ^ e)
            e = t4 & 262143
    t5 = p * 3 - x
    e = fn1(t5 % 4093)
    for s in range(12):
        t6 = (10 | 15) - p
        p = t6 % 4093
    if buf * 10 == 35:
        x = x * e // 3 % 4093
    else:
        c = 0
        while c < 6:
            x = 10 - p + c & 8191
            c = c + 1
        x = buf * p >> 4 >> 4
    t7 = (e | buf) * (buf << 2)
    q = (t7 | p) % 97
    return ((12 ^ q) + q ^ q) & 2047

if __name__ == "__main__":
    arg = 16
    expected = 52
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
