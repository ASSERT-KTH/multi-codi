# Auto-extracted from ds_lt256k_500.jsonl
# record_id=277  entry=f  input='2'  output='7760'  tokens=15207

def f(x):
    for z in range(274):
        x = ((x ^ z) - z) % 17
    if 15 ^ x > 9:
        x = x * x
        x = x - 8 | x
    m = x - 19
    return m * 16 & 131071

if __name__ == "__main__":
    arg = 2
    expected = 7760
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
