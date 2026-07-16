# Auto-extracted from ds_lt256k_500.jsonl
# record_id=157  entry=f  input='6'  output='7'  tokens=41807

def f(x):
    e = (x << 4) + x
    t0 = e * x % 251
    x = t0 * ((6 | e) >> 4)
    e = e + x
    t1 = (x | 13) * (e + 14)
    e = t1 & 255
    for q in range(190):
        t2 = x * 2
        t3 = t2 - x // 4
        e = (t3 + e) % 1009
    return (18 + 15 ^ e) % 251

if __name__ == "__main__":
    arg = 6
    expected = 7
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
