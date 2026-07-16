# Auto-extracted from ds_lt256k_500.jsonl
# record_id=208  entry=f  input='9'  output='0'  tokens=211916

def rec(n, a):
    if n <= 0:
        return a
    t0 = (n + a) % 65521
    t1 = n - 4 + 8
    w = (t0 - t1) % 17
    t2 = a & 15 ^ n
    w = t2 % 4093
    t3 = a >> 3 & 5 + a
    return rec(n - 1, t3)

def fn0(c, g):
    v = [647, 45, 251, 367]
    c = c | g
    g = (c << 4) + (c & g) & 16383
    t0 = v[g % 4]
    t1 = (t0 | 9) * c
    g = t1 >> 1 & 255
    t2 = v[c % 4]
    c = t2 - c
    cnt = 0
    while cnt < 8:
        if cnt - 4 - g >= 52:
            t3 = v[cnt % 4]
            t4 = cnt - t3
            t5 = t4 * (cnt - c)
            g = t5 & 4095
        else:
            g = c // 7 * g & 1023
        cnt = cnt + 1
    return (c + c) % 4093

def f(x):
    e = x | 12
    t0 = e ^ 9
    j = t0 - (e & 20)
    val = x - 20 ^ e * e
    cur = j - val
    for v in range(9):
        t1 = (15 ^ cur) * (v + 13)
        val = (11 * cur - val - t1) % 97
        b = 0
        while b < 36:
            t2 = val // 7 & j
            t3 = (x & v) * e
            x = (t2 + t3) % 9973
            t4 = val - b ^ v * val
            cur = t4 & 2047
            cur = (cur ^ x) % 9973
            b = b + 1
    acc = cur // 8 + e
    t5 = (e << 3) * (j + 1)
    p = t5 + j
    t6 = 4 * 16 & j << 2
    return t6 * 12 & 16383

if __name__ == "__main__":
    arg = 9
    expected = 0
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
