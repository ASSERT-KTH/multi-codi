# Auto-extracted from ds_lt256k_500.jsonl
# record_id=167  entry=f  input='14'  output='71'  tokens=144798

def f(x):
    nxt = ((x | 3) ^ (x | 4)) + x
    if x ^ nxt <= 1:
        for a in range(12):
            t0 = (x ^ nxt) & nxt
            x = (t0 - a) % 1009
        nxt = nxt | 17
    t1 = nxt * 17 - x
    d = t1 - x
    cnt = (x - d) * nxt
    if cnt >> 2 == 18:
        if nxt * d <= 36:
            nxt = nxt | 14
            x = (cnt >> 1) + d
        q = 0
        while q < 2:
            t2 = (q - cnt) // 6
            nxt = t2 & 16383
            t3 = nxt & 15 | q
            cnt = t3 % 65521
            d = (d + q) % 17
            q = q + 1
    else:
        d = d - 10 + 17
    if nxt + cnt == 5:
        for val in range(6):
            cnt = nxt * cnt & 32767
            d = (cnt + nxt) * cnt + d & 131071
    else:
        d = cnt % 65521 - nxt
        d = 14 ^ x
    y = (x & nxt) * d % 1009
    g = nxt // 2 - nxt
    t4 = (17 ^ d) // 3
    hi = t4 >> 1
    e = d % 17
    c = 0
    while c < 9:
        for p in range(55):
            cnt = ((15 ^ x) + cnt) % 1009
            x = (c - hi | x) % 9973
        c = c + 1
    t5 = cnt & 1 ^ d
    tmp = t5 * d & 2047
    t6 = g >> 2
    t7 = d % 17
    t8 = t6 + (d + nxt)
    t9 = t7 ^ 6 - hi
    tot = (t8 | t9) % 65521
    return y + nxt & 255

if __name__ == "__main__":
    arg = 14
    expected = 71
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
