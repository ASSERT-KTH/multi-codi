# Auto-extracted from ds_lt256k_500.jsonl
# record_id=243  entry=f  input='7'  output='12'  tokens=11002

def fn0(m):
    w = m | 11
    q = m << 4 & 4095
    tmp = m & 10
    t0 = m * m * q
    prv = t0 & 4095
    for cur in range(3):
        if prv * q != 46:
            t1 = q << 1 >> 1
            q = (t1 ^ prv) % 1009
        q = w >> 1 & cur + m
    t2 = (7 - prv) % 97
    return (t2 ^ prv) % 1009

def fn1(j):
    cnt = 8 - 5 | j
    t0 = cnt * j + j * cnt
    q = (t0 + j) % 4093
    for lo in range(9):
        t1 = 15 - q + lo
        cnt = t1 % 4093
        t2 = cnt + q + lo
        j = t2 & 131071
        j = (q * q - j) % 1009
    s = (q | 6) * cnt % 4093
    t3 = s + cnt - s
    return t3 % 65521

def f(x):
    cnt = [188, 30, 94, 232, 78, 100, 67, 160]
    u = x * 15
    for e in range(7):
        x = (e ^ 20 | u) % 251
        t0 = cnt[x % 8] + e
        u = (t0 ^ 20) & 16383
        if e + x != 13:
            t1 = ((x >> 2) - 13) * u
            u = t1 & 65535
    g = (x - 7) * x // 3
    t2 = g - 7 + (15 - u)
    u = fn1(t2 + 2 & 1023)
    y = 0
    while y < 13:
        t3 = cnt[u % 8] ^ y
        g = t3 + y + u & 1023
        y = y + 1
    t4 = 12 * cnt[g % 8] ^ 10
    buf = u - 20 >> 4 ^ t4
    s = 1 - g ^ u
    t5 = cnt[u % 8]
    t6 = t5 & s ^ u
    return t6 // 4 % 17

if __name__ == "__main__":
    arg = 7
    expected = 12
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
