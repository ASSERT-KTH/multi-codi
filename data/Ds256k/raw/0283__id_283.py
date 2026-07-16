# Auto-extracted from ds_lt256k_500.jsonl
# record_id=283  entry=f  input='8'  output='6791'  tokens=32176

def fn0(b, g):
    m = [58, 149, 46, 188, 74, 70, 189, 157]
    for v in range(12):
        if b * m[g % 8] != 55:
            t0 = (g | b) * b
            g = (t0 | 10) % 9973
            m[b % 8] = (g - b) % 251
        b = (v & 15 ^ b) & 65535
        t1 = m[g % 8] ^ 14
        t2 = (b ^ v) * t1 >> 1
        g = t2 & 131071
    res = m[g % 8] - 14
    if 12 - m[b % 8] <= 2:
        b = b * res % 251
        t3 = (res & 9) + res
        t4 = m[res % 8]
        g = t3 | t4
    for acc in range(9):
        res = (res << 3) // 5 % 251
    t5 = (g >> 1) + g ^ res
    return t5 % 9973

def f(x):
    t = (5 * x >> 1) + 6
    if x * 1 >= 13:
        for u in range(7):
            t0 = 1 * x
            t1 = t0 + (t & 7)
            x = t1 % 65521
            t2 = u * u - (x - u)
            t3 = (x - t) * x * t2
            t = t3 & 131071
            t = x & u
    else:
        t = 14 * t & 32767
    t4 = 20 * t
    t5 = t4 - (x & 19)
    cnt = (t5 + t) % 97
    t6 = 5 - cnt
    t7 = t6 & cnt - x
    val = t7 * 17
    t8 = (val | 10) * t & x
    t9 = cnt // 3 + (9 << 4)
    t10 = (t9 ^ x) & 511
    t = fn0(t8, t10)
    hi = (7 & t) + cnt
    s = hi * cnt + hi
    v = t * t & 131071
    t11 = (s - t) % 251
    t12 = (v ^ 11) % 65521
    t = fn0(t11, t12)
    j = x * s - 14 & 131071
    t13 = 12 & x & t * cnt
    t14 = (s * 1 | val) + t13
    for a in range(17):
        s = ((val + x) % 17 | a) & 2047
        t15 = hi + 16 | s
        s = t15 % 65521
        v = v * t % 65521
    return t14 % 65521

if __name__ == "__main__":
    arg = 8
    expected = 6791
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
