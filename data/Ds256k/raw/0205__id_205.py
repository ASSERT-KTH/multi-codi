# Auto-extracted from ds_lt256k_500.jsonl
# record_id=205  entry=f  input='11'  output='125'  tokens=97602

def f(x):
    s = [34, 20, 43, 94, 66, 31, 43, 37]
    c = (19 << 2) + x
    cnt = (x | 12) << 1
    t0 = cnt * 19
    t1 = t0 | (x | 14)
    aux = t1 + c
    a = cnt // 2 * (x | c) ^ x
    t2 = (2 | aux) >> 1
    tmp = t2 ^ 9
    idx = c ^ 9
    t3 = c + aux - a
    b = t3 + tmp
    d = 0
    while d < 11:
        q = 0
        while q < 13:
            t4 = 17 + aux + (cnt >> 1)
            b = (t4 % 17 | b) % 1009
            t5 = tmp + b | q
            c = t5 & 255
            q = q + 1
        d = d + 1
    t6 = s[b % 8] ^ idx | 17
    t7 = t6 ^ x & c & a * x
    return t7 & 2047

if __name__ == "__main__":
    arg = 11
    expected = 125
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
