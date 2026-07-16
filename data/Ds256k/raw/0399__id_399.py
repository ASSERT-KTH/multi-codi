# Auto-extracted from ds_lt256k_500.jsonl
# record_id=399  entry=f  input='6'  output='288'  tokens=104110

def fn0(b, a, g):
    j = a << 2
    res = j * 4 % 17
    t0 = j + j ^ b ^ 2
    j = t0 % 17
    g = res & 3
    if res ^ a == 38:
        t1 = g - 9 - g
        b = t1 - (15 | 9 | g)
        res = res - 5
    else:
        a = res - a
        res = b | 12
    return (14 | res) & a

def f(x):
    val = [24, 17, 89, 18, 86, 17, 8, 90]
    t0 = x - 12 + (x + x)
    q = x * 4 - 11 + t0
    c = 16 | q
    for cur in range(5):
        t1 = c | x
        t2 = t1 & c * c
        t3 = q + q << 3
        x = (t2 - t3) % 4093
        t4 = cur << 3
        t5 = t4 - (cur ^ x)
        t6 = 2 * 16 - cur
        x = t5 & t6
    for cnt in range(8):
        for prv in range(8):
            t7 = val[cnt % 8]
            t8 = cnt - t7
            t9 = t8 * (x ^ prv)
            x = t9 & 8191
        if (cnt | 15) ^ x < 2:
            t10 = val[x % 8] & q
            q = t10 & 18 + q
        t11 = 5 * c // 3 + x
        x = t11 % 251
    w = c + 13 + (q + x) >> 4
    tot = 3 - val[x % 8] + 9
    aux = 0
    while aux < 9:
        t12 = tot // 5 >> 4
        t13 = (t12 | q) ^ aux
        w = t13 % 251
        for y in range(11):
            t14 = (q + x | 10) + tot
            tot = t14 & 8191
        aux = aux + 1
    t15 = val[w % 8] << 4
    return t15 & 8191

if __name__ == "__main__":
    arg = 6
    expected = 288
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
