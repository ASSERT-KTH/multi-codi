# Auto-extracted from ds_lt256k_500.jsonl
# record_id=242  entry=f  input='3'  output='64'  tokens=24099

def fn0(e, j):
    t0 = j ^ 16
    z = t0 & e + 9
    if z // 4 >= 19:
        z = z & 13
    else:
        j = (e * e >> 1) % 17
        z = (6 << 1) * z
    tmp = (j & 4) * e
    c = (j ^ tmp) * tmp & 2047
    tmp = c + tmp
    t1 = c * e - e // 4
    return t1 % 17

def f(x):
    z = x | 17
    cnt = z * z
    c = (cnt << 2) + z * x
    prv = 8 + 7 | z
    prv = ((cnt ^ 6) >> 4) + prv
    for idx in range(6):
        m = 0
        while m < 8:
            z = (idx | z) & cnt - z
            t0 = (cnt << 2) - m
            t1 = (7 ^ 14) & prv
            x = (t0 + t1) % 4093
            z = ((10 << 1) - z) % 9973
            m = m + 1
        prv = (prv // 3 >> 1) % 4093
    return (c ^ x | prv) % 4093

if __name__ == "__main__":
    arg = 3
    expected = 64
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
