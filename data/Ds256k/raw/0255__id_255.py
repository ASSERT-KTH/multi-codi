# Auto-extracted from ds_lt256k_500.jsonl
# record_id=255  entry=f  input='16'  output='841'  tokens=97100

def rec(n, a):
    if n <= 0:
        return a
    t0 = 16 * 9 | a
    tmp = t0 - n & 255
    t1 = tmp * tmp + n - a
    return rec(n - 1, t1 & 255)

def fn0(j, c, e):
    if c - j != 29:
        e = 1 ^ e ^ c
    if e + e > 55:
        if c * j >= 26:
            t0 = (e * c >> 4) % 4093
            c = rec(53, t0)
            c = (j - e) // 5
        else:
            j = c + j - (c + c)
            t1 = (16 | 18) * (e & 2)
            c = t1 - j
        t2 = (j + e) % 17
        e = rec(55, t2)
    else:
        t3 = j ^ 18 ^ (e | 13)
        e = t3 & 32767
    tmp = (j % 17 | 14) - e
    t4 = (j | e) * 8
    a = t4 % 17
    hi = a * tmp % 17
    for res in range(6):
        hi = hi * e % 97
        a = (tmp // 4 + a) % 4093
        t5 = 1 * j // 4 * e
        a = (t5 + a) % 9973
    t6 = (tmp ^ a) + 11
    t7 = t6 | (e + c | 15)
    return t7 % 17

def f(x):
    res = x & 13
    t0 = 16 * 14 - res & 65535
    res = rec(61, t0)
    x = x * x
    s = 0
    while s < 299:
        x = (x >> 2) % 1009
        t1 = res + s << 2
        x = (t1 + (res >> 1) // 2) % 1009
        x = (s << 2 ^ x + s) % 1009
        s = s + 1
    t2 = (3 | 16) % 17
    return (t2 - res) % 1009

if __name__ == "__main__":
    arg = 16
    expected = 841
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
