# Auto-extracted from ds_lt256k_500.jsonl
# record_id=98  entry=f  input='16'  output='935'  tokens=260855

def fn0(j):
    aux = [165, 183, 101, 111, 11, 229]
    idx = j % 97 + (8 - j) - 19
    if 9 + j <= 23:
        t0 = aux[idx % 6] | j
        idx = (9 & j) - t0 ^ idx
        m = 0
        while m < 2:
            t1 = 1 * aux[idx % 6] % 17
            t2 = (aux[m % 6] | 7) * idx
            aux[m % 6] = ((t1 | t2) & 262143) % 251
            j = (idx + j) % 9973
            m = m + 1
    t3 = aux[idx % 6]
    t4 = idx - t3
    t5 = aux[j % 6]
    t6 = t4 - (j ^ idx)
    v = t6 - t5 % 97
    idx = idx - 9
    v = 6 + j
    t7 = j * 18
    t8 = t7 ^ v + 10
    j = t8 * idx & 32767
    t9 = j // 6 + idx
    return t9 & 8191

def f(x):
    for prv in range(11):
        t0 = x | prv
        t1 = t0 ^ (x ^ prv)
        x = t1 & 511
    if x | 9 == 16:
        x = 2 & x
    else:
        t2 = (x + x) * x
        x = t2 + (x & 18 ^ x)
        x = fn0(x * x % 4093)
    t3 = x * x
    t4 = t3 + x // 6
    x = fn0((t4 | x) & 65535)
    m = 0
    while m < 11:
        if 18 + 14 - x < 14:
            t5 = m * 12 - m
            t6 = t5 * m | x
            x = t6 % 4093
        x = (14 ^ x) % 97
        t7 = (x | 17) * (m + x)
        x = t7 // 7 % 97
        m = m + 1
    cnt = x % 97
    for v in range(6):
        t8 = (9 ^ cnt) // 8
        cnt = t8 & 32767
    t9 = x % 97
    j = t9 + (2 - x)
    if j * j != 4:
        if cnt * x < 59:
            j = fn0((x << 3) % 97)
            t10 = (x >> 3) - cnt
            cnt = fn0(t10 // 7 & 32767)
        else:
            j = x * cnt & 16383
            x = fn0(cnt % 97)
        t11 = 8 + j
        t12 = t11 + (1 & x)
        x = fn0(t12 % 97)
    b = cnt + x
    for a in range(9):
        t13 = a + b
        t14 = (14 | a) * b
        t15 = t13 | x - 14
        cnt = t14 * t15 & 32767
        acc = 0
        while acc < 6:
            j = (x * b ^ j) % 97
            cnt = (x >> 4 | cnt) & 1023
            acc = acc + 1
        b = (x >> 3) - b & 262143
    lo = 0
    while lo < 8:
        for nxt in range(12):
            t16 = j * j
            t17 = t16 - (j ^ x)
            j = t17 % 97
            t18 = (cnt - nxt & cnt << 3) + nxt
            b = t18 & 511
            t19 = (cnt + b) * (7 | b) - 7
            j = (t19 - nxt) % 97
        for tot in range(2):
            j = (b & 19 ^ j) + b & 8191
        t20 = (x - 15 >> 2) + x + lo
        b = t20 & 16383
        lo = lo + 1
    b = fn0((b // 8 & j ^ b) % 97)
    t = 0
    while t < 3:
        c = 0
        while c < 7:
            x = (2 & c ^ j) & 131071
            x = t * t * x % 97
            t21 = x % 97
            t22 = t21 + (b - j)
            x = t22 % 4093
            c = c + 1
        t = t + 1
    t23 = (j ^ b) * (7 + 4)
    return (t23 | x >> 3 ^ cnt) % 4093

if __name__ == "__main__":
    arg = 16
    expected = 935
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
