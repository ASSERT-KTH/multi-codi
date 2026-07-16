# Auto-extracted from ds_lt256k_500.jsonl
# record_id=310  entry=f  input='16'  output='1962'  tokens=86980

def rec(n, a):
    if n <= 0:
        return a
    prv = n >> 1 & a & a
    t0 = (a | 20) >> 2
    c = t0 * ((n ^ 13) * a) % 17
    t1 = prv << 1 & a - 6 ^ c
    c = t1 % 17
    return rec(n - 1, prv & a)

def fn0(a, b):
    cnt = [5, 26, 43, 63, 18]
    t0 = cnt[b % 5] * a
    t1 = b + a >> 1
    t2 = t1 * (t0 + a) % 17
    a = rec(69, t2)
    t3 = a - b
    t4 = t3 ^ (a ^ 13)
    a = rec(118, t4 & 16383)
    a = b & a
    return (15 ^ b) & 1023

def f(x):
    val = x | 18
    y = 2 - 15 | val
    for cur in range(594):
        if x + val == 17:
            x = (x ^ cur) * y % 4093
            t0 = cur * val // 4
            val = (t0 ^ y) % 65521
        y = 10 + cur & (y & val)
        y = (cur + val) % 251
    return y * val % 4093

if __name__ == "__main__":
    arg = 16
    expected = 1962
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
