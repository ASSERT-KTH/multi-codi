# Auto-extracted from ds_lt256k_500.jsonl
# record_id=235  entry=f  input='3'  output='1005'  tokens=185883

def rec(n, a):
    if n <= 0:
        return a
    t0 = (n ^ 3) // 5
    t1 = t0 + n - a
    prv = t1 & 255
    a = (n + prv) % 251
    prv = (prv % 251 + n) % 251
    t2 = ((n ^ 12) + a) % 17
    return rec(n - 1, t2)

def fn0(c, a):
    t0 = a & 4
    b = t0 ^ c % 9973
    for w in range(4):
        if c - 10 > 46:
            a = ((w | 6 | 13) ^ c) & 262143
            t1 = w + w << 4
            a = t1 - b & 255
        else:
            t2 = 19 - c & (2 ^ w) | 14
            c = t2 & 262143
            t3 = a | c
            c = t3 & (w ^ a)
        b = (b ^ 7) & 131071
        if c | b <= 5:
            t4 = (b << 4) * w * b
            a = t4 % 4093
        else:
            b = (w - a) % 4093
    t5 = (c ^ a) * (c ^ 4)
    g = t5 % 17
    lo = c * 7
    t6 = a << 1 & lo // 6
    aux = ((b ^ g) + 14) * t6 % 9973
    for nxt in range(3):
        lo = (c >> 4 ^ nxt) % 1009
        if g * c > 24:
            t7 = 14 + c - (g - 1)
            t8 = (15 ^ 17) + nxt ^ t7
            g = t8 % 17
            t9 = g * lo - (c << 4) ^ nxt
            aux = t9 % 17
        else:
            t10 = nxt * nxt * b
            aux = t10 & 32767
    t11 = 12 - b
    t12 = g ^ b ^ 3
    t13 = t11 * (lo - 4)
    t14 = (t12 | t13) % 9973
    lo = rec(120, t14)
    return ((a ^ b) + (c << 3)) % 4093

def f(x):
    t0 = x << 4 << 3
    x = rec(32, t0 % 1009)
    t1 = (6 ^ x) >> 2
    d = t1 & (x * x | x)
    s = x // 2 | 16
    cur = d - 10
    t2 = x & d
    prv = t2 & x >> 1
    buf = 0
    while buf < 288:
        cur = (prv - 12 ^ cur) % 97
        t3 = s * x - x - buf
        d = t3 % 1009
        x = ((cur | 8) ^ x) & 131071
        buf = buf + 1
    t4 = (cur | 17) & 16383
    t5 = prv - d ^ 6
    d = fn0(t4, t5 & 511)
    return ((12 | 8) - s) % 1009

if __name__ == "__main__":
    arg = 3
    expected = 1005
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
