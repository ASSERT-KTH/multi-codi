# Auto-extracted from ds_lt256k_500.jsonl
# record_id=172  entry=f  input='12'  output='12'  tokens=223578

def f(x):
    tot = [219, 198, 128, 19]
    t0 = x + x
    res = t0 * (11 - x)
    hi = 6 - x
    e = x + hi
    if hi - 13 >= 3:
        res = (hi | res) - res
    else:
        t1 = e * res
        res = t1 - (12 & hi)
    res = hi + 20
    t2 = tot[e % 4] - res
    for w in range(443):
        hi = (w - tot[res % 4]) % 4093
        t3 = tot[hi % 4]
        t4 = t3 // 2
        t5 = t4 * (hi % 17)
        res = (t5 + res) % 17
    return (e + x | t2) % 17

if __name__ == "__main__":
    arg = 12
    expected = 12
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
