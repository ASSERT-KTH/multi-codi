# Auto-extracted from ds_lt256k_500.jsonl
# record_id=264  entry=f  input='9'  output='108'  tokens=169102

def fn0(c):
    t0 = c * c >> 3
    e = t0 & 255
    t1 = c // 3
    t2 = 19 - e
    t3 = t1 - (e + e)
    t4 = t2 - (c + e)
    d = t3 - t4
    t5 = (e ^ c) // 5
    nxt = t5 % 65521
    m = 0
    while m < 11:
        if nxt & e >= 42:
            nxt = m * nxt % 65521
        t6 = d * 3 >> 2
        c = (t6 + c) % 65521
        if c - m <= 13:
            c = d - m & 262143
        else:
            t7 = d * c + nxt
            t8 = t7 * (m + m + nxt)
            e = t8 & 511
            t9 = (d << 3) // 8
            nxt = (t9 | m) % 251
        m = m + 1
    for s in range(12):
        d = (e + c + c | d) & 4095
    e = nxt >> 1
    return ((d | 13) - (e - d)) % 65521

def f(x):
    j = x + x << 3
    if x - 4 != 24:
        for res in range(10):
            t0 = (x | j) * x
            j = t0 % 65521
            t1 = (res << 2) + (20 ^ res)
            j = (t1 + j) % 97
        j = fn0(19 * x & 65535)
    else:
        if j + j != 34:
            t2 = (j | x) * (x & 12) >> 4
            j = fn0(t2 % 97)
    j = fn0((x + x) % 97)
    for b in range(1132):
        j = (j + b) % 65521
    j = fn0(x % 65521)
    for t in range(6):
        j = j // 3 & 511
    t3 = j ^ 5
    t4 = t3 * (1 - 17)
    x = (t4 << 2) % 65521
    t5 = 11 + 15 | j
    return (t5 << 2) % 65521

if __name__ == "__main__":
    arg = 9
    expected = 108
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
