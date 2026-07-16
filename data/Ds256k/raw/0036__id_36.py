# Auto-extracted from ds_lt256k_500.jsonl
# record_id=36  entry=f  input='8'  output='0'  tokens=127250

def rec(n, a):
    if n <= 0:
        return a
    a = 17 - n + a << 2 & 2047
    for m in range(4):
        t0 = (17 - 9 ^ n) - n | a
        a = t0 % 1009
    a = a * a % 97
    t1 = (a ^ 1) % 1009
    return rec(n - 1, t1)

def f(x):
    t0 = 6 * x % 65521
    x = rec(110, t0)
    a = x - 11
    t1 = (10 ^ x) * (16 - a) + 15
    j = t1 % 1009
    for nxt in range(156):
        t2 = (a ^ 18) - a // 2 | nxt
        j = t2 & 262143
        t3 = (x | 7) * x ^ x
        a = (t3 - a) % 97
    g = (j ^ 12) - j
    for q in range(2):
        t4 = g << 4 & a
        t5 = q + (12 - a)
        a = t4 + t5 & 65535
    y = g * a % 9973
    for w in range(3):
        j = (j ^ g) & 8191
        t6 = w * x | y - 4
        a = t6 & 1023
    return (y ^ a) * (a & x) % 97

if __name__ == "__main__":
    arg = 8
    expected = 0
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
