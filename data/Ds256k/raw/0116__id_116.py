# Auto-extracted from ds_lt256k_500.jsonl
# record_id=116  entry=f  input='11'  output='235'  tokens=66636

def fn0(d, j):
    lo = 13 * j
    t0 = (lo & j) * 7
    q = t0 & d // 4 - d
    q = (15 ^ d) // 2
    lo = lo & 19
    return (q >> 4 >> 4) % 17

def fn1(j, m, g):
    cur = [83, 50, 96, 13, 33, 70]
    j = m - g + 17 & g
    for t in range(7):
        t0 = j * 12
        t1 = t * m
        t2 = t0 ^ t * j
        t3 = t1 * (g // 7)
        g = (t2 + t3) % 17
        for w in range(8):
            t4 = m // 2 & j * m
            t5 = t4 * ((t | m) * w) & 32767
            cur[w % 6] = t5 % 97
            m = (w - m) % 65521
    j = g * m & 262143
    t6 = j ^ g
    t7 = t6 ^ (16 | g)
    t8 = (j // 8 + 12 - j) % 65521
    j = fn0(t7 % 65521, t8)
    g = (j - g) % 97
    t9 = (m - 17) * j
    j = t9 % 17
    g = g + g
    for aux in range(12):
        for cnt in range(9):
            t10 = cnt << 1 ^ g
            g = t10 % 97
            cur[cnt % 6] = (6 - g >> 3) // 5 % 97
        t11 = cur[m % 6] + j
        t12 = (5 ^ aux) + 15
        m = t12 - (t11 >> 3) & 511
        t13 = j << 4 ^ j
        t14 = t13 >> 1 | aux
        g = t14 & 65535
    t15 = m * j - g
    t16 = g + 3 << 3
    return (t15 - t16) % 17

def f(x):
    tmp = [940, 513, 506, 781, 514, 117, 983, 551]
    aux = (x & 7) - 19 ^ x
    t0 = 11 | x
    t1 = tmp[aux % 8]
    t2 = t0 * (x + aux)
    t3 = (t1 >> 1) * 6
    x = t2 | t3
    aux = x | 9
    x = x * aux % 17
    s = 0
    while s < 246:
        t4 = aux - (tmp[aux % 8] | x)
        aux = t4 & 255
        s = s + 1
    t5 = tmp[x % 8] + x
    t6 = x + 18 + t5 + aux
    tmp[aux % 8] = t6 % 1009
    t7 = x - 3 - 6 | aux
    return t7 & 8191

if __name__ == "__main__":
    arg = 11
    expected = 235
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
