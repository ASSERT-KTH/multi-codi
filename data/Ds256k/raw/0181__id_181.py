# Auto-extracted from ds_lt256k_500.jsonl
# record_id=181  entry=f  input='17'  output='0'  tokens=124233

def f(x):
    t0 = x & 14
    c = t0 - (x ^ 9)
    t1 = (x ^ 6) & (x ^ 18)
    e = (x - c) * c * t1
    tmp = c + (6 + x)
    t2 = 14 - c
    t3 = t2 | 9 + c
    cur = t3 & 3
    if x - e <= 17:
        t = 0
        while t < 2:
            tmp = tmp * c % 17
            t4 = e * c - e * 16
            t5 = t4 - (tmp - 20 - 8)
            tmp = t5 & 511
            t6 = e - x - cur
            cur = t6 % 1009
            t = t + 1
        c = (14 - tmp) // 3 >> 3
    prv = tmp % 251 | c ^ 6
    t7 = (cur & c) // 2
    e = t7 * e & 131071
    for d in range(8):
        e = (c | e) & 255
        idx = 0
        while idx < 12:
            c = c & e
            idx = idx + 1
        g = 0
        while g < 18:
            t8 = c * (c | 9) >> 2
            c = t8 % 1009
            t9 = x * prv >> 4 << 2
            c = (t9 | c) & 1023
            g = g + 1
    return cur // 5 // 3 & 131071

if __name__ == "__main__":
    arg = 17
    expected = 0
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
