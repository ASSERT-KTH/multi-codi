# Auto-extracted from ds_lt256k_500.jsonl
# record_id=80  entry=f  input='16'  output='425'  tokens=57065

def rec(n, a):
    if n <= 0:
        return a
    b = (n << 3 >> 3 ^ a) & 131071
    t0 = (b >> 3) + a - b
    return rec(n - 1, t0 % 251)

def f(x):
    for y in range(3):
        idx = 0
        while idx < 43:
            t0 = ((idx & y) + y * idx) * idx
            x = (t0 ^ x) % 17
            x = idx - x - x & 255
            t1 = x << 3 ^ y
            x = t1 << 2 & 2047
            idx = idx + 1
    p = 0
    while p < 11:
        for t in range(10):
            x = (p | 13) + x & 32767
        t2 = 1 - 4 + x
        x = t2 & 4095
        p = p + 1
    t3 = 8 - x >> 1
    aux = t3 // 5
    t4 = (13 * 18 & x) - aux
    return t4 & 2047

if __name__ == "__main__":
    arg = 16
    expected = 425
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
