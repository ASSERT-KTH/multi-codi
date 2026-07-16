# Auto-extracted from ds_lt256k_500.jsonl
# record_id=99  entry=f  input='7'  output='41919'  tokens=254459

def fn0(c):
    m = [95, 48, 67, 62, 48, 51]
    b = c - 12
    tmp = (c - b) * c % 1009
    m[c % 6] = tmp & 3
    hi = 0
    while hi < 11:
        a = 0
        while a < 6:
            t0 = 7 * 8 & hi
            m[tmp % 6] = (t0 + tmp) % 97
            t1 = (hi & 3) - a - 14
            m[c % 6] = (t1 ^ tmp) % 97
            c = ((a | c) + hi) % 65521
            a = a + 1
        hi = hi + 1
    lo = c - 6
    v = 0
    while v < 10:
        for idx in range(11):
            t2 = m[b % 6]
            t3 = m[lo % 6]
            lo = (t2 - t3) % 1009
            t4 = 13 ^ m[v % 6]
            tmp = t4 + (c | tmp) << 3 & 262143
        for cnt in range(10):
            t5 = 6 * tmp * (cnt | b) % 1009
            m[v % 6] = t5 % 97
        v = v + 1
    return (m[c % 6] + lo) % 17

def fn1(m, c):
    q = [62, 1, 60, 9]
    t0 = 16 * c * (m * m)
    cur = t0 & (7 << 3) - c * m
    t1 = cur + cur + c % 1009
    e = t1 & 1023
    acc = cur >> 2 & 8191
    c = (e - cur) % 17
    buf = 0
    while buf < 2:
        hi = 0
        while hi < 12:
            q[hi % 4] = (buf | c) % 97
            hi = hi + 1
        t2 = acc % 97 + acc // 5 - buf
        cur = t2 % 17
        buf = buf + 1
    if acc << 2 == 58:
        for p in range(2):
            t3 = e & q[m % 4]
            q[e % 4] = (p * 5 ^ t3) % 97
            t4 = (cur ^ acc) // 4 // 3
            q[e % 4] = t4 % 97
            e = cur - 20 - m + e & 65535
        idx = 0
        while idx < 6:
            m = (e % 251 ^ m) % 17
            cur = e + idx & (e & 6)
            cur = e * cur % 97
            idx = idx + 1
    t5 = m + 9 >> 4 ^ c
    return t5 - cur & 4095

def f(x):
    for w in range(6):
        x = (1 ^ w) - x & 1023
        x = (x + 10) % 9973
    res = 0
    while res < 9:
        for v in range(7):
            x = (v * 16 | x) & 32767
        for z in range(9):
            t0 = 6 ^ res | x
            x = t0 % 9973
            t1 = 10 + res - res
            t2 = t1 - x * 1
            x = t2 % 65521
        res = res + 1
    b = x + x
    acc = x // 4 << 1
    e = 12 - acc
    if b * x <= 45:
        idx = 0
        while idx < 7:
            t3 = (idx ^ x) * (e % 65521)
            x = (t3 + (e % 9973 + acc)) % 9973
            t4 = idx - x ^ 2
            x = t4 + e & 262143
            b = ((e % 65521 >> 4) - b) % 9973
            idx = idx + 1
    else:
        acc = fn0((11 | acc) + b & 262143)
        for c in range(7):
            t5 = (b & acc) + e
            b = t5 + 3 & 4095
    x = 3 * e
    buf = 0
    while buf < 5:
        for t in range(12):
            acc = (x | t) & 1023
            t6 = (x | 2) ^ b
            e = t6 * e & 255
        d = 0
        while d < 9:
            t7 = buf + b
            t8 = t7 - (b + b)
            t9 = t8 * buf - x
            x = t9 & 65535
            d = d + 1
        t10 = b + acc
        t11 = t10 - (x + x)
        t12 = (b & 11) * b
        x = t11 * t12 & 262143
        buf = buf + 1
    t13 = 16 | 10
    t14 = t13 - (acc - x)
    return t14 % 65521

if __name__ == "__main__":
    arg = 7
    expected = 41919
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
