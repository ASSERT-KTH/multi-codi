# Auto-extracted from ds_lt256k_500.jsonl
# record_id=481  entry=f  input='17'  output='65532'  tokens=104657

def fn0(c, e, b):
    t0 = (e >> 2) + (b - e)
    e = t0 ^ e
    c = c // 5 << 2
    t1 = b - c ^ b
    b = t1 >> 4
    for j in range(2):
        t2 = (17 | 16) * 5 + b | c
        c = t2 % 4093
        e = ((j * e << 4) + j) % 1009
        t3 = e // 6
        t4 = t3 + (20 + b)
        c = t4 + c & 255
    return c & e

def fn1(a, c, d):
    t0 = (d & 18) - 8 & 16383
    t1 = (c - a) % 251
    t2 = c // 8 & 1023
    d = fn0(t0, t1, t2)
    prv = 0
    while prv < 7:
        d = c + a + prv & 511
        d = (c - 11 - prv) % 17
        prv = prv + 1
    for w in range(8):
        cnt = 0
        while cnt < 7:
            a = (w + 4 | a) & 511
            cnt = cnt + 1
    c = a - 6
    t3 = a & c
    t4 = t3 - a // 6
    return t4 * d & 8191

def f(x):
    y = 19 ^ 8 | x
    t0 = y & 16 ^ (y | x)
    nxt = t0 & (15 * y & y)
    aux = y + y + y
    t1 = aux * aux % 9973 | aux
    t2 = (nxt | aux) & 18
    t3 = (4 + 20) % 17 | x
    aux = fn0(t1 % 9973, t2, t3 % 97)
    t4 = (14 ^ x) * 7
    hi = t4 & (aux >> 4 ^ x)
    lo = x - hi
    val = 0
    while val < 175:
        if aux % 1009 >= 41:
            t5 = aux & lo ^ val
            x = t5 & 32767
        else:
            nxt = val * aux & 255
        if hi + lo != 29:
            y = (9 - hi - y ^ y) & 4095
            nxt = (nxt - val) // 7 % 1009
        val = val + 1
    t6 = lo // 3
    t7 = t6 * (y ^ 14)
    t8 = (lo ^ 5) // 5
    m = t7 * t8 % 17
    if hi // 5 > 33:
        t9 = 17 * lo & 131071
        t10 = (m << 3) + m * 2
        t11 = y + x & lo
        aux = fn0(t9, t10 & 65535, t11)
        res = 0
        while res < 6:
            t12 = y * res >> 4 ^ m
            lo = t12 & 2047
            hi = y * 16 - res & 65535
            res = res + 1
    e = m + aux & lo
    cnt = (nxt & x) * (nxt + nxt)
    return aux - 4 & 65535

if __name__ == "__main__":
    arg = 17
    expected = 65532
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
