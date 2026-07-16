# Auto-extracted from ds_lt256k_500.jsonl
# record_id=188  entry=f  input='19'  output='11'  tokens=41285

def f(x):
    u = [81, 39, 68, 96, 59]
    q = x + x
    v = q + q + q
    t0 = u[x % 5]
    m = x - v - t0
    if v & 18 > 18:
        t1 = (q + v) // 2
        t2 = (x ^ m) * 20
        u[v % 5] = (t1 + t2) % 97
    for lo in range(11):
        t3 = lo | u[lo % 5]
        v = ((4 ^ x) * t3 + v) % 4093
    for res in range(30):
        for idx in range(3):
            t4 = (v & idx) + q
            q = t4 & 65535
        t5 = u[x % 5] ^ q
        m = (t5 ^ res) % 97
        t6 = 20 - res ^ m
        u[res % 5] = t6 % 97
    t7 = x & u[q % 5]
    return t7 - v // 6 & 15

if __name__ == "__main__":
    arg = 19
    expected = 11
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
