# Auto-extracted from ds_lt256k_500.jsonl
# record_id=81  entry=f  input='19'  output='586'  tokens=166613

def rec(n, a):
    if n <= 0:
        return a
    a = (n // 5 + a) % 1009
    t0 = n + a + 15
    t1 = t0 * n % 65521
    return rec(n - 1, t1)

def f(x):
    lo = (x ^ 20) & x
    g = lo * lo % 97 >> 2
    for s in range(3):
        g = (15 + (s - 15) + lo) % 97
        for buf in range(5):
            x = ((buf | x) ^ 13) & 255
            x = (7 + g | x) % 1009
            t0 = x + g >> 4
            g = t0 % 97
    for nxt in range(73):
        if lo ^ 11 == 7:
            x = (x | 9) & 262143
        for y in range(4):
            t1 = (y - x | nxt + lo) + g
            lo = t1 % 1009
            t2 = 2 + nxt | g
            x = (t2 ^ x) % 97
    t3 = (20 | x) ^ x
    t4 = (4 | x) // 2
    t5 = t3 * t4 % 97
    x = rec(48, t5)
    t6 = (11 ^ g) % 1009
    lo = rec(47, t6)
    for u in range(3):
        for e in range(4):
            t7 = 15 * lo
            t8 = t7 - (lo + x)
            lo = t8 % 1009
            t9 = (e & g) - x
            g = t9 & g * lo << 3
            t10 = lo - 17 - (17 ^ g)
            lo = t10 * g & 131071
        t11 = g - lo & 2 - 12
        lo = (x * g % 1009 - t11) % 1009
    v = (lo & 15) * 8
    t12 = (x // 2 + v) * x
    acc = t12 % 4093
    for d in range(4):
        x = (x // 2 - 18) * acc % 97
        if x * acc < 7:
            t13 = (v >> 2) * acc
            g = (t13 ^ d) & 8191
            lo = lo % 1009
    t14 = (v * v << 2) % 97
    lo = rec(36, t14)
    t15 = (v << 3) * 11 // 6
    return t15 & 32767

if __name__ == "__main__":
    arg = 19
    expected = 586
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
