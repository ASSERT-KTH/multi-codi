# Auto-extracted from ds_lt256k_500.jsonl
# record_id=108  entry=f  input='12'  output='114'  tokens=71426

def rec(n, a):
    if n <= 0:
        return a
    t0 = n + n
    t1 = (a + n) // 7
    t2 = t0 ^ a + 16
    b = (t1 ^ t2) & 255
    t3 = (n * a & (a ^ b)) // 4
    a = t3 & 16383
    t4 = (a - n) % 17
    return rec(n - 1, t4)

def f(x):
    t0 = x * 17 - x
    j = t0 - (x & 8) * 11
    t1 = j << 2
    c = t1 + (j >> 2)
    d = j // 7
    t2 = d | x
    t3 = t2 + (c & j)
    t4 = (c + 1) // 7
    d = t3 + t4
    d = x * x * j ^ x
    t5 = 4 - 7 - c << 1
    for aux in range(272):
        if aux - 13 - j <= 32:
            t6 = (aux & 5) - x
            x = t6 % 251
    return t5 % 251

if __name__ == "__main__":
    arg = 12
    expected = 114
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
