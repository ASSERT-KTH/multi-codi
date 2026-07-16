# Auto-extracted from ds_lt256k_500.jsonl
# record_id=14  entry=f  input='2'  output='66'  tokens=69572

def fn0(g, b):
    idx = 6 * b * 5 & 15
    if 5 + g != 25:
        t0 = g % 65521 + g
        b = t0 * 15 & 511
    else:
        if b * idx < 40:
            t1 = (4 << 2) + g
            b = t1 % 65521
            g = 7 * 16 - idx
        cnt = 0
        while cnt < 2:
            t2 = idx + b + b
            idx = (t2 + g) % 97
            g = idx // 2 + cnt & 2047
            t3 = (b - 10 | cnt) // 4
            b = t3 & 8191
            cnt = cnt + 1
    hi = idx * b % 65521
    t4 = g & b & b
    val = t4 >> 4
    t5 = val // 5 * b
    q = t5 % 251
    for res in range(3):
        j = 0
        while j < 4:
            idx = ((5 ^ 11) - g | j) % 97
            t6 = hi << 4 ^ val
            t7 = t6 + (idx >> 1)
            g = (t7 | j) % 9973
            hi = (j | idx) & 32767
            j = j + 1
        t8 = (b & g | 16) - res
        val = t8 & 2047
        val = val // 7 % 97
    return (idx + 18) % 97

def f(x):
    tot = [94, 59, 24, 1, 29]
    z = 13 + x
    t0 = tot[z % 5] * 14 * x
    aux = t0 // 6
    cur = (z ^ 9) - x ^ aux
    q = x - aux
    t1 = x * cur * cur
    t2 = (15 - cur) // 2
    z = t1 * t2 & 131071
    c = 0
    while c < 7:
        cur = (q >> 3 ^ cur) & 511
        c = c + 1
    q = z - 14 & q
    cnt = 0
    while cnt < 169:
        cur = (aux * q // 3 ^ cur) & 8191
        if x + aux != 57:
            tot[z % 5] = (20 - cnt + cur) % 97
        else:
            t3 = x * cnt & aux
            z = (t3 << 4) % 97
        cnt = cnt + 1
    return (x | 5 | z) % 97

if __name__ == "__main__":
    arg = 2
    expected = 66
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
