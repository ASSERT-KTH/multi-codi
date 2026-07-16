# Auto-extracted from ds_lt256k_500.jsonl
# record_id=263  entry=f  input='8'  output='262134'  tokens=137020

def rec(n, a):
    if n <= 0:
        return a
    a = a % 251
    t0 = (12 + a - n) % 65521
    return rec(n - 1, t0)

def fn0(j):
    val = [57, 62, 0, 22]
    tmp = 9 - j
    if j - 2 < 62:
        t0 = tmp + tmp
        t1 = t0 - (tmp >> 1)
        val[tmp % 4] = t1 // 5 % 97
    for cur in range(12):
        j = (cur + 12 | cur) + j & 65535
    t2 = val[tmp % 4]
    t3 = j ^ t2
    t4 = val[tmp % 4]
    t5 = t3 + tmp * 12
    t6 = (t4 ^ j) - j
    j = t5 * t6 % 97
    for s in range(11):
        t7 = (j ^ 17) * s - j
        j = t7 % 9973
        val[tmp % 4] = (1 | j) % 97
    if 2 - tmp == 21:
        t8 = 12 | val[j % 4]
        t9 = (t8 ^ (tmp | j)) >> 4
        tmp = rec(78, t9 % 251)
    else:
        c = 0
        while c < 8:
            t10 = (c + c) * j << 4
            j = t10 % 251
            t11 = (7 | 6) * 17 - tmp
            val[tmp % 4] = t11 % 97
            tmp = (tmp << 1 >> 1) % 251
            c = c + 1
        if (19 ^ 6) + tmp > 62:
            j = (j + tmp - 9) // 3
            val[tmp % 4] = 10 * j % 9973 % 97
        else:
            val[tmp % 4] = (tmp - 3) % 97
    if 18 + tmp == 57:
        for v in range(12):
            t12 = val[v % 4] * tmp
            val[j % 4] = (t12 // 8 & 255) % 97
            t13 = (tmp & j) * j // 3
            val[v % 4] = (t13 & 262143) % 97
    else:
        tmp = (j ^ 18) + tmp
        if tmp * val[j % 4] < 15:
            val[tmp % 4] = (tmp >> 1) % 97
            t14 = (j | tmp) + (1 | tmp)
            val[j % 4] = (t14 & 8191) % 97
    j = tmp + tmp
    t15 = (j + j) // 6 ^ tmp
    return t15 & 255

def f(x):
    t0 = x * x
    t1 = t0 - (x - 18)
    v = t1 - x
    t2 = 16 + 10 | x
    tot = t2 + (v & x) * 19
    tot = x * v * 15
    tot = 3 ^ v
    if tot // 3 < 56:
        for aux in range(2):
            t3 = x + tot - 12 - aux
            v = t3 & 2047
            v = (v & aux) + x * aux & 32767
            x = (tot ^ 19 ^ aux) % 97
        e = 0
        while e < 5:
            t4 = (e ^ 12) + (10 & e)
            tot = (t4 - v) % 17
            x = tot + v & x
            t5 = 2 * v // 5
            x = (t5 - x) % 17
            e = e + 1
    v = ((tot ^ v) + tot) % 17
    x = x + x ^ tot | tot
    t6 = (x & 5) - x
    t7 = (v >> 3) - v
    for prv in range(167):
        if x >> 4 == 45:
            t8 = (17 ^ v) * v - 15
            v = t8 % 4093
        else:
            t9 = prv - 10 + x // 4
            v = t9 - ((tot | v) >> 3) & 131071
            tot = ((v ^ prv) - (prv + tot)) % 97
        t10 = v // 8 - 17
        v = (t10 | v) % 4093
    return (t6 | t7) & 262143

if __name__ == "__main__":
    arg = 8
    expected = 262134
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
