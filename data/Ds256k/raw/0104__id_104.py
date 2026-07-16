# Auto-extracted from ds_lt256k_500.jsonl
# record_id=104  entry=f  input='4'  output='24'  tokens=41331

def fn0(c):
    if 14 + 8 | c != 55:
        c = c + c
    else:
        t0 = 13 << 2
        t1 = t0 & c >> 2
        c = t1 - c
    g = 0
    while g < 5:
        t2 = (g << 3) + g
        c = (t2 | c) % 4093
        g = g + 1
    if 9 - c >= 33:
        c = c ^ 8
    else:
        c = c | 1
        t3 = c - 6 ^ c
        t4 = t3 ^ (3 + 12 ^ c)
        c = t4 & 8191
    nxt = c * c * c % 97
    z = nxt ^ 10
    return nxt * z - c & 8191

def fn1(j):
    nxt = [153, 154, 149, 208, 91, 109, 26]
    t = 11 | j
    b = t + t
    t0 = t & j ^ 9
    t = fn0(t0 & 2047)
    t1 = nxt[b % 7] - 16
    t2 = t1 - t * t & 65535
    nxt[t % 7] = t2 % 251
    for c in range(9):
        nxt[c % 7] = b * b % 17
        t3 = c | nxt[b % 7]
        t = t3 & 65535
        t = (j // 2 ^ c) & 262143
    t4 = nxt[b % 7] - j
    idx = t4 - (j + t)
    if t // 7 > 51:
        t5 = t // 3 % 17
        t6 = nxt[j % 7]
        t = t5 ^ t6
    else:
        g = 0
        while g < 3:
            t7 = idx * nxt[j % 7]
            j = t7 % 1009
            g = g + 1
    t8 = nxt[t % 7]
    t9 = j ^ b ^ t8
    t10 = t9 | nxt[t % 7]
    return t10 % 1009

def f(x):
    res = 12 & x
    if res ^ 5 == 3:
        x = fn1(((res - x ^ x) - res) % 9973)
        for tmp in range(7):
            t0 = (x >> 3) - tmp
            res = t0 % 4093
            t1 = (x ^ tmp ^ x) // 7
            x = t1 & 16383
            t2 = (res | 19) // 4 + tmp
            x = t2 % 17
    t3 = (20 - res) * (res & x)
    d = t3 & 8191
    t4 = d // 8 // 6
    d = fn1(t4 % 9973)
    res = (x - res) // 8
    t5 = (d + x) // 5
    x = fn1(t5 % 4093)
    res = d * 15
    for prv in range(104):
        t6 = res - d
        t7 = t6 ^ d + x
        res = t7 % 17
    return (res << 2) % 9973

if __name__ == "__main__":
    arg = 4
    expected = 24
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
