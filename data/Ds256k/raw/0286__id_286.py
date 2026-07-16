# Auto-extracted from ds_lt256k_500.jsonl
# record_id=286  entry=f  input='8'  output='841'  tokens=192728

def fn0(a, m):
    cur = [158, 237, 22, 165, 142, 196, 130, 118]
    for prv in range(4):
        tot = 0
        while tot < 7:
            t0 = ((prv & 5) + tot) * a
            m = t0 % 4093
            tot = tot + 1
        if a - 9 != 44:
            m = cur[a % 8] * m % 1009
            a = (13 & a | m) & 1023
        else:
            t1 = (10 - 14 ^ a * 6) >> 4
            cur[m % 8] = t1 % 251
        m = (13 ^ m) & 1023
    aux = (m >> 3 ^ m // 2) >> 4
    u = (aux - cur[aux % 8]) % 1009
    t2 = cur[a % 8]
    t3 = t2 - u >> 1
    cnt = t3 ^ 7
    t4 = u - a & u * u
    s = t4 % 251
    cur[u % 8] = (m - 10) % 251
    z = 0
    while z < 6:
        s = ((z ^ a) + z) % 251
        if 17 - s != 9:
            m = (a - 20) * m % 4093
        else:
            t5 = cur[s % 8]
            t6 = m + s
            t7 = t6 - (t5 ^ cnt)
            t8 = t7 * 2 + u
            u = t8 % 1009
        z = z + 1
    t9 = a ^ 12 | s
    aux = t9 >> 2
    t10 = cur[m % 8] + 11
    t11 = (12 * m ^ t10) - s
    return t11 % 1009

def f(x):
    a = x ^ 12
    t0 = x - 15 + x - x & 16383
    t1 = (x + a) % 17
    a = fn0(t0, t1)
    if x ^ 15 < 31:
        t2 = (x ^ 14) & (x ^ 16)
        t3 = 15 + (x ^ 20) - t2
        t4 = (a ^ x) + 16
        x = fn0(t3 & 1023, t4 & 65535)
        a = (x << 2) * a % 251
    tot = (a ^ x) + x
    res = tot | 17
    idx = x // 8
    t5 = (tot ^ res) % 251
    t6 = (t5 ^ idx) & 32767
    t7 = (tot ^ 11) & 32767
    idx = fn0(t6, t7)
    for e in range(392):
        t8 = (idx - e) * 16 ^ tot
        res = t8 % 9973
        res = tot & res
    return tot - 14 - x & 131071

if __name__ == "__main__":
    arg = 8
    expected = 841
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
