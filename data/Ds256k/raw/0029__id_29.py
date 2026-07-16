# Auto-extracted from ds_lt256k_500.jsonl
# record_id=29  entry=f  input='8'  output='64052'  tokens=127873

def rec(n, a):
    if n <= 0:
        return a
    g = (n - 2 ^ a >> 3) & 16383
    t0 = g >> 1
    t1 = t0 & (g & 20)
    t2 = t1 - a & 2047
    return rec(n - 1, t2)

def fn0(d):
    e = [66, 79, 55, 51, 15, 79]
    for val in range(12):
        t0 = val - 10
        t1 = t0 - (13 - val)
        d = (t1 | d) & 2047
        d = d // 6 + (val + 7) & 2047
    cur = 0
    while cur < 3:
        t2 = 5 << 2 ^ 18
        d = (t2 | d) % 17
        cur = cur + 1
    t3 = d - 10 & 8191
    d = rec(110, t3)
    u = (12 & d) + d // 6
    t4 = e[u % 6] + d
    aux = (7 & 13 ^ t4) * d % 4093
    t5 = 9 - 13 - u % 4093
    b = (1 + u) // 3 & t5
    b = 20 - u
    u = 14 + u
    t6 = (12 | d) - u
    return t6 % 17

def f(x):
    cur = x ^ 6
    acc = cur << 4 >> 2
    for d in range(11):
        cur = (3 - 7 ^ x ^ d) % 9973
        if acc // 4 <= 29:
            t0 = 4 - d + x
            x = t0 & 131071
            x = (cur << 4 << 2) * d & 131071
        for e in range(4):
            t1 = e * acc - cur
            acc = t1 % 97
            t2 = x // 4 ^ 8 + cur
            x = t2 % 97
            t3 = (d << 4 >> 2) + acc
            x = t3 + x & 1023
    res = 0
    while res < 10:
        t4 = (acc >> 2) + 5 + cur
        acc = t4 % 65521
        for p in range(21):
            cur = (res - (x >> 1) + cur) % 65521
            t5 = 9 - p - x
            x = t5 % 9973
            x = (16 ^ 6 | cur) + x & 255
        res = res + 1
    aux = cur >> 4
    if acc >> 4 > 45:
        x = 8 ^ acc ^ aux
        x = 2 - 9 ^ acc
    else:
        if acc ^ aux <= 57:
            t6 = cur + aux | (aux | 4)
            t7 = t6 * x % 65521
            cur = rec(60, t7)
    if 20 * x <= 7:
        for q in range(4):
            x = (aux & 11) * x & 65535
    z = cur | 5
    t8 = (aux & x) + cur
    return t8 & 65535

if __name__ == "__main__":
    arg = 8
    expected = 64052
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
