# Auto-extracted from ds_lt256k_500.jsonl
# record_id=9  entry=f  input='7'  output='225'  tokens=103898

def fn0(c):
    w = [57, 37, 35, 46]
    t0 = w[c % 4] + c
    w[c % 4] = (t0 & c + c & c) % 97
    t1 = c + c
    t2 = t1 * (c * c)
    y = t2 & 65535
    t3 = w[c % 4]
    v = t3 + y | c
    w[c % 4] = c * y % 9973 % 97
    g = c << 1
    return g >> 2 & 262143

def fn1(b, a, d):
    a = fn0(b * b & 16383)
    t0 = a - d ^ 3 - a
    t1 = t0 - (a * b + 10)
    d = t1 % 17
    for z in range(5):
        t2 = (16 & z & (b & a)) + d
        b = t2 & 1023
    t3 = 19 * b ^ d
    a = (t3 + 19) % 17
    t4 = (d & b) + a * 9
    return t4 - (d - 4) * 16 & 8191

def f(x):
    val = x
    t0 = x + x
    t1 = t0 & (x & val)
    t2 = t1 + x & 4095
    t3 = (val ^ 12) % 17
    t4 = 13 + x
    t5 = t4 * (x + x)
    val = fn1(t2, t3, t5 & 32767)
    t6 = val & 16
    y = t6 * (10 & x)
    val = fn0(x * val + x & 65535)
    x = fn0((17 & y ^ val) % 17)
    t7 = y | x
    t8 = t7 - (y >> 3)
    tmp = t8 + y
    for v in range(5):
        tot = 0
        while tot < 44:
            t9 = y * 5 // 6 + tot
            val = t9 & 131071
            tot = tot + 1
        if val ^ tmp == 60:
            t10 = (12 << 4 ^ 10 | x) + y
            y = t10 & 16383
            tmp = (2 - y | tmp) % 17
    for nxt in range(2):
        t11 = (y ^ 3) // 2 - nxt
        tmp = t11 % 17
    acc = 2 + x >> 4
    t12 = (18 | acc) % 1009
    t13 = (acc - y) % 17
    t14 = (tmp | 1) - x
    acc = fn1(t12, t13, t14 & 16383)
    if y >> 2 >= 8:
        t15 = (x * val ^ tmp) // 2
        x = t15 % 1009
        t16 = (tmp + acc) * x
        val = t16 >> 2 & 255
    else:
        x = 5 + y - 9
    t17 = (y | x) // 3
    t = t17 - 20
    t18 = y >> 4
    t19 = x + acc
    t20 = t18 - tmp * 13
    t21 = t19 ^ (x ^ val)
    return t20 + t21 & 255

if __name__ == "__main__":
    arg = 7
    expected = 225
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
