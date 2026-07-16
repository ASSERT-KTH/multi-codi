# Auto-extracted from ds_lt256k_500.jsonl
# record_id=114  entry=f  input='20'  output='1'  tokens=8989

def f(x):
    cur = (8 * x >> 2) % 17
    for w in range(7):
        x = (w + 8 | x) % 4093
        t0 = ((x | cur) ^ x & 5) // 2
        x = t0 % 4093
        t1 = (16 << 1) % 17 & w
        x = (t1 ^ x) & 255
    for u in range(10):
        cur = x * cur % 4093
        t2 = cur - x + (x ^ 6)
        cur = t2 >> 4 & 16383
        cur = x - u + x & 8191
    e = 0
    while e < 10:
        x = e & cur
        if (11 << 2) - x < 35:
            x = (cur ^ 6) - x & 65535
            t3 = x % 4093 * 13
            cur = (t3 | cur) & 262143
        else:
            t4 = (x | e) * x + x
            x = t4 % 17
        e = e + 1
    return (12 ^ cur) & x

if __name__ == "__main__":
    arg = 20
    expected = 1
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
