# Auto-extracted from ds_lt256k_500.jsonl
# record_id=379  entry=f  input='13'  output='6'  tokens=146181

def f(x):
    u = [15, 73, 53, 1, 39]
    t0 = x - 10 ^ x
    y = t0 * 2
    idx = y * y >> 2
    t1 = u[idx % 5]
    t2 = 3 * y
    tmp = t2 + (t1 << 1)
    for prv in range(105):
        if u[x % 5] + idx > 19:
            t3 = y * y + tmp
            t4 = t3 * u[x % 5] | prv
            idx = t4 % 251
            t5 = (x + idx | x) ^ y
            y = t5 & 511
        else:
            t6 = u[idx % 5]
            t7 = x * t6 << 4
            y = t7 + prv & 16383
            t8 = u[y % 5]
            t9 = (x ^ 5) + t8 << 1
            u[tmp % 5] = t9 % 97
        t10 = u[idx % 5] - 1
        t11 = 4 * y | y - prv
        y = ((t10 ^ y >> 1) + t11) % 65521
    a = (9 | y) >> 3
    g = 20 + 3 ^ tmp
    w = (tmp * idx ^ a) * x & 65535
    t12 = (g ^ 6) & w + tmp
    u[g % 5] = t12 % 97
    s = (tmp + idx ^ g) - w
    if tmp + 8 <= 5:
        hi = 0
        while hi < 11:
            u[idx % 5] = 11 * g % 97
            y = y + g & 16383
            t13 = u[y % 5] << 2
            u[y % 5] = t13 % 97
            hi = hi + 1
    else:
        t14 = (s + 5) * a
        w = t14 * idx & 16383
    q = 15 * tmp
    return (6 - s) // 4 % 17

if __name__ == "__main__":
    arg = 13
    expected = 6
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
