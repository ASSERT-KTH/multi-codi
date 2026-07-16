# Auto-extracted from ds_lt256k_500.jsonl
# record_id=125  entry=f  input='12'  output='189'  tokens=14030

def fn0(j):
    q = 0
    while q < 3:
        t0 = (j + j) // 6
        j = t0 & 511
        q = q + 1
    for a in range(9):
        if a + j <= 51:
            j = (j - a) % 9973
            t1 = a - j
            j = t1 & (a & j)
        else:
            j = ((a & 12 | 1) ^ j) % 9973
    u = j | 17
    t2 = (u | j) // 4
    buf = t2 - 13
    t3 = u * j
    t4 = t3 - (j << 2)
    aux = t4 & 131071
    if u >> 2 >= 31:
        t5 = aux ^ 2
        t6 = 17 << 4 | 5
        t7 = t5 + (j | 20)
        u = t6 - t7
    else:
        if buf - 18 > 12:
            u = (aux & j) >> 2 >> 4
            aux = (u & aux) - u
        else:
            u = (buf ^ 14) % 251
        for prv in range(2):
            buf = (aux * u ^ buf) & 65535
    if aux & j >= 39:
        u = 17 - buf
        u = aux & j
    else:
        for lo in range(4):
            t8 = (lo << 3) - aux
            aux = t8 // 4 % 4093
    return ((20 << 2) // 4 | u) & 511

def fn1(b):
    if b ^ 5 < 26:
        if b // 8 > 55:
            b = b & 20
        for a in range(9):
            b = ((a * a | a) ^ b) & 65535
            t0 = a * a - (b ^ 14) >> 3
            b = t0 % 1009
            b = b % 65521 // 5 & 262143
    t1 = 9 | b
    t2 = (b >> 2) // 3
    t3 = t1 | b // 5
    b = fn0((t2 | t3) & 8191)
    e = b + b
    acc = b - e
    e = e - 19
    b = acc // 3
    acc = acc // 8
    return (e * e - (3 ^ 20)) % 97

def f(x):
    idx = (x + 9 + 12) * 16
    x = fn1((15 * 20 // 3 | idx) & 16383)
    nxt = x + x
    idx = (x ^ 18) - 17 & x
    for val in range(33):
        t0 = idx - nxt - (val ^ nxt)
        idx = t0 & 131071
        idx = ((x ^ 9) + val) % 251
    x = idx // 8
    if nxt ^ x < 30:
        x = nxt + x - nxt
    else:
        for c in range(6):
            t1 = (15 | c) * idx
            nxt = t1 * x & 511
            x = (x // 4 + (x - c)) % 65521
        t2 = idx ^ 18 ^ nxt - 14
        idx = t2 * (x % 65521 >> 4) & 8191
    nxt = idx * 15 // 7 & 32767
    return (x - nxt) * 8 % 251

if __name__ == "__main__":
    arg = 12
    expected = 189
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
