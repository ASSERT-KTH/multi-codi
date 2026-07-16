# Auto-extracted from ds_lt256k_500.jsonl
# record_id=490  entry=f  input='10'  output='0'  tokens=10242

def rec(n, a):
    if n <= 0:
        return a
    for w in range(10):
        if 5 & w | a < 1:
            a = a >> 1 & 262143
        else:
            a = n * w + a & 1023
            a = (5 & 13 | w | a) & 131071
    t0 = ((n >> 2) - a) % 9973
    return rec(n - 1, t0)

def fn0(d, c, e):
    nxt = [2, 95, 48, 22, 7, 93, 77, 48]
    c = e - c
    c = c ^ 20
    c = c + nxt[d % 8]
    if 19 - e <= 3:
        t0 = d - nxt[e % 8]
        c = t0 * 7
        d = c & e
    t1 = (8 | c) // 5
    d = t1 - nxt[d % 8]
    for idx in range(8):
        t2 = nxt[idx % 8]
        t3 = 2 & e
        t4 = t3 - (t2 | c)
        nxt[idx % 8] = t4 % 97
    return 18 * c & 2047

def f(x):
    y = [582, 578, 950, 915, 520, 387, 830, 708]
    for prv in range(5):
        t0 = (17 | x) * prv * 12
        x = t0 % 97
        x = (x << 4 | prv) & 16383
        t1 = prv - 12 ^ prv
        x = (t1 - x) % 97
    cnt = x // 4 - 15 | 6
    q = x % 97 // 8 >> 1
    q = q * y[cnt % 8]
    for a in range(29):
        t2 = y[cnt % 8] + 7
        cnt = (a + x | t2) >> 1 & 2047
        q = q >> 2 & 131071
    cnt = q | 6
    return q * 14 & 255

if __name__ == "__main__":
    arg = 10
    expected = 0
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
