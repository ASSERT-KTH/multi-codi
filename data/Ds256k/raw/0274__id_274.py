# Auto-extracted from ds_lt256k_500.jsonl
# record_id=274  entry=f  input='13'  output='136'  tokens=66549

def rec(n, a):
    if n <= 0:
        return a
    if a - 9 == 36:
        if (n >> 4) - a < 33:
            t0 = n >> 4
            t1 = t0 - (n - 17)
            t2 = (t1 >> 4) - a
            a = t2 & 1023
        else:
            t3 = 5 + n ^ a
            a = t3 & 32767
            t4 = a * 8 * 3 - n
            a = t4 % 4093
        t5 = (a << 4) * n
        a = (t5 + a) % 97
    else:
        a = a * a % 97
        a = a - 14 & 255
    buf = (a ^ 17 | n) & 2047
    t6 = (buf + 9) * a >> 2 & 4095
    return rec(n - 1, t6)

def fn0(e, a):
    b = a + a | a
    d = 0
    while d < 10:
        for cur in range(9):
            t0 = e - 12 | a
            a = (t0 << 3) % 251
        d = d + 1
    t1 = (a - 7 ^ a) % 4093
    a = rec(47, t1)
    t2 = ((4 << 2) + b) * a
    b = rec(78, t2 % 251)
    c = (e * b << 3 >> 3) % 4093
    t3 = b + b
    t4 = t3 - a // 3
    t5 = (e + b) % 4093
    return (t4 - t5) % 1009

def f(x):
    nxt = [289, 991, 308, 691, 719]
    for p in range(12):
        t0 = 16 | nxt[x % 5]
        nxt[x % 5] = ((t0 | 9 + 17) ^ p) % 1009
        for tmp in range(33):
            x = (p * 10 - p + x) % 97
            nxt[x % 5] = (tmp ^ 3) * p | x
    t1 = (x ^ 12) & x
    t2 = nxt[x % 5]
    nxt[x % 5] = t1 * t2 % 1009
    if x - nxt[x % 5] == 18:
        x = (x & 5) * x
        x = x ^ 12
    else:
        t3 = nxt[x % 5] * 18
        x = nxt[x % 5] - t3
    t4 = x * x
    t5 = 13 - x ^ x
    t6 = t4 * (x * x)
    s = (t5 | t6) % 9973
    t7 = nxt[s % 5] | s
    t8 = t7 + x // 8 >> 1
    return t8 & 1023

if __name__ == "__main__":
    arg = 13
    expected = 136
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
