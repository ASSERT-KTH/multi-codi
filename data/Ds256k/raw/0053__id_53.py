# Auto-extracted from ds_lt256k_500.jsonl
# record_id=53  entry=f  input='1'  output='297'  tokens=70855

def f(x):
    val = x - 10 - x
    g = val + x & val - 12
    idx = x & g
    aux = (15 | g) + val >> 4
    for j in range(10):
        t0 = (j + idx) * (g - 20)
        x = (4 - 13) * t0 & 511
        for y in range(37):
            x = ((idx | aux) - y) % 9973
            aux = (18 * val ^ y) % 9973
        if x & 12 != 0:
            x = (1 - j ^ idx) % 251
    res = val - aux
    t1 = g - 5 + aux
    x = t1 - (x + x | g)
    return (aux ^ g) % 1009

if __name__ == "__main__":
    arg = 1
    expected = 297
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
