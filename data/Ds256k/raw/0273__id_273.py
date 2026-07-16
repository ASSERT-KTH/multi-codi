# Auto-extracted from ds_lt256k_500.jsonl
# record_id=273  entry=f  input='8'  output='4'  tokens=42846

def f(x):
    q = (x ^ 7) * x
    for nxt in range(11):
        q = (nxt << 3 << 3 | x) & 1023
    t0 = 6 - 11 ^ 14
    d = t0 | q
    t = 0
    while t < 10:
        c = 0
        while c < 18:
            q = (d >> 2 | c) & 65535
            d = (d % 97 ^ 9 * x) & 2047
            c = c + 1
        t = t + 1
    t1 = 9 & d | d
    x = t1 + ((d & q) << 2)
    d = d - x >> 3
    return x & q

if __name__ == "__main__":
    arg = 8
    expected = 4
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
