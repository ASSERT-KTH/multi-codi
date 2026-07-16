# Auto-extracted from ds_lt256k_500.jsonl
# record_id=474  entry=f  input='18'  output='4953'  tokens=105884

def f(x):
    t0 = x - 3 - 15
    g = t0 ^ (x * x ^ x)
    cnt = (x | g) * x
    t1 = g - x - (5 ^ 10)
    val = t1 - x * 6
    acc = x ^ 19
    hi = x | g
    m = (val + 7 | acc - hi) // 7
    t2 = 7 * x + cnt
    p = t2 // 3
    for d in range(7):
        cnt = (p * g ^ cnt) % 9973
        for v in range(21):
            t3 = (hi + 10) * val - hi | cnt
            cnt = t3 & 16383
            t4 = val << 3 >> 3 ^ cnt
            cnt = t4 & 8191
        y = 0
        while y < 4:
            x = (y ^ hi) & 15
            t5 = (m ^ cnt) * 4 // 8
            acc = (t5 + acc) % 9973
            y = y + 1
    for c in range(12):
        t6 = (cnt ^ 15) & m >> 3
        cnt = (t6 ^ x) & 16383
        hi = ((val >> 3) - c) % 9973
    t7 = g & hi
    t8 = t7 * (hi + m)
    e = t8 % 65521
    t9 = (12 * 15 | (p | 7)) ^ acc
    return t9 & 16383

if __name__ == "__main__":
    arg = 18
    expected = 4953
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
