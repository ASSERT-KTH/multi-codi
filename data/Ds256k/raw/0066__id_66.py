# Auto-extracted from ds_lt256k_500.jsonl
# record_id=66  entry=f  input='17'  output='0'  tokens=139235

def fn0(e, g):
    s = [123, 236, 162, 145, 221, 238, 26]
    for t in range(4):
        if g - 3 <= 6:
            t0 = 18 + t + s[g % 7]
            g = t0 - t & 2047
            t1 = s[e % 7] & e
            t2 = g * g - t
            g = (t2 ^ t1 * (14 ^ g)) & 4095
        else:
            e = (g - t) % 251
            s[g % 7] = s[g % 7] * 10 % 251
        for tot in range(10):
            s[e % 7] = (t & g) - 1 & 14
    e = 10 + g >> 2
    t3 = s[e % 7]
    e = 6 - t3
    if 18 << 3 ^ e == 51:
        cur = 0
        while cur < 9:
            t4 = cur ^ s[g % 7]
            e = t4 & 8191
            t5 = s[e % 7]
            t6 = g + t5 + 17
            s[g % 7] = t6 * 11 % 251
            cur = cur + 1
    else:
        g = (e + e) * g % 9973
    g = g + g
    g = (s[e % 7] | e) + g
    if s[e % 7] + s[g % 7] < 2:
        s[g % 7] = s[e % 7] // 5
    t7 = e + 5 - g
    return (t7 ^ 5) & 4095

def f(x):
    cnt = [52, 3, 188, 97, 29]
    s = 0
    while s < 20:
        for u in range(10):
            t0 = s - u - s
            x = (t0 ^ x) % 4093
            t1 = 13 + x
            t2 = t1 - (18 + 1)
            cnt[s % 5] = (t2 - 8) % 251
            t3 = 4 - s << 1 ^ x
            cnt[x % 5] = t3 % 251
        for tot in range(2):
            x = (s << 2 | 6 * x) % 4093
        t4 = (x >> 3) + cnt[x % 5]
        x = t4 % 4093
        s = s + 1
    prv = x | 11
    cur = (x ^ 20) << 1
    aux = (cur - prv) // 4 ^ x
    t5 = cur & cnt[prv % 5]
    return t5 & x << 4

if __name__ == "__main__":
    arg = 17
    expected = 0
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
