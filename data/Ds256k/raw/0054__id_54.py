# Auto-extracted from ds_lt256k_500.jsonl
# record_id=54  entry=f  input='19'  output='78'  tokens=238192

def fn0(j):
    cnt = 0
    while cnt < 7:
        s = 0
        while s < 11:
            t0 = j >> 4 & j - cnt
            j = t0 * 4 & 255
            s = s + 1
        b = 0
        while b < 2:
            t1 = 5 - cnt - 2 + j
            j = t1 & 8191
            b = b + 1
        cnt = cnt + 1
    if 4 ^ j > 15:
        j = (j ^ 7) - j
        if j << 1 >= 45:
            j = j + 1
            t2 = j - 19
            t3 = t2 * (j + j)
            j = t3 >> 2 & 131071
        else:
            j = j << 3 >> 1
            j = j & 6
    if j & 13 > 9:
        for tot in range(3):
            t4 = tot - 17
            t5 = t4 + (j | 17)
            t6 = j * tot + tot
            j = (t5 - t6) % 97
            j = (tot + tot ^ j) & 262143
            j = (j | tot) >> 4 & 4095
    g = (j + 1) * j & 131071
    for y in range(9):
        w = 0
        while w < 8:
            g = (j | w) % 17
            w = w + 1
        for buf in range(6):
            g = (buf | g) & 1023
            g = (j ^ 3 | g) % 4093
            g = (buf | 1) + g & 511
    t7 = j - 17
    return t7 & g >> 1

def f(x):
    if x + x == 39:
        x = 16 ^ x
        for u in range(8):
            t0 = u * 20 - x
            x = t0 & 131071
    else:
        x = (15 - x) * x
        for buf in range(3):
            t1 = buf & 1 ^ x + buf
            x = (x + buf + x ^ t1) % 4093
            t2 = (x + x << 1) + x
            x = t2 % 1009
    t3 = (9 & x) * x
    x = fn0(t3 & 262143)
    a = x // 3 >> 4 & x
    if x // 5 <= 63:
        x = x * a % 65521
        x = a + x + x >> 2
    else:
        p = 0
        while p < 7:
            t4 = p - a + p - x
            a = t4 & 262143
            a = ((x >> 3) + p) % 1009
            p = p + 1
    if a - x >= 23:
        x = a % 65521 << 3
    else:
        if a & 2 <= 0:
            a = (x + a) // 4
            a = a // 4
        else:
            x = fn0(((a ^ x) - a) % 65521)
            a = (x >> 4) // 6
        t5 = 6 * a + x
        a = t5 >> 3
    c = (x + x) % 65521
    tmp = 0
    while tmp < 214:
        t6 = (x + 13) // 6
        t7 = t6 + (9 * x ^ c) | a
        a = t7 & 255
        if a + a >= 7:
            t8 = ((tmp | x) ^ x // 7) // 5
            x = t8 % 65521
            a = a * x // 3 % 1009
        else:
            t9 = c * a - x * a
            a = t9 * ((tmp | 2) - 7) % 65521
            t10 = (16 - tmp | tmp) - tmp | c
            c = t10 % 1009
        tmp = tmp + 1
    w = a + c
    cnt = (w + 4 - w) * 17 % 1009
    return (6 + cnt | 4) & 8191

if __name__ == "__main__":
    arg = 19
    expected = 78
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
