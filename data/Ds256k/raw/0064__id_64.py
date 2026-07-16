# Auto-extracted from ds_lt256k_500.jsonl
# record_id=64  entry=f  input='17'  output='20'  tokens=64616

def f(x):
    tot = [78, 77, 96, 68, 54, 46, 64]
    j = 15 + x ^ x
    j = 3 + x - (j >> 2)
    t0 = j - 2 - x
    j = t0 + 20
    res = 0
    while res < 88:
        t1 = tot[x % 7] * res
        t2 = (tot[res % 7] | j) // 4
        x = (j >> 3) * t1 & t2
        t3 = res + 2
        t4 = t3 ^ 16 + 9
        j = (t4 - x) % 1009
        t5 = tot[x % 7]
        j = (j - 13) * t5 & res
        res = res + 1
    t6 = (x ^ j) >> 4 << 2
    return t6 % 1009

if __name__ == "__main__":
    arg = 17
    expected = 20
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
