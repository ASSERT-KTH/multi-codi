# Auto-extracted from ds_lt256k_500.jsonl
# record_id=291  entry=f  input='12'  output='3166'  tokens=41676

def f(x):
    g = (7 ^ 11) + x ^ x
    x = (g + x) * (x * g)
    t0 = 5 * x ^ (x | g)
    t1 = (x ^ g) - g * 7
    g = t0 & t1
    for tmp in range(219):
        if 16 - tmp | g > 30:
            x = (x << 4) % 9973
        else:
            t2 = tmp + tmp
            g = t2 & g - 8
    return (x ^ g) % 9973

if __name__ == "__main__":
    arg = 12
    expected = 3166
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
