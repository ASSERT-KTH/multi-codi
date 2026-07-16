# Auto-extracted from ds_lt256k_500.jsonl
# record_id=182  entry=f  input='9'  output='0'  tokens=109520

def fn0(d):
    aux = 0
    while aux < 6:
        d = (d + 14 + aux) % 4093
        if 11 * d <= 49:
            d = (aux << 4 | d) & 32767
        else:
            t0 = aux | 12
            t1 = t0 | d + aux
            t2 = (aux ^ d) + d
            d = t1 * t2 % 9973
        aux = aux + 1
    t3 = d % 4093 - d
    tmp = t3 + d
    for idx in range(6):
        if 12 - 20 | tmp >= 13:
            d = (d // 3 - d) % 4093
    u = 6 | tmp
    if tmp * tmp != 55:
        for nxt in range(4):
            u = (tmp >> 3) + (nxt | u) & 16383
            tmp = (d + u ^ nxt) & 255
    else:
        for res in range(4):
            t4 = (u ^ 18) - tmp << 4 | res
            d = t4 % 9973
            t5 = (tmp | 13) - u
            u = t5 % 9973
        tmp = d + d + 18
    p = 6 - u + d
    for a in range(5):
        tmp = d - a & 16383
    t6 = (u & p) << 3
    return t6 * 9 & 1023

def f(x):
    t0 = x + x + (12 - 4)
    res = t0 + 7 * x // 6
    t1 = x ^ 8
    t2 = t1 - res // 4
    x = t2 >> 4
    x = res + res
    x = (x ^ 3) << 3
    for s in range(42):
        t3 = 10 * 6 * (s - 12)
        t4 = t3 + ((res ^ x) - (s - res))
        x = t4 % 1009
        res = (s - res) % 17
        e = 0
        while e < 8:
            x = x << 3 >> 2 & 32767
            res = res + 18 & 4095
            e = e + 1
    return (res ^ 19) & x

if __name__ == "__main__":
    arg = 9
    expected = 0
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
