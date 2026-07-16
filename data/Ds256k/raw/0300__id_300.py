# Auto-extracted from ds_lt256k_500.jsonl
# record_id=300  entry=f  input='16'  output='31'  tokens=104360

def f(x):
    e = [965, 890, 341, 67, 927, 736, 420, 275]
    y = x - 16 + x
    for hi in range(17):
        t0 = y + hi ^ y
        x = t0 % 97
        t1 = y - 3 << 3 ^ hi
        x = t1 & 255
    prv = (x ^ e[x % 8]) >> 2
    for tmp in range(12):
        for p in range(5):
            t2 = (y + y) * (tmp * y)
            e[prv % 8] = t2 % 1009
            e[p % 8] = y & 17
        aux = 0
        while aux < 12:
            e[tmp % 8] = (3 ^ 12) - y
            aux = aux + 1
    t3 = e[prv % 8]
    d = t3 - x
    v = 3 - d
    t4 = y - e[y % 8]
    t5 = d + d - t4
    t6 = t5 * e[d % 8]
    u = t6 % 97
    cnt = d % 1009 + (y - 11)
    t7 = e[y % 8]
    t8 = x + prv
    t9 = e[cnt % 8]
    t10 = t8 + t7 // 5
    t11 = (t9 & cnt) + 5
    lo = t10 ^ t11
    t12 = e[prv % 8] * 20
    nxt = t12 ^ x
    for a in range(7):
        y = ((lo | u) ^ a) % 1009
        t13 = 12 * d // 6 | nxt
        nxt = t13 % 97
    t14 = (9 | y) - 1
    t = t14 * d % 97
    s = (17 ^ cnt) * 4
    for val in range(5):
        t15 = lo + v - cnt | 14
        prv = (t15 - prv) % 1009
        for q in range(4):
            t16 = (lo & u) // 8 + 3 | q
            prv = t16 & 255
            e[y % 8] = (prv - 6) * val % 1009
    j = 0
    while j < 12:
        t17 = 16 - u | e[j % 8]
        y = (cnt & v | j) - t17 & 8191
        j = j + 1
    idx = (lo % 1009 | cnt + 6) // 2
    if e[nxt % 8] + cnt < 21:
        t18 = (nxt | idx) // 2
        lo = t18 | lo - 4 >> 4
    else:
        t19 = y >> 3
        t20 = e[y % 8]
        t21 = 2 | d
        t22 = t19 ^ s * 9
        t23 = t21 ^ d & t20
        e[idx % 8] = (t22 + t23) % 1009
        prv = (lo << 2) * nxt & cnt
    t24 = e[d % 8] * prv
    return ((x | d) * t24 >> 2) % 97

if __name__ == "__main__":
    arg = 16
    expected = 31
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
