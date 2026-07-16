# Auto-extracted from ds_lt256k_500.jsonl
# record_id=498  entry=f  input='19'  output='1062'  tokens=230124

def fn0(e):
    if 16 ^ e > 28:
        e = e & 18
    else:
        e = e + e + 14 | 14
        e = e | 9
    val = e // 2 - e
    e = (val * 15 | 10) % 1009
    return (val ^ e) & 1023

def fn1(j, e):
    t0 = (e + j) // 7
    j = fn0((t0 - j) % 1009)
    if j % 1009 >= 23:
        e = e ^ j
    else:
        t1 = 7 * j + 10 ^ 6
        j = fn0(t1 % 1009)
    p = 19 * e % 9973
    if 17 - j <= 46:
        v = 0
        while v < 10:
            e = (10 - 9 - p | v) % 9973
            j = j * 4 % 9973
            v = v + 1
    else:
        j = e * 4 + p
    for c in range(5):
        j = c * p % 4093
        if j * j >= 30:
            t2 = 17 + e + c * j
            t3 = j << 4 ^ c ^ t2
            e = t3 % 65521
    if 5 * 14 ^ j < 9:
        e = p // 3 * (16 + 15)
    else:
        res = 0
        while res < 2:
            t4 = e * 3 ^ 1
            j = (t4 ^ res) % 1009
            res = res + 1
    return (p | e) << 3 & 511

def f(x):
    hi = 0
    while hi < 7:
        for prv in range(6):
            t0 = hi + x + hi
            x = t0 % 4093
            t1 = (prv | x) ^ hi
            t2 = t1 + (1 - hi + hi)
            x = t2 & 2047
        x = (x >> 2) % 251
        hi = hi + 1
    if x << 4 >= 60:
        t3 = (x & 7) - 1
        x = fn0((t3 | x) & 16383)
        t4 = (x + x ^ x) & 32767
        t5 = (x << 3) % 251
        x = fn1(t4, t5)
    else:
        if x + x != 39:
            t6 = x * x | x
            t7 = x // 3 * 10
            t8 = (x ^ 10) + x
            t9 = (t7 + t8) % 4093
            x = fn1(t6 % 4093, t9)
            t10 = (x - 12) * 20
            x = t10 % 65521
        else:
            x = x - 7 ^ x
    lo = x << 3
    cnt = (x + lo) * (13 & 17) & 131071
    lo = fn0((cnt - 10) % 251)
    for val in range(12):
        aux = 0
        while aux < 37:
            t11 = (aux & val) + lo
            x = t11 % 251
            aux = aux + 1
        t12 = lo - x
        t13 = x + lo >> 3
        t14 = t12 | lo * lo
        lo = (t13 - t14) % 65521
    if 20 - 15 - lo == 26:
        x = (16 ^ cnt) >> 4
    t15 = cnt >> 3 << 1
    return t15 & 262143

if __name__ == "__main__":
    arg = 19
    expected = 1062
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
