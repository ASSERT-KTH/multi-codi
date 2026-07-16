# Auto-extracted from ds_lt256k_500.jsonl
# record_id=420  entry=f  input='14'  output='173'  tokens=68894

def fn0(d, c):
    prv = 13 * c
    c = 13 - c
    c = c + prv
    for hi in range(8):
        d = (prv ^ hi) % 251
        t0 = (15 | d) + hi
        prv = t0 & 131071
    return (7 & d ^ prv) & 8191

def fn1(b, d):
    hi = [124, 195, 227, 25]
    hi[d % 4] = b % 9973 % 251
    t0 = (b - 20) * (d // 5)
    aux = t0 * b % 65521
    for y in range(6):
        b = (b - y) * y >> 4 & 65535
        b = ((aux & 9) * aux + y) % 65521
        aux = ((12 ^ b) + aux) % 17
    if aux // 3 > 33:
        t1 = (17 << 1) * aux
        aux = t1 // 8 & 32767
    else:
        d = d * d & 511
        if d - 9 >= 53:
            t2 = hi[d % 4] + b
            t3 = 7 + b - t2 & 131071
            t4 = hi[aux % 4]
            t5 = t4 + b & b
            t6 = t5 - b & 8191
            d = fn0(t3, t6)
        else:
            hi[aux % 4] = (b + d) % 251
    if 20 + aux <= 64:
        d = aux | 15
        for u in range(9):
            t7 = d // 4 << 3
            hi[u % 4] = t7 % 251
            hi[b % 4] = d // 4 % 251
    t8 = (d ^ 7) // 2
    return (t8 | d - aux & aux) & 131071

def f(x):
    res = [831, 779, 55, 761, 441, 538, 151, 951]
    t0 = x | res[x % 8]
    res[x % 8] = (t0 & (x ^ 9)) - x
    y = 0
    while y < 253:
        t1 = y + x + (y ^ 4)
        x = t1 & 511
        if res[x % 8] * x <= 26:
            x = 14 - y + x & 511
        x = (x ^ y ^ x) % 1009
        y = y + 1
    cnt = x | 13
    return (5 << 4 ^ cnt) % 251

if __name__ == "__main__":
    arg = 14
    expected = 173
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
