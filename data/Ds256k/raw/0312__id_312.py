# Auto-extracted from ds_lt256k_500.jsonl
# record_id=312  entry=f  input='4'  output='22'  tokens=256833

def fn0(b):
    cnt = [494, 567, 523, 680]
    for t in range(7):
        t0 = (b ^ 20 ^ b + b) - b
        b = t0 & 8191
        cnt[t % 4] = (t ^ b) % 1009
    t1 = b * 11 - cnt[b % 4]
    t2 = t1 * (b ^ 13 ^ (14 | b))
    res = t2 % 4093
    buf = 0
    while buf < 12:
        res = buf - res & 511
        buf = buf + 1
    for acc in range(10):
        t3 = cnt[b % 4] & 5
        b = (res ^ t3) % 4093
    t4 = cnt[res % 4]
    t5 = b + t4 << 4
    v = t5 % 9973
    d = 0
    while d < 8:
        t6 = v | cnt[d % 4]
        res = t6 & 65535
        t7 = (d ^ 10) - 7
        res = (t7 - res) % 4093
        d = d + 1
    hi = 0
    while hi < 5:
        v = (v + v) % 251
        hi = hi + 1
    val = b >> 1
    t8 = cnt[val % 4] * 8
    t9 = val ^ cnt[val % 4]
    t10 = 13 + val | t8
    return t10 & (t9 | 5)

def fn1(b, g):
    cur = [322, 669, 28, 668]
    s = 11 << 3 ^ g
    for w in range(5):
        cur[s % 4] = s * w % 1009
        t0 = (g & 19) - (g + s)
        b = (t0 + b) % 1009
        t1 = s + cur[g % 4] + 4
        t2 = (g - s) * (w << 1) - t1
        g = t2 & 262143
    a = g + b - s
    if 2 + s > 43:
        t3 = 6 ^ 1
        t4 = t3 ^ 6 & g
        t5 = a // 3 & g
        a = t4 & t5
        s = b // 7
    else:
        if a * g < 56:
            cur[a % 4] = (12 - 11 - s) % 1009
            t6 = a >> 2
            t7 = t6 ^ 4 + a
            t8 = cur[s % 4]
            s = (t7 ^ t8) % 17
        else:
            t9 = 3 + s | g
            t10 = cur[s % 4]
            s = t9 - t10
            cur[a % 4] = ((s ^ 20) >> 1) % 1009
    u = 0
    while u < 6:
        for tmp in range(9):
            a = a + b & tmp
            t11 = 12 ^ s ^ tmp
            a = t11 % 17
            t12 = cur[a % 4]
            t13 = t12 ^ cur[b % 4]
            t14 = (19 | u) * b
            t15 = t14 * (t13 & a) ^ g
            g = t15 % 1009
        for t in range(10):
            cur[g % 4] = (u & 4 | s) % 1009
            t16 = cur[s % 4]
            t17 = cur[t % 4]
            t18 = t16 >> 1 & s
            t19 = b - 2 - t17
            cur[b % 4] = (t18 ^ t19) % 1009
            t20 = s + a ^ 13
            cur[u % 4] = t20 * s % 1009
        u = u + 1
    lo = (a ^ 20) + g
    return lo & b

def f(x):
    b = [89, 47, 93, 61, 53, 74, 84]
    t0 = b[x % 7]
    t1 = 3 | x
    t2 = t1 + (t0 | x)
    b[x % 7] = (t2 | 6) % 97
    for s in range(7):
        for buf in range(3):
            t3 = (3 & buf) * s
            b[s % 7] = t3 ^ x
        x = x * x % 65521
        x = s - x << 2 & 4095
    t4 = b[x % 7]
    t5 = t4 * x
    t6 = t5 - (14 + 14)
    aux = t6 & 2047
    if 12 - aux >= 49:
        aux = aux + aux
    y = 0
    while y < 9:
        x = (x * 8 - aux) % 9973
        for tot in range(10):
            aux = ((aux >> 3) + aux) % 1009
            t7 = (tot << 1) * (x - tot)
            t8 = t7 - (9 * x - 6)
            x = t8 & 32767
        y = y + 1
    t9 = aux & x
    t10 = x + aux
    t11 = t9 + (x - 19)
    t12 = t10 * (x - aux)
    t13 = t11 + t12 & 16383
    b[aux % 7] = t13 % 97
    t14 = b[x % 7] + 14 | aux
    t15 = (aux << 4) + b[aux % 7]
    t16 = (t14 | t15) & 8191
    t17 = b[x % 7] * 6
    x = fn1(t16, t17 & 511)
    aux = fn0(x * x + (x ^ 6) & 262143)
    t18 = b[aux % 7] & x
    b[x % 7] = (t18 ^ 6) % 97
    t19 = x % 4093 // 6
    t20 = (aux << 4) - 10
    return t19 & t20

if __name__ == "__main__":
    arg = 4
    expected = 22
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
