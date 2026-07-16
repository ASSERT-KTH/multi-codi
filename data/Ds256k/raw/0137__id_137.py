# Auto-extracted from ds_lt256k_500.jsonl
# record_id=137  entry=f  input='20'  output='1074'  tokens=46243

def f(x):
    t0 = x | 6
    buf = t0 * (x ^ 10)
    if buf - 19 >= 44:
        buf = (19 - buf >> 2) // 8
        x = x * x - (buf & x)
    tmp = buf << 1
    m = buf ^ x
    t1 = m * buf * buf
    tot = t1 // 6 % 4093
    acc = tot ^ x
    a = 0
    while a < 84:
        t2 = (buf >> 1) // 3
        m = t2 & (acc + a) // 2
        t3 = tot // 2 >> 1 ^ buf
        buf = t3 & 4095
        tot = 16 - tot >> 1 & 32767
        a = a + 1
    p = tmp + buf + buf
    t4 = (x ^ tmp) * m
    z = t4 % 17
    t5 = (x ^ 16) - buf - 2
    return t5 & 2047

if __name__ == "__main__":
    arg = 20
    expected = 1074
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
