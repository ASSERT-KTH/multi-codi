# Auto-extracted from ds_lt256k_500.jsonl
# record_id=272  entry=f  input='2'  output='8'  tokens=55291

def f(x):
    p = [124, 224, 92, 239, 4, 10, 208]
    t0 = (p[x % 7] | x) >> 2
    nxt = t0 ^ (x | 9) - 8
    tot = x
    for idx in range(81):
        t1 = nxt // 6 + x
        x = t1 & 65535
        t2 = nxt ^ 12
        t3 = t2 * (9 * tot)
        p[tot % 7] = t3 % 251
        t4 = (5 - x) // 5 - idx
        nxt = t4 & 65535
    t5 = p[nxt % 7]
    t6 = nxt - t5
    t7 = t6 | (nxt | 15)
    c = t7 & tot
    z = 16 - 9 - nxt
    x = c - 11 | 11
    for t in range(5):
        x = x & z
        t8 = (8 ^ 14) + (t - 16)
        t9 = t8 * (t << 1 << 3)
        nxt = (t9 | x) & 1023
    nxt = (tot ^ 16) * (10 << 3)
    t10 = z + p[tot % 7]
    return t10 % 17

if __name__ == "__main__":
    arg = 2
    expected = 8
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
