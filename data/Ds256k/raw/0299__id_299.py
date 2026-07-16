# Auto-extracted from ds_lt256k_500.jsonl
# record_id=299  entry=f  input='11'  output='235'  tokens=87362

def rec(n, a):
    if n <= 0:
        return a
    for e in range(8):
        t0 = (n | 4) ^ 9 & 3
        a = (t0 + e + a) % 9973
        if (e ^ 4) + a > 35:
            t1 = 5 * n & (e ^ 20)
            a = (t1 - a) % 97
        else:
            a = (e - a) % 9973
    a = a >> 1 & 2047
    t2 = a * n
    t3 = t2 * (n + a)
    a = t3 & 255
    t4 = 11 + 4 - (14 + a)
    return rec(n - 1, t4 % 9973)

def fn0(b, m):
    idx = [421, 63, 585, 751, 44, 415, 764]
    cnt = b >> 1 << 2
    t0 = idx[cnt % 7]
    t1 = (b | t0) // 7
    val = t1 + cnt
    idx[b % 7] = 6 * m % 1009
    t2 = (b - m) * (b + cnt)
    t3 = val - 13 + b - t2
    cnt = t3 & 255
    t4 = cnt * cnt ^ (val ^ b)
    return t4 % 4093

def f(x):
    lo = x * x // 3 * x
    s = x | lo
    for m in range(6):
        t0 = (lo & m) + (s - x)
        x = t0 % 9973
        for tmp in range(65):
            t1 = x * tmp * m
            lo = t1 & 2047
            lo = (s - m) // 4 - lo & 255
    y = 8 & lo ^ (s ^ x)
    q = s + y >> 3
    if x ^ q != 54:
        x = ((y | 2) & x - 3) // 7
    t2 = (y ^ 9) >> 3
    x = t2 + (1 + 18)
    x = y - q
    return (x ^ s) % 9973

if __name__ == "__main__":
    arg = 11
    expected = 235
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
