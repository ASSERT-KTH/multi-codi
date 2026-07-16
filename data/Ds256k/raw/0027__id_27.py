# Auto-extracted from ds_lt256k_500.jsonl
# record_id=27  entry=f  input='14'  output='1'  tokens=229198

def fn0(g, e, d):
    c = 0
    while c < 8:
        for lo in range(4):
            t0 = 16 + lo
            t1 = 6 - c ^ lo
            t2 = t0 & (g ^ e)
            e = t1 * t2 & 16383
        c = c + 1
    tot = d // 7
    z = g - 5
    cur = (d ^ g) % 17
    z = z // 5 - cur
    q = 0
    while q < 10:
        a = 0
        while a < 10:
            z = g - d + a & 4095
            g = ((a | q) - z) % 9973
            t3 = e + q + tot
            tot = t3 % 9973
            a = a + 1
        q = q + 1
    s = 0
    while s < 6:
        t4 = s + s & tot >> 2
        cur = t4 * d & 1023
        s = s + 1
    d = 9 * z
    return g * z - tot & 8191

def f(x):
    cnt = [12, 21, 26, 16, 23, 4, 28, 6]
    idx = x + 1
    cnt[x % 8] = 17 * cnt[x % 8] % 97
    for a in range(1215):
        t0 = a ^ 5 ^ (a ^ 7)
        cnt[x % 8] = t0 ^ x
    t1 = cnt[idx % 8]
    buf = (x | idx) & t1
    for cur in range(2):
        buf = ((5 ^ buf) - (1 + buf)) % 251
        t2 = (11 ^ 6) + buf
        x = (t2 ^ cur) % 251
        t3 = cnt[idx % 8]
        x = ((x ^ idx) + t3) % 251
    t4 = x + x & buf
    t5 = cnt[x % 8]
    t6 = (4 ^ t5) & 16383
    t7 = idx & buf & (buf ^ idx)
    buf = fn0(t4, t6, t7)
    acc = 7 + x - 17
    return ((idx ^ acc) + 2 ^ idx) & 65535

if __name__ == "__main__":
    arg = 14
    expected = 1
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
