# Auto-extracted from ds_lt256k_500.jsonl
# record_id=327  entry=f  input='2'  output='174'  tokens=243342

def f(x):
    prv = x & 3
    t0 = prv ^ x
    v = t0 * (x & prv)
    if 1 ^ prv == 2:
        v = x + 2 + 2
    if 14 ^ prv >= 13:
        if x | prv <= 25:
            x = (x + v) // 5
        else:
            x = x - 1
        v = v ^ prv
    for tot in range(11):
        t1 = (3 ^ v) - x
        t2 = 15 * x - x
        t3 = (t1 ^ t2) + tot
        prv = t3 % 65521
        for lo in range(6):
            t4 = tot * lo - v
            x = t4 & 131071
            v = (lo & v) * v & tot
        v = (6 ^ x ^ v) % 4093
    for val in range(2):
        prv = (12 | prv) % 4093
    for res in range(7):
        x = (5 + v - res) % 4093
        for t in range(59):
            x = (t | x) & t
            prv = (res ^ t ^ x) % 4093
            t5 = 7 - t - prv
            x = t5 % 4093
        t6 = 5 + res + (x & res)
        t7 = t6 + (res - (9 + res))
        x = t7 % 65521
    buf = (v ^ prv) >> 3
    t8 = (prv ^ 6) + (x + v)
    return t8 * ((prv | 19) // 6) % 65521

if __name__ == "__main__":
    arg = 2
    expected = 174
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
