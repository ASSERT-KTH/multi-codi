# Auto-extracted from ds_lt256k_500.jsonl
# record_id=268  entry=f  input='14'  output='126792'  tokens=14698

def fn0(j):
    t0 = j * j - j + j
    e = t0 % 65521
    tmp = (j & 5) + (j - e) | 10
    t1 = 5 + e * tmp
    j = t1 & tmp + e + 19
    for v in range(9):
        tmp = (v + 12 | j - 15) % 65521
        j = (e // 6 | tmp) + j & 4095
        if 13 ^ 9 ^ e < 26:
            tmp = (v + j - j) % 65521
        else:
            tmp = (v ^ 10) - 17 + tmp & 262143
            t2 = (18 + tmp) % 9973 * 18
            e = (t2 | e) & 32767
    if 14 * tmp != 60:
        t3 = (e | tmp) // 3
        e = t3 << 3 & 32767
        j = 4 + tmp
    else:
        for cur in range(3):
            t4 = (j >> 3) + (2 & tmp)
            tmp = t4 % 9973
            j = ((j + e) * e ^ tmp) & 511
    t5 = j >> 1
    tmp = t5 ^ 11 * 11
    t6 = 15 ^ tmp | j
    return t6 % 9973

def fn1(e, g):
    tmp = [104, 175, 298, 32, 209]
    t0 = (tmp[e % 5] & 9) + g
    t1 = t0 + (e // 7 ^ e * g)
    z = t1 & 2047
    nxt = 0
    while nxt < 10:
        t2 = g // 8 >> 1
        t3 = 18 * e * 17
        t4 = t2 & t3 | z
        z = t4 % 65521
        nxt = nxt + 1
    for cur in range(6):
        t5 = e - 14 - z
        z = t5 % 1009
        g = (cur + cur - cur + z) % 65521
    t6 = g + g - z // 6
    tmp[z % 5] = t6 % 1009
    v = 2 - g ^ e * 7
    t7 = 3 + v - z
    e = fn0(t7 % 1009)
    t8 = e - g | v
    return t8 & 8191

def f(x):
    t = [192, 208, 68, 123, 146, 244, 222]
    s = 8 ^ x
    if 4 + t[x % 7] <= 64:
        t[x % 7] = x & t[s % 7]
        s = (x ^ 16) - s
    else:
        for cur in range(7):
            x = s * x % 4093
            t0 = t[x % 7] >> 3
            t[cur % 7] = (t0 + s * cur) % 251
        if s << 3 >= 53:
            s = x | t[x % 7]
    t1 = t[x % 7]
    t2 = ((s | 16) + t1) * x
    s = t2 & 8191
    x = x >> 4
    j = 0
    while j < 20:
        if t[s % 7] >> 4 < 14:
            x = (x ^ j) & 1023
            t3 = (j | x) * (s * x)
            t[x % 7] = (t3 << 3 & 4095) % 251
        x = x * s % 4093
        x = (j - s << 2) % 1009
        j = j + 1
    return (x | 6) - s & 131071

if __name__ == "__main__":
    arg = 14
    expected = 126792
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
