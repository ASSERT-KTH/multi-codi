# Auto-extracted from ds_lt256k_500.jsonl
# record_id=200  entry=f  input='4'  output='2830'  tokens=50494

def fn0(g):
    for j in range(9):
        t0 = j ^ 15 | g
        g = t0 % 65521
        g = j * (g * j) % 65521
    buf = 0
    while buf < 7:
        t1 = (buf ^ 18) * g
        g = (t1 - buf) % 97
        buf = buf + 1
    if g + g != 63:
        g = g * g % 4093
        cur = 0
        while cur < 10:
            t2 = (cur | g) % 97 // 6
            g = t2 % 97
            g = (cur + g) % 4093
            cur = cur + 1
    t3 = (g & 2) + g
    t4 = t3 * ((g | 7) >> 3)
    prv = t4 % 97
    t5 = g ^ 2 ^ prv
    m = t5 + g
    return (g * prv // 2 - g) % 4093

def f(x):
    t0 = x + x
    t1 = 7 - 11 + 20
    t2 = t0 & (x ^ 13)
    nxt = t1 + t2
    for idx in range(155):
        x = idx + x & 511
        t3 = 5 + 6 + (x - nxt)
        t4 = idx + nxt - 16 ^ t3
        x = t4 % 1009
    d = (nxt | 20) * (nxt | x)
    aux = x + 8
    tot = x
    t5 = aux * d + aux
    return t5 & 8191

if __name__ == "__main__":
    arg = 4
    expected = 2830
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
