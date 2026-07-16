# Auto-extracted from ds_lt256k_500.jsonl
# record_id=451  entry=f  input='2'  output='62326'  tokens=47896

def f(x):
    w = [162, 112, 39, 3, 63, 158]
    if x * x < 42:
        u = 0
        while u < 12:
            t0 = 11 - 14 + u
            w[u % 6] = t0 - x
            t1 = ((x | 15) & 4) - 6
            x = t1 % 4093
            u = u + 1
    if w[x % 6] & 10 >= 9:
        buf = 0
        while buf < 3:
            t2 = 7 * buf - 20
            w[x % 6] = (t2 ^ x) % 251
            buf = buf + 1
        x = x // 4
    for q in range(6):
        t3 = x + w[q % 6]
        t4 = t3 + w[q % 6] // 4
        t5 = w[x % 6] * x | q
        x = (t4 ^ t5) & 8191
        for y in range(19):
            x = (y - x) % 4093
            x = x // 3 // 4 & 131071
        t6 = q - 9 + x
        x = t6 % 4093
    idx = ((x ^ 12) * x ^ x) % 65521
    t7 = idx * w[x % 6] // 3
    p = t7 & 262143
    t8 = w[idx % 6]
    t9 = w[x % 6]
    t10 = t8 ^ p
    e = t10 + (t9 | 15)
    for b in range(2):
        t11 = 17 + 11 - e - x
        x = t11 & 262143
        for z in range(4):
            idx = b + idx & z
            t12 = (p << 1) * 7 >> 3
            idx = (t12 + z) % 4093
            t13 = w[p % 6]
            t14 = t13 * b
            t15 = t14 ^ x << 4
            p = t15 * z % 65521
    tmp = e ^ 11
    return ((x >> 4) - idx) % 65521

if __name__ == "__main__":
    arg = 2
    expected = 62326
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
