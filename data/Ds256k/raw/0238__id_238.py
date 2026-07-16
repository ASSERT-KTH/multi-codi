# Auto-extracted from ds_lt256k_500.jsonl
# record_id=238  entry=f  input='11'  output='16'  tokens=67899

def fn0(a, j):
    g = [895, 497, 622, 438, 109, 90, 72, 473]
    t0 = (j & 13) - (a & 15)
    g[j % 8] = (t0 + g[j % 8]) % 1009
    cur = 12 & a
    t1 = (g[cur % 8] + a) % 65521
    g[j % 8] = t1 % 1009
    t2 = 1 * g[a % 8]
    d = t2 - j
    t3 = g[j % 8] // 6
    j = t3 + (d - cur)
    cur = j // 2
    return (cur + d) % 1009

def f(x):
    for q in range(5):
        t0 = q & 18
        t1 = t0 * (q | x)
        x = t1 % 9973
        for idx in range(104):
            x = (q + x) % 65521
        for lo in range(2):
            x = (x * q ^ x | q) % 17
            t2 = x * x ^ 8
            x = t2 % 9973
    cnt = 0
    while cnt < 12:
        t3 = cnt + cnt - x
        x = t3 % 9973
        t4 = x * cnt - cnt
        x = t4 * (cnt - 13 & cnt) % 65521
        cnt = cnt + 1
    t5 = x // 4 & 16383
    t6 = (x | 9) % 9973
    x = fn0(t5, t6)
    m = x | 3
    if x * m >= 14:
        t7 = (x + x) * (m * x) | m
        m = t7 % 17
    else:
        t8 = (x * 5 ^ m) * x
        x = t8 % 251
    t9 = (19 - m) % 17
    t10 = m >> 4 & 32767
    x = fn0(t9, t10)
    t11 = 4 * x
    t12 = m ^ 8 ^ x
    t13 = t11 + m // 2
    return (t12 + t13) % 17

if __name__ == "__main__":
    arg = 11
    expected = 16
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
