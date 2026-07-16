# Auto-extracted from ds_lt256k_500.jsonl
# record_id=145  entry=f  input='9'  output='3'  tokens=200652

def rec(n, a):
    if n <= 0:
        return a
    v = (a & 18 | n) & 131071
    t0 = (v << 2) + (v + v) + a
    return rec(n - 1, t0 & 2047)

def fn0(e):
    aux = [14, 51, 75, 15, 85, 21, 54]
    g = e + e - e
    if g - e <= 50:
        g = aux[e % 7] + 18
        for buf in range(7):
            t0 = buf * aux[buf % 7]
            t1 = t0 - (e >> 4) + buf
            g = t1 % 251
            t2 = aux[e % 7] + g - 9
            aux[e % 7] = t2 % 97
            e = (g - 2 ^ e) & 131071
    else:
        aux[e % 7] = g // 5 * e % 1009 % 97
        e = aux[g % 7] + e
    if e + e != 35:
        t3 = g * g * g
        t4 = (t3 ^ g) % 251
        aux[g % 7] = t4 % 97
    if e - g == 2:
        t5 = (g ^ 13) * (e * g)
        t6 = t5 - aux[e % 7]
        e = t6 % 251
        t7 = aux[g % 7]
        e = t7 // 5
    else:
        t8 = (g - e) % 251
        g = rec(104, t8)
    u = 0
    while u < 7:
        g = (e >> 1) - g & 8191
        aux[e % 7] = (10 * 19 ^ e) % 97
        u = u + 1
    j = (e + e ^ 20) - g
    t9 = (2 - j) // 5
    return t9 % 251

def f(x):
    t0 = 9 & x
    t1 = t0 + (5 + x)
    cur = t1 - x
    b = x & 3
    y = 11 * cur
    for v in range(1109):
        t2 = 3 + cur - x * b
        b = t2 % 251
    return (cur ^ 13) % 9973

if __name__ == "__main__":
    arg = 9
    expected = 3
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
