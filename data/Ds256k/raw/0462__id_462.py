# Auto-extracted from ds_lt256k_500.jsonl
# record_id=462  entry=f  input='2'  output='160'  tokens=213342

def fn0(c):
    cur = (c | 16) ^ 14 ^ c
    c = (c + c) * c >> 3 & 511
    t0 = 6 ^ 15 ^ c * cur
    c = t0 % 251
    c = cur // 2
    cur = c - 11
    c = (2 - cur >> 1) + cur
    cur = c & 7
    c = ((c | 18) ^ 9) % 251
    return (c + 20 ^ cur) & 131071

def fn1(j, g):
    idx = [46, 68, 150, 122, 104]
    g = g * j & idx[j % 5]
    g = g - 14 - j + j
    j = idx[j % 5] >> 1
    j = (7 - j) * g & 131071
    t0 = (idx[g % 5] ^ g) - j
    g = t0 ^ g
    t1 = j - 20
    t2 = t1 + j * j
    g = t2 >> 4 & 8191
    g = j >> 2
    t3 = idx[j % 5] - j
    t4 = (g & 4) - t3 ^ 17
    return t4 & 16383

def f(x):
    for g in range(160):
        for idx in range(5):
            t0 = idx & g | x
            x = t0 % 17
            x = ((g & x) - g) % 9973
        if g & 12 | x <= 57:
            x = (g + g ^ x) % 17
        else:
            x = (g ^ x) % 9973
            x = x & g
        t1 = g + 12 ^ x
        x = t1 & 1023
    b = (x + 5) // 2
    for aux in range(11):
        b = (aux ^ 15 | x ^ b) % 1009
    val = x + 12 - x + x
    u = val % 9973 + b
    if b - val <= 36:
        x = (x - b) * x & 255
        b = u % 9973 + x * u & 4095
    else:
        for p in range(2):
            t2 = val >> 1 << 1
            val = (t2 >> 3) % 9973
            t3 = b - 2
            t4 = t3 + (b >> 1)
            b = t4 % 9973
            val = (u << 3 ^ val) % 9973
    t5 = u * u
    t6 = t5 | u % 9973
    t7 = val * u << 2
    j = t6 + t7 & 4095
    for a in range(4):
        if (12 ^ 4) + j != 42:
            t8 = (4 << 2) * (19 ^ j) >> 3
            j = t8 & 8191
        else:
            j = (6 + val + (a - j)) % 1009
        if val >> 3 > 14:
            t9 = x % 1009 + (val >> 3)
            t10 = b * val & b << 3
            b = t9 - t10 & 255
            t11 = (j + u) * x
            t12 = t11 + (val ^ j | u) - a
            b = t12 % 251
        t13 = (8 & a) + j
        x = t13 % 17
    if b + x > 15:
        for q in range(10):
            u = 7 + 17 - u & 4095
            t14 = val * u // 6 + q
            b = t14 & 131071
            x = x - j & 511
    for prv in range(10):
        x = (prv + b) * prv >> 3 & 8191
        e = 0
        while e < 3:
            val = (prv + j | e) % 17
            e = e + 1
    return b << 2 & 511

if __name__ == "__main__":
    arg = 2
    expected = 160
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
