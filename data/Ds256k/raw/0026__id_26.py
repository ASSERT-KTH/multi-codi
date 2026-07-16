# Auto-extracted from ds_lt256k_500.jsonl
# record_id=26  entry=f  input='6'  output='4095'  tokens=79359

def fn0(j, m):
    u = [49, 40, 13, 86, 42, 56, 91]
    lo = (j | m) - 17
    t0 = j % 97 - m
    aux = t0 // 5
    if m - 17 < 44:
        t1 = u[lo % 7] | j
        t2 = aux - m - t1
        m = t2 - ((j ^ 6) + j)
    else:
        j = lo // 8
    j = 5 * aux
    m = m * aux % 97
    m = lo - 5
    v = 0
    while v < 11:
        t3 = aux - 10 - (aux - m)
        m = t3 % 97
        t4 = (20 + 8 & 8) - lo
        lo = t4 & 8191
        v = v + 1
    m = j - u[j % 7]
    t5 = (aux - 7) * (lo + 5) << 1
    return t5 & 2047

def fn1(e, c):
    idx = [9, 34, 74, 12, 29, 67, 34, 76]
    tot = 0
    while tot < 7:
        if c % 251 >= 64:
            idx[c % 8] = (9 + 9 - e) % 97
            e = (17 - c << 3 | e) % 97
        idx[tot % 8] = (c >> 4) % 97
        tot = tot + 1
    t0 = idx[e % 8] * 20
    t1 = (t0 + (12 - e)) * c % 251
    t2 = (16 ^ e) % 251
    e = fn0(t1, t2)
    val = 6 - e
    if val + c >= 29:
        t3 = 8 + c & c >> 4
        c = 17 & 20 ^ t3
    else:
        if 2 - idx[val % 8] >= 12:
            idx[c % 8] = e % 251 & 18
        else:
            t4 = val & c & c
            val = t4 | val
            t5 = idx[c % 8]
            t6 = 2 + val - c
            t7 = e * val + t5
            val = t6 - t7 & 16383
        e = 13 & c
    return (c - val) * 3 % 65521

def f(x):
    u = x & 16
    b = u ^ 16
    v = 2 << 3 | b
    g = 14 - v - v >> 1
    tot = v - 9 + 19
    t0 = (v ^ u) * tot
    t1 = (7 & 20 | b) % 4093
    b = fn1(t0 & 4095, t1)
    t2 = u ^ b | (tot | v)
    w = t2 - (8 * b ^ 8)
    for val in range(171):
        t3 = tot * 19 ^ x
        v = (t3 ^ val) & 65535
        u = ((g ^ 18) & g | val) % 4093
        if 19 * x == 60:
            x = g - 1 + val & 2047
            t4 = (g + val) * (4 | 9)
            b = t4 * g & 32767
    return g >> 4 & 4095

if __name__ == "__main__":
    arg = 6
    expected = 4095
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
