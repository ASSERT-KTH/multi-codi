# Auto-extracted from ds_lt256k_500.jsonl
# record_id=395  entry=f  input='12'  output='4'  tokens=8027

def f(x):
    if x ^ 9 < 29:
        d = 0
        while d < 12:
            x = d & x
            x = (d - x - x) % 4093
            d = d + 1
        for nxt in range(2):
            x = nxt * x + x & 4095
            x = (nxt - 13 ^ x) & 65535
            x = (nxt - 18 ^ x) % 4093
    if x + x == 12:
        x = (x << 3 ^ x) // 2
        x = ((x & 18) + x) % 9973
    if 9 ^ x >= 13:
        x = 17 & x
        x = x + x
    v = x + 4 ^ x // 4
    j = 0
    while j < 33:
        t0 = 2 & 20 ^ v
        v = t0 % 9973
        j = j + 1
    return (x ^ v) % 4093

if __name__ == "__main__":
    arg = 12
    expected = 4
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
