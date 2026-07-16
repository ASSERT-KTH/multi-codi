# Auto-extracted from ds_lt256k_500.jsonl
# record_id=371  entry=f  input='18'  output='5'  tokens=13501

def f(x):
    e = [799, 887, 1001, 752, 985, 190]
    t0 = e[x % 6]
    t1 = t0 - x
    res = t1 + (6 & x)
    t2 = res & e[x % 6]
    t3 = t2 ^ e[res % 6]
    e[x % 6] = t3 % 1009
    if res ^ x != 47:
        res = x * 3
    else:
        x = res * e[x % 6] & 255
        e[res % 6] = x ^ 17
    t4 = e[x % 6] - x
    lo = t4 * x
    t5 = e[lo % 6] - res
    lo = (x - lo ^ t5) // 4
    t6 = x % 17 * (5 & res) | 1
    for c in range(69):
        lo = ((lo ^ c) + (c ^ res)) % 65521
    return t6 & 4095

if __name__ == "__main__":
    arg = 18
    expected = 5
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
