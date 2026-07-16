# Auto-extracted from ds_lt256k_500.jsonl
# record_id=391  entry=f  input='17'  output='0'  tokens=138956

def rec(n, a):
    if n <= 0:
        return a
    t0 = n >> 2 ^ a
    a = t0 & 131071
    t1 = (n << 3) * 3
    t2 = t1 % 1009 | a
    a = t2 % 4093
    a = ((n + n) // 3 | a) % 4093
    t3 = n * a % 251
    return rec(n - 1, t3)

def fn0(e, d, c):
    for res in range(6):
        c = e + res & 8191
        e = (res + e) // 6 & 131071
    t0 = e * e
    t1 = t0 | d ^ e
    c = rec(115, t1 % 97)
    e = c ^ d
    t2 = (c + d) * e
    d = t2 & 511
    return (c + 6 + d) % 97

def fn1(b, g):
    tmp = 0
    while tmp < 11:
        t0 = b - 1 + g
        g = (t0 - (g + g >> 2)) % 97
        b = b + 10 & 32767
        b = (2 + g ^ b) & 262143
        tmp = tmp + 1
    val = (12 ^ g) - g
    t1 = b * val & 2047
    b = rec(72, t1)
    for v in range(4):
        g = (val + val ^ g) & 8191
        if g ^ val < 1:
            g = v * b & 255
            b = ((1 | g) ^ b) % 65521
    val = g - val >> 4
    return (g ^ 7) * b - val & 8191

def f(x):
    g = [311, 333, 901, 611, 861, 998]
    t0 = g[x % 6] ^ 9
    t1 = x - 17 - x
    hi = t1 - (t0 + (x - 3))
    t2 = g[x % 6] + x
    t3 = x * g[x % 6]
    t4 = (x | 16) ^ hi
    t5 = t4 * (t2 & t3) & 8191
    t6 = g[hi % 6]
    t7 = hi & 10 | x + hi
    t8 = t7 ^ (hi ^ 7 ^ t6)
    t9 = (x - hi + hi) % 65521
    hi = fn0(t5, t8 & 511, t9)
    aux = 20 + hi
    b = hi + x ^ aux
    g[hi % 6] = 16 & b | x
    if 7 + hi > 54:
        if g[b % 6] - 5 > 56:
            g[hi % 6] = 5 & hi
        else:
            aux = x << 1
            t10 = (x + x) * (18 * 8) << 4
            g[hi % 6] = t10 % 1009
    t11 = g[hi % 6]
    for q in range(101):
        if 14 * 13 ^ hi <= 5:
            t12 = b >> 1 << 1
            x = (t12 | q) % 65521
            g[q % 6] = g[b % 6] >> 4 << 2
        else:
            t13 = (aux + q) % 97
            t14 = g[q % 6]
            hi = (t13 ^ t14) & 4095
        aux = b & aux
        if q | x == 45:
            t15 = g[aux % 6]
            g[q % 6] = (hi - t15) % 1009
    return t11 * aux % 251

if __name__ == "__main__":
    arg = 17
    expected = 0
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
