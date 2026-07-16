# Auto-extracted from ds_lt256k_500.jsonl
# record_id=358  entry=f  input='3'  output='113'  tokens=116449

def fn0(d, b):
    hi = 0
    while hi < 11:
        b = (b | d) & 8191
        for val in range(2):
            t0 = 9 * val + hi ^ d
            d = t0 % 9973
        hi = hi + 1
    t1 = d + b + (b ^ d)
    lo = (t1 << 3) % 1009
    if 14 - d >= 17:
        d = lo + b
        b = lo + 11
    for y in range(11):
        for tot in range(7):
            lo = d * lo % 17
        t2 = b - 7 ^ 14 - b
        lo = t2 + y & 65535
        for v in range(11):
            t3 = d * b * v
            b = t3 & 262143
            t4 = y * v + lo * b
            lo = t4 & 14 + lo >> 4
            t5 = (v << 3) + y & 8
            d = (t5 - b) % 251
    for s in range(8):
        b = (s * s | d) % 251
        t6 = (s + lo) // 2
        b = (t6 ^ (s ^ d ^ d)) & 1023
    w = (d + 17) % 1009
    t7 = (lo & 2) * d
    return t7 % 1009

def fn1(a):
    lo = a * a % 9973
    t0 = (lo >> 3) - (lo | 14)
    cnt = t0 | lo
    a = cnt - 10
    if a | 10 != 24:
        a = cnt // 2 - a >> 3
        for e in range(11):
            a = e - a & (19 ^ 13)
    else:
        t1 = (cnt >> 4) * (cnt * 17)
        lo = t1 % 251
    for tot in range(8):
        t2 = tot - 16
        t3 = t2 + (cnt >> 3)
        t4 = (lo ^ a) >> 4
        lo = t3 & t4
        hi = 0
        while hi < 9:
            t5 = cnt - lo + lo & lo
            a = (t5 + hi) % 9973
            lo = (a + cnt ^ lo) & 4095
            lo = lo & tot
            hi = hi + 1
    t6 = (cnt - a) * lo
    a = (t6 + (lo * a + a)) % 9973
    t7 = a % 251 + cnt
    return t7 % 9973

def f(x):
    e = [206, 110, 169, 9, 189, 109]
    aux = x - 6
    for g in range(12):
        t0 = e[g % 6] // 7 | x
        aux = t0 & 131071
        x = (x - 18) % 17
    hi = 5 - x
    y = x + 14
    val = (hi << 4) // 7 + 12
    for t in range(10):
        y = aux - y & val * val
    if aux ^ hi >= 35:
        t1 = e[x % 6] + val
        t2 = (aux ^ e[y % 6]) >> 2
        e[x % 6] = (val << 4 & t1) * t2 % 251
    else:
        t3 = val ^ aux
        t4 = t3 - (18 << 2)
        e[val % 6] = t4 % 251
    for buf in range(27):
        for res in range(6):
            t5 = val + e[y % 6]
            t6 = x * y ^ res * x
            e[res % 6] = (t5 - 6 - t6) % 251
            t7 = e[y % 6] & aux
            aux = t7 - val & 255
    if y | aux >= 10:
        if 2 + 5 + val != 22:
            t8 = (val - y - x) // 5
            e[val % 6] = t8 % 251
            val = x - y
        else:
            aux = (x << 2) + aux
        t9 = hi ^ 7
        x = t9 - (20 ^ 18)
    else:
        if 4 ^ x <= 55:
            e[y % 6] = x
            t10 = val - y - 15 ^ 9
            e[y % 6] = t10 % 251
        val = x
    j = (hi ^ 11) * (val | 8)
    u = e[j % 6] * aux
    t11 = e[aux % 6] | aux
    return t11 + (hi + hi) & 2047

if __name__ == "__main__":
    arg = 3
    expected = 113
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
