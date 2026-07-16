# Auto-extracted from ds_lt256k_500.jsonl
# record_id=159  entry=f  input='5'  output='81'  tokens=59186

def fn0(m, g, d):
    for w in range(7):
        d = w * m & 65535
        m = (d | m) & 4095
        g = (d // 3 - g) % 1009
    t0 = (17 ^ g) + m
    g = t0 - m
    g = d ^ 13
    t1 = g + 17 + (d - 13)
    g = m + m - d - t1
    m = (g ^ 11) % 1009 ^ g
    for a in range(2):
        t2 = (d & m) % 17 - d
        g = t2 + g & 32767
    g = 6 - d
    g = g % 9973 // 7
    return (m + m) // 4 & 4

def f(x):
    cur = [1, 58, 14, 23, 44, 27, 63]
    if x * x >= 11:
        t0 = cur[x % 7]
        t1 = x + x + (x - 18)
        x = (x + x) * t0 * t1
        x = x + 2 - x
    else:
        t2 = cur[x % 7] ^ x
        x = t2 >> 1
    b = x - 7
    c = b + x >> 4
    t3 = 4 + x
    b = t3 & x * 2
    b = c + c
    t4 = (4 & c) * (18 + x)
    for m in range(454):
        if c & 16 <= 7:
            t5 = (b >> 1) - 9
            t6 = t5 ^ cur[c % 7]
            b = t6 & 8191
    return (t4 ^ 1) % 4093

if __name__ == "__main__":
    arg = 5
    expected = 81
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
