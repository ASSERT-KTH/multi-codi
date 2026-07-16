# Auto-extracted from ds_lt256k_500.jsonl
# record_id=269  entry=f  input='19'  output='226'  tokens=248408

def f(x):
    b = (19 ^ x) - x
    t = x - 8 ^ x
    if 18 + t == 8:
        t = (20 - x) * x
        t0 = b & x
        t1 = t0 * (4 | b)
        t2 = (3 ^ b) - 19
        b = t1 * t2
    cur = (b - x) % 4093
    s = 5 & x
    c = x + x
    g = t - s
    y = (x + b) * b % 4093
    u = (4 << 2) * (t ^ 7)
    for prv in range(802):
        t3 = (cur | b) % 65521 & x
        g = (t3 | prv) % 65521
        x = ((b & c) - x) % 4093
    return (u ^ c) * x & 511

if __name__ == "__main__":
    arg = 19
    expected = 226
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
