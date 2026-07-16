# Auto-extracted from ds_lt256k_500.jsonl
# record_id=222  entry=f  input='20'  output='65508'  tokens=142684

def f(x):
    if x & 15 >= 8:
        x = x ^ 8
    else:
        if 2 + x <= 4:
            x = x - 11 - 13
    t0 = (x ^ 10) << 3
    d = t0 << 1
    j = 13 + x
    for cur in range(2):
        if j // 6 == 44:
            x = (1 | x) % 4093
        else:
            j = (x - 8 ^ j) % 4093
        d = (19 | cur | x) & 255
        for v in range(6):
            x = ((cur ^ 6) - x) % 65521
    for hi in range(800):
        t1 = x * x + hi
        j = t1 % 65521
    t2 = (d ^ j) * 13 ^ j >> 4
    z = t2 & 255
    return (x // 4 - z) % 65521

if __name__ == "__main__":
    arg = 20
    expected = 65508
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
