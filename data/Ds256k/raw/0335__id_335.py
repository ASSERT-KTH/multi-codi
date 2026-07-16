# Auto-extracted from ds_lt256k_500.jsonl
# record_id=335  entry=f  input='4'  output='1'  tokens=249354

def rec(n, a):
    if n <= 0:
        return a
    if n ^ a != 29:
        for t in range(4):
            a = 11 - t - a & 8191
        for acc in range(10):
            a = a + n & 8191
    else:
        for aux in range(2):
            a = (n ^ 20 ^ a) & 255
            a = ((aux | 10) + 6 + a) % 4093
            a = (n ^ aux) + aux + a & 32767
        a = (n | a) % 65521
    for cur in range(8):
        if n * a == 41:
            a = (cur + a) % 65521
        else:
            t0 = cur - 14 & cur | cur
            a = t0 - a & 8191
            t1 = a * n >> 4
            a = t1 % 65521
    t2 = 19 + n - n & n ^ a
    return rec(n - 1, t2 % 1009)

def f(x):
    e = x + x
    d = (x & 5) + x - 7
    t0 = d << 4
    idx = t0 + e * x
    prv = 3 + x << 1
    tmp = (e - idx >> 3) + e
    q = 0
    while q < 4:
        for v in range(318):
            d = e * e * d % 97
            e = (x + prv ^ v) & 32767
        q = q + 1
    if d + idx >= 8:
        if tmp - x <= 34:
            x = tmp | x
        if e + 9 <= 13:
            t1 = (d + 10) % 1009
            d = rec(34, t1)
            t2 = 9 - 8
            t3 = t2 + 20 * 16
            t4 = x + 17 >> 4
            t5 = (t3 | t4) % 4093
            d = rec(97, t5)
        else:
            prv = idx >> 2
    else:
        prv = x * e ^ x
        if idx | e <= 45:
            prv = x * prv << 3 & 255
            t6 = x * idx + idx + e
            prv = rec(99, t6 & 16383)
    t7 = (idx - prv) // 8
    return t7 // 4 % 65521

if __name__ == "__main__":
    arg = 4
    expected = 1
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
