# Auto-extracted from ds_lt256k_500.jsonl
# record_id=441  entry=f  input='15'  output='2'  tokens=231217

def f(x):
    c = [72, 133, 181, 185]
    for cnt in range(6):
        t0 = c[x % 4] ^ x
        x = cnt * x * t0 & 4095
        t1 = c[x % 4]
        t2 = (cnt & x) - t1 ^ x
        x = t2 & 511
    t3 = 4 * c[x % 4]
    y = t3 + (x - 13)
    t4 = c[x % 4]
    t5 = t4 - c[y % 4]
    acc = t5 | x
    t6 = c[acc % 4] << 1
    t7 = y // 6 * t6 << 4
    c[x % 4] = t7 % 251
    t = 0
    while t < 5:
        for res in range(4):
            t8 = res - y ^ y & x
            acc = t8 % 4093
            t9 = t * x
            t10 = t9 + (res ^ 15)
            acc = t10 + y & 1023
            t11 = x - res
            t12 = t11 & 4 - acc
            c[x % 4] = (t12 + 4) % 251
        w = 0
        while w < 3:
            c[acc % 4] = (y ^ 14 | 1 + acc) % 251
            w = w + 1
        for buf in range(10):
            acc = y & buf
            t13 = c[acc % 4]
            t14 = 3 + x
            t15 = c[x % 4]
            t16 = acc ^ 16
            t17 = t14 * (t13 + t)
            t18 = t16 - (t | t15)
            acc = (t17 ^ t18) % 4093
        t = t + 1
    d = x * y // 7 % 251
    t19 = d ^ c[y % 4]
    t20 = y - d >> 3
    aux = t20 + t19 // 3
    v = y % 4093
    cur = (x & 4) - v + v
    for s in range(3):
        c[aux % 4] = ((12 | s) + cur) % 251
        d = (y ^ aux ^ d) % 251
    for e in range(100):
        y = 18 + y & 8191
        t21 = v * e // 3 - e
        y = t21 & 1023
    t22 = 8 * 8
    t23 = t22 + aux * acc
    b = t23 % 251
    if 8 & cur > 0:
        d = aux - b << 2
    m = b + 10
    return (15 - d) % 251

if __name__ == "__main__":
    arg = 15
    expected = 2
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
