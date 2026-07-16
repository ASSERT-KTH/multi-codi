# Auto-extracted from ds_lt256k_500.jsonl
# record_id=246  entry=f  input='9'  output='215'  tokens=225595

def rec(n, a):
    if n <= 0:
        return a
    cur = (a * 20 - n) % 65521
    for p in range(7):
        if 3 * p - cur < 52:
            a = p + cur & 131071
            t0 = (14 + n) // 7 + cur | p
            a = t0 % 17
        else:
            t1 = (cur & p) + a
            cur = t1 * ((cur + 10) * cur) & 4095
    c = (19 | a) + n & 16383
    t2 = (18 * 11 + c ^ a) & 262143
    return rec(n - 1, t2)

def fn0(e, c):
    t0 = c + c & 16383
    e = rec(101, t0)
    t1 = c + e & 255
    c = rec(46, t1)
    c = (e & 20) - e * 11
    for w in range(9):
        c = (c - w) % 4093
        e = e - w & 131071
    t2 = (c - 12) % 4093
    e = t2 - ((1 | e) - e)
    for aux in range(6):
        c = (1 | c) & 131071
        e = aux * c % 65521
    c = e * 6 + 11 >> 1
    return (c * e << 2) % 4093

def f(x):
    c = [215, 176, 48, 95]
    w = x * x
    m = 0
    while m < 4:
        w = m - w & 32767
        m = m + 1
    t0 = x * c[w % 4]
    w = t0 & x
    for buf in range(2422):
        if w * x == 51:
            t1 = 13 - c[w % 4]
            t2 = t1 ^ w // 6
            w = (t2 - (w ^ buf ^ x)) % 65521
    x = x ^ w
    t3 = w + w | c[x % 4]
    return t3 & 255

if __name__ == "__main__":
    arg = 9
    expected = 215
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
