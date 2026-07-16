# Auto-extracted from ds_lt256k_500.jsonl
# record_id=212  entry=f  input='13'  output='0'  tokens=130843

def fn0(c, g):
    tmp = [206, 22, 24, 42, 230, 162, 81]
    q = g + 6
    t0 = tmp[c % 7]
    t1 = g & 5
    t2 = g + g
    t3 = t1 | t0 ^ g
    t4 = t2 ^ 17 * 5
    s = t3 + t4
    for d in range(3):
        for cur in range(7):
            g = 6 * s + 17 - g & 2047
            t5 = cur - d - 19 ^ g
            tmp[cur % 7] = t5 % 251
        t6 = (s ^ 14) >> 4
        s = t6 & 511
        q = (d << 1 ^ 6) + c & 255
    t7 = g + tmp[g % 7]
    tmp[s % 7] = (c // 2 + t7) % 251
    b = g | q
    if tmp[b % 7] * 9 >= 0:
        if b + c <= 58:
            c = 14 - 12 ^ b
            t8 = g | 5 | s
            c = t8 - c
    return (10 | q) % 1009

def f(x):
    hi = x + 9
    for d in range(51):
        hi = d + x & 8191
        for lo in range(9):
            hi = (9 * x - lo) % 9973
            hi = (hi ^ x) % 65521
            x = (x | d) + 3 - 14 & 32767
        x = 11 + d + hi & 131071
    prv = hi // 3 * x & 16383
    if prv | 14 != 5:
        if x // 8 > 20:
            t0 = (prv - x) % 17
            t1 = hi + x
            t2 = t1 + (prv & 9)
            x = fn0(t0, t2 % 17)
            t3 = (x + hi + hi) % 17
            prv = fn0(t3, 10 & hi)
        else:
            t4 = hi + hi
            t5 = t4 - (hi | x)
            t6 = (prv & hi) >> 2
            prv = fn0(t5 & 4095, t6 & 65535)
            prv = 10 - x
    t7 = prv * prv * (prv ^ hi)
    y = t7 & 8191
    t = y + hi << 1
    t8 = x + x ^ hi
    m = t8 >> 1
    t9 = prv + m & x - prv
    t10 = t * 3 & 16383
    hi = fn0(t9, t10)
    if prv | 4 == 16:
        y = m >> 3
    else:
        prv = hi * y % 65521
        for s in range(9):
            t11 = (t + hi << 4) - x
            m = (t11 | s) % 17
            t = (s ^ y) & 2047
            prv = m // 8 * prv % 17
    cnt = t << 1
    if hi - 6 <= 46:
        x = hi >> 2
    else:
        t12 = hi - 11
        prv = t12 - (t >> 4)
        for e in range(10):
            t13 = prv + 6 ^ prv
            x = (t13 | e) % 65521
    nxt = hi // 7
    t14 = nxt + x + hi
    return t14 % 17

if __name__ == "__main__":
    arg = 13
    expected = 0
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
