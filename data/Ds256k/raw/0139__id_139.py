# Auto-extracted from ds_lt256k_500.jsonl
# record_id=139  entry=f  input='17'  output='469'  tokens=17504

def f(x):
    t0 = (x ^ 10) * (x ^ 5)
    idx = t0 ^ x
    y = (x ^ 1) - 14 - idx
    if y - 3 < 58:
        t1 = 19 & y ^ y
        t2 = y * 12 + x
        x = t1 - t2
        res = 0
        while res < 12:
            t3 = res << 4 ^ x
            t4 = idx * res - y
            idx = t3 * t4 % 9973
            t5 = y * 14 + 4
            idx = (t5 | res) & 262143
            y = (y | x) & 2047
            res = res + 1
    else:
        z = 0
        while z < 7:
            y = (8 + x ^ z) % 1009
            z = z + 1
        c = 0
        while c < 2:
            t6 = (10 << 1) + (idx ^ c)
            t7 = y + x % 1009 | t6
            x = t7 % 1009
            idx = y - c - idx & 262143
            x = ((y ^ c) >> 3 << 3) % 9973
            c = c + 1
    t8 = (y | x) ^ y - 18
    x = (x << 3 >> 1) * t8 % 1009
    y = x // 5
    t9 = y // 7
    x = t9 - (x << 1)
    for a in range(17):
        y = (a + y ^ idx) & 16383
        t10 = a - 13
        t11 = t10 ^ (a ^ y)
        x = (t11 ^ 11) % 9973
    return (y ^ x) % 1009

if __name__ == "__main__":
    arg = 17
    expected = 469
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
