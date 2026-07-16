# Auto-extracted from ds_lt256k_500.jsonl
# record_id=260  entry=f  input='11'  output='2525'  tokens=84080

def rec(n, a):
    if n <= 0:
        return a
    m = (n - a) % 9973
    m = m // 2 % 251
    m = (m - a) % 251
    t0 = ((n >> 3) - 9 ^ a) % 251
    return rec(n - 1, t0)

def fn0(e, g):
    hi = [914, 456, 257, 892]
    t0 = hi[e % 4]
    t1 = e + g
    t2 = hi[g % 4]
    t3 = t1 * (10 + t0)
    t4 = 8 + g | t2
    hi[g % 4] = (t3 + t4) % 1009
    t5 = hi[g % 4] * g
    t6 = (2 | g) + t5 - e
    cur = t6 % 1009
    if g ^ cur == 54:
        for j in range(5):
            e = ((7 + 20) * g ^ e) % 1009
            t7 = 12 << 4
            t8 = t7 * (j + j)
            hi[e % 4] = (t8 | cur) % 1009
        cur = (e << 3) - g
    else:
        acc = 0
        while acc < 4:
            t9 = (hi[cur % 4] | e) * 12
            g = t9 * g % 4093
            hi[cur % 4] = (e * e + acc | 2) % 1009
            hi[g % 4] = (cur ^ g) % 1009
            acc = acc + 1
    t10 = g >> 1 ^ cur
    e = t10 * ((cur - e) // 6) & 262143
    if 12 | e >= 6:
        g = (e - 5) % 1009 >> 1
    g = e * g % 1009
    if g - hi[g % 4] < 45:
        t11 = (cur | 12) - cur
        g = t11 % 4093
    else:
        for a in range(9):
            t12 = cur - g >> 3
            t13 = cur + e ^ a
            t14 = (t12 + t13) % 4093
            hi[e % 4] = t14 % 1009
            t15 = (2 ^ 18) * 10
            t16 = t15 * (2 - a ^ 15) ^ e
            hi[e % 4] = t16 % 1009
    return e * g + cur & 2047

def fn1(d, a):
    for b in range(7):
        a = (d * d ^ b) % 9973
    g = 10 + 6 ^ a
    for aux in range(9):
        g = a // 7 - aux & 255
        a = (aux * 11 ^ d) & 1023
    p = 0
    while p < 8:
        t0 = (2 ^ g) // 8
        t1 = (t0 >> 2) + d
        d = t1 & 16383
        d = d & g
        p = p + 1
    if g & d >= 41:
        for m in range(3):
            g = (g + d) % 65521
    t2 = a + a
    t3 = t2 - (d & 8)
    t4 = d - 10 - d
    t5 = (t3 & t4) - g
    return t5 & 262143

def f(x):
    cnt = [829, 425, 757, 241, 361]
    m = x * x
    t0 = cnt[m % 5] - m
    b = (m - 4) * t0
    for w in range(8):
        v = 0
        while v < 12:
            t1 = cnt[v % 5]
            t2 = 17 - t1
            t3 = t2 * (x << 1)
            cnt[b % 5] = t3 % 1009
            cnt[v % 5] = (x * m * 19 | m) % 1009
            m = m // 4 % 17
            v = v + 1
        t4 = (5 + b) * (4 * x)
        t5 = t4 + (w + w + 3)
        cnt[b % 5] = t5 % 4093 % 1009
    cnt[x % 5] = x * x ^ m
    b = b + b & b
    if x * b < 31:
        t6 = cnt[b % 5]
        t7 = (x + t6) * x
        m = t7 ^ 6
    t8 = cnt[b % 5]
    t9 = 4 * m | t8
    t10 = (m + m + x) % 9973
    x = fn0(t9 % 17, t10)
    t11 = 9 * cnt[b % 5]
    m = (t11 >> 2) - b
    t12 = 7 * m % 4093
    t13 = cnt[b % 5]
    return t12 + t13 & 131071

if __name__ == "__main__":
    arg = 11
    expected = 2525
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
