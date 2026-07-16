# Auto-extracted from ds_lt256k_500.jsonl
# record_id=464  entry=f  input='6'  output='262080'  tokens=228511

def rec(n, a):
    if n <= 0:
        return a
    t0 = a - 12
    t1 = t0 * (6 * n)
    nxt = t1 & 255
    a = n & nxt
    t2 = nxt % 251
    t3 = t2 + (a + n)
    return rec(n - 1, t3 % 4093)

def fn0(b):
    v = 5 * b
    if 14 ^ b > 48:
        for g in range(5):
            t0 = (v - 3) * 3
            t1 = t0 * (v - b >> 1)
            b = t1 % 9973
            v = (g - v ^ b) & 4095
            t2 = b + b + v
            b = t2 & 1023
    c = b + 1
    t3 = (v % 4093 * b ^ c) % 9973
    b = rec(110, t3)
    p = b - 19 + c & b
    c = (c - p) // 7
    t4 = 6 * v - v
    return t4 * (12 & c & v) & 255

def f(x):
    t0 = x ^ 12 ^ x
    x = rec(68, t0 % 4093)
    t1 = x * x << 1
    t2 = t1 + (x + 7 >> 1) & 131071
    x = rec(114, t2)
    aux = 0
    while aux < 7:
        u = 0
        while u < 11:
            x = (u + aux - x) % 65521
            x = (x - u) % 4093
            x = (aux - u | x) & 255
            u = u + 1
        t3 = aux + aux
        t4 = (x ^ aux) << 3
        t5 = t3 + aux * 20
        x = (t4 + t5) % 17
        t6 = x - 9 + (aux & x)
        x = t6 + ((aux ^ x) << 1) & 8191
        aux = aux + 1
    if x + x > 47:
        x = (x - 12) * x % 17
        for w in range(2):
            t7 = (x - 1 >> 3) // 8
            x = t7 % 17
    t8 = x % 65521
    t9 = t8 ^ x - 14
    cnt = t9 + 17
    t10 = cnt // 3 // 2
    val = t10 >> 2
    lo = 17 + 10 - cnt
    t11 = cnt // 6
    t12 = (2 | x) % 17
    t13 = t11 - (17 | cnt)
    g = t12 ^ t13
    for tmp in range(8):
        if x - tmp >= 53:
            t14 = cnt * x - x
            x = t14 // 2 % 4093
        t15 = tmp - val << 1
        g = t15 * lo % 65521
    for e in range(13):
        for m in range(10):
            t16 = 7 + g + m
            val = t16 % 17
            x = (m - e - x) % 65521
            g = (8 ^ g) - cnt & 2047
    for d in range(10):
        val = val & d
    t17 = 13 - (x - 4)
    return t17 - ((x ^ val) >> 2) & 262143

if __name__ == "__main__":
    arg = 6
    expected = 262080
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
