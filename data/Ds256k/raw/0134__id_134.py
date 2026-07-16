# Auto-extracted from ds_lt256k_500.jsonl
# record_id=134  entry=f  input='12'  output='7262'  tokens=177231

def rec(n, a):
    if n <= 0:
        return a
    t0 = 16 * a + (a - 17) + n
    u = t0 % 9973
    prv = (a - 17 ^ n) % 1009
    t1 = (14 - 20 + 10 ^ a) % 251
    return rec(n - 1, t1)

def f(x):
    t0 = (x << 2) * (x - 9)
    acc = t0 ^ x
    aux = x - 5
    b = x * acc >> 1
    tmp = b >> 1
    t1 = (tmp >> 2) % 17
    tmp = rec(93, t1)
    aux = rec(100, tmp & x)
    t2 = (x ^ 10) - b
    for prv in range(28):
        s = 0
        while s < 7:
            tmp = (x - tmp) % 4093
            t3 = (aux ^ b) + (tmp + prv)
            tmp = t3 & 262143
            t4 = prv - 12 - aux
            x = (t4 - x) % 4093
            s = s + 1
        tmp = ((b - 10) // 3 | tmp) & 8191
    return t2 & 8191

if __name__ == "__main__":
    arg = 12
    expected = 7262
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
