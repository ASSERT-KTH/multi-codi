# Auto-extracted from ds_lt256k_500.jsonl
# record_id=279  entry=f  input='17'  output='122139'  tokens=96375

def f(x):
    tot = [238, 148, 208, 53, 91]
    tmp = x
    for buf in range(2):
        if tmp * tot[tmp % 5] >= 17:
            x = x * buf & 8191
    if 16 | tmp <= 20:
        for y in range(7):
            x = x & 511
            tot[y % 5] = x - y ^ tmp
        if tmp >= 11:
            t0 = tot[x % 5]
            t1 = x * tmp * tmp
            t2 = t0 // 5 * 15
            tot[x % 5] = t1 * t2 % 97
        else:
            x = x << 2 & x
            t3 = tot[x % 5]
            tot[tmp % 5] = (t3 - tot[tmp % 5]) % 251
    else:
        tmp = tmp << 2
    val = x - tmp - tmp
    cur = (9 - 10) * tmp % 97
    prv = tot[tmp % 5] * 12
    hi = tot[cur % 5] - tmp
    z = 0
    while z < 11:
        t4 = val // 3
        t5 = t4 * (tmp >> 1)
        tmp = t5 % 9973
        z = z + 1
    idx = prv - hi
    u = 0
    while u < 9:
        for v in range(8):
            t6 = (15 ^ 20) - cur
            x = (t6 ^ x) & 65535
            t7 = prv + 16
            t8 = t7 + (6 << 3)
            t9 = v * hi | 16
            t10 = t8 * t9 & 65535
            tot[val % 5] = t10 % 251
        u = u + 1
    t11 = (x ^ cur) - tmp
    return t11 & 131071

if __name__ == "__main__":
    arg = 17
    expected = 122139
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
