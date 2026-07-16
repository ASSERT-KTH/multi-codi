# Auto-extracted from ds_lt256k_500.jsonl
# record_id=44  entry=f  input='6'  output='0'  tokens=185849

def f(x):
    t0 = 19 + 3 + 3
    lo = t0 % 17 - x
    y = (x - 8) * 8
    t1 = y - 10 >> 2
    v = t1 + lo
    val = 0
    while val < 4:
        x = ((val & 19) - y) % 4093
        prv = 0
        while prv < 6:
            t2 = val | lo
            t3 = t2 - (4 + prv)
            v = t3 - prv & 2047
            t4 = (prv + v) // 8
            x = t4 >> 4 & 16383
            prv = prv + 1
        val = val + 1
    for q in range(263):
        if lo % 17 > 7:
            t5 = y - 7 >> 1
            t6 = t5 - y - v
            v = t6 & 131071
            x = ((x & q) + x) % 97
        else:
            t7 = (v - y) // 7 - x
            x = t7 % 17
            t8 = 1 - x ^ q
            y = t8 % 4093
    res = x ^ v
    for acc in range(8):
        t9 = v % 97 // 7
        t10 = t9 - (v * x >> 3)
        lo = (t10 ^ acc) % 97
        lo = lo // 6 & 511
        for p in range(3):
            t11 = p & 2 ^ res
            x = t11 & 16383
    for a in range(12):
        t12 = (v - lo ^ y) + 11 - a
        x = t12 % 65521
        x = lo + lo - x & 2047
    return ((14 | lo) >> 4) % 97

if __name__ == "__main__":
    arg = 6
    expected = 0
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
