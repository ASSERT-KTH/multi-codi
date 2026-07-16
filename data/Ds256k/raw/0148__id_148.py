# Auto-extracted from ds_lt256k_500.jsonl
# record_id=148  entry=f  input='12'  output='1044'  tokens=251876

def f(x):
    w = 18 ^ 10 ^ x
    t0 = 7 & w ^ w
    cnt = t0 << 3
    for tot in range(11):
        for q in range(12):
            t1 = (19 - q) * cnt >> 3
            w = t1 % 65521
            t2 = w - 9
            t3 = t2 * (19 + 9)
            x = t3 * x % 17
        t4 = ((x | 19) ^ 1) * x ^ w
        w = t4 & 1023
        w = w * tot & 17
    if 19 | x <= 1:
        a = 0
        while a < 3:
            cnt = 4 - x + cnt & 32767
            a = a + 1
    hi = x + cnt
    t = cnt + w ^ cnt
    v = 15 * 1 ^ w * 1
    p = v >> 1
    t5 = t // 5 & x
    t6 = (w & 11) * p
    c = t5 & t6
    for prv in range(370):
        t7 = (p >> 4) + 4
        t8 = t7 * (5 + 19 - prv)
        t = t8 & 65535
    t9 = 8 * cnt + 20
    return t9 & 262143

if __name__ == "__main__":
    arg = 12
    expected = 1044
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
