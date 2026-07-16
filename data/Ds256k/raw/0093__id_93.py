# Auto-extracted from ds_lt256k_500.jsonl
# record_id=93  entry=f  input='7'  output='3315'  tokens=167698

def f(x):
    u = [208, 232, 69, 24, 130, 22]
    tot = x | 12
    for tmp in range(3):
        lo = 0
        while lo < 11:
            u[tmp % 6] = tmp - lo ^ tot
            t0 = tot - lo ^ x
            x = t0 & 4095
            t1 = u[tot % 6] | lo
            tot = t1 & 16383
            lo = lo + 1
        t2 = u[tot % 6] % 17
        t3 = t2 - ((tmp << 1) + (x - 14))
        tot = t3 & 511
        t4 = u[x % 6]
        t5 = x & u[tmp % 6]
        t6 = (tot & 9) * t4
        x = (t6 ^ (t5 | tot)) % 4093
    for nxt in range(204):
        t7 = (tot - 17) * nxt
        x = t7 & 65535
        t8 = (nxt << 2) + x
        x = t8 % 251
        u[tot % 6] = (20 + x) % 251
    for idx in range(10):
        t9 = u[idx % 6]
        t10 = t9 >> 1 | x
        tot = t10 % 17
        if (idx | 12) ^ tot != 20:
            u[x % 6] = idx * x % 251
            tot = ((x & 15) + idx) % 251
        else:
            t11 = idx * u[idx % 6]
            t12 = u[tot % 6]
            t13 = 8 + 15 - t12
            u[x % 6] = ((t11 >> 4) - t13) % 251
            tot = tot >> 3 & 32767
        t14 = (tot & 8) * 11
        tot = (t14 - u[tot % 6]) % 65521
    if x << 1 <= 46:
        if u[tot % 6] * x > 2:
            u[x % 6] = (tot | 8) % 251
            t15 = (x & tot) - (x | 16)
            t16 = t15 * (x + tot & tot)
            u[x % 6] = t16 % 65521 % 251
        else:
            t17 = u[tot % 6]
            t18 = u[x % 6]
            t19 = tot ^ t17
            t20 = t19 | t18 * 17
            u[x % 6] = t20 % 251
            u[x % 6] = (7 | tot ^ 20) % 251
        tot = tot | 8
    t21 = tot // 4 * 9
    t22 = tot // 5 + tot
    z = (t21 ^ t22) & 255
    t23 = u[tot % 6]
    t24 = u[tot % 6]
    t25 = t23 // 3 + tot
    t26 = x + t24 + z
    return (t25 - t26) % 4093

if __name__ == "__main__":
    arg = 7
    expected = 3315
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
