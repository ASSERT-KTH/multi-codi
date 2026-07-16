# Auto-extracted from ds_lt256k_500.jsonl
# record_id=122  entry=f  input='15'  output='19'  tokens=49322

def rec(n, a):
    if n <= 0:
        return a
    a = (n ^ 16 | 13) * a % 251
    for b in range(7):
        if a & 20 > 6:
            a = b * n - a & 2047
        for buf in range(3):
            t0 = (8 - buf) * (19 - 14) ^ a
            a = t0 & 131071
            a = b - buf - a & 2047
    a = a % 65521
    t1 = (n ^ a) % 251
    return rec(n - 1, t1)

def f(x):
    tmp = [83, 60, 2, 42, 52]
    t0 = (18 ^ x) & x - 12
    tmp[x % 5] = (t0 | tmp[x % 5]) % 97
    if x == 4:
        if x + 17 <= 27:
            x = x * x
    e = x | 5
    t1 = tmp[e % 5]
    t2 = 7 * 9 & t1
    t3 = tmp[x % 5]
    for nxt in range(10):
        x = (e & x) % 17
        t4 = (x >> 2) - x
        tmp[e % 5] = t4 % 97
        for d in range(8):
            t5 = (d << 3) + e
            tmp[x % 5] = t5 % 97
            e = 19 * tmp[e % 5] & 131071
            t6 = 10 * nxt - 18
            tmp[x % 5] = (t6 + e) % 97
    return t2 & t3

if __name__ == "__main__":
    arg = 15
    expected = 19
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
