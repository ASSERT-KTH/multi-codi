# Auto-extracted from ds_lt256k_500.jsonl
# record_id=360  entry=f  input='13'  output='0'  tokens=182414

def f(x):
    v = [589, 889, 4, 589, 147, 367, 748, 650]
    tot = x ^ 3
    if v[x % 8] & tot <= 21:
        tot = tot ^ 6
    x = x - tot ^ tot * 6
    if x * 20 < 21:
        t0 = x - v[tot % 8]
        v[x % 8] = (t0 - 16 * x) // 4 % 1009
        for hi in range(5):
            tot = (tot + 20 ^ 19) % 4093
            t1 = 19 + v[x % 8]
            t2 = tot - v[x % 8]
            t3 = t1 - 12 + t2 // 8
            tot = t3 % 4093
    else:
        t4 = 4 * 18 // 8 >> 1
        tot = t4 + tot
        t5 = v[x % 8]
        t6 = 7 - t5
        t7 = t6 - (tot ^ x)
        x = t7 - x
    x = x ^ 15 ^ x >> 4
    for res in range(501):
        if res | tot > 17:
            t8 = (v[res % 8] | res) - tot
            v[res % 8] = t8 % 1009
        x = tot & res & tot
    return (tot - 12) % 65521

if __name__ == "__main__":
    arg = 13
    expected = 0
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
