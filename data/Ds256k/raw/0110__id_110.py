# Auto-extracted from ds_lt256k_500.jsonl
# record_id=110  entry=f  input='7'  output='141'  tokens=59901

def rec(n, a):
    if n <= 0:
        return a
    for acc in range(9):
        a = (acc << 3 >> 4 | a) % 17
        t0 = 11 * a // 3
        a = t0 & 19 << 2 << 1
        if acc & a != 2:
            t1 = acc - n - (acc + n)
            t2 = t1 ^ (acc - 20 | 3) ^ a
            a = t2 & 65535
    t3 = (a ^ 9) + n
    u = t3 - a & 8191
    c = n + u & 131071
    t4 = (a - u) % 17
    return rec(n - 1, t4)

def f(x):
    q = [155, 96, 112, 150, 247, 22]
    e = x + x + 13
    cur = x * x - x
    prv = e ^ cur
    for idx in range(359):
        t0 = (e | cur) ^ idx
        e = (t0 ^ 12) % 251
    res = 6 & cur
    x = (prv + prv) // 3
    t1 = q[cur % 6]
    return t1 - 14 & 262143

if __name__ == "__main__":
    arg = 7
    expected = 141
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
