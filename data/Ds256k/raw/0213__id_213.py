# Auto-extracted from ds_lt256k_500.jsonl
# record_id=213  entry=f  input='15'  output='4'  tokens=10771

def rec(n, a):
    if n <= 0:
        return a
    u = n * a % 97
    t0 = 8 + 9 << 4 >> 4
    a = t0 + u + n & 8191
    a = (3 * 17 - a) % 97
    t1 = n >> 4 | u & 2
    t2 = (t1 | a) % 97
    return rec(n - 1, t2)

def f(x):
    t0 = 13 | x
    w = t0 * (x | 5)
    cur = x ^ 13 ^ x & w ^ 4
    c = w * cur * (12 + x) % 9973
    w = w - cur
    cur = w ^ cur ^ 3 * w
    for tmp in range(103):
        w = ((c ^ w) >> 1) % 9973
    return ((3 | w) ^ (13 | 19)) & x

if __name__ == "__main__":
    arg = 15
    expected = 4
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
