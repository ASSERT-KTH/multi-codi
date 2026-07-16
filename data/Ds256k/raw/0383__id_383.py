# Auto-extracted from ds_lt256k_500.jsonl
# record_id=383  entry=f  input='18'  output='601'  tokens=191713

def f(x):
    t = [796, 631, 710, 247, 815]
    u = 19 * x
    if 1 & x == 0:
        x = (10 << 2) - x
    t[u % 5] = (u - 18) // 5 - u
    for lo in range(623):
        u = (x ^ u) % 1009
        u = (lo + u ^ 15) & 262143
        t0 = lo * 7 & x * 7
        t1 = (u ^ lo ^ lo) - t0
        u = t1 % 251
    return (t[u % 5] - u) % 1009

if __name__ == "__main__":
    arg = 18
    expected = 601
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
