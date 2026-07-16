# Auto-extracted from ds_lt256k_500.jsonl
# record_id=111  entry=f  input='20'  output='65456'  tokens=197823

def f(x):
    for prv in range(7):
        t0 = (x << 1) - x ^ 3
        x = t0 % 65521
    t1 = 6 * x * (10 & 6)
    t = (t1 + x) % 65521
    g = 13 << 3 | x
    for buf in range(160):
        for idx in range(2):
            g = (t - 7 + t ^ idx) % 1009
            t2 = (x >> 1) % 1009
            t3 = t2 ^ (g // 6 ^ buf) ^ idx
            t = t3 & 511
        t = t // 3 & 131071
        t4 = 17 | t | x // 3
        g = ((t4 & 20) + buf) % 251
    q = 0
    while q < 7:
        t5 = 12 + t
        t6 = t5 * (q * q)
        t = t6 // 2 % 17
        t7 = t * (t - x)
        t8 = t7 ^ x | g
        g = t8 & 1023
        q = q + 1
    m = 2 * t ^ 1
    w = m ^ t
    t9 = m - x << 2
    return (t9 - 1) % 65521

if __name__ == "__main__":
    arg = 20
    expected = 65456
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
