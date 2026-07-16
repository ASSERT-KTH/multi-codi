# Auto-extracted from ds_lt256k_500.jsonl
# record_id=78  entry=f  input='20'  output='55'  tokens=253769

def rec(n, a):
    if n <= 0:
        return a
    tot = (n | a) & 16383
    nxt = 0
    while nxt < 6:
        t0 = a * n % 1009
        a = (t0 + a) % 1009
        a = (a // 7 | tot) & 16383
        nxt = nxt + 1
    t1 = a // 8 ^ a << 4
    t2 = t1 & (tot - a) * (a * n)
    return rec(n - 1, t2)

def fn0(b):
    t0 = (b | 2) * (b % 17) & 131071
    b = rec(88, t0)
    buf = b + 20
    for tot in range(5):
        if b * tot <= 22:
            t1 = buf ^ tot ^ buf
            buf = t1 & 255
            b = tot * buf & 16383
        else:
            b = tot + buf & 8191
        t2 = 8 + 17 - tot
        buf = (t2 + buf) % 17
    y = b >> 3 ^ buf
    t3 = b | 4
    t4 = t3 * (b + buf)
    t5 = (t4 >> 4) % 65521
    y = rec(82, t5)
    t6 = (b - 10) * 18 - y
    return t6 % 65521

def fn1(b):
    for e in range(11):
        if 10 - e - b >= 13:
            b = e + 10 + b & 16383
        z = 0
        while z < 5:
            b = (e + z + b) % 97
            t0 = e - z + (e ^ b)
            b = t0 + (b % 251 >> 3) & 2047
            z = z + 1
        t1 = b * e - 9
        b = t1 % 4093
    c = 9 << 4 | b
    nxt = c % 97 * (12 - c) % 4093
    t2 = b * nxt * b
    q = (t2 >> 1) % 4093
    lo = 0
    while lo < 8:
        if b ^ 16 > 10:
            t3 = (lo - q) * (lo - 16)
            t4 = 12 - b - q ^ t3
            q = t4 % 4093
            t5 = (b << 3) + lo * c + q
            b = t5 & 8191
        else:
            b = (b ^ nxt) % 97
            b = ((14 & nxt) + 19 | lo) & 262143
        lo = lo + 1
    c = fn0((q - c) % 4093)
    return (3 - b | c) & 32767

def f(x):
    tmp = [71, 85, 90, 53, 94, 73]
    prv = 0
    while prv < 9:
        for e in range(10):
            t0 = ((e - 1) * e | 5) - x
            tmp[e % 6] = t0 % 97
            t1 = 19 ^ prv ^ e
            t2 = 12 + prv | 20
            t3 = t1 + t2 ^ x
            x = t3 % 251
        for val in range(11):
            x = prv - x & x
            t4 = 4 - tmp[prv % 6]
            t5 = (prv - val ^ val) * t4 ^ x
            x = t5 % 65521
            t6 = 16 - 7
            t7 = t6 + (x & prv)
            x = t7 - 20 & 4095
        t8 = prv + prv + 11 + x
        tmp[prv % 6] = t8 % 97
        prv = prv + 1
    acc = x ^ 8 ^ x
    t9 = x - 9
    t10 = t9 + (acc - x)
    cur = t10 >> 2
    z = 0
    while z < 38:
        t11 = (tmp[cur % 6] ^ x) + 2
        acc = t11 // 2 - z & 1023
        t12 = x & 2 & acc
        cur = (t12 - z) % 65521
        for d in range(6):
            x = (d ^ acc) & 32767
        z = z + 1
    for tot in range(4):
        if x & tmp[acc % 6] == 30:
            t13 = 10 * acc - cur
            tmp[cur % 6] = t13 % 251 % 97
        else:
            t14 = 18 + tmp[cur % 6] - tot
            x = t14 & 262143
            t15 = tmp[x % 6] + cur + 5
            cur = t15 & 8191
        t16 = (20 | 15 | cur) * x
        cur = t16 % 65521
    buf = x >> 1
    y = (3 + cur << 2) // 2
    j = cur << 3
    t17 = (y - 19) // 7
    return t17 % 251

if __name__ == "__main__":
    arg = 20
    expected = 55
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
