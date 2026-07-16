# Auto-extracted from ds_lt256k_500.jsonl
# record_id=124  entry=f  input='16'  output='2043'  tokens=19598

def fn0(m, d):
    t = (d | m) - d
    t0 = (t - 3) * (t + d) - t
    cnt = t0 & 2047
    if cnt - d == 48:
        d = d | m
    else:
        cnt = t + m
        t1 = cnt ^ 5
        cnt = t1 & (m | 18)
    if t // 2 >= 4:
        a = 0
        while a < 2:
            t2 = d - m >> 2 >> 2 | a
            cnt = t2 % 1009
            cnt = (7 + cnt) % 65521
            d = 3 & d
            a = a + 1
        if 9 + cnt > 34:
            cnt = (m >> 1) * 13
        else:
            d = cnt - m
            t3 = t - cnt ^ 16
            d = t3 & 13
    else:
        nxt = 0
        while nxt < 9:
            t4 = nxt << 4 ^ d
            t = t4 % 1009
            t5 = t + t ^ m
            m = t5 & 511
            nxt = nxt + 1
        cnt = d * 3 % 251
    t6 = cnt | m
    t7 = t6 * (d % 251)
    m = t7 & 8191
    if t % 65521 <= 57:
        t = m >> 2
        c = 0
        while c < 11:
            t = (t + 18) % 17
            cnt = (3 | cnt) % 17
            t8 = d * t + (9 & c)
            m = t8 & t
            c = c + 1
    else:
        m = (m & cnt) - 10
        d = (17 ^ 12) + d
    t9 = d + d << 4
    t10 = (3 ^ t) - cnt
    m = (t9 ^ t10) & 511
    t11 = (d << 1) - (m + m)
    return (t11 ^ t) % 17

def fn1(d, c):
    t0 = (d ^ c) + c % 97
    cur = t0 & (d + 18) * c
    if c % 4093 == 40:
        t1 = (d - 9) % 97
        t2 = cur + c & 9
        cur = fn0(t1, t2)
        for hi in range(12):
            c = c * c % 97
    if 1 | c >= 43:
        t3 = d - 15 - (cur - 6)
        t4 = ((13 ^ c) % 4093 ^ 14) % 17
        c = fn0(t3 & 16383, t4)
    t5 = c % 17 + (cur >> 1)
    c = t5 - ((c | 15) + cur)
    return cur * d & d - 11

def f(x):
    t0 = x - 11 & 1023
    t1 = (x | 9) - (11 - 17) & 4095
    x = fn1(t0, t1)
    j = x % 65521
    u = 18 ^ 12 ^ x
    t2 = j + x >> 4 & 1023
    t3 = (u - x) % 251
    j = fn0(t2, t3)
    if 6 | u < 11:
        j = u * 8
    for buf in range(25):
        if u & j < 2:
            t4 = (u ^ 16 | u) >> 2
            j = (t4 - buf) % 251
            x = (x << 1) - u & 4095
        if 15 * x != 21:
            t5 = (u | x) << 2 ^ j
            j = t5 % 251
            t6 = buf + x ^ buf
            x = t6 & 131071
    w = ((10 | j) + j) % 1009
    t7 = w ^ u
    p = t7 ^ w << 2
    t8 = x + 19 | p
    return t8 % 4093

if __name__ == "__main__":
    arg = 16
    expected = 2043
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
