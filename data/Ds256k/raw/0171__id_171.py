# Auto-extracted from ds_lt256k_500.jsonl
# record_id=171  entry=f  input='15'  output='0'  tokens=54249

def rec(n, a):
    if n <= 0:
        return a
    a = (n | a) % 97
    t0 = (6 | n) ^ a
    a = t0 & 131071
    t1 = (a << 3) % 17
    return rec(n - 1, t1)

def fn0(a, c):
    res = 0
    while res < 6:
        if c << 4 == 41:
            c = (c * c << 4) % 4093
            t0 = (c | a) ^ 19 - c
            c = t0 & 255
        else:
            t1 = a * 5
            t2 = t1 * (4 + 5)
            c = (t2 + res) % 97
            a = ((res | 3) ^ a) & 1023
        if res | c == 58:
            t3 = (c | 5) - a
            a = t3 & 2047
            a = a - 7 & 4095
        a = (c * c ^ c ^ res) % 4093
        res = res + 1
    t4 = (c ^ 13) & 32767
    a = rec(95, t4)
    t5 = 16 - c + a
    c = t5 * 15 & 131071
    t6 = a - c
    t7 = t6 * (a * c)
    t8 = t7 - c & 32767
    c = rec(56, t8)
    a = (c << 4) - a & 32767
    m = 0
    while m < 7:
        if c & a >= 13:
            t9 = c + c ^ m
            a = t9 % 97
        else:
            c = a * m % 4093
        m = m + 1
    a = (a << 3) - 10
    t10 = c & a
    t11 = t10 & c * c
    return t11 + c & 4095

def fn1(c):
    j = 0
    while j < 5:
        if c ^ j < 61:
            c = (j - 20 - c) % 17
        else:
            t0 = j + 20 + c
            c = t0 & 262143
        if c + c <= 32:
            c = (c - 16) % 65521
        j = j + 1
    for tmp in range(6):
        c = (1 | c) & (tmp | 12)
    nxt = c + c
    t1 = (c | 5) & 65535
    c = rec(25, t1)
    t2 = nxt // 8 // 6 & 131071
    t3 = 15 * c & 1023
    nxt = fn0(t2, t3)
    u = (9 - nxt) // 8
    for prv in range(2):
        nxt = prv * nxt % 17
    u = ((u ^ c) >> 4) * c & 1023
    return (nxt ^ c) % 65521

def f(x):
    val = x * x // 7
    tmp = val * x & val | x
    b = 0
    while b < 11:
        t0 = 20 * tmp ^ b
        val = t0 % 4093
        t1 = val >> 4 ^ b
        tmp = t1 % 251
        b = b + 1
    v = x - tmp
    for p in range(7):
        z = 0
        while z < 7:
            t2 = val + val | val
            t3 = (t2 << 2) + z
            tmp = t3 & 262143
            z = z + 1
        t4 = (x ^ p ^ val) - val
        x = t4 % 9973
    m = (1 & tmp | v) ^ v
    cur = m // 8 >> 1
    for w in range(79):
        v = (val ^ tmp | v) % 4093
        cur = (6 & v) + (cur + cur) & 255
    if cur - 2 == 53:
        if m + val >= 9:
            t5 = (11 ^ x) << 2
            x = t5 | (val | 7 | 8)
            t6 = cur // 5 // 5 & 4095
            m = rec(20, t6)
        else:
            x = (5 | x) + tmp
            t7 = 6 | m
            t8 = t7 & tmp + x
            cur = t8 ^ x
    t9 = (tmp + x) // 3 << 4
    q = t9 % 4093
    u = 0
    while u < 5:
        q = m - 5 + u & 1023
        t10 = (tmp | cur) - u
        x = t10 & 16383
        val = 5 - val & 4095
        u = u + 1
    return m * tmp % 251

if __name__ == "__main__":
    arg = 15
    expected = 0
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
