# Auto-extracted from ds_lt256k_500.jsonl
# record_id=435  entry=f  input='9'  output='71'  tokens=50974

def fn0(a):
    buf = [340, 504, 564, 157, 736]
    t0 = buf[a % 5]
    t = 10 | t0
    s = (16 + t & t) + 19
    for y in range(6):
        t = (y ^ 16 ^ s) % 4093
        c = 0
        while c < 2:
            buf[y % 5] = buf[s % 5] // 3 >> 4
            c = c + 1
        for u in range(7):
            a = u - 12 - (a ^ t) & 255
            t1 = buf[a % 5] >> 2
            t2 = (y ^ a) >> 4
            t3 = t2 + (a - s) * t1
            s = t3 % 4093
    idx = buf[a % 5] + s
    if t | 16 <= 1:
        if t ^ 20 > 34:
            s = idx - s
            buf[s % 5] = (idx & t) % 1009
    else:
        for b in range(4):
            idx = (idx | a) >> 1 & b * 12
        for res in range(11):
            t4 = idx % 251 * (s * 15) ^ a
            a = t4 & 2047
            idx = idx * idx % 4093
    buf[idx % 5] = (s ^ 3) % 1009
    t5 = s & 11
    t6 = t5 + s % 4093
    return t6 // 2 % 251

def f(x):
    for res in range(35):
        tot = 0
        while tot < 3:
            t0 = (res ^ 15) * res
            x = (t0 | x) & 2047
            tot = tot + 1
        t1 = res ^ 10 | res
        t2 = (t1 | 13) ^ x
        x = t2 % 97
        t3 = res * x
        t4 = t3 + (3 | res)
        t5 = res - x & x
        x = t4 * t5 & 511
    y = x * x
    t6 = x // 3
    buf = t6 & 13 + y
    e = y + y
    t7 = e * e * (x // 6)
    return t7 % 97

if __name__ == "__main__":
    arg = 9
    expected = 71
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
