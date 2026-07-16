# Auto-extracted from ds_lt256k_500.jsonl
# record_id=88  entry=f  input='16'  output='16'  tokens=137624

def f(x):
    j = x << 4 | x + x
    if x - j == 8:
        if x ^ j != 1:
            x = x << 1
        else:
            t0 = x - 12 - x
            t1 = x * j - x
            x = t0 + t1
            j = (j + x | x & 12) + 8
    else:
        x = 20 ^ j
        j = x & 4
    tot = j * x % 4093
    t2 = (tot + x) * (j + x)
    y = ((tot | j) - 15 + t2) % 97
    buf = x ^ 5 ^ (y ^ 12)
    t = y // 2
    for d in range(5):
        t3 = tot * y & d * j
        y = t3 + (15 + 9) & 32767
    b = 0
    while b < 4:
        for a in range(48):
            t4 = buf + j
            t5 = t4 + (y << 3)
            t = (t5 | t) & 8191
            t = t + 3 & 32767
        t6 = 16 - b
        t7 = t6 * (b + x)
        tot = t7 % 4093
        b = b + 1
    cur = 0
    while cur < 2:
        for tmp in range(10):
            t8 = ((tmp << 3) + 3 << 1) + x
            x = t8 % 4093
            buf = ((9 ^ y) - tmp) % 4093
        t9 = (tot & buf) - y
        y = t9 & 131071
        cur = cur + 1
    t10 = y * buf | tot
    w = t10 % 4093
    cnt = t + x << 1
    nxt = cnt + 18
    e = w & tot ^ j
    for res in range(8):
        tot = j // 8 - res & 262143
    s = (e >> 3) * j & 65535
    g = 0
    while g < 6:
        for acc in range(2):
            tot = (12 + x | acc) % 4093
            t11 = 6 - g & (g & nxt)
            t12 = t11 + (11 | buf) % 4093
            w = (t12 | acc) % 97
            t13 = (x * 16 + cnt) // 6
            nxt = (t13 + nxt) % 97
        g = g + 1
    if x // 4 >= 7:
        u = 0
        while u < 9:
            t14 = nxt - e + 8 * w
            t = t14 + 17 - u & 511
            u = u + 1
        t15 = 6 & j & 12
        x = t15 * (e >> 2 << 1)
    t16 = (w << 4) - e * j
    return t16 % 97

if __name__ == "__main__":
    arg = 16
    expected = 16
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
