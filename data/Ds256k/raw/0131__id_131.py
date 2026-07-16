# Auto-extracted from ds_lt256k_500.jsonl
# record_id=131  entry=f  input='8'  output='28629'  tokens=12715

def fn0(e, b, j):
    hi = [75, 16, 79, 59, 13, 47]
    j = b - e
    e = (1 & j) + e
    e = 4 + e
    return (e - j) % 4093 & 17

def fn1(c, e, g):
    cnt = [26, 76, 93, 91, 34, 50, 3, 82]
    t0 = cnt[g % 8] + e
    t1 = g // 8 + t0
    nxt = t1 * cnt[g % 8] & 255
    prv = 0
    while prv < 11:
        t2 = cnt[prv % 8]
        e = (t2 - cnt[e % 8]) % 17
        for tot in range(3):
            t3 = e | cnt[c % 8]
            t4 = t3 % 65521 ^ nxt ^ tot
            g = t4 & 511
        prv = prv + 1
    t5 = cnt[e % 8]
    t6 = cnt[g % 8]
    t7 = nxt - t5 + 9
    t8 = (t6 & nxt) << 4
    w = t7 + t8
    aux = nxt + 11 + (w ^ c)
    for t in range(5):
        if t * c > 13:
            t9 = w // 2 - 8
            e = (t9 + e) % 65521
            t10 = (17 << 2) + t << 2 | aux
            cnt[nxt % 8] = t10 % 97
    for q in range(10):
        t11 = cnt[c % 8] // 5 ^ e
        e = (t11 | (19 & 13) * g) & 511
        if c ^ nxt < 15:
            t12 = cnt[e % 8] + aux
            nxt = (c - 11 + t12 ^ q) % 9973
            t13 = cnt[c % 8]
            t14 = (t13 | w) ^ aux
            e = t14 + q & 8191
        else:
            t15 = 9 * 1 + aux
            g = t15 - q & 32767
            t16 = aux % 17 + w
            w = t16 & 4095
    return ((g ^ c) // 4 | nxt) & 8191

def f(x):
    v = [351, 610, 22, 555, 641, 76, 396]
    t0 = x + x & (x ^ 15)
    j = t0 ^ 20
    if 6 * x >= 52:
        t1 = x ^ v[x % 7]
        t2 = x * v[j % 7]
        t3 = (x ^ 3) - t1
        j = t3 | (t2 | x)
        prv = 0
        while prv < 9:
            x = 5 - x - x & 65535
            x = (x << 2) % 17
            t4 = v[j % 7] - 13 ^ 6
            j = t4 - j & 4095
            prv = prv + 1
    c = x * x
    z = 12 + 5 + x * c
    for d in range(18):
        t5 = (d ^ z) + v[j % 7]
        v[c % 7] = (t5 - (c * 19 & c)) % 1009
        x = (d ^ j) % 251
        c = c >> 1 >> 3 & 4095
    for q in range(8):
        t6 = q ^ j ^ (c ^ 11)
        c = t6 & z + x - 1
        if q | j >= 6:
            t7 = z // 8 - z % 251
            v[z % 7] = t7 % 1009
            c = c + z & 511
        else:
            v[c % 7] = x & 5
        x = j % 17 - (z - x) & 262143
    return (4 * j | x) & 32767

if __name__ == "__main__":
    arg = 8
    expected = 28629
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
