# Auto-extracted from ds_lt256k_500.jsonl
# record_id=469  entry=f  input='4'  output='56'  tokens=145054

def f(x):
    v = [209, 25, 202, 110, 233, 230]
    v[x % 6] = x * x % 251
    if v[x % 6] + v[x % 6] != 18:
        v[x % 6] = 4 | x
    t0 = v[x % 6]
    res = t0 & 5
    u = res + v[res % 6]
    idx = 0
    while idx < 3:
        for p in range(115):
            t1 = idx + u ^ p
            t2 = v[idx % 6]
            u = (t1 ^ t2) & 255
            res = ((x & 16) - p) % 65521
        prv = 0
        while prv < 12:
            t3 = 5 * res + u
            res = t3 - idx & 255
            v[x % 6] = (14 | res) * 11 % 251
            prv = prv + 1
        idx = idx + 1
    w = res | 3
    t4 = v[w % 6]
    t5 = t4 * res - 16
    lo = t5 & 65535
    s = lo + 8
    return (res | x) << 3 & 255

if __name__ == "__main__":
    arg = 4
    expected = 56
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
