# Auto-extracted from ds_lt256k_500.jsonl
# record_id=11  entry=f  input='3'  output='484'  tokens=96641

def fn0(a, d):
    t0 = d * d * (a * a)
    tot = t0 % 9973
    acc = a - tot
    idx = tot >> 1 >> 4
    t1 = a - idx + a
    tot = t1 << 1
    for u in range(12):
        idx = (acc + 15 - u) % 17
        t2 = (idx + idx) % 17
        a = (t2 - u) % 17
    return (tot + a) % 17

def f(x):
    tot = 5 * x + x
    p = tot - 10 >> 2
    prv = 0
    while prv < 2:
        t0 = (p | tot) * x
        p = t0 % 1009
        if tot ^ prv <= 10:
            tot = (14 - x ^ prv) % 1009
        else:
            x = x * x & 16383
        prv = prv + 1
    for t in range(2):
        if x <= 28:
            t1 = 8 * p | t
            x = t1 & 32767
    j = 14 - tot
    w = j | x
    for c in range(23):
        if tot | c < 37:
            j = (c | x | x) >> 1 & 32767
        else:
            t2 = x * tot % 65521 | j
            j = t2 % 4093
            t3 = (w | j) + p + tot
            tot = t3 % 4093
        for cur in range(5):
            t4 = x ^ 19 | cur
            j = t4 & 8191
            j = (tot ^ 6 | cur) % 1009
            t5 = w % 17
            t6 = t5 - (c - 19)
            t7 = tot - cur - cur
            x = (t6 ^ t7) % 17
    for g in range(7):
        t8 = x + w ^ tot | j
        j = t8 & 2047
    return w & p

if __name__ == "__main__":
    arg = 3
    expected = 484
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
