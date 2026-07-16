# Auto-extracted from ds_lt256k_500.jsonl
# record_id=92  entry=f  input='6'  output='239'  tokens=254835

def rec(n, a):
    if n <= 0:
        return a
    if a | 1 != 44:
        p = 0
        while p < 7:
            t0 = a * a
            t1 = t0 * (a >> 2)
            a = t1 % 4093
            t2 = a + a & a - n
            a = (t2 - (18 - 10)) % 9973
            a = n * a % 4093
            p = p + 1
    t3 = n | 5 | a
    t = t3 % 4093
    t4 = n - 15 + (n ^ t)
    t5 = (t4 | n | a) % 97
    return rec(n - 1, t5)

def fn0(e, c):
    t0 = c + c + 8 & 16383
    c = rec(59, t0)
    prv = c * e & 32767
    s = (prv - c) * e % 251
    if 5 * c == 49:
        prv = 5 | 11 | prv
        if prv ^ c <= 1:
            prv = 1 ^ 19 ^ prv
        else:
            s = prv - c
            t1 = c * s - (c - e)
            t2 = t1 * ((prv - s) * s)
            e = t2 % 97
    else:
        t3 = prv ^ 14
        prv = t3 - (e - 2)
    t4 = (s | 20) * (c & prv)
    t5 = (e + 7) // 4 - t4
    c = rec(66, t5 & 16383)
    buf = 0
    while buf < 4:
        s = (12 ^ buf) * s % 65521
        s = s + c & 32767
        buf = buf + 1
    t6 = (e + c) * 4
    t7 = 9 + c + 3
    c = rec(83, t6 & t7)
    for b in range(9):
        s = (e ^ prv | s) & 4095
        tot = 0
        while tot < 5:
            t8 = (15 | e) - (4 + c)
            e = t8 & 16383
            t9 = (c & 8) - tot
            s = t9 % 251
            t10 = b + e ^ c + c
            s = (t10 % 65521 | tot) % 65521
            tot = tot + 1
        z = 0
        while z < 8:
            e = e & z
            t11 = 11 + 12
            t12 = t11 - (b + 18)
            c = (t12 + c) % 251
            t13 = b * s | z * b
            s = t13 & 32767
            z = z + 1
    t14 = s + c
    t15 = t14 - (s ^ prv)
    return t15 & 32767

def f(x):
    v = [202, 626, 337, 1006]
    t0 = 14 * (10 ^ x)
    y = t0 * x
    t1 = y // 2 >> 1
    nxt = t1 * y % 251
    t2 = x - v[nxt % 4]
    buf = t2 | nxt - x
    for cnt in range(32):
        for idx in range(12):
            nxt = ((y % 251 >> 1) + idx) % 251
        t3 = nxt * nxt + cnt
        buf = t3 & 131071
        t4 = v[x % 4] >> 3
        t5 = t4 ^ v[y % 4] + x
        v[cnt % 4] = t5 % 1009
    for res in range(4):
        x = res * nxt % 9973
    w = x + v[y % 4] - x
    prv = 0
    while prv < 7:
        if 4 * x <= 28:
            buf = w * x + prv & 16383
            v[x % 4] = (w + prv) % 1009
        prv = prv + 1
    if v[y % 4] // 3 < 45:
        t6 = nxt * y * (w * 17) + y
        nxt = t6 % 251
    t7 = (w + y) % 9973
    x = rec(48, t7)
    lo = 15 + y
    u = 11 << 1 ^ buf
    for g in range(10):
        if 6 ^ buf == 11:
            t8 = v[x % 4]
            t9 = (nxt - g) * t8
            t10 = buf + g | 10
            lo = (t9 ^ t10) & 131071
    t11 = (buf >> 4) + lo
    t12 = (buf & u) >> 1
    s = t11 + t12
    t13 = buf ^ w
    t14 = t13 * (1 * buf)
    acc = t14 & 4095
    return y + lo & 255

if __name__ == "__main__":
    arg = 6
    expected = 239
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
