# Auto-extracted from ds_lt256k_500.jsonl
# record_id=367  entry=f  input='8'  output='740'  tokens=201883

def rec(n, a):
    if n <= 0:
        return a
    lo = (a + n) % 1009
    t0 = (a | n) * (lo // 8)
    u = (t0 - (n & 2)) % 1009
    for b in range(5):
        a = (a % 251 - 7) % 251
        a = (a & n ^ lo) & 32767
    t1 = lo - n ^ u
    t2 = (t1 ^ a) & 32767
    return rec(n - 1, t2)

def f(x):
    for hi in range(16):
        t0 = 17 & x & 11
        x = t0 * hi & 8191
    t1 = (1 - x) % 1009
    x = rec(105, t1)
    t2 = (9 + x) % 1009
    x = rec(70, t2)
    idx = 19 + 19 | x
    val = 11 + x
    return val + 5 & 1023

if __name__ == "__main__":
    arg = 8
    expected = 740
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
