# Auto-extracted from ds_lt256k_500.jsonl
# record_id=166  entry=f  input='6'  output='764'  tokens=8224

def rec(n, a):
    if n <= 0:
        return a
    t0 = 20 - 2 << 2
    a = (t0 - a) % 1009
    t1 = n * n ^ n - 2
    a = t1 + a & 4095
    t2 = 14 * a % 65521
    return rec(n - 1, t2)

def f(x):
    buf = [336, 125, 874, 81, 218, 136]
    t0 = buf[x % 6]
    t1 = x | t0
    t2 = t1 & (x & 3)
    hi = t2 & x
    val = (13 << 3) - x
    x = hi - 5
    for a in range(28):
        if buf[a % 6] + x == 43:
            t3 = buf[a % 6] ^ x
            buf[hi % 6] = t3 % 1009
            t4 = (x * hi & a) * x
            val = t4 % 251
        t5 = 8 - x - 19 + val
        val = t5 % 9973
    return (val - hi) % 1009

if __name__ == "__main__":
    arg = 6
    expected = 764
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
