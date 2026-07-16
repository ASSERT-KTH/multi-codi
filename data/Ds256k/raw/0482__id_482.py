# Auto-extracted from ds_lt256k_500.jsonl
# record_id=482  entry=f  input='8'  output='118672'  tokens=10121

def f(x):
    for z in range(60):
        t0 = 10 * z
        t1 = t0 * (14 | 12)
        x = (t1 + x) % 1009
    u = x & 18
    if x ^ 11 < 62:
        m = 0
        while m < 6:
            t2 = 17 - m ^ 18
            t3 = m - 16 - t2 + u
            x = t3 % 4093
            m = m + 1
        u = u - 17 | u
    t4 = x * 9 << 4
    aux = t4 // 7
    u = u >> 2
    return u - aux & 131071

if __name__ == "__main__":
    arg = 8
    expected = 118672
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
