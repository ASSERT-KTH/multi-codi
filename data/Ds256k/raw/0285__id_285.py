# Auto-extracted from ds_lt256k_500.jsonl
# record_id=285  entry=f  input='10'  output='208'  tokens=41430

def fn0(m):
    t0 = 15 | 5
    b = t0 - 7 * m
    for v in range(10):
        t1 = b * b + (m + m) + m
        b = t1 % 97
    if b >> 4 > 52:
        m = 4 + b
        e = 0
        while e < 5:
            b = (18 * e | b) % 9973
            t2 = e - 19 - b
            t3 = t2 | b - 2 & b
            m = t3 % 9973
            b = (e * e - b) * m & 16383
            e = e + 1
    for y in range(12):
        for buf in range(7):
            t4 = buf * buf + m
            b = t4 << 2 & 1023
            t5 = (12 << 2) + m - buf
            b = t5 % 9973
        for prv in range(10):
            t6 = 6 + y
            t7 = t6 | prv - m
            m = t7 % 9973
            t8 = 2 ^ prv ^ m
            b = t8 & 262143
            t9 = 17 * 15 // 6 + m
            m = t9 & 131071
    aux = m | 6
    j = 13 + b
    u = 0
    while u < 11:
        b = u & m
        if b | 20 != 22:
            t10 = 8 * 3 | b
            b = t10 % 9973
        u = u + 1
    return m - b & 255

def f(x):
    t0 = (x | 10) * x
    t = t0 - x
    if x * x == 52:
        x = fn0((t >> 1) // 5 * x % 65521)
    j = 0
    while j < 4:
        for cnt in range(79):
            t = (t ^ j) * (cnt | t) & t
        t1 = (x >> 2) + x
        t = t1 & (t & 3) - j
        t2 = x * t
        t3 = t2 & j - 3
        t4 = (9 ^ t) // 3
        t = (t3 | t4) % 4093
        j = j + 1
    acc = x * x % 97
    return acc + x << 4 & 1023

if __name__ == "__main__":
    arg = 10
    expected = 208
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
