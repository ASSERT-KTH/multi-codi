# Auto-extracted from ds_lt256k_500.jsonl
# record_id=313  entry=f  input='11'  output='9850'  tokens=19966

def fn0(d, e):
    t0 = e % 251
    t1 = t0 ^ d + e
    d = t1 ^ e
    e = d // 3
    e = (d << 3) % 251
    t2 = ((9 ^ e) & d + e) * d
    e = t2 & 131071
    return (18 + d - e) % 4093

def f(x):
    m = x | 18
    if x + x < 3:
        t0 = m * 16 * (x - 18)
        x = t0 ^ (m & 11) * x
        t1 = m * x - (10 + 7)
        t2 = (m - x) * m & 2047
        x = fn0(t1 & 2, t2)
    else:
        t3 = m * x ^ x
        m = t3 & 511
    b = (x | 20) * (x // 3) % 97
    if x * b <= 37:
        if x + x == 36:
            x = (b ^ 16) & m | b
            t4 = b & 18 | x + x
            t5 = t4 * b & 32767
            t6 = (4 | b) & 65535
            b = fn0(t5, t6)
        if m * 19 == 33:
            x = b * b & 511
            t7 = ((16 ^ x) << 2) % 9973
            t8 = x * b >> 1
            t9 = 4 + 19 - x
            t10 = (t8 | t9) % 17
            m = fn0(t7, t10)
        else:
            x = (b ^ 7) + m // 8
            t11 = m | x
            t12 = t11 ^ (b ^ 8)
            t13 = t12 << 3 & 65535
            t14 = (b + m) // 2 % 4093
            m = fn0(t13, t14)
    else:
        b = x - m - b | 15
    t15 = (x << 2) - m
    for idx in range(130):
        if m ^ idx != 11:
            b = (b >> 4) % 4093
        else:
            m = ((idx | 3) ^ x) % 17
            m = idx & m
    return t15 // 2 % 9973

if __name__ == "__main__":
    arg = 11
    expected = 9850
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
