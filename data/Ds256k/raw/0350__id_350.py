# Auto-extracted from ds_lt256k_500.jsonl
# record_id=350  entry=f  input='16'  output='951'  tokens=209351

def f(x):
    for tot in range(3301):
        x = (x + 11 | 7 - x) % 1009
    if x // 2 >= 3:
        t0 = 6 & 1 & (x ^ 5)
        x = t0 ^ 1
        x = x * x % 1009
    else:
        x = (x ^ 9) // 2
        if 13 - x == 1:
            x = x >> 3
            x = 9 << 2 ^ x
        else:
            x = x - 5
    res = x ^ 20
    if res + x == 49:
        j = 0
        while j < 10:
            x = (x - 18) % 17
            res = (4 - j ^ res) & 8191
            j = j + 1
        res = 13 - x
    else:
        x = (12 * 5 << 4) - x
        t1 = x * x - 5 * x
        res = t1 * res % 17
    buf = x & 5 ^ x + x
    hi = x ^ res
    v = res + hi
    t2 = v // 7 ^ v
    z = t2 ^ v
    if 6 + res <= 36:
        for lo in range(8):
            t3 = (v + hi | buf * res) >> 3
            x = (t3 | lo) % 1009
            t4 = 6 - (19 + lo)
            res = t4 - z & 32767
        if x - hi != 57:
            t5 = z - 16 - buf
            t6 = (1 | hi) * res
            z = (t5 ^ t6) % 17
        else:
            v = 17 ^ x
            buf = res - x
    p = 7 & x & buf * x
    aux = (x & 7) + hi | v
    g = buf % 17
    e = z - 2 >> 4 << 1
    return (aux ^ x) - p & 16383

if __name__ == "__main__":
    arg = 16
    expected = 951
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
