# Auto-extracted from ds_lt256k_500.jsonl
# record_id=389  entry=f  input='10'  output='28'  tokens=135323

def rec(n, a):
    if n <= 0:
        return a
    t0 = (11 ^ n) - n ^ a
    a = t0 & 262143
    t1 = (a - 4) % 9973
    return rec(n - 1, t1)

def fn0(c):
    idx = c >> 2 ^ c - 15
    e = 17 - c >> 1 & c
    if c ^ e == 5:
        t0 = 1 & e
        idx = t0 & e * 8
    j = (c * 5 & (e ^ c)) - 3
    t1 = j & 1
    t2 = e * idx
    t3 = t1 - e % 17
    t4 = t2 - (j - 18)
    return (t3 ^ t4) & 65535

def f(x):
    d = [184, 162, 226, 177, 30, 88]
    t0 = d[x % 6]
    z = (x & 16) * t0
    nxt = x | 17
    if x & nxt <= 11:
        z = nxt ^ 1
        for tmp in range(2):
            x = x * x * x % 1009
    t1 = d[z % 6]
    t2 = x // 7 - t1
    res = t2 & nxt
    q = d[nxt % 6] + res - z
    cur = d[q % 6] + res
    idx = 0
    while idx < 117:
        t3 = d[nxt % 6]
        t4 = t3 * x & q
        q = (t4 ^ cur) % 9973
        t5 = (z ^ q) + res
        res = t5 & 511
        if 16 + 5 - q < 31:
            t6 = 15 ^ cur ^ idx
            x = t6 % 9973
            x = nxt + x & 255
        else:
            t7 = 18 * res + idx
            z = t7 % 65521
        idx = idx + 1
    return (q ^ 8) // 2 % 9973

if __name__ == "__main__":
    arg = 10
    expected = 28
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
