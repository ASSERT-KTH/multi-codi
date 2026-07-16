# Auto-extracted from ds_lt256k_500.jsonl
# record_id=374  entry=f  input='2'  output='52'  tokens=56093

def rec(n, a):
    if n <= 0:
        return a
    t0 = a * a ^ n
    w = t0 & 262143
    t1 = (9 ^ 15) - (a & 20)
    t2 = t1 + a & 255
    return rec(n - 1, t2)

def fn0(j):
    y = j ^ 8
    buf = (j - 6 & y) >> 4
    j = ((j & 12) - j) * buf & 255
    for w in range(3):
        j = (w + 5) * j % 65521
        y = ((w ^ 18) + y) % 251
        j = j // 6 % 65521
    lo = 0
    while lo < 12:
        j = lo - y & 131071
        for a in range(4):
            t0 = y % 251 << 2
            y = t0 * buf & 4095
            t1 = lo - 10 + buf | j
            j = t1 & 262143
            t2 = buf + y ^ a
            j = t2 & 2047
        j = (j ^ 18 ^ 17) & 262143
        lo = lo + 1
    g = 0
    while g < 8:
        t3 = (j | 5) >> 3
        t4 = t3 >> 2 | y
        y = t4 % 1009
        for res in range(4):
            t5 = res - 5 | g
            y = (t5 - y) % 9973
        if g * g - buf == 12:
            y = (g ^ 11) & j
            t6 = (18 | y) + buf ^ j
            y = t6 % 1009
        else:
            y = buf + g & 131071
            buf = (y << 3) + buf & 131071
        g = g + 1
    for e in range(11):
        for d in range(4):
            buf = d & j
            t7 = 19 - 16 | y
            j = (t7 ^ d) % 9973
        y = buf + j & e
        t8 = (17 << 2) * j - y - buf
        buf = t8 & 8191
    if j * j != 41:
        j = buf * buf * 18 % 1009
        t9 = (9 - y) % 251
        j = rec(78, t9)
    else:
        buf = 7 + j
    t10 = (j & buf) - 3
    return t10 % 251

def f(x):
    prv = [236, 400, 551, 521, 642, 307, 104]
    j = 0
    while j < 165:
        t0 = prv[x % 7] + x
        x = t0 & 262143
        t1 = prv[x % 7] | x
        x = t1 & 1023
        j = j + 1
    t2 = x + x >> 2
    acc = t2 // 2
    w = x - 19
    p = w - acc - acc
    hi = acc << 3
    q = hi * x % 251
    t3 = hi // 2 * (q ^ 17)
    y = t3 % 97
    t4 = w // 7
    cur = t4 ^ p << 4
    t5 = prv[q % 7]
    t6 = t5 - prv[w % 7]
    tmp = t6 // 6
    e = 0
    while e < 12:
        q = ((cur | 15 | 6) + e) % 251
        t7 = prv[y % 7]
        t8 = t7 - w + tmp
        tmp = t8 & 8191
        e = e + 1
    idx = 7 * cur >> 1
    return (q - idx) % 251

if __name__ == "__main__":
    arg = 2
    expected = 52
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
