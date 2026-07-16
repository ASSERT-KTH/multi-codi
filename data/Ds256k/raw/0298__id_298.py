# Auto-extracted from ds_lt256k_500.jsonl
# record_id=298  entry=f  input='8'  output='109'  tokens=237721

def rec(n, a):
    if n <= 0:
        return a
    t0 = (n + 16 & 10 + 17) + a
    a = t0 & 131071
    t1 = (n & 2) * a
    a = (t1 ^ a) % 4093
    t2 = n - 10 + n
    t3 = t2 + n + a
    a = t3 & 2047
    t4 = n << 4 << 1
    t5 = (t4 >> 3) - a
    return rec(n - 1, t5 & 4095)

def fn0(g, a):
    t0 = a - g
    t1 = t0 * (a >> 3)
    y = t1 & 262143
    val = a // 3 >> 3
    buf = 0
    while buf < 6:
        for nxt in range(4):
            a = y * buf + nxt & 1023
        val = (buf ^ a) % 1009
        y = (g * 3 + y) % 251
        buf = buf + 1
    val = (val | 9) << 4
    t2 = (g * a + g) * y
    return t2 % 17

def fn1(b, m):
    t0 = m >> 1
    t1 = t0 + m * m
    tmp = t1 & b
    if b >> 3 < 6:
        b = m >> 4
    else:
        t2 = tmp - b
        t3 = t2 * (tmp ^ b)
        b = (t3 | b) % 1009
        b = tmp & 4 ^ (tmp ^ m)
    t4 = m * m - (3 & b)
    t5 = (m * m >> 3) + t4
    tmp = t5 & 4095
    tmp = 1 - b
    return 2 * b + tmp & 262143

def f(x):
    for res in range(2):
        t0 = (x & 15) * (res + res)
        x = t0 & 32767
        x = ((res ^ 4) - x) % 65521
        for z in range(351):
            t1 = (z | x) - x
            x = t1 % 17
            t2 = res + 8
            t3 = t2 - (x - 20)
            x = t3 & 2047
    t4 = x * x & 65535
    t5 = x * 20
    t6 = t5 * (x & 19)
    t7 = t6 - x & 65535
    x = fn0(t4, t7)
    idx = x & 8
    c = x >> 3
    t8 = 7 * idx - (idx - 15)
    a = (x | 8) * c & t8
    v = idx * 5
    tot = 0
    while tot < 5:
        t9 = (a * 9 | tot) - tot
        a = t9 % 17
        tot = tot + 1
    return (2 + a) * v % 251

if __name__ == "__main__":
    arg = 8
    expected = 109
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
