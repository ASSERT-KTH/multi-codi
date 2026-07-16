# Auto-extracted from ds_lt256k_500.jsonl
# record_id=448  entry=f  input='12'  output='147'  tokens=137689

def fn0(d, c):
    g = [72, 57, 62, 24, 93, 31]
    t0 = (11 + c) * (5 + d)
    acc = (t0 | d) % 97
    t1 = g[c % 6]
    w = acc ^ 17 | t1
    if d << 2 <= 0:
        acc = 6 | g[acc % 6]
        idx = 0
        while idx < 11:
            t2 = (d // 2 & w) // 2
            g[w % 6] = t2 % 97
            t3 = 20 << 1
            t4 = 15 - w
            t5 = t3 - d % 97
            t6 = t4 - (19 + 16)
            t7 = (t5 | t6) - acc
            acc = t7 & 32767
            idx = idx + 1
    for e in range(4):
        t8 = (acc | d) * d
        acc = t8 & 4095
        acc = (w >> 1 ^ acc) % 17
    t9 = g[d % 6] * d
    return (t9 + acc * 15) % 4093

def fn1(e):
    t0 = e - 3 + 9
    acc = t0 % 4093
    t1 = acc - 8
    t2 = t1 * (acc // 2)
    t3 = acc - 1 | acc
    t4 = ((e ^ 17) >> 1) % 9973
    acc = fn0(t2 & t3, t4)
    hi = 17 - acc
    for u in range(7):
        e = (acc + u) % 4093
        e = ((e >> 1) - acc) // 3 & 131071
    z = acc ^ hi
    return (acc + e) % 9973

def f(x):
    t0 = 7 * x
    t1 = t0 & (x | 2)
    idx = t1 ^ x
    cur = 8 + idx
    t2 = (idx | 13) & 16383
    t3 = 7 - idx - idx
    x = fn0(t2, t3 & x)
    x = fn1(cur + 16 & 4095)
    acc = cur ^ cur * idx
    x = cur ^ x
    for p in range(974):
        cur = p * acc & 32767
    if acc + cur <= 12:
        j = 0
        while j < 4:
            acc = 15 * acc - cur & 16383
            t4 = (idx & cur | idx) >> 3
            idx = t4 & 2047
            j = j + 1
    t5 = (idx & 16 | acc + idx) - 5
    return t5 & 8191

if __name__ == "__main__":
    arg = 12
    expected = 147
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
