# Auto-extracted from ds_lt256k_500.jsonl
# record_id=427  entry=f  input='12'  output='90'  tokens=49678

def rec(n, a):
    if n <= 0:
        return a
    idx = (9 ^ n | a) % 1009
    idx = n * 4 + a & 16383
    t0 = n * a - idx
    t1 = t0 & (a >> 2) - 19
    return rec(n - 1, t1)

def fn0(b, g):
    buf = [161, 28, 95, 58, 59, 135]
    t0 = (g | b) ^ b
    t1 = t0 << 3 & 32767
    b = rec(83, t1)
    idx = (b | 5) - buf[g % 6]
    tot = g >> 2
    c = (1 ^ idx) * idx & 32767
    t2 = (c - b) * (b // 8) * b
    b = t2 % 251
    tot = 18 * 10 - b
    return (9 | c) * idx % 4093

def f(x):
    s = 0
    while s < 9:
        for idx in range(21):
            x = ((s | idx) ^ x) & 32767
        t0 = (13 & s) * x
        x = (t0 - x) % 65521
        s = s + 1
    acc = (x ^ 9) << 4 & 262143
    t1 = (acc ^ 15) & x + acc
    w = t1 - 15
    t2 = (x * w - (x & w)) % 97
    x = rec(68, t2)
    t3 = acc * w - 17 * x ^ 16
    return t3 % 97

if __name__ == "__main__":
    arg = 12
    expected = 90
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
