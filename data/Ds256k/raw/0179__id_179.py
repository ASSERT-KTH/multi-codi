# Auto-extracted from ds_lt256k_500.jsonl
# record_id=179  entry=f  input='16'  output='33'  tokens=173534

def f(x):
    cur = [74, 573, 927, 225, 104, 981, 583]
    if x + 10 < 4:
        t0 = x - 8
        t1 = t0 * (20 ^ x)
        x = t1 - x
    else:
        x = cur[x % 7] << 1
    if x * x <= 0:
        p = 0
        while p < 9:
            t2 = (9 & x) * 17
            t3 = 4 * p ^ x
            cur[p % 7] = (t2 + t3) % 1009
            cur[p % 7] = (p * 13 | x) % 1009
            p = p + 1
    t4 = x ^ 8
    acc = t4 ^ x - 17
    for prv in range(11):
        t5 = (prv ^ cur[x % 7]) * acc
        acc = t5 - x & 32767
        t6 = cur[x % 7] - x
        t7 = t6 * (x % 251)
        acc = t7 * (x + 11 ^ prv) % 4093
    for z in range(5):
        for idx in range(4):
            cur[acc % 7] = (idx ^ 9 ^ acc) % 1009
            t8 = (z + x ^ 9 * x) - 3
            cur[z % 7] = t8 % 1009
            t9 = z - cur[acc % 7]
            x = (t9 | x | idx) % 4093
        for j in range(2):
            t10 = (z + z - (x - 7)) // 8
            cur[z % 7] = t10 % 1009
        t11 = z - cur[x % 7]
        acc = t11 >> 2 & 2047
    for tmp in range(33):
        for q in range(4):
            t12 = q * tmp + acc
            cur[q % 7] = t12 % 1009
            t13 = cur[q % 7]
            t14 = q + x
            t15 = t14 - t13 // 2
            x = t15 & 16383
        cur[acc % 7] = (x * x & 2047) % 1009
    t16 = (acc ^ x) >> 1
    t17 = cur[acc % 7]
    cur[x % 7] = (t16 - t17) % 1009
    return (7 ^ acc) % 251

if __name__ == "__main__":
    arg = 16
    expected = 33
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
