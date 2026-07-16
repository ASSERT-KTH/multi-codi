# Auto-extracted from ds_lt256k_500.jsonl
# record_id=431  entry=f  input='7'  output='209'  tokens=107723

def f(x):
    for a in range(324):
        t0 = (a ^ 19) * (x & a)
        x = t0 % 251
        x = ((x ^ 12) + x) % 4093
    p = 0
    while p < 12:
        x = p + p + x & 511
        for cnt in range(5):
            t1 = x * p
            t2 = x & cnt & 1
            t3 = t1 ^ p - 2
            x = (t2 - t3) % 251
            t4 = (10 - p) * (cnt * p)
            x = (t4 ^ 7 ^ x) % 9973
        t5 = x * x - x
        x = t5 & 262143
        p = p + 1
    for tmp in range(8):
        x = (tmp * tmp - x) % 9973
        x = (x - tmp) % 17
        b = 0
        while b < 6:
            x = x * 13 % 17
            t6 = b * b + b
            x = t6 + x & 2047
            b = b + 1
    t7 = x % 251 & x - 20
    aux = t7 ^ x * 17 >> 4
    for buf in range(3):
        if x - 19 == 19:
            t8 = (14 ^ buf) + aux
            t9 = aux ^ 2 ^ aux
            aux = (t8 + t9) % 251
    x = aux + x
    x = x + x + aux >> 4
    return ((x - 19) * x + aux) % 251

if __name__ == "__main__":
    arg = 7
    expected = 209
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
