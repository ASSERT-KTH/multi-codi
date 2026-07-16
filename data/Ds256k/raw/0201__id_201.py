# Auto-extracted from ds_lt256k_500.jsonl
# record_id=201  entry=f  input='10'  output='143'  tokens=44346

def f(x):
    cnt = (x + 17) * (19 * x)
    cur = (cnt | 13) - cnt
    x = cur // 5 % 1009
    t0 = x // 8 + x
    cur = t0 - x
    if x ^ 9 == 35:
        cnt = 5 + x
        t1 = cnt >> 1
        t2 = t1 ^ cur + cur
        cur = t2 * 18 & 2047
    for tmp in range(144):
        if 9 + 10 | cnt > 63:
            cur = cur // 6 & 262143
            t3 = cnt & 18 | cur | tmp
            x = t3 & 32767
        else:
            cnt = (8 + tmp ^ cur) % 65521
        x = (cur & 5 | 6 | tmp) & 32767
    return (x + cur) % 65521

if __name__ == "__main__":
    arg = 10
    expected = 143
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
