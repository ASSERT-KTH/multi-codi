# Auto-extracted from ds_lt256k_500.jsonl
# record_id=347  entry=f  input='8'  output='1232'  tokens=67348

def f(x):
    u = [64, 96, 37, 67, 55]
    if x ^ 3 >= 22:
        u[x % 5] = ((x & 4) + x) * 20 % 97
    t0 = (15 + x) * x
    idx = t0 - (x * x >> 2)
    t1 = 20 * 7 * (idx ^ x)
    cur = t1 // 8
    t = idx >> 1
    t2 = cur - 17 - (idx ^ 5)
    s = t2 >> 1
    t3 = cur + 4
    t4 = 11 - idx + idx
    t5 = t3 & cur >> 1
    for z in range(122):
        t6 = u[cur % 5]
        t7 = idx | t6
        t8 = t7 - (2 | s)
        u[cur % 5] = t8 % 97
    return t4 * t5 & 131071

if __name__ == "__main__":
    arg = 8
    expected = 1232
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
