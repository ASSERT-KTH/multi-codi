# Auto-extracted from ds_lt256k_500.jsonl
# record_id=23  entry=f  input='13'  output='49'  tokens=124603

def rec(n, a):
    if n <= 0:
        return a
    a = ((4 | n) & n ^ a) % 1009
    t0 = a * a // 8 & 262143
    return rec(n - 1, t0)

def fn0(m, j):
    c = 0
    while c < 9:
        t0 = c + m - (j | 8) - m
        m = t0 % 17
        c = c + 1
    e = 0
    while e < 3:
        t1 = (e ^ j) // 6 * 5
        m = t1 % 97
        t2 = j >> 2 >> 4 >> 2 ^ m
        m = t2 % 9973
        e = e + 1
    if 3 | m >= 44:
        for val in range(10):
            t3 = (m ^ val) - m
            m = t3 % 9973
            j = j - 19 - j & val
    aux = (j ^ 16) << 3
    t4 = j * aux + aux + j
    s = t4 % 9973
    nxt = (m & s) - s << 4
    m = j * aux % 4093
    t5 = (m | nxt) * s
    return (t5 | j) & 1023

def fn1(m, a, b):
    acc = 0
    while acc < 7:
        t0 = (b + m ^ m) - acc
        a = t0 & 32767
        acc = acc + 1
    if 7 - m <= 61:
        t1 = (b | 13) & 8191
        t2 = (b * a - 9) % 251
        a = fn0(t1, t2)
        t3 = (b ^ m) + a
        b = rec(108, t3 % 1009)
    t4 = (11 ^ 3) * m
    buf = (t4 ^ 17) % 1009
    for e in range(2):
        t5 = buf & 10 & buf
        t6 = t5 + buf - a
        a = t6 % 251
        a = a % 1009
    v = (b ^ buf) // 6
    for y in range(3):
        t7 = (a & v) - y
        b = t7 & 511
    t8 = (a | b) & 32767
    m = rec(95, t8)
    return (14 * 9 ^ v) % 251

def f(x):
    res = (x * x ^ x) * x
    for d in range(4):
        for prv in range(92):
            x = x - 1 & 8191
            x = (res ^ prv) % 251
            x = (x // 7 + res - prv) % 97
    aux = 9 - res - 16
    if res - 6 == 6:
        aux = 16 * 6 | res
        aux = x ^ 6
    else:
        t0 = 6 + res - 5
        t1 = (t0 + x) % 97
        t2 = (res + aux) * aux
        t3 = (aux | res) & res
        t4 = t3 * (x * aux - res) % 251
        x = fn1(t1, t2 & 2047, t4)
    t = 0
    while t < 6:
        t5 = t * t + t + aux
        aux = t5 % 97
        aux = (2 - res | aux) & 131071
        t = t + 1
    if aux + aux < 6:
        x = (16 - x) // 3
        t6 = (res | aux) & 4095
        t7 = 7 - x & 32767
        x = fn0(t6, t7)
    t8 = (16 & 17 << 2) - aux
    aux = rec(109, t8 & 65535)
    q = aux // 2
    return ((res | 9) - aux // 2) % 97

if __name__ == "__main__":
    arg = 13
    expected = 49
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
