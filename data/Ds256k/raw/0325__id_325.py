# Auto-extracted from ds_lt256k_500.jsonl
# record_id=325  entry=f  input='14'  output='7262'  tokens=107518

def rec(n, a):
    if n <= 0:
        return a
    t = (n + n + a) % 1009
    t0 = t * t // 3 + n
    idx = t0 & 262143
    t1 = a % 251 * (a * idx)
    t = (t1 ^ t) & 8191
    t2 = (idx + 20) * n >> 3
    t3 = t2 - a & 8191
    return rec(n - 1, t3)

def fn0(j):
    prv = [523, 858, 842, 429, 643, 265, 328, 405]
    t0 = prv[j % 8]
    t1 = j * j
    t2 = prv[j % 8]
    t3 = j << 4
    t4 = t1 - (t0 & j)
    t5 = t3 * (j - t2)
    t6 = t4 + t5 & 4095
    prv[j % 8] = t6 % 1009
    if prv[j % 8] // 5 <= 40:
        for lo in range(9):
            t7 = j % 97 & 8 - j
            t8 = t7 ^ prv[j % 8]
            j = t8 & 8191
            j = j * lo % 251
            t9 = 3 + lo + j
            j = t9 & 8191
    t10 = j * j | prv[j % 8]
    prv[j % 8] = (t10 & 16383) % 1009
    for s in range(9):
        if s & 9 | j == 39:
            j = j + s & (16 & s)
            t11 = 9 + s ^ j
            prv[s % 8] = t11 % 1009
        j = j - prv[s % 8] & 65535
    cnt = 13 * j // 4
    m = j - 10 >> 1
    nxt = 0
    while nxt < 9:
        t12 = m << 1 | cnt + cnt
        cnt = (t12 | cnt % 65521 - cnt) & 8191
        nxt = nxt + 1
    t13 = cnt * prv[m % 8] - j
    return t13 % 97

def f(x):
    t0 = x + x & 8191
    x = rec(100, t0)
    x = fn0(1 - 2 + x & 131071)
    for j in range(5):
        t1 = x & 1 | j - 7
        x = t1 & 255
        for u in range(53):
            x = (u ^ j) + x & 8191
    for idx in range(6):
        for val in range(7):
            t2 = val * idx | val + val
            x = (t2 * 12 - x) % 65521
            t3 = val - 6 + x
            x = t3 & 4095
    p = 0
    while p < 2:
        t4 = p - 10 + x
        x = t4 - 9 & 4095
        t5 = x + x - x
        x = t5 >> 4 & 255
        p = p + 1
    for b in range(6):
        t6 = 13 * x * (8 * 1)
        x = t6 & 8191
        t7 = (12 - b) * (4 - x)
        x = t7 * 19 & 8191
        t8 = (4 & 2) - b - x
        x = t8 & 1023
    t9 = x * x // 5
    return (t9 - (3 * x ^ x)) % 65521

if __name__ == "__main__":
    arg = 14
    expected = 7262
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
