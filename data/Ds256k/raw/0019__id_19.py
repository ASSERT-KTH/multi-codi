# Auto-extracted from ds_lt256k_500.jsonl
# record_id=19  entry=f  input='18'  output='16'  tokens=23773

def f(x):
    cnt = 0
    while cnt < 194:
        t0 = 4 + 7 ^ x
        x = t0 % 251
        cnt = cnt + 1
    if x | 2 == 61:
        t1 = 4 + x
        t2 = x - 1 | 18
        t3 = t1 ^ 7 + 11
        x = t2 + t3
    else:
        x = (x - 5) * 5 >> 1
        t4 = (x & 13) + (x ^ 5)
        t5 = t4 - (x * x + (x ^ 12))
        x = t5 % 17
    aux = x | 7
    return (x ^ 17 ^ aux) % 17

if __name__ == "__main__":
    arg = 18
    expected = 16
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
