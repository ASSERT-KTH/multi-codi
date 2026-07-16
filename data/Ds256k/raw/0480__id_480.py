# Auto-extracted from ds_lt256k_500.jsonl
# record_id=480  entry=f  input='16'  output='3'  tokens=229203

def f(x):
    e = (18 * x << 2) * 15
    t0 = (x + e) * x
    a = t0 - e
    w = 0
    while w < 9:
        t1 = x - w
        t2 = t1 | 20 - 12
        a = (t2 - 12) % 251
        t3 = x * x
        t4 = t3 | a // 7
        t5 = t4 >> 4 ^ w
        e = t5 & 1023
        for c in range(5):
            t6 = w * e >> 4 | x
            x = t6 & 255
        w = w + 1
    if x | 6 < 4:
        for val in range(4):
            x = (a * a | val) & 32767
            t7 = x * 3 | e ^ 11
            e = ((11 + a >> 3) + t7) % 251
        if 7 - a == 20:
            a = x + 17 - a
        else:
            t8 = (e | 4) ^ a - x
            t9 = (13 - a | a) - t8
            x = t9 % 251
    cur = 0
    while cur < 4:
        t10 = e - cur ^ cur
        e = (t10 + cur) % 251
        a = (x * cur & e) % 17
        x = e * x % 17
        cur = cur + 1
    idx = 2 * x + x
    for buf in range(2):
        t11 = x + 18
        t12 = t11 * (a - e)
        x = t12 % 251
    tmp = x & 11 & e
    for nxt in range(11):
        e = (x // 6 ^ e) & 65535
        t13 = tmp | 10
        t14 = t13 + (tmp | x)
        t15 = t14 * tmp ^ nxt
        e = t15 & 262143
    t16 = x + tmp & 12 + tmp
    aux = t16 + idx
    if a + e < 39:
        aux = x * a % 251
    else:
        e = (2 ^ aux) - aux % 17
        t17 = (x ^ 14) - (8 | x)
        aux = t17 - idx
    hi = 0
    while hi < 12:
        t18 = (x + x ^ 12) + hi
        idx = t18 % 17
        hi = hi + 1
    z = 0
    while z < 7:
        for v in range(10):
            aux = (aux - a) % 251
            t19 = (tmp & 9) - (idx << 1)
            t20 = t19 * ((aux - a) // 5)
            e = (t20 + v) % 251
        z = z + 1
    for cnt in range(36):
        tot = 0
        while tot < 2:
            t21 = idx >> 4 >> 3
            t22 = t21 * x - aux
            aux = t22 % 251
            tot = tot + 1
        x = ((tmp | 13) - cnt) % 17
    if e - x >= 55:
        aux = 17 & aux
        for g in range(3):
            idx = ((a << 3) + g) % 251
            t23 = idx * idx * e + aux
            aux = t23 & 131071
    else:
        if e // 4 == 27:
            t24 = a >> 3 & 8
            t25 = 2 * tmp * x
            a = t24 + t25
        else:
            x = (a | 12) % 17
            a = aux + e
    return e - idx & 4095

if __name__ == "__main__":
    arg = 16
    expected = 3
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
