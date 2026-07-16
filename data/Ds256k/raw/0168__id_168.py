# Auto-extracted from ds_lt256k_500.jsonl
# record_id=168  entry=f  input='5'  output='1719'  tokens=49401

def rec(n, a):
    if n <= 0:
        return a
    t0 = (n & 12) + a
    t1 = a + n >> 2
    val = t0 * t1 % 65521
    t2 = (n + a) % 65521
    return rec(n - 1, t2)

def f(x):
    res = [64, 31, 77, 1, 92]
    t0 = res[x % 5] | x
    d = t0 - x
    t1 = (x ^ 1) + 17
    t2 = (t1 + 18 * d) % 9973
    d = rec(39, t2)
    cur = res[d % 5]
    for c in range(47):
        t3 = res[c % 5] + x
        res[cur % 5] = t3 % 97
        t4 = (cur // 5 >> 1) + x
        x = t4 % 9973
        t5 = cur + d
        t6 = t5 ^ 20 + 18
        x = t6 - c & 16383
    prv = d & 7
    if prv * 11 >= 25:
        if cur & d <= 28:
            t7 = res[x % 5]
            t8 = (x - t7) % 65521
            prv = rec(99, t8)
        for aux in range(3):
            cur = (prv // 8 + aux) % 65521
    else:
        tmp = 0
        while tmp < 6:
            res[tmp % 5] = 6 & d & (tmp ^ d)
            t9 = 10 - res[d % 5]
            x = (t9 ^ x) % 65521
            t10 = (res[tmp % 5] << 1) + x
            res[tmp % 5] = t10 % 97
            tmp = tmp + 1
    s = (d ^ cur) // 7
    if 2 & x < 2:
        for u in range(4):
            t11 = res[s % 5] ^ 7
            t12 = (t11 + prv * s) % 9973
            res[d % 5] = t12 % 97
            prv = cur & prv
            d = d // 3 % 9973
        t13 = (9 << 2) * (cur << 4)
        t14 = t13 ^ res[d % 5]
        d = t14 % 65521
    t15 = s * prv ^ d
    return t15 % 65521

if __name__ == "__main__":
    arg = 5
    expected = 1719
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
