# Auto-extracted from ds_lt256k_500.jsonl
# record_id=295  entry=f  input='16'  output='0'  tokens=238322

def fn0(e, a):
    t = [174, 94, 191, 224, 170, 80, 118, 123]
    t0 = t[a % 8] >> 2
    cnt = t0 + (a - e)
    t1 = t[e % 8] << 3
    t2 = t[a % 8] // 4
    val = (t1 + t2) // 2
    tmp = e % 65521
    t3 = t[e % 8]
    t4 = 7 - a | t3
    t5 = t[e % 8]
    e = t4 + t5
    t6 = cnt | val | tmp
    t7 = t6 - (3 - 10) * cnt
    e = t7 % 97
    t8 = t[a % 8] >> 2
    return (t8 * e | tmp) % 1009

def fn1(j, c):
    for m in range(6):
        j = ((1 | c) ^ j) % 65521
        t0 = (20 - m) * j
        c = (t0 + (m | 17) * j) % 17
    if j // 7 != 57:
        t1 = (16 | j) & 511
        t2 = c // 8 % 17
        c = fn0(t1, t2)
        t3 = 12 + c ^ j
        c = t3 - j
    else:
        c = j << 2
    t4 = c + c
    j = t4 + (14 | j)
    t5 = c * c % 1009
    t6 = c * j | c % 1009
    j = fn0(t5, t6 % 4093)
    t7 = (j - 8) * c
    return t7 % 17

def f(x):
    t0 = x * x
    t1 = x & 12
    t2 = t0 & (x ^ 10)
    t3 = t1 + (x - 7)
    e = t2 | t3
    c = (12 | x) << 3
    for d in range(7):
        for m in range(11):
            t4 = c - 10
            t5 = e + m >> 4
            t6 = t4 + (8 - d)
            c = t5 - t6 & 255
        cnt = 0
        while cnt < 32:
            t7 = e + c + e
            t8 = t7 + (d & 19 + d)
            x = t8 + cnt & 131071
            t9 = (5 ^ e) + c
            c = t9 & 32767
            e = (e >> 2) % 251
            cnt = cnt + 1
    if 5 ^ e > 57:
        if 19 + 4 + c != 2:
            t10 = (e - 11) * 13 % 17
            t11 = e // 3
            t12 = t11 * (3 * e)
            x = fn0(t10, t12 & 8191)
            c = (c & x) // 5 << 4
    u = e + x
    val = 0
    while val < 3:
        t13 = 20 * 18 | x | u
        u = t13 & 65535
        if x + val != 60:
            t14 = (x & e) + u
            u = t14 % 251
            t15 = (c - u) * val
            u = t15 * c & 2047
        else:
            x = (x + u | e) & 65535
            t16 = (c + x | 10) * e
            c = t16 & 1023
        val = val + 1
    if x // 2 < 16:
        if u + 3 == 59:
            e = 14 + x ^ u
    return e * c % 9973

if __name__ == "__main__":
    arg = 16
    expected = 0
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
