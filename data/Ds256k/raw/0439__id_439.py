# Auto-extracted from ds_lt256k_500.jsonl
# record_id=439  entry=f  input='10'  output='0'  tokens=106905

def f(x):
    for u in range(135):
        for tot in range(2):
            t0 = (10 | tot) + x
            x = t0 % 97
        if u - 16 + x != 45:
            x = x * u * x // 2 & 65535
        else:
            t1 = u * 20 // 8
            t2 = (t1 >> 3) - x
            x = t2 & 2047
            t3 = (x ^ 2) * x
            x = t3 % 4093
        t4 = 9 - x & u
        t5 = t4 * ((u << 3) // 7)
        x = t5 & 255
    t6 = (x ^ 10) & x
    tmp = t6 & (x * 3 | x)
    j = 12 * x + (tmp << 2) & 255
    t7 = tmp // 8 ^ x
    lo = t7 * j & 16383
    c = (j << 2) * (10 - x) % 97
    acc = tmp << 4 >> 4
    return (c - lo) % 1009

if __name__ == "__main__":
    arg = 10
    expected = 0
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
