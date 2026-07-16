# Auto-extracted from ds_lt256k_500.jsonl
# record_id=97  entry=f  input='13'  output='110'  tokens=99625

def fn0(c):
    val = 20 * 5 | c
    w = (c - 15) // 5
    t0 = (c & w) - w * w
    z = t0 * c & 65535
    t1 = (z | w) ^ z << 3
    idx = t1 * val % 17
    for prv in range(6):
        t2 = idx + idx | z
        z = t2 % 4093
    t3 = 9 ^ val ^ 2
    y = t3 * idx & 511
    w = z ^ y
    if idx + 17 >= 14:
        z = val + val
    t4 = w - y - 17
    return t4 % 4093

def f(x):
    z = [227, 48, 88, 67]
    for tmp in range(11):
        t0 = z[x % 4]
        t1 = tmp * x
        t2 = t1 - tmp * t0
        x = t2 % 251
        t3 = (z[tmp % 4] | tmp) + x
        x = t3 % 4093
        t4 = z[x % 4] * tmp
        x = t4 % 17
    j = 0
    while j < 4:
        for a in range(91):
            x = (x + x) % 4093
            z[j % 4] = ((a + a << 1) - x) % 251
        x = (2 ^ 15 | x) & 1023
        z[j % 4] = (j + x - 2) % 251
        j = j + 1
    nxt = x + x
    hi = 0
    while hi < 3:
        t5 = z[nxt % 4]
        t6 = 7 & 19
        t7 = t6 * (t5 * 18)
        nxt = t7 % 17
        t8 = z[nxt % 4]
        z[hi % 4] = (t8 + 1) % 251
        hi = hi + 1
    t9 = z[nxt % 4] >> 3
    p = t9 * (11 * x) & 32767
    t10 = (8 ^ nxt) // 5
    t11 = t10 + (nxt * nxt + nxt)
    return t11 & 4095

if __name__ == "__main__":
    arg = 13
    expected = 110
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
