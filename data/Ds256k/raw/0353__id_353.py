# Auto-extracted from ds_lt256k_500.jsonl
# record_id=353  entry=f  input='13'  output='78'  tokens=14012

def rec(n, a):
    if n <= 0:
        return a
    t0 = 10 - n + n >> 4 ^ a
    a = t0 % 65521
    t1 = ((n << 1) - (a ^ 1)) % 65521
    return rec(n - 1, t1)

def f(x):
    for val in range(27):
        x = x & 7
        x = (x + val + x) % 251
    t0 = 19 & x & x
    x = rec(51, t0)
    if x * x < 62:
        x = x << 4 >> 3
        m = 0
        while m < 10:
            x = (x + x) % 251
            m = m + 1
    z = 18 + 15 ^ x
    return ((x << 3) + z) % 251

if __name__ == "__main__":
    arg = 13
    expected = 78
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
