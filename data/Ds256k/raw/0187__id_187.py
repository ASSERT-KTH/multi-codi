# Auto-extracted from ds_lt256k_500.jsonl
# record_id=187  entry=f  input='14'  output='3320'  tokens=73645

def fn0(g):
    cnt = [789, 778, 336, 997, 387, 65]
    m = 2 * g + g >> 4
    b = (m << 4) // 7
    if 13 + b > 30:
        g = m + g ^ g
    idx = (m << 3) - 11 >> 4
    t0 = cnt[b % 6]
    t1 = (t0 - b) * g
    a = t1 & 511
    t2 = cnt[m % 6]
    return idx // 7 & t2

def f(x):
    a = [435, 636, 752, 984, 573]
    q = 1 + 8 - x
    tmp = 0
    while tmp < 200:
        if tmp | x <= 1:
            a[tmp % 5] = 10 - q
            a[q % 5] = 13 * q
        else:
            t0 = a[tmp % 5]
            t1 = t0 * tmp + tmp
            q = (t1 | x) & 65535
            a[q % 5] = (q & x) * (x - 2) ^ tmp
        tmp = tmp + 1
    val = (q & a[x % 5]) + q
    val = (20 ^ val) + q
    q = (val + val) % 4093
    q = (x + x ^ q) & q
    t2 = 2 + q
    t3 = t2 - (q ^ 20)
    q = t3 // 5
    return val + val & 4095

if __name__ == "__main__":
    arg = 14
    expected = 3320
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
