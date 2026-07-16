# Auto-extracted from ds_lt256k_500.jsonl
# record_id=362  entry=f  input='1'  output='4020'  tokens=10836

def rec(n, a):
    if n <= 0:
        return a
    cur = (n + a) % 1009
    t0 = n - cur | n + 15
    d = t0 + a & 511
    if 5 * d < 6:
        t1 = n * cur >> 4
        d = t1 % 97
        cur = ((7 & a) + cur) % 4093
    else:
        for v in range(9):
            a = (v ^ n ^ a) & 262143
            t2 = (d | v) - n
            t3 = t2 ^ (n | 12) + 3
            d = t3 & 131071
    t4 = (d ^ a) & 16383
    return rec(n - 1, t4)

def fn0(j):
    t0 = j - 4 & j
    t1 = (j >> 4) + j
    buf = t0 + t1
    j = (buf >> 2) - (6 | j)
    s = 0
    while s < 4:
        t2 = s * s + buf
        buf = t2 & 1023
        t3 = j - 14 + 12
        buf = t3 - buf & 2047
        s = s + 1
    t4 = (15 ^ buf) >> 1 | j
    j = rec(116, t4 & 262143)
    t5 = buf ^ j
    t6 = t5 + (buf | 3)
    return t6 & 131071

def fn1(j, c, b):
    c = (b + 14 & 17 - c) << 2
    c = j - b + c & 15
    j = j - c - b
    j = (b ^ j) - 13
    return (j ^ c) & 255

def f(x):
    y = [181, 14, 205, 236, 114, 40, 209]
    y[x % 7] = x - 7
    d = x * x - 11
    t0 = x + d - x * x
    t1 = d * d * (d + d)
    hi = t0 + t1 & 1023
    j = 0
    while j < 45:
        hi = (x | hi) % 1009
        x = j + d >> 3 & 32767
        j = j + 1
    t2 = d * d * y[x % 7]
    m = (d - 20 - x - t2) % 251
    cur = m & 17
    t3 = y[cur % 7] - x
    return (x + cur) * t3 % 65521

if __name__ == "__main__":
    arg = 1
    expected = 4020
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
