# Auto-extracted from ds_lt256k_500.jsonl
# record_id=315  entry=f  input='15'  output='7'  tokens=116989

def rec(n, a):
    if n <= 0:
        return a
    idx = (a - n) % 251
    t0 = a - 4 - 17 * idx
    return rec(n - 1, t0 % 4093)

def fn0(d):
    if d - 16 == 32:
        for p in range(5):
            d = (d + p) // 6 * p & 1023
    for v in range(2):
        t0 = v + v | d
        t1 = 4 + v - 13
        d = (t0 ^ t1) % 65521
        for w in range(8):
            t2 = d >> 2
            t3 = 2 + 18 | w
            t4 = t2 ^ 11 - v
            d = t3 + t4 & 32767
    a = d * 5
    tmp = d * a // 3 % 4093
    t5 = (tmp // 8 | d) - tmp
    return t5 % 4093

def fn1(j):
    res = [67, 26, 89, 78, 77, 36, 69]
    idx = j % 97
    t0 = j >> 3
    t1 = (j >> 4) - j
    t2 = t0 * (idx ^ 15)
    y = t1 - t2 & 262143
    for cur in range(11):
        idx = (y // 3 + idx) % 17
    t3 = 6 * idx - y & 2047
    y = rec(102, t3)
    hi = 0
    while hi < 6:
        if j // 2 > 60:
            t4 = (idx >> 2) * hi
            y = t4 & 262143
        for cnt in range(4):
            res[idx % 7] = (idx * cnt | hi) % 97
            t5 = (idx ^ 8) - res[j % 7]
            j = t5 // 7 & 262143
        q = 0
        while q < 3:
            res[j % 7] = (20 ^ idx | y) % 97
            q = q + 1
        hi = hi + 1
    nxt = (y >> 3 & j) // 4
    if nxt ^ j > 38:
        if 2 - y != 12:
            t6 = (res[nxt % 7] << 4) + j
            y = t6 - y
        else:
            t7 = y * nxt
            t8 = t7 * (nxt | 17)
            nxt = t8 * nxt & 32767
    else:
        t9 = y * nxt % 4093
        res[idx % 7] = t9 % 97
    t10 = (18 & nxt) * (8 - 4)
    return (t10 + j) % 4093

def f(x):
    e = [201, 9, 78, 132, 223, 56, 148, 60]
    for b in range(21):
        for y in range(11):
            t0 = e[b % 8]
            t1 = 6 * b ^ 17
            t2 = (t0 ^ x) >> 2
            x = t1 * t2 & 1023
            e[b % 8] = (b + b ^ x) % 251
    t3 = x + x
    t4 = t3 ^ x & 19
    res = t4 & 9
    g = e[x % 8] * res
    for a in range(11):
        t5 = (a ^ g) // 3
        res = t5 & 4095
        e[x % 8] = res // 7 % 251
        for buf in range(6):
            e[x % 8] = (x & res) % 251
            t6 = g + 16 ^ x + x + x
            x = t6 % 4093
    g = g * res % 17
    t7 = e[x % 8] * 7
    return ((g ^ 13) - t7 | res) % 4093

if __name__ == "__main__":
    arg = 15
    expected = 7
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
