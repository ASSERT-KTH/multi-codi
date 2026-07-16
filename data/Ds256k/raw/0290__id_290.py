# Auto-extracted from ds_lt256k_500.jsonl
# record_id=290  entry=f  input='15'  output='507'  tokens=125557

def rec(n, a):
    if n <= 0:
        return a
    a = 14 * a % 97
    t0 = (a + a | a // 5) & 65535
    return rec(n - 1, t0)

def f(x):
    for z in range(734):
        t0 = x - z - x
        x = t0 & 16383
        x = (z ^ 18 | x) & 65535
    buf = x + 10
    for cur in range(3):
        x = buf + buf + x & 1023
        t1 = (buf ^ x) // 2
        buf = (t1 ^ (4 & x) * x) & 511
    t2 = (buf | x) + x
    buf = t2 // 4
    x = rec(86, x & 511)
    t3 = (7 * 7 ^ (20 | x)) * x
    x = rec(39, t3 & 65535)
    x = (18 & buf) - (x ^ 7)
    x = x % 251
    t4 = (x << 2) % 17
    t5 = (x << 1) % 251
    t6 = t4 ^ t5 | buf
    return t6 & 262143

if __name__ == "__main__":
    arg = 15
    expected = 507
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
