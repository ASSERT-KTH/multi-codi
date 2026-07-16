# Auto-extracted from ds_lt256k_500.jsonl
# record_id=292  entry=f  input='15'  output='198'  tokens=23243

def rec(n, a):
    if n <= 0:
        return a
    for c in range(9):
        a = 5 - a & c + n
        a = (n + a) % 4093
    t0 = (a ^ n) * (n - a)
    return rec(n - 1, t0 % 1009)

def fn0(d, c):
    acc = d + d
    for p in range(5):
        if d - 6 == 22:
            c = (4 - 6 ^ c) & 16383
    c = rec(50, 2 & acc)
    if d // 3 != 60:
        tot = 0
        while tot < 7:
            d = (tot & 12 | d) & 8191
            t0 = ((d >> 4) * acc >> 3) + tot
            c = t0 % 65521
            c = c - 3 & 8191
            tot = tot + 1
    for cnt in range(8):
        t1 = (12 | 9) + acc
        t2 = acc - c - 9
        c = t1 & t2
        acc = c + cnt & 4095
    return ((c ^ acc) - c) % 97

def fn1(g, a):
    hi = a - 13 + a
    t0 = a * g - (6 - 9)
    t1 = t0 * ((hi ^ g) - 11 * a)
    t2 = (g + hi ^ 10 * a) % 4093
    a = fn0(t1 % 65521, t2)
    t3 = hi ^ 5
    t4 = t3 - a * a
    w = t4 & 16383
    nxt = a - hi << 4 >> 2
    t5 = w * a | w - nxt
    w = (t5 ^ a) % 4093
    w = g + 7 + hi // 5
    return (w - hi ^ nxt) % 4093

def f(x):
    t = [40, 52, 37, 85, 30, 11]
    for p in range(329):
        t[x % 6] = (x | p) + 13
    acc = (x + x) * (x + 6) | x
    idx = x & 6
    y = 16 | idx
    t0 = idx + t[idx % 6]
    y = t0 - (acc | 19) + x
    t1 = ((x ^ 14) - (y - x)) // 3
    return t1 & 1023

if __name__ == "__main__":
    arg = 15
    expected = 198
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
