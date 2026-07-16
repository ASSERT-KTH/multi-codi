# Auto-extracted from ds_lt256k_500.jsonl
# record_id=447  entry=f  input='2'  output='56'  tokens=89353

def f(x):
    w = [37, 960, 563, 782, 837]
    if 16 * x < 56:
        x = x * (x * x)
        t0 = w[x % 5]
        x = x - t0
    for b in range(2):
        x = b * x % 65521
        if b + x != 37:
            t1 = b | w[b % 5]
            t2 = t1 - (19 + b) | 11
            x = t2 - x & 1023
            t3 = (b ^ 13 ^ b) - b
            w[b % 5] = (t3 + x) % 1009
        if x | 12 < 60:
            t4 = x + w[b % 5] & 19
            t5 = (w[x % 5] & x) + b
            x = t4 * t5 & 511
            w[x % 5] = (b + b | x) % 1009
    t6 = w[x % 5]
    t7 = 11 * x + x
    t8 = x * t6 >> 3
    a = t7 & t8
    val = (11 ^ 18 + a) & 255
    y = 1 * val + x
    v = 0
    while v < 122:
        t9 = a * v + x
        x = t9 % 9973
        t10 = w[val % 5] * a
        val = t10 * y % 65521
        v = v + 1
    w[val % 5] = 8 * x % 1009
    s = y - a + y
    t11 = w[val % 5]
    t12 = (t11 ^ 7) * a
    return t12 & 255

if __name__ == "__main__":
    arg = 2
    expected = 56
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
