# Auto-extracted from ds_lt256k_500.jsonl
# record_id=62  entry=f  input='15'  output='22'  tokens=67815

def fn0(d):
    z = [23, 88, 47, 34, 59]
    if d - 9 == 40:
        t0 = 4 + d >> 4
        z[d % 5] = t0 % 97
        for u in range(2):
            z[d % 5] = ((u - 10 ^ 20) + d) % 97
    t1 = z[d % 5]
    t2 = 7 * d
    t3 = t2 * (d * t1)
    hi = t3 * d & 262143
    if 8 | hi < 52:
        t4 = z[hi % 5]
        hi = (t4 | d) // 8
    t5 = hi * 19 % 251
    z[hi % 5] = t5 % 97
    t6 = z[d % 5]
    t7 = d * t6 - 16
    return (t7 ^ hi) % 17

def f(x):
    cur = [0, 3, 91, 21, 33]
    tmp = x * x
    hi = ((x & 4) << 3) * tmp
    x = tmp + 12
    t0 = (hi ^ 8 ^ hi % 9973) + 14
    for q in range(2):
        if 13 | hi == 41:
            t1 = tmp * q << 4
            x = t1 % 17
            t2 = (q - hi) // 3
            x = (t2 >> 4) % 65521
        for e in range(161):
            x = (11 ^ hi | e) & 65535
            x = (hi ^ cur[x % 5]) & 16383
        res = 0
        while res < 10:
            t3 = 14 - 15 + tmp
            cur[res % 5] = t3 % 97
            res = res + 1
    return t0 % 9973

if __name__ == "__main__":
    arg = 15
    expected = 22
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
