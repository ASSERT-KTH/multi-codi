# Auto-extracted from ds_lt256k_500.jsonl
# record_id=12  entry=f  input='10'  output='317'  tokens=31592

def rec(n, a):
    if n <= 0:
        return a
    t0 = a // 2
    a = t0 & a + a
    t1 = a >> 3 << 4
    t2 = t1 + (n ^ 19 | a)
    a = t2 & 1023
    t3 = (9 & n) + n
    t4 = (t3 >> 1) + a
    return rec(n - 1, t4 & 255)

def f(x):
    val = [839, 115, 102, 901, 907]
    b = x - 19
    if x * b <= 7:
        t0 = val[x % 5] * b
        t1 = b * b * t0
        t2 = t1 * ((x ^ b) >> 3)
        x = t2 & 8191
    else:
        t3 = val[b % 5] * b
        t4 = 2 - val[b % 5]
        t5 = (17 ^ x) & t3
        b = t5 * (t4 * b) & 511
    q = 10 * b
    if x ^ 1 < 10:
        c = 0
        while c < 6:
            t6 = q - b + x
            val[q % 5] = t6 % 1009
            b = (x | b) & 262143
            t7 = x * 1 // 3 | x
            b = (t7 | c) & 65535
            c = c + 1
    v = b ^ 4
    j = b + q + 4
    t8 = (v - q) * (v + j)
    t9 = t8 * (b + v ^ 1)
    tmp = t9 % 4093
    if j * v != 33:
        j = (x & 8) - v
        t10 = val[j % 5] - j
        v = j ^ 5 | t10
    else:
        if 6 | v == 33:
            val[q % 5] = (tmp + q) % 1009
        else:
            val[x % 5] = (7 | j) * (2 & 10) % 1009
    p = 0
    while p < 7:
        j = p * tmp // 7 * 12 & 8191
        if j << 1 == 0:
            t11 = tmp ^ b ^ val[q % 5]
            x = (t11 + x) % 4093
            t12 = val[tmp % 5] // 5 * v
            tmp = t12 % 97
        if val[x % 5] % 97 <= 46:
            x = (13 * b ^ x) % 4093
            tmp = (x - 20 + p) % 97
        p = p + 1
    for nxt in range(6):
        t13 = val[v % 5] & x
        q = (t13 | q) % 97
        t14 = (b & 7) + nxt
        tmp = t14 % 4093
        x = (4 + 20 - q + nxt) % 4093
    for z in range(74):
        j = ((19 | q) ^ j) % 4093
    u = v % 97
    return (5 ^ j) & 65535

if __name__ == "__main__":
    arg = 10
    expected = 317
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
