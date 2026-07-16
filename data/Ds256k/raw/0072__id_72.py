# Auto-extracted from ds_lt256k_500.jsonl
# record_id=72  entry=f  input='15'  output='29'  tokens=173409

def rec(n, a):
    if n <= 0:
        return a
    a = (n * 13 + n | a) % 251
    t0 = n - 1 + (a | 8) & 1023
    return rec(n - 1, t0)

def f(x):
    a = [204, 17, 247, 89, 88]
    acc = x ^ 13
    z = 0
    while z < 2:
        for p in range(10):
            a[x % 5] = p + 9 - x
            t0 = 17 | p
            t1 = t0 ^ (z ^ acc)
            acc = t1 % 65521
        for prv in range(10):
            t2 = 17 - 19 | 5
            t3 = (t2 ^ x) + acc
            acc = t3 & 262143
            a[z % 5] = (acc - 4) % 251
            t4 = prv - 15 | x
            a[z % 5] = t4 & 10
        t5 = acc * z
        t6 = t5 - (z + z)
        x = t6 % 65521
        z = z + 1
    nxt = 0
    while nxt < 3:
        t7 = acc >> 2 & (7 ^ 6) ^ 10
        acc = t7 % 65521
        nxt = nxt + 1
    q = 0
    while q < 13:
        t8 = (2 & 6) - 14 + acc | x
        x = t8 % 97
        for cur in range(12):
            t9 = a[x % 5]
            t10 = t9 ^ a[q % 5]
            a[x % 5] = t10 % 251
            t11 = a[acc % 5]
            a[q % 5] = (t11 - x) % 251
        q = q + 1
    t12 = 13 - 5 ^ 12
    tot = t12 + acc
    x = 8 + 9 & a[acc % 5]
    y = 0
    while y < 5:
        if acc ^ 3 < 23:
            t13 = a[y % 5]
            t14 = tot // 3 * tot
            t15 = (t13 | y) + tot
            a[x % 5] = t14 * t15 % 97
            acc = (y << 3 | tot) % 65521
        a[x % 5] = (x // 8 << 2) % 251
        y = y + 1
    t16 = x ^ 18 ^ acc
    return t16 % 65521

if __name__ == "__main__":
    arg = 15
    expected = 29
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
