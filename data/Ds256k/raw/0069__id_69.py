# Auto-extracted from ds_lt256k_500.jsonl
# record_id=69  entry=f  input='19'  output='266'  tokens=45520

def fn0(d, g):
    y = 1 & d
    for b in range(11):
        if 3 & 18 ^ y > 0:
            t0 = (g - b ^ g // 3) * b
            g = t0 % 65521
            g = (b + b - g) % 9973
        y = (b | y) & y
    c = y * 4 - g
    z = d | 8
    d = (z >> 1) - (y & g)
    t1 = (5 - 3) * c
    c = t1 * c % 4093
    return (c - z) * 7 % 9973

def f(x):
    tot = 7 & x
    prv = 0
    while prv < 10:
        tot = ((tot - prv) * x | tot) & 32767
        prv = prv + 1
    hi = 14 * tot - (x ^ tot)
    cur = 0
    while cur < 7:
        t0 = (hi + hi) * (tot ^ x)
        tot = t0 - cur & 1023
        cur = cur + 1
    for val in range(12):
        t1 = 15 & val & (x & 9)
        t2 = (tot - val >> 1) - t1
        hi = t2 % 1009
        acc = 0
        while acc < 6:
            tot = tot // 3 % 1009
            t3 = x - 12 - acc
            hi = t3 & val
            tot = (acc ^ 12) - hi & 262143
            acc = acc + 1
        t4 = (tot << 3) * tot
        hi = (t4 ^ val) & 255
    return (tot << 1) * x & 2047

if __name__ == "__main__":
    arg = 19
    expected = 266
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
