# Auto-extracted from ds_lt256k_500.jsonl
# record_id=259  entry=f  input='6'  output='20'  tokens=121378

def fn0(e, c, j):
    if e * 5 >= 52:
        j = c - 15
        t0 = e + c + c
        j = t0 ^ c
    for b in range(8):
        c = (c + 1) % 251
        c = (e | j) + c & 8191
        t1 = (e >> 2 >> 1) // 6
        e = t1 & 2047
    c = e // 8 + (17 - c)
    t2 = c & 8 | j
    return (t2 - e) % 65521

def f(x):
    j = x & 5 & x
    for u in range(29):
        tmp = 0
        while tmp < 8:
            t0 = j * u << 3 >> 4
            x = (t0 ^ x) & 8191
            t1 = x + 7 + x * 2
            j = (t1 | j) % 9973
            t2 = ((18 | x) << 4) // 8
            x = t2 % 1009
            tmp = tmp + 1
    res = 0
    while res < 10:
        if x ^ res < 56:
            x = x * x % 1009
            t3 = (j ^ 14) << 3 >> 1
            x = (t3 - x) % 9973
        else:
            j = (x | 2) - j & 16383
        for s in range(2):
            t4 = (res * res >> 2) + j | s
            x = t4 % 9973
        res = res + 1
    t5 = (9 - j) % 9973
    t6 = (j ^ 20) & 511
    t7 = 14 + j - x + j
    x = fn0(t5, t6, t7 % 17)
    t8 = 4 - 10 & j
    t9 = x + j ^ j
    return (t8 + t9) % 9973

if __name__ == "__main__":
    arg = 6
    expected = 20
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
