# Auto-extracted from ds_lt256k_500.jsonl
# record_id=184  entry=f  input='16'  output='4080'  tokens=65543

def fn0(b, j):
    y = [121, 239, 171, 67, 94, 103, 130, 36]
    t0 = (1 ^ j) * b
    j = t0 % 17
    t1 = j + j
    j = t1 + j // 8
    for z in range(3):
        for d in range(11):
            t2 = y[d % 8]
            t3 = b + d
            t4 = t3 & (t2 | d)
            y[j % 8] = (t4 << 4) % 251
            y[d % 8] = (z * d | j) % 251
        if 11 - z - b != 4:
            t5 = y[j % 8]
            t6 = t5 * z
            t7 = y[b % 8]
            t8 = t6 | b - 15
            t9 = j + b + t7
            b = (t8 - t9) % 17
            t10 = (z ^ b) * j
            b = t10 + b & 4095
        else:
            t11 = (z << 3 & z) * z
            b = (t11 | b) % 97
    nxt = 0
    while nxt < 2:
        for buf in range(6):
            y[j % 8] = (9 * 4 - j) % 251
        b = (y[j % 8] ^ nxt) % 65521
        for hi in range(10):
            t12 = b - j << 3
            b = t12 % 17
            t13 = (j + 3 - (9 - hi)) * b
            j = t13 & 32767
        nxt = nxt + 1
    t14 = b + b + 16
    return (t14 - (b >> 3 | b)) % 65521

def f(x):
    tmp = (20 - x ^ 19 - x) // 3
    nxt = (x ^ 14) + x
    if nxt * 1 <= 35:
        nxt = x + nxt
    else:
        x = nxt & x
        t0 = x ^ 3 | 9 * nxt
        nxt = t0 * 11
    if nxt ^ x < 51:
        t1 = (14 & tmp) - tmp & 511
        tmp = fn0(2 & tmp, t1)
    else:
        t2 = x * 5 * nxt
        x = t2 % 1009
    t3 = (x | 19) + tmp
    t4 = t3 << 1 & 32767
    t5 = tmp % 1009
    t6 = t5 + (7 & 18)
    x = fn0(t4, t6 % 4093)
    for buf in range(86):
        t7 = 6 - 9 | x
        tmp = (t7 ^ tmp) % 1009
    return 12 - x + (nxt & 1) & 4095

if __name__ == "__main__":
    arg = 16
    expected = 4080
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
