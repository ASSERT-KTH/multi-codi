# Auto-extracted from ds_lt256k_500.jsonl
# record_id=472  entry=f  input='5'  output='3998'  tokens=169905

def fn0(e, d, a):
    m = [69, 82, 937, 830, 244, 604, 344]
    y = (20 | 3) * (6 * e) % 251
    t0 = (e * y ^ y << 1) * e
    u = t0 % 65521
    d = 1 - u
    t1 = m[d % 7]
    t2 = a ^ t1
    t3 = t2 ^ (y ^ d)
    t4 = y // 8 // 4
    y = t3 + t4
    for res in range(12):
        w = 0
        while w < 10:
            m[e % 7] = ((y >> 4) + u & d) % 1009
            w = w + 1
        u = u * e & 65535
    e = ((5 | 10) << 4) - e
    t5 = m[y % 7]
    t6 = d + t5
    t7 = t6 - (7 | 6)
    t8 = (u - 10) // 2
    y = t7 - t8
    t9 = (13 - m[a % 7]) * d
    return (t9 ^ u) & 8191

def fn1(b):
    for tot in range(4):
        b = (15 + 11 - b) % 1009
        cur = 0
        while cur < 4:
            b = 12 * b % 1009
            b = (tot + 19 << 4) + b & 1023
            cur = cur + 1
    a = 8 + 5 ^ b
    cnt = (20 ^ a | a) + a
    nxt = (b ^ 19) // 4 ^ b
    a = b << 3
    t0 = (b ^ a) * b * nxt
    b = t0 % 1009
    return (nxt | a) - cnt & 7

def f(x):
    cnt = x - 7 - x
    if cnt & x <= 4:
        if x + cnt < 40:
            cnt = cnt + x
        else:
            t0 = (cnt | 3) & 131071
            t1 = x * cnt & 8191
            t2 = 19 & 6 | x
            cnt = fn0(t0, t1, t2 & 255)
        cnt = cnt | 20
    buf = (cnt >> 3) + cnt
    t3 = cnt ^ 7
    prv = t3 + (buf - 4)
    for b in range(12):
        buf = ((cnt & x) - b) % 17
        buf = ((cnt | x) & b) * 12 % 4093
        d = 0
        while d < 12:
            t4 = cnt - 15 ^ cnt + b | buf
            buf = t4 & 8191
            t5 = prv >> 4 ^ prv
            t6 = t5 ^ b ^ cnt
            cnt = t6 & 262143
            d = d + 1
    e = prv % 17 * 17
    lo = 0
    while lo < 11:
        buf = (buf + lo + cnt) % 251
        if x * lo >= 34:
            buf = (lo - 17 + e) % 251
        t7 = (x | prv) % 4093
        t8 = 20 * 8 // 3
        t9 = t7 * t8 - cnt
        cnt = t9 % 17
        lo = lo + 1
    for u in range(8):
        t10 = (x ^ 10) * (buf ^ 12)
        x = t10 % 17
        prv = 3 - e & prv
        x = (u | x) % 251
    val = (2 << 1) - x
    t = (15 | 4) + 6 + prv
    for aux in range(8):
        idx = 0
        while idx < 7:
            t11 = (idx + cnt) % 251 + cnt
            val = t11 % 251
            x = ((20 + aux) * buf ^ x) % 17
            t12 = idx * cnt ^ cnt + 5
            t13 = t12 + (e + x & prv)
            cnt = t13 % 17
            idx = idx + 1
        if cnt >> 2 > 17:
            t14 = e + val + e
            buf = t14 + buf & 4095
        else:
            t = (prv + x << 4 | t) & 255
            x = (aux + val ^ cnt) % 4093
        buf = buf + cnt & 262143
    acc = 13 ^ prv
    z = t // 4 % 251
    q = 0
    while q < 2:
        z = ((z ^ 12) + 6) % 17
        q = q + 1
    return (x % 17 - buf) % 4093

if __name__ == "__main__":
    arg = 5
    expected = 3998
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
