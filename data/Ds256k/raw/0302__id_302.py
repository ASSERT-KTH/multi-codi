# Auto-extracted from ds_lt256k_500.jsonl
# record_id=302  entry=f  input='10'  output='14736'  tokens=110415

def fn0(g):
    q = [56, 90, 37, 0, 81, 25, 86, 89]
    for hi in range(8):
        t0 = hi + 11 ^ g
        g = t0 & 511
        if g * q[hi % 8] <= 12:
            q[g % 8] = (hi - 8 + g) % 97
        else:
            t1 = 9 - hi + (hi | g)
            g = t1 % 4093
            q[g % 8] = g * 10 % 97
    u = g + 7
    t2 = 9 + u
    c = t2 | u + u
    for z in range(9):
        for prv in range(6):
            t3 = u - 16 | g
            g = t3 & 4095
            c = (g // 8 - c) % 17
            t4 = (g ^ 17 ^ 10) - c
            q[u % 8] = t4 % 97
        if 14 & g < 0:
            t5 = (c - 17) % 65521 - u
            u = t5 % 4093
            t6 = q[c % 8]
            t7 = (t6 + z) // 8
            u = t7 * c % 17
        else:
            q[z % 8] = g & 18
            t8 = z + 11 - 3 + c
            u = t8 % 4093
    cur = u // 6
    b = g & u
    for aux in range(12):
        t9 = cur * cur
        t10 = t9 * (g >> 4)
        u = (t10 + u) % 4093
    t11 = g + q[c % 8]
    t12 = 10 * cur ^ cur
    return t12 & (t11 ^ u * cur)

def fn1(b):
    v = b ^ 3
    if b >> 3 < 29:
        for m in range(2):
            t0 = v >> 2 | m
            b = t0 & 2047
    else:
        v = fn0(v // 5 & 262143)
    t1 = (v >> 1) - v // 2
    cnt = t1 - 19
    t2 = b // 6 - v
    return t2 % 97

def f(x):
    w = 17 * x * x ^ x
    for y in range(462):
        t0 = (w ^ 6) * (y << 1)
        w = (t0 - w) % 4093
        t1 = (5 & 18) - (y & x) + w
        w = t1 % 17
    t2 = x - w
    w = t2 ^ x * 12
    w = (3 * x + x) // 7
    w = fn1((x * x + x) // 8 % 65521)
    x = 19 * x >> 4
    t3 = 3 + 5 + w * x
    w = t3 % 4093
    return (x << 1 & w) * w & 131071

if __name__ == "__main__":
    arg = 10
    expected = 14736
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
