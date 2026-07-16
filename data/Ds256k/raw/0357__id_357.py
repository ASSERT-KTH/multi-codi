# Auto-extracted from ds_lt256k_500.jsonl
# record_id=357  entry=f  input='19'  output='188'  tokens=152884

def fn0(j):
    aux = 4 - j
    j = aux % 4093
    for tmp in range(5):
        t0 = 18 ^ aux
        t1 = t0 * (11 * tmp)
        j = (t1 >> 4) % 4093
        for prv in range(10):
            j = (prv - tmp - j) % 17
            t2 = tmp * prv
            t3 = t2 | prv - aux
            j = t3 % 17
    aux = j ^ 19
    t4 = j // 5 - j % 4093
    t5 = t4 - (aux - 8) * j
    aux = t5 & 262143
    for d in range(4):
        t6 = j << 2
        t7 = t6 - j * j
        j = t7 - aux & 131071
    t8 = 9 - 19
    t9 = t8 + (19 - j)
    j = t9 // 4
    t10 = (j + j) * aux
    return t10 & 511

def f(x):
    hi = x * x * x << 3
    t0 = hi * x
    t1 = t0 & x - hi
    j = t1 | x
    for z in range(311):
        x = z * j & 32767
        t2 = z << 1
        t3 = (16 | x) // 6
        t4 = t2 * (20 - 5)
        x = (t3 | t4) & 4095
        j = (18 | hi) - x - j & 2047
    t5 = (x & 3) - hi
    return t5 + 17 & 255

if __name__ == "__main__":
    arg = 19
    expected = 188
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
