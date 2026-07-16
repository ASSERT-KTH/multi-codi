# Auto-extracted from ds_lt256k_500.jsonl
# record_id=16  entry=f  input='12'  output='996'  tokens=248876

def f(x):
    val = [64, 15, 88, 23]
    cur = x + x - (x ^ 15)
    t0 = val[cur % 4] * 19
    t1 = (x ^ cur) * (cur // 7)
    res = t1 | t0 >> 2
    y = res << 4 | 14
    p = cur + res
    for q in range(1164):
        t2 = (x + (10 - x)) * x + cur
        cur = t2 % 97
    j = p ^ 1
    aux = 14 ^ x
    b = aux - 1 << 1
    idx = (x ^ y) % 97
    return (8 - cur) % 1009

if __name__ == "__main__":
    arg = 12
    expected = 996
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
