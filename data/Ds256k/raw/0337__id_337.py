# Auto-extracted from ds_lt256k_500.jsonl
# record_id=337  entry=f  input='19'  output='32732'  tokens=75672

def f(x):
    res = [65, 66, 19, 53, 30, 10, 67, 27]
    for nxt in range(19):
        cur = 0
        while cur < 3:
            t0 = res[cur % 8]
            t1 = res[cur % 8]
            t2 = t0 // 2
            t3 = t2 ^ t1 - 12
            x = (t3 - x) % 9973
            t4 = res[x % 8]
            t5 = (18 | nxt) * (x << 2)
            t6 = (4 << 4 | t4) + t5
            res[x % 8] = t6 % 17
            t7 = (17 - res[x % 8]) // 8
            res[cur % 8] = (t7 ^ x) % 97
            cur = cur + 1
        x = (x ^ 11) % 17
    v = (6 - x << 2) * x % 251
    if v | 19 > 31:
        if res[v % 8] - x < 11:
            t8 = v * x & 511
            res[x % 8] = t8 % 97
        else:
            t9 = (v + x) * v
            v = t9 % 9973
    else:
        if x * x >= 14:
            res[v % 8] = v * x % 9973 % 97
            t10 = 3 + res[x % 8]
            x = (3 << 3) - t10
        v = 13 ^ x
    t11 = x >> 1 << 4
    t12 = res[x % 8]
    prv = t11 ^ t12
    t13 = res[v % 8]
    t14 = res[v % 8]
    t15 = t13 * 10 - prv
    t16 = t14 - v ^ v
    g = t15 ^ t16
    hi = prv - x - g
    if 11 + g > 4:
        res[g % 8] = (g + hi) % 97
    else:
        t17 = v * v // 6
        t18 = t17 | hi * g * 10
        hi = t18 & 1023
    return hi - prv << 2 & 32767

if __name__ == "__main__":
    arg = 19
    expected = 32732
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
