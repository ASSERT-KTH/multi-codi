# Auto-extracted from ds_lt256k_500.jsonl
# record_id=25  entry=f  input='4'  output='447'  tokens=36751

def f(x):
    tmp = [13, 75, 116, 109, 26, 140, 239]
    acc = x - 13 | x
    cnt = acc + acc
    hi = ((cnt | x) + cnt) * acc
    tot = x | acc
    t0 = tot ^ cnt ^ cnt
    t1 = acc + 8 - x
    y = t0 - t1
    if tot + y == 34:
        t2 = tmp[hi % 7]
        t3 = tmp[x % 7]
        t4 = t2 + tot ^ t3
        cnt = t4 & cnt
    t5 = tot * acc ^ 17 - hi
    t6 = t5 * tmp[tot % 7]
    buf = t6 & 8191
    p = 2 - 18 - x
    for g in range(191):
        p = p - buf - (5 - x) & 255
    return (11 << 1 | buf) % 1009

if __name__ == "__main__":
    arg = 4
    expected = 447
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
