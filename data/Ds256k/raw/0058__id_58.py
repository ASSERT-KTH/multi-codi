# Auto-extracted from ds_lt256k_500.jsonl
# record_id=58  entry=f  input='3'  output='1602'  tokens=155840

def fn0(b, c):
    v = (c ^ 17) + c & 17
    t0 = v << 4
    t1 = t0 & c >> 2
    buf = t1 | v
    if 19 - buf != 37:
        for nxt in range(8):
            v = ((c ^ v) & 14) * nxt & 8191
            b = (16 & nxt) * (v | c) % 97
            t2 = (b << 2) * 10 ^ buf
            buf = t2 % 1009
    else:
        buf = (c ^ 5) * v % 97
        b = v - 8 + buf
    val = 0
    while val < 11:
        v = v & 1023
        val = val + 1
    t3 = 17 * b + b * v
    res = ((c + b) // 2 | t3) & 1023
    c = (b ^ 20) + (c + buf)
    if 11 - c > 21:
        res = res ^ 3
    c = c * res & 16383
    return (buf ^ v) >> 2 & 131071

def fn1(e, g, c):
    e = g >> 1
    t0 = g + 4 - e * g
    e = t0 & 16383
    for buf in range(5):
        t1 = (buf - 20 - buf ^ 16) + e
        g = t1 & 8191
    for z in range(5):
        t2 = z * 16 - c
        g = t2 & 16383
        t3 = 6 - e
        e = t3 & (e | z)
    t4 = g * 19 * (5 << 2)
    g = t4 % 251
    t5 = (c - 20 ^ c) % 251
    t6 = ((c - g) % 251 + e) % 1009
    g = fn0(t5, t6)
    return c + 7 + c & 8191

def f(x):
    tmp = 5 | x
    cnt = 0
    while cnt < 4:
        for q in range(10):
            t0 = cnt ^ q | tmp
            tmp = t0 & 4095
        cnt = cnt + 1
    v = 0
    while v < 7:
        if x | v >= 32:
            x = ((14 ^ x) + v) % 251
        else:
            t1 = x - 8
            t2 = (x & v) + tmp
            t3 = t1 - (9 + v)
            tmp = t2 & t3
            t4 = tmp * v
            t5 = tmp & 9
            t6 = t4 * (x - 11)
            t7 = t5 ^ tmp * tmp
            tmp = (t6 ^ t7) % 17
        for res in range(6):
            tmp = ((v << 3 << 4) + tmp) % 1009
            t8 = v + 15 - tmp + x
            x = t8 & 16383
            tmp = tmp << 2 & 255
        t9 = (v & 8) * (8 | tmp)
        tmp = t9 * x % 17
        v = v + 1
    for cur in range(19):
        for hi in range(6):
            t10 = 14 * x | 17 - x
            tmp = (t10 + hi) % 251
            t11 = (x | cur) ^ tmp + x | cur
            tmp = t11 & 131071
            t12 = cur - tmp ^ x * hi
            x = t12 - x & 255
        x = (cur - 18 - x) % 1009
    t13 = 19 % 17 * 15 // 3
    lo = t13 - tmp
    j = (x | 5) + (x | lo) << 2
    t14 = tmp - x + x
    t15 = t14 * (x - lo - 5)
    return t15 & 8191

if __name__ == "__main__":
    arg = 3
    expected = 1602
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
