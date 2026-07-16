# Auto-extracted from ds_lt256k_500.jsonl
# record_id=382  entry=f  input='13'  output='39'  tokens=152573

def f(x):
    if 17 * 17 ^ x > 58:
        if x ^ 5 > 15:
            x = (x ^ 9) + x
        t0 = x ^ 17
        t1 = x << 4 | 3
        t2 = t0 + x * 15
        x = t1 - t2
    hi = (x * x ^ x) & x
    cur = 0
    while cur < 8:
        x = (x - cur) % 9973
        cur = cur + 1
    idx = x + hi
    res = 0
    while res < 4:
        if idx * x > 45:
            t3 = x & res | hi
            idx = t3 % 9973
        else:
            t4 = (4 ^ res) * res
            t5 = (t4 ^ 4) + hi
            idx = t5 & 262143
        res = res + 1
    j = idx & hi
    if j + 3 == 11:
        x = hi % 1009 | j
    w = j - x
    for val in range(2):
        t6 = 3 - w - x | idx
        idx = t6 % 9973
    for tmp in range(4):
        t7 = (tmp - idx) % 1009
        hi = t7 - idx & 65535
        w = (w ^ 1) % 65521
    for g in range(7):
        t8 = (j ^ idx) >> 4
        idx = t8 % 65521
        for acc in range(56):
            t9 = (w << 1) + (w & acc)
            j = t9 // 2 % 1009
    q = idx | j
    d = (j & x) << 1
    t10 = j * d
    t11 = t10 | x * q
    s = t11 + hi & 255
    t12 = (d & x) + (idx >> 1)
    return t12 % 1009

if __name__ == "__main__":
    arg = 13
    expected = 39
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
