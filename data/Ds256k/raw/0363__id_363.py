# Auto-extracted from ds_lt256k_500.jsonl
# record_id=363  entry=f  input='20'  output='3'  tokens=215321

def fn0(a, j):
    if j // 5 < 38:
        buf = 0
        while buf < 10:
            a = (a + a) % 251
            t0 = j // 7 | buf
            a = t0 % 1009
            buf = buf + 1
        j = 19 & a
    else:
        q = 0
        while q < 11:
            t1 = 9 - q
            t2 = t1 & q - 4
            a = (t2 ^ j) % 1009
            q = q + 1
    s = j + a >> 1
    t3 = (j << 1) * s
    a = t3 // 2 & 4095
    return (j * a | 20 - s) & 255

def f(x):
    t0 = x << 3
    t1 = t0 | x * x
    t2 = (x + 3) * 7
    t3 = t1 + t2 & 2047
    t4 = 11 + x ^ x << 3
    t5 = (t4 | (x * x | 7)) % 97
    x = fn0(t3, t5)
    t6 = x << 3
    aux = t6 ^ x + 16
    cur = aux - x
    v = x + 15
    for val in range(3):
        t7 = x * val * (val * 15) // 6
        x = t7 % 97
        t8 = v // 6
        t9 = t8 - (val ^ aux)
        aux = t9 & 131071
    for p in range(29):
        t10 = 18 + 5 ^ (x ^ 6) ^ p
        cur = t10 & 262143
        hi = 0
        while hi < 10:
            t11 = x - cur & aux
            t12 = t11 - 8 + v
            v = t12 % 4093
            hi = hi + 1
    q = 12 + cur & cur >> 4
    w = aux * v % 97
    t13 = (q >> 1) * v - 7
    j = t13 & 2047
    return (cur >> 2) % 4093

if __name__ == "__main__":
    arg = 20
    expected = 3
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
