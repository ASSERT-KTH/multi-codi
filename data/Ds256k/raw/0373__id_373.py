# Auto-extracted from ds_lt256k_500.jsonl
# record_id=373  entry=f  input='14'  output='182'  tokens=236656

def f(x):
    t0 = x * x + x
    idx = t0 - (x - 9 & x)
    a = x - 14
    nxt = idx - 3 ^ x
    a = (x | 7) << 1
    nxt = a & idx
    x = x | a
    t1 = (idx ^ 16) + 13
    nxt = t1 + ((nxt ^ 2) & a)
    t2 = 11 - nxt ^ a
    t3 = t2 ^ (nxt << 3 | 4)
    for j in range(416):
        nxt = idx * 12 + nxt & 131071
        t4 = 2 - (3 | j)
        a = (t4 + a) % 1009
        if a + 13 < 7:
            t5 = (idx + nxt ^ 20 - j) - x
            idx = t5 % 251
            t6 = idx & nxt | j
            idx = t6 // 6 % 17
        else:
            t7 = 18 * x | nxt
            nxt = t7 & 131071
    return t3 & 2047

if __name__ == "__main__":
    arg = 14
    expected = 182
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
