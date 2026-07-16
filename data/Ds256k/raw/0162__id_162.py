# Auto-extracted from ds_lt256k_500.jsonl
# record_id=162  entry=f  input='1'  output='29'  tokens=28032

def rec(n, a):
    if n <= 0:
        return a
    if (n | 17) ^ a < 57:
        a = n + a & (n | 7)
    for t in range(6):
        a = (a + 9) % 65521
    t0 = a * n % 97
    return rec(n - 1, t0)

def f(x):
    prv = [87, 323, 195, 641, 989]
    prv[x % 5] = x * x - 2 + x
    tot = x - 6 + x * x
    t0 = prv[tot % 5]
    cnt = t0 + 16
    t1 = cnt - tot
    t2 = t1 & tot - 13
    v = t2 & x
    m = tot - cnt & 10
    m = tot - v
    t3 = prv[v % 5]
    t4 = prv[m % 5]
    t5 = x + t3 ^ t4
    cnt = t5 >> 2
    x = cnt * x - tot
    t6 = prv[v % 5] // 3
    for w in range(50):
        t7 = 1 * cnt ^ v
        v = t7 % 1009
        t8 = (v - 20) // 8
        cnt = (t8 | cnt) & 511
    return t6 % 4093

if __name__ == "__main__":
    arg = 1
    expected = 29
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
