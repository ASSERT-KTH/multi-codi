# Auto-extracted from ds_lt256k_500.jsonl
# record_id=147  entry=f  input='5'  output='638'  tokens=71976

def f(x):
    p = [743, 391, 205, 926, 586]
    for hi in range(109):
        if x * hi <= 33:
            t0 = p[hi % 5]
            t1 = hi * 18
            t2 = p[hi % 5]
            t3 = t1 - (t0 - 13)
            t4 = (t2 | x) // 6
            x = t3 + t4 & 255
        else:
            t5 = 7 & hi
            t6 = t5 ^ hi - 15
            x = t6 & x
            t7 = 9 - hi | hi
            x = (t7 ^ x) & 131071
    t8 = p[x % 5] * 2
    g = t8 * x
    if p[x % 5] // 7 < 45:
        p[x % 5] = (x & 20) + 19
        t9 = g - p[g % 5]
        x = (t9 * x + 19) % 9973
    else:
        x = (x ^ 10) // 2
    c = (x >> 2) - (g ^ x)
    aux = (g & 14 | x) // 5
    t10 = g * g ^ aux
    cur = t10 % 1009
    t11 = 2 * g
    t12 = t11 ^ (cur ^ x)
    cnt = t12 & 65535
    z = cnt + 19 << 1
    if aux >> 1 < 34:
        cur = 17 & 5 ^ cnt
        t13 = p[cnt % 5]
        x = z - t13 ^ z
    else:
        t14 = aux + cnt + 3
        p[z % 5] = t14 % 1009
        for m in range(6):
            t15 = aux * p[x % 5]
            t16 = 11 * x * t15 % 9973
            p[g % 5] = t16 % 1009
            t17 = cnt * cnt // 4
            p[c % 5] = t17 // 8 % 1009
    val = p[z % 5] * x % 9973
    p[g % 5] = 12 * c % 1009
    t18 = cnt % 9973 // 2
    p[x % 5] = t18 % 1009
    t19 = p[aux % 5] + g
    p[c % 5] = (14 ^ g) + t19 & 255
    t20 = p[x % 5] + x
    a = t20 & p[z % 5]
    t21 = p[val % 5]
    acc = t21 - p[z % 5]
    idx = acc + 15 + x + acc
    t22 = p[aux % 5] // 3
    nxt = a - cur & t22
    t23 = g | p[val % 5]
    t24 = t23 | 1 * 17
    return (t24 - p[aux % 5]) % 1009

if __name__ == "__main__":
    arg = 5
    expected = 638
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
