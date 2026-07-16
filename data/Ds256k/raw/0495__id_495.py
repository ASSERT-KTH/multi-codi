# Auto-extracted from ds_lt256k_500.jsonl
# record_id=495  entry=f  input='19'  output='184'  tokens=243130

def f(x):
    nxt = [90, 212, 169, 212, 17, 0]
    for res in range(432):
        if res << 4 | x != 42:
            t0 = x ^ nxt[x % 6]
            nxt[res % 6] = (t0 - (20 & x) << 1) % 251
            t1 = (res ^ 19) * res
            t2 = t1 * nxt[res % 6]
            x = (t2 - x) % 97
        if 7 ^ x >= 58:
            t3 = nxt[res % 6] * res
            nxt[res % 6] = (t3 | x) % 251
    if x ^ 6 > 19:
        if x | 9 >= 17:
            t4 = nxt[x % 6]
            t5 = x // 7
            t6 = t5 | x * t4
            nxt[x % 6] = t6 % 251
    j = 8 - 1 ^ x
    t7 = nxt[x % 6]
    p = x ^ t7
    return 18 * 12 - p & 65535

if __name__ == "__main__":
    arg = 19
    expected = 184
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
