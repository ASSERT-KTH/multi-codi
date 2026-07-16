# Auto-extracted from ds_lt256k_500.jsonl
# record_id=28  entry=f  input='20'  output='173'  tokens=242876

def fn0(g, j, a):
    for u in range(5):
        t0 = g + j - a
        a = t0 & 131071
        t1 = u + 17 + a * g
        t2 = (g ^ u) - g ^ t1
        a = t2 & 8191
    a = a // 3
    cnt = 0
    while cnt < 11:
        t3 = (g & 12) * (j | g)
        j = t3 >> 1 & 1023
        cnt = cnt + 1
    t4 = 14 + 11 | a
    return t4 % 4093

def f(x):
    t0 = x - 19
    aux = t0 + (15 & x)
    s = 0
    while s < 8:
        d = 0
        while d < 68:
            t1 = x * x & (d & 6)
            x = ((s | 9) - t1) % 17
            t2 = (x ^ d) + aux
            t3 = aux * s >> 3
            aux = t2 * t3 & 2047
            d = d + 1
        s = s + 1
    if 9 + x == 28:
        t4 = aux - x
        aux = t4 - (aux + 20)
    else:
        for buf in range(10):
            aux = (buf + buf | x) % 17
            t5 = x ^ 15
            t6 = t5 * (x | 2)
            aux = (t6 ^ buf) & 1023
            t7 = (buf - x + (10 & 18)) * x
            x = t7 % 1009
        for w in range(11):
            x = aux - 4 + x & 8191
    for m in range(4):
        x = (m ^ aux) + x & 131071
        if aux + aux == 34:
            t8 = x | m
            t9 = t8 - (9 + m)
            aux = t9 % 1009
    if aux * x <= 44:
        t10 = (aux + x) % 17
        t11 = ((aux >> 3) + 5) // 7 & 16383
        aux = fn0(t10, aux & x, t11)
    else:
        t12 = (aux + aux) % 1009
        t13 = ((aux ^ 5) >> 1) * x & 511
        t14 = aux * 11 & 262143
        aux = fn0(t12, t13, t14)
    aux = aux * aux & 262143
    t15 = aux & x | x ^ 1
    t16 = t15 ^ (x | 16) << 3
    return t16 & 511

if __name__ == "__main__":
    arg = 20
    expected = 173
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
