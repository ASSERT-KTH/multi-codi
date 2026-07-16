# Auto-extracted from ds_lt256k_500.jsonl
# record_id=443  entry=f  input='18'  output='26'  tokens=252474

def rec(n, a):
    if n <= 0:
        return a
    a = (n + n) * a & 262143
    a = 2 - a & 65535
    t0 = ((4 & 20) << 3 | a) % 97
    return rec(n - 1, t0)

def fn0(j, e):
    tmp = j << 4 & 4095
    t0 = j ^ e | tmp
    aux = t0 & tmp
    t1 = (j >> 3) * j
    v = t1 % 4093
    v = v * aux % 9973
    if aux | v > 46:
        t2 = e - aux
        t3 = t2 * (j + v)
        t4 = 19 - e >> 4
        v = (t3 - t4) % 4093
    else:
        if tmp - e < 25:
            t5 = 9 | 18
            t6 = (e ^ 15) % 4093
            t7 = t5 * (tmp - v)
            t8 = t6 + t7 & 16383
            j = rec(33, t8)
            t9 = tmp * 17 >> 3 & 131071
            aux = rec(25, t9)
    for lo in range(9):
        s = 0
        while s < 7:
            v = ((20 ^ 9) + s | tmp) & 262143
            j = (tmp ^ 20) + j & 1023
            s = s + 1
        t10 = e - aux
        t11 = 13 & lo | aux
        t12 = t10 | tmp ^ 18
        j = (t11 - t12) % 4093
        prv = 0
        while prv < 8:
            t13 = 4 + prv - 4
            j = (t13 | j) % 9973
            t14 = ((j ^ 12) & prv) - j
            aux = t14 & 262143
            aux = (prv - lo ^ tmp) % 17
            prv = prv + 1
    aux = v + tmp + e + 1
    t15 = 12 + tmp ^ e
    return t15 + 19 & 8191

def f(x):
    z = 10 * 2 * x + x
    cnt = (x | 19) + z
    t = cnt | 8
    t0 = 5 - t & 2047
    t1 = (x << 3) - (19 - z)
    t2 = (t + x | 11) * t1
    z = fn0(t0, t2 % 97)
    e = (x * t & t) - cnt
    if cnt | z <= 51:
        t3 = t ^ cnt | e
        t4 = z * cnt >> 1
        x = (t3 ^ t4) % 65521
        if t + 3 == 34:
            z = (x - t) % 97
            cnt = 7 + z << 1
        else:
            t5 = (cnt | 3) % 65521
            t6 = e * e * cnt
            t7 = (t6 ^ ((e | 20) ^ 15)) % 65521
            z = fn0(t5, t7)
            t = (7 ^ e) << 4
    for u in range(8):
        for q in range(11):
            t = u - t & 16383
            t8 = cnt * u + 18
            t = (t8 - q) % 251
            z = (q + t) * (e ^ 6) % 251
        b = 0
        while b < 31:
            e = (x + z & 12) + e & 511
            t9 = (cnt ^ b) - 6
            e = t9 % 251
            b = b + 1
    hi = cnt << 4 & 262143
    y = x | 13
    return t % 97

if __name__ == "__main__":
    arg = 18
    expected = 26
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
