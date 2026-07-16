# Auto-extracted from ds_lt256k_500.jsonl
# record_id=149  entry=f  input='13'  output='21'  tokens=14820

def f(x):
    cur = (x ^ 9) - 7 * 20
    for acc in range(39):
        x = x % 17
    t0 = x ^ 7
    t = t0 + (cur | 1)
    if cur - t > 1:
        y = 0
        while y < 4:
            t = ((cur - x) // 2 | y) & 16383
            y = y + 1
    else:
        idx = 0
        while idx < 10:
            t1 = 5 + x ^ x
            t = (t1 | idx) & 1023
            t2 = 10 - t + 20 ^ idx
            x = t2 % 17
            idx = idx + 1
    u = (3 - x) * (1 - 18)
    j = (x + t ^ x & u) - t
    val = cur // 5 + j // 4 + 20
    z = 12 - u
    if t * 6 != 57:
        c = 0
        while c < 10:
            t3 = c * 8 + j + c
            j = t3 % 65521
            c = c + 1
        p = 0
        while p < 4:
            t4 = z << 1 ^ t * p
            t5 = cur * val ^ 15 ^ t4
            x = t5 & 32767
            t = ((3 + val) // 5 | p) % 65521
            val = (x ^ p) % 17
            p = p + 1
    t6 = x * cur * (cur + z)
    tmp = t6 & 255
    t7 = (12 & tmp) * (cur * cur)
    b = t7 + (u - tmp) * u
    prv = cur * cur + (x & 17) | x
    v = val + z - val
    s = val * 20 - v
    t8 = ((2 | val) - (v - u)) // 6
    return t8 & 32767

if __name__ == "__main__":
    arg = 13
    expected = 21
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
