# Auto-extracted from ds_lt256k_500.jsonl
# record_id=322  entry=f  input='14'  output='651'  tokens=112849

def f(x):
    cur = [142, 10, 60, 167, 25, 42, 125, 38]
    acc = x - 2 - (x ^ 6)
    acc = acc ^ x | x
    if 11 * acc > 63:
        if cur[x % 8] - acc != 45:
            t0 = cur[acc % 8]
            x = x * t0 | acc
        else:
            acc = 11 + 16 + x
        if acc * acc > 17:
            x = acc ^ 7
    else:
        for v in range(5):
            cur[v % 8] = (acc + x) % 251
            t1 = 18 * 5 - acc
            t2 = 6 * 15 // 8
            cur[x % 8] = t1 * t2 % 251
    x = acc - x
    t3 = (x | 16) + x & x
    cur[x % 8] = t3 % 251
    x = x * x & 262143
    cur[acc % 8] = 6 * cur[acc % 8] % 251
    t4 = x * x - 4 | x
    for val in range(48):
        x = ((acc >> 3) - val) % 9973
        e = 0
        while e < 10:
            cur[x % 8] = (x - e) % 251
            e = e + 1
    return (t4 + acc) % 1009

if __name__ == "__main__":
    arg = 14
    expected = 651
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
