# Auto-extracted from ds_lt256k_500.jsonl
# record_id=479  entry=f  input='16'  output='0'  tokens=15436

def fn0(a, j):
    w = [202, 68, 58, 231]
    d = j ^ 16
    t0 = (d + d) % 4093
    tmp = t0 >> 1
    tmp = (d + 5 >> 3) * 13
    t1 = w[d % 4]
    t2 = tmp ^ 19
    t3 = t2 & t1 * tmp
    a = t3 >> 2
    t4 = d * 4 * a >> 1
    a = t4 & 1023
    d = j % 4093
    if w[j % 4] | w[tmp % 4] >= 10:
        t5 = w[tmp % 4] - j
        a = t5 * (a - d) & 65535
    return j + d & tmp

def f(x):
    for d in range(13):
        tot = 0
        while tot < 3:
            x = (11 * d - x) % 4093
            t0 = d & tot ^ x
            x = t0 & 8191
            tot = tot + 1
        x = (d - 2) * x % 9973
    if x // 3 < 42:
        if 16 ^ x == 54:
            x = x + 9
            t1 = 17 * x // 2 & 8191
            t2 = x * x & 262143
            x = fn0(t1, t2)
        else:
            x = (x & 13) * x + x
    else:
        for q in range(5):
            t3 = x // 5 + q - q
            x = t3 % 4093
            t4 = q + x | q
            t5 = t4 ^ (x | 20) >> 1
            x = t5 & 2047
        t6 = x << 4 & x
        t7 = (x + x) // 8 - x & 32767
        x = fn0(t6, t7)
    t8 = (x | 3) & 4095
    t9 = (x + x) % 4093
    x = fn0(t8, t9)
    t10 = (18 ^ x) - x
    t11 = (t10 << 4) % 4093
    t12 = (x << 3) % 9973
    x = fn0(t11, t12)
    t13 = x ^ 1 | x
    return t13 // 6 & 1023

if __name__ == "__main__":
    arg = 16
    expected = 0
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
