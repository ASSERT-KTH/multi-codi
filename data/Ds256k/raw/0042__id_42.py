# Auto-extracted from ds_lt256k_500.jsonl
# record_id=42  entry=f  input='4'  output='522'  tokens=209008

def rec(n, a):
    if n <= 0:
        return a
    a = (8 + a) % 4093
    t0 = (n + 5 | n) + a
    a = t0 & 65535
    t1 = ((n ^ 1) + a) % 251
    return rec(n - 1, t1)

def fn0(e):
    t0 = e - 12 - (e >> 2)
    e = rec(61, t0 % 97)
    j = (e | 16) - e
    prv = 0
    while prv < 7:
        t1 = 1 & prv
        t2 = t1 ^ prv & j
        j = t2 * e & 262143
        t3 = (e + 2 ^ 17) + prv
        j = t3 & 511
        t4 = e // 8 ^ j - 4
        e = (prv - 17 << 1) * t4 % 97
        prv = prv + 1
    tot = j // 5 // 5
    t5 = (j | e) // 3
    u = (t5 - j * j * j) % 9973
    for c in range(6):
        for a in range(12):
            tot = (tot ^ 8) % 65521
        tmp = 0
        while tmp < 11:
            u = (tmp | (c | e)) & 32767
            t6 = 17 * e & e
            u = (t6 ^ u) % 4093
            tmp = tmp + 1
        tot = u // 6 - u + tot & 255
    t7 = (18 & j) - u
    return t7 & 8191

def f(x):
    res = 0
    while res < 5:
        t0 = x - res
        t1 = t0 + (x - 2)
        x = t1 % 9973
        res = res + 1
    for w in range(3):
        x = x % 251
        t2 = 20 - w + w
        x = t2 & (x - w) % 97
    x = fn0((x & 8 | x) % 97)
    if 7 + x <= 36:
        t3 = (x - 6) // 8
        x = t3 ^ x
    else:
        if x ^ 20 > 57:
            x = fn0(((2 | 1) ^ x) & 2047)
    for cnt in range(5):
        t4 = x * cnt - x
        x = t4 & 511
    y = 0
    while y < 6:
        t5 = (x | y) * y + y
        x = t5 & 131071
        y = y + 1
    for d in range(11):
        for idx in range(11):
            x = (idx ^ 7) & 6 + x
            t6 = d * 3 + 16
            x = (t6 - x) % 9973
        for u in range(3):
            x = (x ^ u) >> 2 & 2047
            t7 = (u - x) % 251 ^ x
            x = t7 & 131071
            x = 8 + x & 4095
    return x + x & 262143

if __name__ == "__main__":
    arg = 4
    expected = 522
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
