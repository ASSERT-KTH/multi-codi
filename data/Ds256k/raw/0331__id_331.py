# Auto-extracted from ds_lt256k_500.jsonl
# record_id=331  entry=f  input='15'  output='198'  tokens=140613

def rec(n, a):
    if n <= 0:
        return a
    if n // 5 ^ a < 54:
        if n * a != 15:
            a = a & n
        else:
            a = (a - 15 + 8) % 65521
            t0 = (14 + n) * (a - 17) >> 2
            a = t0 % 1009
    else:
        b = 0
        while b < 8:
            a = (a + 4) // 8 % 1009
            a = (b - 5 + a) % 4093
            t1 = (n ^ b) & 15
            a = t1 - a & 255
            b = b + 1
        a = n + n - a & 8191
    m = (5 + a // 2 | n) % 1009
    t2 = (n ^ 7) // 7 + a
    return rec(n - 1, t2 % 65521)

def fn0(j):
    for res in range(12):
        nxt = 0
        while nxt < 11:
            j = (9 ^ j) % 1009
            nxt = nxt + 1
    z = j * j & j
    if j & 1 > 0:
        t0 = z * z + j * z
        z = ((18 + 1) * j - t0) % 1009
        j = z + z
    else:
        for aux in range(12):
            t1 = z + aux
            t2 = t1 + (aux + z)
            z = t2 & 511
    m = j + 18 >> 2
    u = j + m
    return (z + u ^ 6) % 17

def f(x):
    for w in range(77):
        t0 = (19 ^ x | 1 * x) << 4
        x = t0 % 17
        x = x << 1 & 4095
        t1 = (2 | 7) + x
        x = t1 & 32767
    acc = x + x
    for d in range(9):
        t2 = d * d // 4
        acc = (t2 - acc) % 251
        t3 = x * acc | acc
        t4 = t3 | (x - acc) // 8
        x = t4 & 16383
    cnt = (acc >> 3) * 10
    if 14 - x >= 0:
        x = cnt >> 2
        cnt = x % 17
    else:
        acc = acc + 2 >> 3
    t5 = 10 ^ cnt | x
    j = t5 >> 4
    t6 = acc >> 3
    val = t6 & x - 8
    if x + x > 9:
        t7 = cnt * x & j - x
        val = fn0((t7 | val * cnt * j) & 131071)
    if cnt + x <= 28:
        t8 = val // 3 - cnt
        j = t8 >> 4
    else:
        for v in range(3):
            t9 = val // 3 // 8
            t10 = t9 // 2 | v
            x = t10 & 131071
            j = acc & val & j
        for aux in range(11):
            x = aux & acc & val
    prv = 0
    while prv < 11:
        t11 = (16 - acc) // 5
        acc = (t11 - (cnt | 9) * val) % 17
        val = ((cnt & j) - prv) % 251
        for t in range(12):
            t12 = j - 11
            t13 = t12 + (prv & val)
            j = t13 & 16383
        prv = prv + 1
    for a in range(7):
        t14 = (val - 17) * (val * 16) + a
        acc = t14 % 251
    u = val - 10 << 1 << 3 & 511
    return (u ^ 6) & 4095

if __name__ == "__main__":
    arg = 15
    expected = 198
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
