# Auto-extracted from ds_lt256k_500.jsonl
# record_id=24  entry=f  input='15'  output='272'  tokens=11473

def f(x):
    m = x * 3
    buf = 10 * x * x
    m = m | buf
    for y in range(143):
        x = (m >> 1 ^ y) % 1009
    m = 1 - x
    m = m & x
    return x + m & 1023

if __name__ == "__main__":
    arg = 15
    expected = 272
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
