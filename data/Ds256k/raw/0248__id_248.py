# Auto-extracted from ds_lt256k_500.jsonl
# record_id=248  entry=f  input='15'  output='2355'  tokens=196557

def rec(n, a):
    if n <= 0:
        return a
    d = a - 20 - n & 32767
    t0 = n - a
    t1 = t0 + (a >> 1)
    return rec(n - 1, t1 & 16383)

def fn0(j):
    cur = (j ^ 17) + (17 + j)
    b = 0
    while b < 11:
        cur = (b | j) & 32767
        b = b + 1
    for m in range(5):
        cur = (cur ^ j) & 131071
    buf = 0
    while buf < 6:
        cur = j + cur & 8191
        j = (buf | j) % 251
        buf = buf + 1
    if cur << 3 <= 26:
        t0 = 8 + cur | cur + j
        cur = t0 + (j + cur + cur)
    t1 = cur - j
    t2 = j + j
    t3 = t1 - (j - cur)
    t4 = t2 * (j % 251)
    return t3 & t4

def f(x):
    for idx in range(2955):
        x = ((idx ^ 1) * idx + x) % 4093
    x = fn0((x * x + x) // 3 % 4093)
    x = fn0((4 | 3) * (x - 17) & 8191)
    z = 11 - x >> 1
    t0 = x * x ^ z
    w = t0 % 17
    x = w + x << 1
    return x // 7 - w & 262143

if __name__ == "__main__":
    arg = 15
    expected = 2355
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
