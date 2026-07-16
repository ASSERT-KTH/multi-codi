# Auto-extracted from ds_lt256k_500.jsonl
# record_id=308  entry=f  input='13'  output='32701'  tokens=44776

def rec(n, a):
    if n <= 0:
        return a
    t0 = n + 14 & n
    prv = (t0 ^ a) % 4093
    t1 = n // 2 | a
    return rec(n - 1, t1 % 97)

def fn0(j):
    t0 = 19 * 13 ^ j
    j = rec(20, t0 % 251)
    if j ^ 6 == 42:
        t1 = (j - 16) % 65521
        t2 = j - 20 | 8
        j = t1 & t2
        for w in range(8):
            j = (j * 9 >> 4) % 251
            j = j * w - j & 262143
    else:
        for tmp in range(7):
            j = (tmp + tmp ^ j) & 8191
            j = j * 13 + j & j
    cnt = j ^ 1
    for prv in range(6):
        t3 = j & cnt
        t4 = t3 - (prv + prv)
        j = t4 & cnt
    t5 = (j ^ cnt) - (8 - cnt)
    return t5 & 262143

def f(x):
    v = [77, 55, 56, 15, 72, 33, 6, 47]
    t0 = 14 - x
    cur = t0 * (x ^ 15)
    if v[cur % 8] + cur <= 21:
        for j in range(12):
            t1 = v[x % 8]
            t2 = x + j
            t3 = t2 | j + t1
            cur = t3 - j & 131071
        x = 18 ^ cur
    w = (cur ^ 10) // 5
    for hi in range(472):
        x = hi * cur % 97
    d = cur & 18
    e = cur >> 2 >> 4 << 3
    return (3 & d) - (x + e) & 32767

if __name__ == "__main__":
    arg = 13
    expected = 32701
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
