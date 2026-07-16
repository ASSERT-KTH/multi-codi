# Auto-extracted from ds_lt256k_500.jsonl
# record_id=75  entry=f  input='9'  output='626'  tokens=179290

def rec(n, a):
    if n <= 0:
        return a
    t0 = n >> 3
    t1 = t0 + (13 + n)
    m = (t1 | a) & 8191
    t2 = n * (n & 6) ^ a
    q = t2 % 9973
    a = (n ^ a) & 2047
    t3 = 20 - n + a
    return rec(n - 1, t3 & 8191)

def fn0(m, a):
    cnt = [578, 541, 472, 327]
    for cur in range(9):
        b = 0
        while b < 9:
            t0 = (b | m) // 7
            cnt[m % 4] = t0 % 1009
            cnt[m % 4] = (15 | a) % 1009
            t1 = m >> 4
            t2 = t1 ^ b * b
            t3 = cnt[cur % 4]
            cnt[a % 4] = (t2 - t3) % 1009
            b = b + 1
        if cnt[cur % 4] + a <= 52:
            t4 = cur - 12
            t5 = t4 * (cur ^ a)
            a = t5 & 65535
        else:
            t6 = m * a * a & 32767
            cnt[cur % 4] = t6 % 1009
            t7 = a // 4 % 17 - m
            a = t7 % 251
        m = ((m << 2 ^ 20) >> 2) % 17
    t8 = a | cnt[m % 4]
    buf = t8 - 20
    tot = 10 & m
    t9 = a * cnt[tot % 4]
    t10 = (buf >> 1) - t9 >> 4 & 255
    a = rec(58, t10)
    idx = m - a
    t11 = cnt[a % 4]
    t12 = t11 + cnt[m % 4]
    g = (t12 + buf) % 251
    t13 = m | cnt[buf % 4]
    t14 = 6 + g & g
    t15 = t14 + ((17 & g) - t13)
    return t15 % 17

def f(x):
    tmp = [129, 25, 6, 180, 107, 249, 196]
    t0 = tmp[x % 7]
    t1 = x - 5
    s = t1 + (t0 ^ x)
    e = (s << 1) + 3
    acc = (x | s) & 4 | e
    j = x | e
    t2 = tmp[s % 7]
    j = x - 17 ^ t2
    t3 = tmp[e % 7]
    t4 = acc + t3
    j = t4 - 13 * s
    for m in range(141):
        t5 = (18 - j ^ x) >> 4
        x = t5 & 262143
        t6 = x * 19 - m
        acc = t6 & 262143
        if acc ^ j < 45:
            x = (acc * acc - 7 ^ x) % 9973
            t7 = tmp[m % 7]
            t8 = x * 19 + x
            t9 = 14 + 6 & t7
            x = (t8 ^ t9) & 131071
        else:
            t10 = tmp[j % 7]
            t11 = m * t10 - 4
            j = t11 % 9973
            t12 = 20 | acc | m
            s = t12 % 251
    return (20 * acc - x) % 9973

if __name__ == "__main__":
    arg = 9
    expected = 626
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
