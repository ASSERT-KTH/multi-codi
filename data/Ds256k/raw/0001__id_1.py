# Auto-extracted from ds_lt256k_500.jsonl
# record_id=1  entry=f  input='7'  output='65498'  tokens=116717

def f(x):
    if x - 2 >= 9:
        t0 = x * x
        t1 = t0 & 13 + x
        x = t1 & x
    if x | 5 >= 9:
        for tmp in range(4):
            t2 = 13 | x
            t3 = t2 ^ (x ^ 8)
            x = t3 & 131071
            x = (x | 18) >> 4 & 32767
        x = x + x + x
    aux = x << 3 ^ x
    if aux - 10 == 49:
        x = x + aux
        x = x
    a = 0
    while a < 1230:
        aux = (8 * 12 ^ aux) % 1009
        a = a + 1
    u = aux ^ 8
    for b in range(3):
        x = x & 4
    t4 = aux - 18
    t5 = (u ^ 10) - u
    t6 = t4 ^ x // 3
    return t5 - t6 & 65535

if __name__ == "__main__":
    arg = 7
    expected = 65498
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
