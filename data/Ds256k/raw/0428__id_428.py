# Auto-extracted from ds_lt256k_500.jsonl
# record_id=428  entry=f  input='16'  output='33'  tokens=112234

def rec(n, a):
    if n <= 0:
        return a
    a = a >> 3 & 262143
    t0 = n >> 1
    t1 = t0 + n // 5
    t2 = n - 2 - 10
    t3 = t1 - t2 - a
    return rec(n - 1, t3 & 511)

def f(x):
    acc = x + x
    prv = (acc + acc >> 1) + 14
    cur = acc + 12 | (x | prv)
    t0 = 20 * acc * (cur << 1)
    nxt = t0 << 2
    for v in range(181):
        if nxt + prv == 30:
            prv = (prv & cur) + prv * v & 8191
        else:
            x = (nxt & v) + nxt * x & cur
            t1 = (prv >> 2) + acc
            acc = t1 & 32767
        cur = cur & v
        prv = prv & x
    t2 = ((acc << 4) - nxt) * 5
    lo = t2 & 262143
    y = 0
    while y < 4:
        t3 = prv ^ x
        t4 = lo + y >> 2
        t5 = t3 - (acc >> 2)
        prv = t4 * t5 % 97
        t6 = acc | 4
        t7 = t6 + (10 - y)
        cur = t7 * 9 & 1023
        t8 = prv * 6 & 17 * nxt
        x = (t8 ^ x) & 8191
        y = y + 1
    buf = lo + cur - 20
    t9 = 15 * lo // 8 % 97
    lo = rec(113, t9)
    t10 = ((lo & nxt) + (buf | cur)) // 2
    return t10 % 97

if __name__ == "__main__":
    arg = 16
    expected = 33
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
